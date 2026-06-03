# GitHub Issues Plan — LLM Wiki

> PRD 기반 작업 분류. M1(하네스 세팅)은 완료. M2~M5를 이슈 단위로 분리.
> 작성일: 2026-06-03

---

## M2 — MCP 서버 구현

### Issue 1: [M2] wiki_store.py — 파일 기반 저장소 레이어 구현

**목표**: `wiki/` 및 `raw/` 디렉토리를 관리하는 Python 저장소 모듈 구현

**작업 범위**
- `mcp_server/wiki_store.py` 신규 작성
- slug → 파일 경로 매핑 (`wiki/{category}/{name}.md`)
- YAML frontmatter 파싱 및 직렬화
- 페이지 목록 반환 (slug 리스트)
- 키워드 검색: 제목·본문 대소문자 무시 문자열 매칭
- `raw/` 파일 저장·읽기 (bytes)

**완료 기준**
- `wiki_store.py` 단독 import 시 에러 없음
- 기본 CRUD 동작 수동 확인

**참고**
- MCP 도구 명세: `CLAUDE.md` > MCP 도구 명세 섹션
- Round 2 결정: 검색은 단순 문자열 매칭(MVP)

---

### Issue 2: [M2] server.py — FastMCP 7개 도구 구현

**목표**: FastMCP를 사용하여 7개 MCP 도구를 stdio 방식으로 서빙하는 서버 구현

**작업 범위**
- `mcp_server/server.py` 신규 작성
- 도구 구현:
  - `wiki_list()` — 전체 slug 목록 반환 (F-01)
  - `wiki_read(slug)` — 페이지 내용 반환, 없으면 에러 (F-02)
  - `wiki_write(slug, content)` — 생성/덮어쓰기 (F-03)
  - `wiki_search(query)` — 키워드 검색 (F-04)
  - `wiki_delete(slug)` — 페이지 삭제 (F-05)
  - `raw_save(filename, content)` — `raw/`에 파일 저장 (F-06)
  - `raw_read(filename)` — `raw/` 파일 내용 반환 (F-07)
- FastMCP stdio 방식 실행 (`if __name__ == "__main__"`)
- `.claude/settings.json`에 MCP 서버 등록

**완료 기준**
- `python mcp_server/server.py` 실행 시 에러 없음
- Claude Code에서 `wiki_list()` 호출 성공

**참고**
- Round 2 결정: stdio 방식 채택
- 우선순위: Must 도구(F-01~F-04, F-06~F-07) 먼저, F-05(wiki_delete)는 Should

---

### Issue 3: [M2] MCP 서버 통합 테스트 및 Claude Code 연동 확인

**목표**: 7개 도구가 실제 Claude Code 세션에서 올바르게 동작하는지 검증

**작업 범위**
- 각 도구별 호출 시나리오 수동 테스트
  - `wiki_write` → `wiki_read` → `wiki_list` → `wiki_delete` 순서
  - `raw_save` → `raw_read` 순서
  - `wiki_search` 검색어 매칭 확인
- 에러 케이스 확인: 없는 slug 읽기, 없는 파일 읽기
- `wiki/index.md`, `wiki/log.md` 초기 파일 생성

**완료 기준**
- 모든 Must 도구 정상 동작 확인
- `wiki/index.md`, `wiki/log.md` 파일 존재

---

## M3 — 에이전트 스킬 검증

### Issue 4: [M3] ingest 스킬 엔드투엔드 검증

**목표**: 실제 소스 파일을 업로드하여 ingest 워크플로우 전체 실행 및 Wiki 페이지 생성 확인

**작업 범위**
- 샘플 소스 파일 선정 (LangChain/LangGraph 공식 문서 발췌 MD 또는 PDF)
- `raw_save`로 소스 저장
- ingest 스킬 트리거: "[파일명] 인제스트해줘"
- 생성된 Wiki 페이지 목록 및 내용 검토
- `wiki/index.md`, `wiki/log.md` 업데이트 확인

**완료 기준**
- Wiki 페이지 20개 이상 생성
- YAML frontmatter 포함, 내부 링크(`[[slug]]`) 사용
- `wiki/index.md` 갱신 확인

**참고**
- wiki-schema.md: 페이지 유형별 템플릿
- ingest 스킬: `.claude/skills/ingest.md`

---

### Issue 5: [M3] query 스킬 동작 검증

**목표**: 생성된 Wiki를 참조한 자연어 질의응답이 올바르게 동작하는지 확인

**작업 범위**
- Issue 4에서 생성된 Wiki 기반으로 질의 3가지 이상 테스트
  - 단순 개념 질문: "RAG란 무엇인가?"
  - 비교 질문: "RAG와 Fine-tuning의 차이는?"
  - 연결 질문: "LangChain에서 LangGraph가 왜 필요한가?"
- 답변에 출처 링크(`[[slug]]`) 포함 여부 확인
- `wiki_search` → `wiki_read` 순서로 MCP 도구 사용하는지 확인

**완료 기준**
- 3개 이상 질의에 대해 Wiki 기반 답변 생성
- 답변에 출처 slug 포함

---

## M4 — Streamlit 뷰어 구현

