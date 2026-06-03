"""
wiki_store.py — 파일 기반 Wiki 저장소 레이어

slug 형식:
  - 루트 레벨: "index", "log"
  - 카테고리 내: "concepts/rag", "frameworks/langchain"

파일 경로 매핑:
  slug "index"         → wiki/index.md
  slug "concepts/rag"  → wiki/concepts/rag.md
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

# --- 경로 설정 -----------------------------------------------------------------

_ROOT = Path(__file__).parent.parent          # 프로젝트 루트
WIKI_DIR = _ROOT / "wiki"
RAW_DIR = _ROOT / "raw"


# --- 내부 유틸 ----------------------------------------------------------------

def _slug_to_path(slug: str) -> Path:
    """slug → wiki/ 하위 .md 파일 경로."""
    parts = slug.strip("/").split("/")
    return WIKI_DIR.joinpath(*parts).with_suffix(".md")


def _path_to_slug(path: Path) -> str:
    """wiki/ 하위 .md 파일 경로 → slug."""
    rel = path.relative_to(WIKI_DIR).with_suffix("")
    return rel.as_posix()   # "concepts/rag", "index" 등


def _serialize_frontmatter(meta: dict[str, Any]) -> str:
    """dict를 YAML frontmatter 형식 문자열로 직렬화.

    Returns:
        "---\\nkey: value\\n---\\n" 형식의 문자열.
        meta가 비어 있으면 빈 문자열 반환.
    """
    if not meta:
        return ""
    lines = ["---"]
    for key, value in meta.items():
        lines.append(f"{key}: {value}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """YAML frontmatter 파싱.

    Returns:
        (meta dict, body string)
        frontmatter가 없으면 ({}, 전체 content)
    """
    if not content.startswith("---"):
        return {}, content

    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    fm_block = content[3:end].strip()
    body = content[end + 4:].lstrip("\n")

    meta: dict[str, Any] = {}
    for line in fm_block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()

    return meta, body


def _extract_title(meta: dict[str, Any], body: str, slug: str) -> str:
    """frontmatter title → 본문 첫 번째 H1 → slug 순서로 제목 추출."""
    if "title" in meta and meta["title"]:
        return meta["title"]

    for line in body.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()

    return slug


def _make_excerpt(body: str, length: int = 120) -> str:
    """본문에서 앞부분 발췌. 마크다운 문법 제거."""
    # 헤딩, 코드 펜스, 빈 줄 제거
    lines = []
    in_code = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            continue
        lines.append(stripped)

    text = " ".join(lines)
    return text[:length] + ("…" if len(text) > length else "")


# --- Public API ---------------------------------------------------------------

def wiki_list() -> list[str]:
    """wiki/ 하위 전체 .md 파일을 slug 리스트로 반환."""
    if not WIKI_DIR.exists():
        return []
    return sorted(
        _path_to_slug(p)
        for p in WIKI_DIR.rglob("*.md")
    )


def wiki_read(slug: str) -> str:
    """slug에 해당하는 페이지 내용 반환.

    Raises:
        FileNotFoundError: 페이지가 존재하지 않을 때
    """
    path = _slug_to_path(slug)
    if not path.exists():
        raise FileNotFoundError(f"Wiki 페이지를 찾을 수 없습니다: {slug!r}")
    return path.read_text(encoding="utf-8")


def wiki_write(slug: str, content: str) -> None:
    """slug 경로에 페이지를 생성하거나 덮어씁니다.

    부모 디렉토리가 없으면 자동으로 생성합니다.
    """
    path = _slug_to_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def wiki_search(query: str) -> list[dict[str, str]]:
    """제목·본문에서 대소문자 무시 키워드 매칭 검색.

    Returns:
        [{"slug": ..., "title": ..., "excerpt": ...}, ...]
    """
    query_lower = query.lower()
    results: list[dict[str, str]] = []

    for slug in wiki_list():
        try:
            content = wiki_read(slug)
        except FileNotFoundError:
            continue

        meta, body = _parse_frontmatter(content)
        title = _extract_title(meta, body, slug)

        if query_lower in title.lower() or query_lower in body.lower():
            results.append({
                "slug": slug,
                "title": title,
                "excerpt": _make_excerpt(body),
            })

    return results


def wiki_delete(slug: str) -> None:
    """slug에 해당하는 페이지를 삭제합니다.

    Raises:
        FileNotFoundError: 페이지가 존재하지 않을 때
    """
    path = _slug_to_path(slug)
    if not path.exists():
        raise FileNotFoundError(f"삭제할 Wiki 페이지가 없습니다: {slug!r}")
    path.unlink()


def raw_save(filename: str, content: bytes) -> None:
    """raw/ 디렉토리에 바이너리 파일을 저장합니다.

    부모 디렉토리가 없으면 자동으로 생성합니다.
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    dest = RAW_DIR / filename
    dest.write_bytes(content)


def raw_read(filename: str) -> bytes:
    """raw/ 디렉토리에서 바이너리 파일을 읽습니다.

    Raises:
        FileNotFoundError: 파일이 존재하지 않을 때
    """
    path = RAW_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"raw 파일을 찾을 수 없습니다: {filename!r}")
    return path.read_bytes()
