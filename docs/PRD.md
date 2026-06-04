# PRD — LLM Wiki: MCP 서버 기반 Wiki Tool

**작성일**: 2026-06-03
**최종 수정**: 2026-06-04
**작성자**: Wiki Agent (Claude Sonnet 4.6)
**상태**: v1.3 — 실제 구현 기준으로 전면 업데이트

---

## 1. 배경 및 목적

### 문제 정의

RAG, LangChain, LangGraph 생태계는 빠르게 진화하며 개념 간 의존 관계가 복잡합니다. 개발자가 이 기술들을 학습할 때 직면하는 문제:

1. **파편화된 정보**: 공식 문서, 블로그, 논문이 분산되어 있음
2. **컨텍스트 부재**: 개념이 *왜*, *언제* 필요한지 설명이 부족
3. **지식 누적 없음**: 학습할 때마다 처음부터 검색해야 함

### 해결 방안

MCP 서버를 중간 계층으로 두고, LLM 에이전트가 구조화된 Wiki를 자동으로 축적·관리하게 합니다. 사용자는 자연어로 질문하거나 소스를 추가하기만 하면 됩니다.

---

## 2. 목표 (Goals)

### Primary Goals

- [x] MCP 서버를 통해 Wiki 페이지를 CRUD할 수 있는 도구 제공
- [x] Flask UI 채팅 패널에서 파일 업로드 → `wiki_store.raw_save` 직접 호출 → 에이전트 인제스트 트리거
- [x] 에이전트가 소스 문서를 읽고 Wiki를 자동 생성하는 Ingest 워크플로우 구현
- [x] 에이전트가 Wiki를 참조하여 자연어 질문에 답변하는 Query 워크플로우 구현
- [x] Flask 기반 Wiki 뷰어 (파일 업로드 + 채팅 패널 + 페이지 열람 + 키워드 검색) 구현

### Secondary Goals

- [ ] Wiki 페이지 간 링크 일관성 검증 (`/lint`)
- [x] 위키 편집 이력 추적 (`wiki/log.md`)

### Non-Goals

- LLM 모델 학습 또는 파인튜닝
- 실시간 웹 크롤링
- 다중 사용자 동시 편집

---

## 3. 사용자 시나리오

### 시나리오 1: 소스 인제스트 (UI 기반 전체 흐름)

```
[1단계 — 채팅 패널에서 파일 업로드]
사용자: 우측 채팅 패널 하단 "📎 파일 첨부" 버튼으로 PDF/MD 파일 선택
       → 파일 칩(📄 파일명) 표시 후 "전송" 클릭
Flask: wiki_store.raw_save(filename, bytes) 직접 호출 → raw/{filename} 저장
채팅 패널: "✅ {파일명} 업로드 완료" 시스템 버블 표시

[2단계 — 채팅 패널에서 인제스트 트리거]
사용자: 채팅 패널에 "langchain-docs.pdf 인제스트해줘" 입력
Flask: subprocess.run(["claude", "-p", <질문>, "--allowedTools", <MCP 도구 목록>],
       cwd=project_root) 호출
       → .mcp.json 자동 로드 → MCP 도구로 ingest 스킬 트리거

[3단계 — 에이전트 인제스트]
에이전트:
  1. MCP wiki_list() 로 기존 페이지 확인
  2. MCP raw_read(filename) 로 업로드된 소스 읽기
  3. 핵심 개념 추출
  4. MCP wiki_write() 로 신규/업데이트 페이지 저장
  5. MCP wiki_write("index") 로 인덱스 업데이트
  6. MCP wiki_write("log") 로 이력 기록

[4단계 — 결과 확인]
채팅 패널: 생성된 페이지 목록을 assistant 버블로 표시
사용자: 사이드바에서 생성된 Wiki 페이지 즉시 열람 가능 (페이지 이동은 AJAX)

결과: 10~15개 Wiki 페이지 생성
```

### 시나리오 2: 개념 질문