### Issue 6: [M4] Flask 기본 레이아웃 — 사이드바 + 본문 패널 (V-01, V-02)

**목표**: Wiki 열람이 가능한 기본 Flask 앱 구현

**작업 범위**
- `viewer/` 디렉토리 구조 신규 생성:
  - `viewer/app.py` — Flask 라우팅
  - `viewer/templates/` — Jinja2 HTML 템플릿
  - `viewer/static/` — CSS 스타일
- 사이드바 (V-01):
  - `wiki_store.wiki_list()` 직접 import로 페이지 목록 로드 (MCP 경유 없음)
  - 카테고리별 그룹핑 (slug prefix 기준: `concepts/`, `frameworks/` 등)
  - 페이지 클릭 시 선택
- 중앙 본문 패널 (V-02):
  - `wiki_store.wiki_read(slug)` 직접 호출
  - `markdown2` 라이브러리로 서버 사이드 렌더링 (헤더, 코드블록, 리스트)
- `requirements.txt`에 `flask`, `markdown2` 의존성 추가

**완료 기준**
- `flask --app viewer/app.py run` 실행 후 localhost:5000 접근 가능
- 페이지 목록 표시 및 클릭 시 내용 렌더링 확인

---

### Issue 7: [M4] 파일 업로드 + claude -p subprocess 채팅 패널 연동 (V-03, V-04)

**목표**: Flask에서 파일 업로드 후 채팅으로 인제스트 트리거 가능한 UI 완성

**작업 범위**
- 파일 업로드 패널 (V-03):
  - 사이드바 HTML form에 파일 업로드 입력 추가 (PDF, MD, TXT)
  - Flask `/upload` 라우트에서 `wiki_store.raw_save(filename, content)` 직접 호출
  - 업로드 완료 알림 표시
- 채팅 패널 (V-04):
  - 우측 패널에 HTML 채팅 입력창 + 메시지 목록 배치
  - Flask `/chat` 라우트에서 subprocess 방식으로 Claude Code 호출:
    ```python
    result = subprocess.run(
        ["claude", "-p", query],
        capture_output=True, text=True, encoding="utf-8",
        cwd="<project_root>"  # .mcp.json 위치
    )
    ```
  - `.mcp.json` 자동 로드 → MCP 도구로 wiki/ 접근 후 응답 반환
  - MVP 비스트리밍 (AJAX fetch → JSON 응답)
  - 로딩 표시: 요청 중 스피너 표시

**완료 기준**
- 파일 업로드 후 `raw/` 디렉토리에 저장 확인
- 채팅 패널에서 "인제스트해줘" 입력 시 claude -p subprocess 응답 반환
- MCP 도구(`wiki_list`, `wiki_search` 등)가 subprocess 내에서 호출되는지 확인

**참고**
- Round 4 결정: B안 (파일 업로드 + 채팅 패널 통합)
- Round 20 결정: Claude API 직접 호출 → subprocess claude -p + .mcp.json 방식으로 변경

---

### Issue 8: [M4] 키워드 검색 구현 (V-05)

**목표**: 사이드바 검색창에서 Wiki 페이지를 키워드로 검색하는 기능 추가

**작업 범위**
- 사이드바에 `st.text_input` 검색창 추가
- 입력값으로 `wiki_search(query)` MCP 호출
- 검색 결과 목록 표시 → 클릭 시 본문 패널에 렌더링

**완료 기준**
- 검색어 입력 후 관련 페이지 목록 표시
- 결과 클릭 시 본문 패널에 렌더링

**참고**
- V-06 (내부 링크 클릭 이동)은 Could 우선순위이므로 시간 여유 시 포함

---

## M5 — 문서화

### Issue 9: [M5] 제출용 문서 4종 완성

**목표**: 과제 제출 요건 충족을 위한 최종 문서 정리

**작업 범위**
- 제출 요건 재확인 후 누락 항목 작성
- `README.md` 최종 업데이트 (실행 방법, 스크린샷 경로 포함)
- MVP GUI 스크린샷 캡처 및 저장 (`docs/screenshots/`)
- `docs/decision-log.md` 최종 Round 추가 (MCP 서버 및 뷰어 구현 결정 사항)
- 압축 파일 구성 확인

**완료 기준**
- 제출 요건의 문서 4종 모두 존재
- MVP 스크린샷 1장 이상 포함

---

## 우선순위 요약

| 이슈 | 마일스톤 | 우선순위 | 의존성 | 비고 |
|------|---------|---------|--------|------|
| Issue 1 | M2 | 1 | 없음 | |
| Issue 2 | M2 | 2 | Issue 1 | |
| Issue 3 | M2 | 3 | Issue 2 | |
| Issue 4 | M3 | 4 | Issue 3 | |
| Issue 5 | M3 | 5 | Issue 4 | |
| Issue 6 | M4 | 6 | Issue 3 | Flask 기본 레이아웃 (wiki_store.py 직접 import) |
| Issue 7 | M4 | 7 | Issue 6 | 파일 업로드 + subprocess 채팅 (claude -p) |
| Issue 8 | M4 | 8 | Issue 6 | |
| Issue 9 | M5 | 9 | Issue 4~8 | |
