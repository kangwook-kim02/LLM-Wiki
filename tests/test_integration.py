"""
tests/test_integration.py — MCP 서버 통합 테스트

wiki_store.py를 직접 import하여 7개 도구의 동작을 검증한다.
MCP 프로토콜 레이어 없이 저장소 레이어만 테스트한다.
"""

import sys
import os

# 프로젝트 루트를 sys.path에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mcp_server.wiki_store import (
    wiki_write,
    wiki_read,
    wiki_list,
    wiki_delete,
    wiki_search,
    raw_save,
    raw_read,
)

PASS = "PASS"
FAIL = "FAIL"

results: list[tuple[str, str, str]] = []  # (test_name, status, message)


def record(name: str, ok: bool, msg: str = "") -> None:
    status = PASS if ok else FAIL
    results.append((name, status, msg))
    indicator = "[PASS]" if ok else "[FAIL]"
    print(f"  {indicator} {name}" + (f" — {msg}" if msg else ""))


# ---------------------------------------------------------------------------
# 1. wiki_write → wiki_read → wiki_list → wiki_delete
# ---------------------------------------------------------------------------

print("\n=== [1] wiki_write / wiki_read / wiki_list / wiki_delete ===")

TEST_SLUG = "concepts/test-integration"
TEST_CONTENT = """\
---
title: Integration Test Page
type: concept
date: 2026-06-03
---

# Integration Test Page

통합 테스트용 임시 페이지입니다.
"""

# wiki_write
try:
    wiki_write(TEST_SLUG, TEST_CONTENT)
    record("wiki_write: 페이지 생성", True)
except Exception as e:
    record("wiki_write: 페이지 생성", False, str(e))

# wiki_read — 정상 케이스
try:
    content = wiki_read(TEST_SLUG)
    match = "Integration Test Page" in content
    record("wiki_read: 정상 읽기", match, "" if match else "내용 불일치")
except Exception as e:
    record("wiki_read: 정상 읽기", False, str(e))

# wiki_list — 방금 쓴 slug가 목록에 있어야 함
try:
    slugs = wiki_list()
    found = TEST_SLUG in slugs
    record("wiki_list: slug 포함 확인", found, "" if found else f"{TEST_SLUG!r} not in {slugs}")
except Exception as e:
    record("wiki_list: slug 포함 확인", False, str(e))

# wiki_delete
try:
    wiki_delete(TEST_SLUG)
    record("wiki_delete: 페이지 삭제", True)
except Exception as e:
    record("wiki_delete: 페이지 삭제", False, str(e))

# wiki_list — 삭제 후 없어야 함
try:
    slugs = wiki_list()
    gone = TEST_SLUG not in slugs
    record("wiki_list: 삭제 후 slug 제거 확인", gone, "" if gone else f"{TEST_SLUG!r} still in list")
except Exception as e:
    record("wiki_list: 삭제 후 slug 제거 확인", False, str(e))

# ---------------------------------------------------------------------------
# 2. raw_save → raw_read
# ---------------------------------------------------------------------------

print("\n=== [2] raw_save / raw_read ===")

RAW_FILENAME = "test_integration_sample.txt"
RAW_CONTENT = b"Hello, raw store!\n\xc7\xd2\xb7\xce raw \xc0\xfa\xc0\xe5\xbd\xc2\xc0\xce\xc1\xa4."

# raw_save
try:
    raw_save(RAW_FILENAME, RAW_CONTENT)
    record("raw_save: 파일 저장", True)
except Exception as e:
    record("raw_save: 파일 저장", False, str(e))

# raw_read — 저장한 내용과 동일해야 함
try:
    data = raw_read(RAW_FILENAME)
    match = data == RAW_CONTENT
    record("raw_read: 저장 내용 일치", match, "" if match else "내용 불일치")
except Exception as e:
    record("raw_read: 저장 내용 일치", False, str(e))

# 정리: 테스트 raw 파일 제거
try:
    from mcp_server.wiki_store import RAW_DIR
    (RAW_DIR / RAW_FILENAME).unlink(missing_ok=True)
except Exception:
    pass

# ---------------------------------------------------------------------------
# 3. wiki_search — 키워드 매칭
# ---------------------------------------------------------------------------

print("\n=== [3] wiki_search ===")

SEARCH_SLUG = "concepts/search-test"
SEARCH_CONTENT = """\
---
title: RAG 개요
type: concept
date: 2026-06-03
---

# RAG 개요

Retrieval-Augmented Generation(RAG)은 LLM에 외부 지식을 결합하는 패턴이다.
"""