```
사용자: "RAG와 Fine-tuning의 차이가 뭐야?"

에이전트:
  1. MCP wiki_search("RAG fine-tuning") 로 관련 페이지 검색
  2. MCP wiki_read("concepts/rag") 로 페이지 읽기
  3. 답변 합성 및 출처 링크 포함

결과: Wiki 기반 구조화된 답변
```

### 시나리오 3: Wiki 뷰어 (3패널 UI)

```
사용자: python viewer/app.py 실행 → http://localhost:5000 접속

뷰어 레이아웃:
  [좌] 사이드바
       - 키워드 검색창 (실시간 디바운스, 제목 일치 우선 정렬)
       - 전체 페이지 목록 (카테고리별: 개념/프레임워크/패턴/출처)

  [중] 본문 패널
       - 선택한 Wiki 페이지 Markdown 렌더링
       - 내부 링크 클릭 시 AJAX로 본문만 교체 (채팅 패널 상태 유지)

  [우] 채팅 패널
       - 파일 첨부 버튼 (📎) + 채팅 입력창 통합 UI
       - subprocess claude -p 기반 채팅 인터페이스 (API 호출 없음)
       - cwd=project_root → .mcp.json 자동 로드 → MCP 도구 사용
       - 인제스트 트리거: "파일명 인제스트해줘"
       - 질의응답: "RAG란 무엇인가요?"
       - Wiki 편집 요청: "LangGraph 페이지 수정해줘"
```

---

## 4. 기능 요구사항

### 4.1 MCP 서버

| ID | 기능 | 우선순위 | 상태 |
|----|------|---------|------|
| F-01 | `wiki_list()` — 전체 페이지 slug 목록 반환 | Must | ✅ 완료 |
| F-02 | `wiki_read(slug)` — 페이지 내용 반환, 없으면 에러 | Must | ✅ 완료 |
| F-03 | `wiki_write(slug, content)` — 생성/덮어쓰기 | Must | ✅ 완료 |
| F-04 | `wiki_search(query)` — 제목·본문 키워드 검색 | Must | ✅ 완료 |
| F-05 | `wiki_delete(slug)` — 페이지 삭제 | Should | ✅ 완료 |
| F-06 | `raw_save(filename, content)` — 업로드 파일을 `raw/`에 저장 | Must | ✅ 완료 |
| F-07 | `raw_read(filename)` — `raw/` 파일 내용 반환 (에이전트 인제스트용) | Must | ✅ 완료 |

### 4.2 Wiki 에이전트 스킬

| ID | 스킬 | 트리거 조건 | 우선순위 | 상태 |
|----|------|------------|---------|------|
| S-01 | **ingest** | 파일 추가/인제스트 요청 | Must | ✅ 완료 |
| S-02 | **query** | 개념·기술 질문 | Must | ✅ 완료 |
| S-03 | **wiki-edit** | 특정 페이지 편집 요청 | Should | ✅ 완료 |

### 4.3 Flask 뷰어

| ID | 기능 | 우선순위 | 상태 |
|----|------|---------|------|
| V-01 | 사이드바 페이지 목록 표시 (카테고리별) | Must | ✅ 완료 |
| V-02 | 중앙 패널 Markdown 렌더링 (헤더, 코드블록, 리스트, 표) | Must | ✅ 완료 |
| V-03 | 채팅 패널 파일 첨부 → `wiki_store.raw_save` 직접 호출 (MCP 경유 없음) | Must | ✅ 완료 |
| V-04 | 우측 채팅 패널 — `subprocess(claude -p, --allowedTools, cwd=root)` 기반 대화 인터페이스 | Must | ✅ 완료 |
| V-05 | 사이드바 키워드 검색 → `wiki_store.wiki_search()` 직접 호출, 제목 일치 우선 정렬 | Should | ✅ 완료 |
| V-06 | 페이지 간 내부 링크 AJAX 이동 (채팅 패널 상태 유지) | Could | ✅ 완료 |

---

