# 의사결정 라운드 기록 (Decision Log)

> 이 문서는 프로젝트 설계 과정에서 에이전트와 사용자가 나눈 의사결정 라운드를 기록합니다.
> 과제 2번의 "Agent와 의사결정 라운드를 거쳐왔던 문서" 요구사항을 충족합니다.

---

## Round 0 — 과제 이해 및 방향 설정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

사용자가 과제 2번(MCP 서버 기반 Wiki Tool 구현)을 처음 접했을 때, 요구사항 해석에 혼란이 있었습니다.

### 논의된 질문들

**Q1. 시각화(GUI)를 구현해야 하는가?**

- 사용자 초기 이해: 불확실
- 에이전트 분석: 과제 텍스트에 "Wiki Pages를 어떤 방식으로 시각화 할 것인가", "MVP GUI를 캡쳐한 PNG" 가 명시되어 있으므로 GUI 필요
- **결론**: GUI 구현 필수. 단, MVP 수준으로 충분.

**Q2. 레퍼런스 이미지(3패널 데스크탑 앱)와 동일하게 구현해야 하는가?**

- 에이전트 분석: 레퍼런스는 Electron 또는 웹 앱으로 보임. 과제는 동일 구현을 요구하지 않음.
- **결론**: Streamlit 기반 웹 뷰어로 MVP 구현. 과제 요건 충족 가능.

**Q3. 과제 1(Agentic_Coding_Basics)과 무엇이 다른가?**

- 과제 1: Claude Code가 내장 Read/Write 도구로 파일 직접 접근
- 과제 2: MCP 서버가 도구를 제공, 에이전트는 MCP 도구만 사용
- **결론**: 핵심 차이는 MCP 서버 계층의 추가. 아키텍처적으로 더 확장 가능한 구조.

---

## Round 1 — 도메인 선정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 논의

**후보 도메인들:**
- 게임 공략 위키
- 영화/드라마 세계관
- CS 개념 (강의 무관)
- RAG, LangChain, LangGraph (LLM 애플리케이션 프레임워크)

**선택 기준:**
1. CSE-3308 강의 내용과 겹치지 않을 것
2. 개념 간 연결이 풍부할 것 (Wiki 패턴이 효과적)
3. 제작자가 실제로 관심 있고 콘텐츠를 만들기 쉬울 것

### 결정

**선택: LLM Application Frameworks & Agent Systems (RAG, LangChain, LangGraph)**

**근거:**
- 빠르게 진화하는 생태계 → 지식 누적의 가치 높음
- 개념 간 의존 관계 복잡 → Wiki 링크 구조가 유효
- 과제 주제(Agentic Coding)와 시너지 — 방법론은 같고 도메인만 다름
- 제작자가 실제로 학습하고 싶은 분야

**도메인명 확정:** "LLM Application Frameworks & Agent Systems"
- "Multi-Agent System"은 LangGraph에 특화된 용어이므로, 전체를 아우르는 상위 명칭 사용

---

## Round 2 — 시스템 아키텍처 설계

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 논의

**Q1. MCP 서버 구현 방식: stdio vs HTTP?**

| | stdio | HTTP (SSE) |
|---|---|---|
| Claude Code 통합 | 기본 지원 | 추가 설정 필요 |
| 디버깅 | 어려움 | 쉬움 (curl 테스트 가능) |
| 배포 | 단순 | 서버 실행 필요 |

**결론**: stdio 방식 채택. Claude Code와의 통합이 단순하고, 로컬 개발 환경에 적합.

**Q2. 검색 구현 방식?**

| | 단순 문자열 매칭 | TF-IDF | 임베딩 |
|---|---|---|---|
| 구현 복잡도 | 낮음 | 중간 | 높음 |
| 의존성 | 없음 | scikit-learn | API 호출 필요 |
| MVP 적합성 | ✅ | ✅ | ✗ |

**결론**: MVP는 단순 문자열 매칭(대소문자 무시). 추후 TF-IDF로 업그레이드 가능.

**Q3. 뷰어에 채팅 패널을 통합할 것인가?**

