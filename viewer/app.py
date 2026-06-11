"""
viewer/app.py — Flask 기반 Wiki 뷰어

라우팅:
  GET  /               → 첫 번째 페이지로 redirect, 페이지 없으면 빈 상태
  GET  /page/<slug>    → Markdown 렌더링 페이지 표시
  POST /upload         → 파일 업로드 후 raw/ 저장 (V-03)
  POST /chat           → claude -p subprocess 채팅 응답 (V-04)
  GET  /api/search     → 키워드 검색 결과 JSON 반환 (V-05)
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# 프로젝트 루트를 sys.path에 추가하여 mcp_server 패키지 import 가능하게 함
_PROJECT_ROOT = Path(__file__).parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import markdown2
from flask import Flask, jsonify, redirect, render_template, request, url_for

from mcp_server.wiki_store import _parse_frontmatter, raw_save, wiki_list, wiki_read, wiki_search

app = Flask(__name__)

# 사이드바에 표시하지 않을 내부 slug
_HIDDEN_SLUGS = {"index", "log"}

# 카테고리 표시 순서 및 레이블
_CATEGORY_ORDER = ["concepts", "frameworks", "patterns", "sources"]
_CATEGORY_LABELS = {
    "concepts": "개념 (Concepts)",
    "frameworks": "프레임워크 (Frameworks)",
    "patterns": "패턴 (Patterns)",
    "sources": "출처 (Sources)",
    "etc": "기타",
}


def _get_page_title(slug: str) -> str:
    """페이지 제목 반환 — frontmatter title > 본문 첫 H1 > slug."""
    try:
        content = wiki_read(slug)
    except FileNotFoundError:
        return slug
    meta, body = _parse_frontmatter(content)
    if meta.get("title"):
        return meta["title"]
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return slug


def _build_sidebar() -> list[dict]:
    """사이드바용 카테고리 그룹 목록 반환.

    Returns:
        [
          {"label": "개념 (Concepts)", "pages": [{"slug": ..., "title": ...}, ...]},
          ...
        ]
    """
    all_slugs = [s for s in wiki_list() if s not in _HIDDEN_SLUGS]

    groups: dict[str, list[dict]] = defaultdict(list)
    for slug in all_slugs:
        prefix = slug.split("/")[0] if "/" in slug else "etc"
        groups[prefix].append({"slug": slug, "title": _get_page_title(slug)})

    result = []
    seen: set[str] = set()

    # 정해진 순서대로 먼저 추가
    for cat in _CATEGORY_ORDER:
        if cat in groups:
            result.append({
                "label": _CATEGORY_LABELS.get(cat, cat),
                "key": cat,
                "pages": groups[cat],
            })
            seen.add(cat)

    # 나머지 카테고리 추가
    for cat, pages in sorted(groups.items()):
        if cat not in seen:
            result.append({
                "label": _CATEGORY_LABELS.get(cat, cat),
                "key": cat,
                "pages": pages,
            })

    return result


def _convert_wiki_links(text: str) -> str:
    """[[slug]](display) → [display](/page/slug) / [[slug]] → [slug](/page/slug)"""
    text = re.sub(
        r'\[\[([^\]]+)\]\]\(([^)]+)\)',
        lambda m: f'[{m.group(2)}](/page/{m.group(1)})',
        text,
    )
    text = re.sub(
        r'\[\[([^\]]+)\]\]',
        lambda m: f'[{m.group(1)}](/page/{m.group(1)})',
        text,
    )
    return text


def _render_markdown(body: str) -> str:
    """Markdown 본문을 HTML로 변환."""
    return markdown2.markdown(
        _convert_wiki_links(body),
        extras=["fenced-code-blocks", "tables", "header-ids", "strike", "task_list"],
    )


def _strip_frontmatter(content: str) -> tuple[dict, str]:
    """frontmatter를 파싱하고 본문만 반환."""
    return _parse_frontmatter(content)


@app.route("/")
def index():
    """루트 — 첫 번째 표시 가능 페이지로 redirect."""
    slugs = [s for s in wiki_list() if s not in _HIDDEN_SLUGS]
    if slugs:
        return redirect(url_for("page", slug=slugs[0]))
    return render_template("page.html", sidebar=_build_sidebar(), content=None, slug=None, meta={})


@app.route("/page/<path:slug>")
def page(slug: str):
    """페이지 뷰 — slug에 해당하는 Wiki 페이지를 렌더링."""
    try:
        raw_content = wiki_read(slug)
    except FileNotFoundError:
        return render_template(
            "page.html",
            sidebar=_build_sidebar(),
            content=f"<p>페이지를 찾을 수 없습니다: <code>{slug}</code></p>",
            slug=slug,
            meta={},
            not_found=True,
        ), 404

    meta, body = _strip_frontmatter(raw_content)
    html_content = _render_markdown(body)

    return render_template(
        "page.html",
        sidebar=_build_sidebar(),
        content=html_content,
        slug=slug,
        meta=meta,
        title=meta.get("title", slug),
        not_found=False,
    )


@app.route("/upload", methods=["POST"])
def upload():
    """파일 업로드 라우트 (V-03).

    multipart/form-data 로 파일을 수신하여 raw/ 디렉토리에 저장.
    """
    if "file" not in request.files:
        return jsonify({"ok": False, "error": "파일이 없습니다."}), 400

    f = request.files["file"]
    if not f or f.filename == "":
        return jsonify({"ok": False, "error": "파일명이 비어 있습니다."}), 400

    filename = f.filename
    raw_save(filename, f.read())
    return jsonify({"ok": True, "filename": filename})


@app.route("/chat", methods=["POST"])
def chat():
    """채팅 라우트 (V-04).

    요청 JSON {"message": "..."} 을 claude -p subprocess 로 전달하고
    {"reply": "..."} 를 반환.
    """
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"ok": False, "error": "메시지가 비어 있습니다."}), 400

    try:
        # Windows에서 claude는 .cmd 래퍼로 설치됨
        # --allowedTools: 비대화형 subprocess에서 필요한 MCP 도구만 허용
        claude_cmd = "claude.cmd" if sys.platform == "win32" else "claude"
        _ALLOWED_TOOLS = ",".join([
            "mcp__llm-wiki__wiki_list",
            "mcp__llm-wiki__wiki_read",
            "mcp__llm-wiki__wiki_write",
            "mcp__llm-wiki__wiki_search",
            "mcp__llm-wiki__wiki_delete",
            "mcp__llm-wiki__raw_save",
            "mcp__llm-wiki__raw_read",
        ])
        result = subprocess.run(
            [claude_cmd, "-p", message, "--allowedTools", _ALLOWED_TOOLS, "--output-format", "json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=str(_PROJECT_ROOT),
            timeout=120,
        )
        raw_output = result.stdout.strip()
        try:
            parsed = json.loads(raw_output)
            reply = parsed.get("result", "") or result.stderr.strip() or "(응답 없음)"
            usage_data = parsed.get("usage", {})
            usage = {
                "input": usage_data.get("input_tokens", 0),
                "output": usage_data.get("output_tokens", 0),
            }
        except (json.JSONDecodeError, AttributeError):
            # JSON 파싱 실패 시 B안(글자 수 기반 추정)으로 폴백
            reply = raw_output or result.stderr.strip() or "(응답 없음)"
            usage = {
                "input": len(message) // 4,
                "output": len(reply) // 4,
            }
        return jsonify({"reply": reply, "usage": usage})
    except subprocess.TimeoutExpired:
        return jsonify({"reply": "오류: 응답 시간이 초과되었습니다 (120초).", "error": True})
    except FileNotFoundError:
        return jsonify({"reply": "오류: claude CLI를 찾을 수 없습니다. claude 명령어가 PATH에 있는지 확인하세요.", "error": True})
    except Exception as exc:  # noqa: BLE001
        return jsonify({"reply": f"오류: {exc}", "error": True})


@app.route("/api/page/<path:slug>")
def api_page(slug: str):
    """AJAX 네비게이션용 JSON 엔드포인트 — 본문 HTML만 반환."""
    try:
        raw_content = wiki_read(slug)
    except FileNotFoundError:
        html = render_template(
            "_content.html",
            content=f"<p>페이지를 찾을 수 없습니다: <code>{slug}</code></p>",
            not_found=True,
            meta={},
        )
        return jsonify({"ok": False, "slug": slug, "title": slug, "html": html}), 404

    meta, body = _strip_frontmatter(raw_content)
    html_content = _render_markdown(body)
    html = render_template(
        "_content.html",
        content=html_content,
        not_found=False,
        meta=meta,
    )
    return jsonify({
        "ok": True,
        "slug": slug,
        "title": meta.get("title", slug),
        "html": html,
    })


@app.route("/api/search")
def api_search():
    """키워드 검색 엔드포인트 (V-05).

    GET /api/search?q=<query>
    Returns: [{"slug": ..., "title": ..., "excerpt": ...}, ...]
    """
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify([])

    results = wiki_search(query)
    # 내부 관리 slug(index, log)는 결과에서 제외
    results = [r for r in results if r["slug"] not in _HIDDEN_SLUGS]
    # 제목 일치 결과를 본문만 일치하는 결과보다 먼저 표시
    query_lower = query.lower()
    results.sort(key=lambda r: 0 if query_lower in r["title"].lower() else 1)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