try:
    wiki_write(SEARCH_SLUG, SEARCH_CONTENT)
    record("wiki_write: 검색 테스트용 페이지 생성", True)
except Exception as e:
    record("wiki_write: 검색 테스트용 페이지 생성", False, str(e))

# 본문 키워드 매칭
try:
    hits = wiki_search("RAG")
    found = any(h["slug"] == SEARCH_SLUG for h in hits)
    record("wiki_search: 본문 키워드 'RAG' 매칭", found, "" if found else f"hits={hits}")
except Exception as e:
    record("wiki_search: 본문 키워드 'RAG' 매칭", False, str(e))

# 제목 키워드 매칭
try:
    hits = wiki_search("RAG 개요")
    found = any(h["slug"] == SEARCH_SLUG for h in hits)
    record("wiki_search: 제목 키워드 'RAG 개요' 매칭", found, "" if found else f"hits={hits}")
except Exception as e:
    record("wiki_search: 제목 키워드 'RAG 개요' 매칭", False, str(e))

# 존재하지 않는 키워드 — 결과 없어야 함
try:
    hits = wiki_search("존재하지않는키워드XYZ")
    empty = len(hits) == 0
    record("wiki_search: 없는 키워드 → 빈 결과", empty, "" if empty else f"unexpected hits={hits}")
except Exception as e:
    record("wiki_search: 없는 키워드 → 빈 결과", False, str(e))

# 검색 테스트 페이지 정리
try:
    wiki_delete(SEARCH_SLUG)
except Exception:
    pass

# ---------------------------------------------------------------------------
# 4. 에러 케이스
# ---------------------------------------------------------------------------

print("\n=== [4] 에러 케이스 ===")

# 없는 slug 읽기 → FileNotFoundError
try:
    wiki_read("concepts/nonexistent-page-xyz")
    record("wiki_read: 없는 slug → FileNotFoundError", False, "예외가 발생하지 않았습니다")
except FileNotFoundError:
    record("wiki_read: 없는 slug → FileNotFoundError", True)
except Exception as e:
    record("wiki_read: 없는 slug → FileNotFoundError", False, f"예상치 못한 예외: {type(e).__name__}: {e}")

# 없는 raw 파일 읽기 → FileNotFoundError
try:
    raw_read("nonexistent_file_xyz.txt")
    record("raw_read: 없는 파일 → FileNotFoundError", False, "예외가 발생하지 않았습니다")
except FileNotFoundError:
    record("raw_read: 없는 파일 → FileNotFoundError", True)
except Exception as e:
    record("raw_read: 없는 파일 → FileNotFoundError", False, f"예상치 못한 예외: {type(e).__name__}: {e}")

# ---------------------------------------------------------------------------
# 5. wiki/index.md, wiki/log.md 존재 확인
# ---------------------------------------------------------------------------

print("\n=== [5] 필수 파일 존재 확인 ===")

try:
    slugs = wiki_list()
    has_index = "index" in slugs
    record("wiki/index.md 존재", has_index, "" if has_index else "index slug 없음")
except Exception as e:
    record("wiki/index.md 존재", False, str(e))

try:
    slugs = wiki_list()
    has_log = "log" in slugs
    record("wiki/log.md 존재", has_log, "" if has_log else "log slug 없음")
except Exception as e:
    record("wiki/log.md 존재", False, str(e))

# index.md YAML frontmatter 확인
try:
    content = wiki_read("index")
    has_fm = content.startswith("---")
    record("wiki/index.md YAML frontmatter 존재", has_fm)
except Exception as e:
    record("wiki/index.md YAML frontmatter 존재", False, str(e))

# log.md YAML frontmatter 확인
try:
    content = wiki_read("log")
    has_fm = content.startswith("---")
    record("wiki/log.md YAML frontmatter 존재", has_fm)
except Exception as e:
    record("wiki/log.md YAML frontmatter 존재", False, str(e))

# ---------------------------------------------------------------------------
# 최종 결과 요약
# ---------------------------------------------------------------------------

print("\n" + "=" * 60)
print("최종 결과 요약")
print("=" * 60)

passed = sum(1 for _, s, _ in results if s == PASS)
failed = sum(1 for _, s, _ in results if s == FAIL)
total = len(results)

for name, status, msg in results:
    indicator = "[PASS]" if status == PASS else "[FAIL]"
    line = f"  {indicator} {name}"
    if msg:
        line += f" — {msg}"
    print(line)

print("-" * 60)
print(f"총 {total}개 중 {passed}개 통과, {failed}개 실패")

if failed > 0:
    sys.exit(1)
else:
    print("모든 테스트 통과.")
    sys.exit(0)