## 5. 비기능 요구사항

| 항목 | 요구사항 |
|------|---------|
| **응답 시간** | wiki_read/write 100ms 이내 |
| **저장 형식** | UTF-8 Markdown (.md) |
| **호환성** | Python 3.11+, mcp[cli] 1.0+, Flask 3.0+, markdown2 2.4+ |
| **확장성** | 슬러그 기반 구조로 카테고리 추가 용이 |
| **보안** | subprocess `--allowedTools`로 MCP 도구 7개만 허용 (Bash/Write 등 차단) |

---

## 6. 시스템 구조

```
┌─────────────────────────────────────────────────────────────────┐
│                Flask 뷰어 (viewer/app.py :5000)                  │
│  ┌──────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │   사이드바    │  │   본문 패널    │  │      채팅 패널         │ │
│  │ 키워드 검색   │  │  MD 렌더링     │  │  파일 첨부 + 입력창   │ │
│  │ 페이지 목록   │  │  (markdown2)  │  │  subprocess           │ │
│  │ (카테고리별)  │  │  AJAX 교체    │  │  ["claude","-p",      │ │
│  │              │  │               │  │   "--allowedTools",..]│ │
│  └──────┬───────┘  └───────┬────────┘  └──────────┬────────────┘ │
└─────────┼──────────────────┼───────────────────────┼────────────┘
          │ wiki_store        │ wiki_store             │ cwd=root
          │ 직접 import        │ 직접 import             │ .mcp.json 자동 로드
          ▼                  ▼                        ▼
     ┌──────────┐       ┌──────────┐      ┌────────────────────────┐
     │  raw/    │       │  wiki/   │◄─────│  MCP 서버 (mcp[cli])   │
     │ 원본 파일 │       │  *.md    │      │  wiki_list  wiki_read  │
     └──────────┘       └──────────┘      │  wiki_write wiki_search│
                                          │  wiki_delete raw_save  │
                                          │  raw_read              │
                                          └────────────────────────┘
```

---

## 7. 마일스톤

| 단계 | 목표 | 산출물 | 상태 |
|------|------|--------|------|
| **M1: 하네스 세팅** | 프로젝트 구조 및 문서 완성 | CLAUDE.md, README, docs/, skills, .github/ | ✅ 완료 |
| **M2: MCP 서버** | 7개 도구 구현 및 테스트 | `mcp_server/wiki_store.py`, `mcp_server/server.py` | ✅ 완료 |
| **M3: 에이전트** | Ingest + Query 스킬 동작 확인 | Wiki 페이지 21개 생성 | ✅ 완료 |
| **M4: 뷰어** | Flask 앱 실행 + 전체 기능 동작 | `viewer/app.py`, 3패널 UI, 검색, AJAX 네비게이션 | ✅ 완료 |
| **M5: 문서화** | 제출용 문서 4종 완성 | 압축 파일 | 진행 중 |

---

## 8. 열린 질문 (Open Questions)

- ~~`wiki_search`의 검색 방식: 단순 문자열 매칭(MVP) vs TF-IDF(추후)?~~ → **MVP 문자열 매칭 확정, 제목 일치 우선 정렬 추가** (Round 2, 27)
- ~~MCP 서버를 stdio 방식으로 실행할 것인가, HTTP 방식으로 실행할 것인가?~~ → **stdio 확정** (Round 2)
- ~~GUI 채팅 백엔드: Anthropic API 직접 호출 vs subprocess?~~ → **`subprocess(claude -p, --allowedTools)` 확정** (Round 20, 25)
- ~~GUI 프레임워크: Streamlit vs Flask?~~ → **Flask + HTML/CSS 확정** (Round 20)
- ~~파일 업로드 위치: 사이드바 vs 채팅 패널?~~ → **채팅 패널 통합 확정** (Round 24)
- ~~페이지 이동 시 채팅 패널 상태 유지 방법?~~ → **AJAX 네비게이션(history.pushState) 확정** (Round 26)
