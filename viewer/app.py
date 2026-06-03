"""
viewer/app.py — Flask 기반 Wiki 뷰어

라우팅:
  GET /               → 첫 번째 페이지로 redirect, 페이지 없으면 빈 상태
  GET /page/<slug>    → Markdown 렌더링 페이지 표시
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

# 프로젝트 루트를 sys.path에 추가하여 mcp_server 패키지 import 가능하게 함
_PROJECT_ROOT = Path(__file__).parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import markdown2
from flask import Flask, redirect, render_template, url_for

from mcp_server.wiki_store import _parse_frontmatter, wiki_list, wiki_read

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


def _render_markdown(body: str) -> str:
    """Markdown 본문을 HTML로 변환."""
    return markdown2.markdown(
        body,
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


if __name__ == "__main__":
    app.run(debug=True)
