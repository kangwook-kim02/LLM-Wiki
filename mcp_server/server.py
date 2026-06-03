"""
server.py — FastMCP 기반 Wiki MCP 서버

stdio 방식으로 7개 MCP 도구를 서빙한다.

실행:
    python mcp_server/server.py
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from wiki_store import (
    wiki_list as _wiki_list,
    wiki_read as _wiki_read,
    wiki_write as _wiki_write,
    wiki_search as _wiki_search,
    wiki_delete as _wiki_delete,
    raw_save as _raw_save,
    raw_read as _raw_read,
)

mcp = FastMCP("llm-wiki")


# ---------------------------------------------------------------------------
# Wiki 도구
# ---------------------------------------------------------------------------

@mcp.tool()
def wiki_list() -> list[str]:
    """wiki/ 하위 전체 페이지의 slug 목록을 반환한다."""
    return _wiki_list()


@mcp.tool()
def wiki_read(slug: str) -> str:
    """slug에 해당하는 Wiki 페이지 내용을 반환한다.

    Args:
        slug: 페이지 식별자 (예: "concepts/rag", "index")

    Raises:
        FileNotFoundError: 페이지가 존재하지 않을 때
    """
    return _wiki_read(slug)


@mcp.tool()
def wiki_write(slug: str, content: str) -> str:
    """slug 경로에 Wiki 페이지를 생성하거나 덮어쓴다.

    Args:
        slug: 페이지 식별자 (예: "concepts/rag", "index")
        content: 저장할 Markdown 내용 (YAML frontmatter 포함 권장)

    Returns:
        완료 메시지
    """
    _wiki_write(slug, content)
    return f"Wiki 페이지 저장 완료: {slug}"


@mcp.tool()
def wiki_search(query: str) -> list[dict]:
    """제목·본문에서 대소문자 무시 키워드 검색을 수행한다.

    Args:
        query: 검색 키워드

    Returns:
        [{"slug": ..., "title": ..., "excerpt": ...}, ...] 형식의 결과 리스트
    """
    return _wiki_search(query)


@mcp.tool()
def wiki_delete(slug: str) -> str:
    """slug에 해당하는 Wiki 페이지를 삭제한다.

    Args:
        slug: 삭제할 페이지 식별자

    Returns:
        완료 메시지

    Raises:
        FileNotFoundError: 페이지가 존재하지 않을 때
    """
    _wiki_delete(slug)
    return f"Wiki 페이지 삭제 완료: {slug}"


# ---------------------------------------------------------------------------
# Raw 파일 도구
# ---------------------------------------------------------------------------

@mcp.tool()
def raw_save(filename: str, content: str) -> str:
    """raw/ 디렉토리에 파일을 저장한다.

    MCP 레이어에서 str → bytes (UTF-8) 변환을 수행한다.

    Args:
        filename: 저장할 파일명 (예: "paper.pdf", "notes.txt")
        content: 파일 내용 (UTF-8 인코딩 가능한 문자열)

    Returns:
        완료 메시지
    """
    _raw_save(filename, content.encode("utf-8"))
    return f"raw 파일 저장 완료: {filename}"


@mcp.tool()
def raw_read(filename: str) -> str:
    """raw/ 디렉토리에서 파일을 읽어 문자열로 반환한다.

    .pdf 파일의 경우 pypdf로 텍스트를 추출한다.
    나머지 파일은 UTF-8로 디코딩한다.

    Args:
        filename: 읽을 파일명

    Returns:
        파일 내용 (텍스트)

    Raises:
        FileNotFoundError: 파일이 존재하지 않을 때
    """
    data = _raw_read(filename)

    if filename.lower().endswith(".pdf"):
        import io
        from pypdf import PdfReader

        reader = PdfReader(io.BytesIO(data))
        pages_text = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)
        return "\n\n".join(pages_text)

    return data.decode("utf-8")


# ---------------------------------------------------------------------------
# 진입점
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