- 레퍼런스 구현은 오른쪽에 채팅 패널 포함
- Streamlit에서 채팅 패널 구현: `st.chat_input`, `st.chat_message` 사용 가능
- 단, MCP 서버와 Streamlit 간 직접 통신 설계 필요

**결론**: MVP에서는 뷰어(읽기 전용)만 구현. 에이전트 채팅은 Claude Code CLI에서 수행. 추후 통합 가능.

---

## Round 3 — 하네스 세팅 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 논의

**Q1. 하네스에 필요한 파일 목록?**

에이전트 제안:
- `CLAUDE.md` — 에이전트 운영 스키마
- `README.md` — 프로젝트 소개 및 실행 방법
- `docs/domain-definition.md` — 도메인 정의
- `docs/PRD.md` — 제품 요구사항
- `docs/decision-log.md` — 의사결정 이력 (이 파일)
- `.claude/skills/ingest.md` — 인제스트 스킬
- `.claude/skills/query.md` — 쿼리 스킬
- `.claude/skills/wiki-edit.md` — 편집 스킬
- `.github/PULL_REQUEST_TEMPLATE.md` — PR 템플릿
- `.github/ISSUE_TEMPLATE/` — 이슈 템플릿

**결론**: 위 목록 전부 작성 후 MCP 서버 구현으로 진행.

**Q2. 스킬 트리거 방식?**

- ingest: 파일명 + "인제스트/위키 만들어줘" 패턴
- query: Ingest 트리거가 아닌 모든 질문
- wiki-edit: "편집해줘", "추가해줘", "수정해줘" 명시적 요청

---

---

## Round 4 — 소스 업로드 흐름 개선

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자 지적: "사용자가 직접 raw/ 폴더에 파일을 넣으면 시각화(Streamlit 뷰어)의 의미가 없다."

### 논의

**기존 흐름의 문제:**
- 사용자가 파일 탐색기로 `raw/`에 직접 파일 복사 → Streamlit과 무관한 작업
- Streamlit은 단순 열람 도구로 전락

**개선 방향 후보:**
- A안: Streamlit에서 파일 업로드 → `raw/`에만 저장, 인제스트는 CLI에서
- B안: Streamlit에서 파일 업로드 + 채팅 패널에서 인제스트 트리거 (Claude API)
- C안: Streamlit이 업로드 + 자동 인제스트 (버튼 클릭)

### 결정

**B안 채택**: 파일 업로드 + 채팅 패널 통합

**근거:**
- 레퍼런스 구현의 3패널 구조(사이드바/본문/채팅)와 일치
- 사용자가 자연어로 인제스트 트리거 가능 → UX가 자연스럽다
- Claude API를 Streamlit에서 직접 호출하면 CLI 없이도 에이전트 기능 사용 가능

**변경된 MCP 도구:**
- `raw_save(filename, content)` 추가 — Streamlit이 업로드 파일 저장
- `raw_read(filename)` 추가 — 에이전트가 소스 읽기 (내장 Read 도구 대체)

**영향 받은 문서:**
- `docs/PRD.md` — 시나리오 1, 기능 요구사항 4.1/4.3, 아키텍처 다이어그램
- `CLAUDE.md` — MCP 도구 명세, 운영 규칙
- `README.md` — 아키텍처 다이어그램, MCP 도구 목록, 사용 방법

---

---

## Round 5 — CLAUDE.md 리팩터링 및 wiki-schema.md 분리

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자 지적: "CLAUDE.md 파일이 길어질수록 좋아 보이지 않는다. 필요 없는 건 다른 md에 작성해야 할 것 같다."

### 논의

섹션별 필요성 검토:

| 섹션 | 판단 | 근거 |
|------|------|------|
| 프로젝트 개요 | 유지 | 에이전트 컨텍스트 파악 필수 |
| 디렉토리 구조 | 축소 | `.github/` 등 에이전트 불필요 항목 포함 |
| MCP 도구 명세 | 유지 | 에이전트가 반드시 알아야 함 |
| Wiki 페이지 유형 (4개 템플릿) | **이동** | 100줄+ 템플릿, 별도 파일이 적합 |
| 스킬 테이블 | 유지 | 간결하여 문제 없음 |
| 운영 규칙 | 유지 | 에이전트 행동 지침 핵심 |
| 컨벤션 | 통합 | 운영 규칙과 중복, 흡수 |

### 결정

- Wiki 페이지 유형 4개 템플릿 → `docs/wiki-schema.md` 신규 생성 후 이동
- 컨벤션 섹션 → 운영 규칙 7·8번으로 흡수
- 디렉토리 구조 → 에이전트 관련 폴더만 축소 유지

**결과**: CLAUDE.md 222줄 → 67줄

**영향 받은 파일:**
- `CLAUDE.md` — 전면 리팩터링
- `docs/wiki-schema.md` — 신규 생성

---

## Round 6 — 스킬 파일 구조 표준화

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자 질문: "스킬 파일에 description만 있는데 name은 필요 없는 걸까?"

### 논의

레퍼런스(Agentic_Coding_Basics) 스킬 파일과 비교:

| 항목 | 기존 (LLM-Wiki) | 레퍼런스 | 문제 |
|------|----------------|---------|------|
| frontmatter | 없음 (본문 텍스트) | YAML frontmatter | Claude Code가 description을 인식 못할 수 있음 |
| name 필드 | 없음 | `name: ingest` | 스킬 식별자 누락 |
| description | 본문 텍스트 블록 | frontmatter 한 줄 | 트리거 판단에 사용되는 위치가 틀림 |

추가 발견: `ingest.md` 2단계가 "내장 Read 도구로 raw/ 읽기"로 되어 있어 Round 4 결정(raw_read MCP 도구 사용)이 미반영된 상태였음.

### 결정

- 모든 스킬 파일에 YAML frontmatter 추가 (`name` + `description`)
- `description`을 frontmatter 한 줄 트리거 조건으로 이동
- 본문 내 페이지 템플릿 제거 → `docs/wiki-schema.md` 참조로 대체
- `ingest.md` Step 2: 내장 Read → `MCP: raw_read()` 로 수정

**영향 받은 파일:**
- `.claude/skills/ingest.md`
- `.claude/skills/query.md`
- `.claude/skills/wiki-edit.md`

---

---

## Round 7 — impl/verify 에이전트 및 orchestrate 스킬 추가

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 요청

"구현 에이전트, 검증 에이전트를 만들고 이를 처리하는 오케스트레이션 스킬을 만들어서 github-issue-work에서 호출하도록 해달라"

### 논의

**구조 검증:**
- 스킬은 LLM이 따르는 지침이므로 "스킬이 스킬을 호출"한다는 것은 "해당 스킬의 지침을 따르라"는 의미
- 에이전트는 `Agent` 도구로 스폰되는 독립 서브프로세스, `.claude/agents/`에 명세 정의
- impl → verify 순서가 핵심 (역방향 불가)

**검증 실패 처리 방안:**
- A안: 무한 재시도 → 루프 위험
- B안: 1회 재시도 후 실패 시 사용자 보고 → 채택

**최종 구조:**
```
github-issue-work (Step 1~3: 파악/브랜치/계획)
    ↓ Step 4에서 위임
orchestrate (skill)
    ├── impl-agent 스폰 → 구현
    └── verify-agent 스폰 → 검증
         ├── PASS → 커밋
         └── FAIL → 1회 재시도 → 실패 시 사용자 보고
```

### 결정

- `.claude/agents/impl-agent.md` 신규 생성
- `.claude/agents/verify-agent.md` 신규 생성
- `.claude/skills/orchestrate.md` 신규 생성
- `github-issue-work.md` Step 4~5 수정 (직접 구현 → orchestrate 위임)

**영향 받은 파일:**
- `.claude/agents/impl-agent.md` — 신규
- `.claude/agents/verify-agent.md` — 신규
- `.claude/skills/orchestrate.md` — 신규
- `.claude/skills/github-issue-work.md` — Step 4~5 수정
- `CLAUDE.md` — 스킬 테이블에 orchestrate 추가

---

## 향후 라운드 예정

- **Round 8**: MCP 서버 구현 세부 결정 (wiki_store 및 raw_store 설계)
- **Round 9**: Streamlit 뷰어 UI 상세 구성 (채팅 패널 Claude API 연동 방식)
- **Round 10**: 최초 인제스트 소스 선정 및 실행
