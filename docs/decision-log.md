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

---

## Round 8 — /health 커맨드 신설 및 명칭 확정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 결정 사항

1. **하네스 검증 커맨드 신설**: `.claude/commands/validate-harness.md` 생성
   - 6개 항목 점검: 필수 파일 / 스킬 frontmatter / 에이전트 frontmatter / CLAUDE.md 일관성 / orchestrate 연결 / decision-log 최신성

2. **명칭 변경**: `validate-harness` → `health`
   - 이유: 입력 편의성 (`/health`가 더 짧고 직관적)
   - 파일명 `health.md`, 커맨드 헤더도 `# /health`로 변경

3. **로그 저장 기능 추가**: 점검 결과를 `docs/health/YYYY-MM-DD.md`로 자동 저장
   - 같은 날 재실행 시 `-2`, `-3` suffix
   - 점검 이력을 git으로 추적

**영향 받은 파일:**
- `.claude/commands/health.md` — 신규 생성 (validate-harness.md 대체)
- `CLAUDE.md` — 커맨드 섹션 추가, 디렉토리 구조에 `docs/health/` 추가
- `README.md` — 커맨드 테이블 추가

---

## Round 9 — 세션 운영 전략 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 질문

"매번 새로운 세션에서 작업하는 게 좋을까요, 아니면 `claude --resume`에서 작업하는 게 좋을까요?"

### 논의

**이 하네스의 설계 원칙 확인:**
- `CLAUDE.md`, `decision-log.md`, 스킬·에이전트 명세가 모두 파일에 기록됨
- 에이전트가 매 세션 시작 시 파일에서 프로젝트 상태를 복원 가능
- 즉, 세션 간 연속성을 파일 시스템이 대신 제공함

**결론:**

| 상황 | 방식 |
|---|---|
| 새 이슈 작업 시작 | 새 세션 |
| 이슈 작업 도중 compact 발생 | --resume |
| 이슈 완료 후 다음 이슈 | 새 세션 |
| 간단한 Wiki 질의/편집 | 새 세션 |

### 결정

**이슈 단위 = 세션 단위** 패턴 채택

- `github-issue-work` 스킬이 이슈 단위 작업으로 설계되어 있으므로 자연스럽게 일치
- `--resume`은 mid-task 중단 복구 용도로만 사용
- compact가 발생할 만큼 한 이슈가 길어진다면 이슈를 더 작게 쪼개는 신호로 간주

**영향 받은 파일:** 없음 (운영 방침 결정)

---

## Round 10 — PRD 기반 태스크 분류 및 issues-plan.md 생성

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 논의

PRD의 마일스톤(M2~M5)을 GitHub 이슈 단위로 분해하는 작업.

**분류 기준:**
- M1(하네스 세팅)은 이미 완료 → 제외
- 마일스톤 내에서 의존성이 명확한 경계에서 이슈를 분리
- 이슈 하나가 하나의 세션(이슈 단위 = 세션 단위, Round 9)에서 처리 가능한 크기

**결과: 9개 이슈 확정**

| 이슈 | 마일스톤 | 의존성 |
|------|---------|--------|
| #1 wiki_store.py | M2 | 없음 |
| #2 server.py FastMCP | M2 | #1 |
| #3 MCP 통합 테스트 | M2 | #2 |
| #4 ingest 검증 | M3 | #3 |
| #5 query 검증 | M3 | #4 |
| #6 Streamlit 기본 레이아웃 | M4 | #3 |
| #7 파일 업로드 + 채팅 패널 | M4 | #6 |
| #8 키워드 검색 | M4 | #6 |
| #9 제출용 문서 | M5 | #4~#8 |

### 결정

`docs/issues-plan.md` 신규 생성 — 각 이슈별 목표·작업 범위·완료 기준·의존성 기록

**영향 받은 파일:**
- `docs/issues-plan.md` — 신규 생성

---

## Round 11 — decision-log.md 에이전트 컨텍스트 활용 방법

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자 질문: "decision-log.md는 단순 사람만 보려는 건가? 새 세션의 Claude가 과거 결정을 알려면 어떻게 해야 하나?"

### 논의

**현재 문제:**
- `decision-log.md`는 CLAUDE.md의 디렉토리 구조에만 언급됨
- 새 세션의 Claude는 CLAUDE.md를 자동 로드하지만 decision-log를 읽으라는 지침이 없음
- 따라서 과거 결정(MCP 방식, 검색 전략, 뷰어 설계 등)의 맥락을 모름

**해결 방향:**
- CLAUDE.md는 매 세션 시스템 컨텍스트로 자동 주입됨
- CLAUDE.md 운영 규칙에 "새 세션 시작 시 decision-log.md 읽기"를 추가하면 모든 스킬에 적용
- `github-issue-work` Step 1에도 명시적으로 추가하면 이슈 작업 시 중복 확인 가능

### 결정

1. `CLAUDE.md` 운영 규칙 9번 추가: "새 세션 시작 시 `docs/decision-log.md`를 읽어 이전 의사결정 컨텍스트를 파악한다."
2. `github-issue-work.md` Step 1에 decision-log 읽기 단계 추가

**영향 받은 파일:**
- `CLAUDE.md` — 운영 규칙 9번 추가
- `.claude/skills/github-issue-work.md` — Step 1 수정

---

## Round 12 — GitHub 이슈 일괄 등록 방식 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 논의

**질문**: 9개 이슈를 등록할 때 `github-issue-create` 스킬을 9번 호출해야 하는가, 아니면 `issues-plan.md`를 읽어 한 번에 처리할 수 있는가?

**현재 스킬의 설계:**
- `github-issue-create`는 단건 대화형 — 유형 질문 → 내용 수집 → 한 건 생성
- 9번 호출 시 매번 확인 대화를 거쳐야 함

**판단:**
- `issues-plan.md`에 모든 내용이 이미 정의되어 있음
- 스킬은 ad-hoc 이슈 하나를 올릴 때 적합
- 계획된 배치 등록은 직접 `gh issue create`로 처리하는 것이 효율적

### 결정

`issues-plan.md`를 읽어 `gh issue create`로 9개 일괄 등록. 스킬 미사용.

**운영 원칙 정립:** `github-issue-create` 스킬은 사전 계획 없는 단발성 이슈에만 사용한다.

**영향 받은 파일:** 없음 (운영 방침 결정)

---

## Round 13 — skills/ 폴더 구조 유지 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 논의

**질문**: `.claude/skills/`의 스킬 파일 6개를 폴더로 분리(wiki 운영 / 개발 전용)해야 하는가?

**검토 결과:**

| 항목 | 판단 |
|------|------|
| 파일 수 | 6개 — 평탄 구조로 충분히 관리 가능 |
| Claude Code 하위 폴더 스캔 | 공식 보장 없음 — 폴더 분리 시 스킬 미인식 위험 |
| 그룹핑 방법 | CLAUDE.md 스킬 테이블이 이미 Wiki/개발 두 그룹 구분 |

### 결정

평탄 구조 유지. 스킬이 10개를 초과하거나 새 도메인 스킬 묶음이 추가될 때 재검토.

**영향 받은 파일:** 없음

---

## Round 14 — pr-review 스킬 추가

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 요청

"PR #N번 리뷰해줘를 트리거로 하는 PR 리뷰 스킬을 만들어달라"

### 설계 결정

**4개 검토 관점:**
1. **완료 기준 충족** — 이슈의 완료 기준 항목을 하나씩 대조
2. **CLAUDE.md 운영 규칙 준수** — MCP 도구만 사용, index/log 업데이트 여부 등
3. **코드 품질** — 네이밍, dead code, 에러 처리 범위
4. **범위 이탈** — 이슈 밖의 변경이 섞이지 않았는지

**판정 원칙:**
- 완료 기준 미충족 항목이 하나라도 있으면 LGTM 불가
- CLAUDE.md 규칙 위반은 코드 품질 문제보다 높은 우선순위
- 스킬은 리뷰만 수행 — 머지 실행 금지

**Step 흐름:** PR 정보 파악 → 연결 이슈 파악 → decision-log 확인 → 4관점 리뷰 → 종합 판정 보고

### 결정

`.claude/skills/pr-review.md` 신규 생성, `CLAUDE.md` 스킬 테이블에 추가

**영향 받은 파일:**
- `.claude/skills/pr-review.md` — 신규 생성
- `CLAUDE.md` — 개발 전용 스킬 테이블에 pr-review 추가

---

## Round 15 — 스킬 파일 구조 변환 (flat → subdirectory/SKILL.md)

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 발견

`Skill` 도구가 `.claude/skills/github-issue-work.md`를 인식하지 못하는 문제 발생.

### 원인 분석

Claude Code의 `Skill` 도구는 `skillname/SKILL.md` 구조(서브디렉토리 + SKILL.md)만 인식한다.
기존 프로젝트 스킬 파일은 `skillname.md` 평탄 구조였으므로 시스템 프롬프트에 주입되지 않았다.

**글로벌 스킬 구조 (작동):**
```
~/.claude/skills/harness/SKILL.md
~/.claude/skills/health/SKILL.md
```

**프로젝트 스킬 구조 (미작동):**
```
.claude/skills/github-issue-work.md  ← 인식 불가
```

### 결정

7개 스킬 파일 전부 `skillname/SKILL.md` 구조로 변환. 기존 평탄 파일 삭제.

**변환 대상:**
- `ingest.md` → `ingest/SKILL.md`
- `query.md` → `query/SKILL.md`
- `wiki-edit.md` → `wiki-edit/SKILL.md`
- `github-issue-create.md` → `github-issue-create/SKILL.md`
- `orchestrate.md` → `orchestrate/SKILL.md`
- `github-issue-work.md` → `github-issue-work/SKILL.md`
- `pr-review.md` → `pr-review/SKILL.md`

**영향 받은 파일:**
- `.claude/skills/*/SKILL.md` — 신규 생성 (내용 동일)
- `.claude/skills/*.md` — 삭제

---

## Round 16 — wiki_store.py 구현 세부 설계 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

이슈 #1 작업 중 `mcp_server/wiki_store.py` 구현 과정에서 세부 설계를 결정함.

### 결정 사항

**Q1. YAML frontmatter 파서 — PyYAML vs 표준 라이브러리?**

- **결론**: 표준 라이브러리(문자열 파싱)만 사용. `key: value` 단일 줄 형태만 지원.
- **근거**: 외부 의존성 최소화. MVP 범위에서 복잡한 YAML 구조(중첩, 콜론 포함 값 등) 불필요.

**Q2. frontmatter 직렬화 함수 필요성?**

- verify-agent가 1차 검증에서 `_serialize_frontmatter` 미구현을 FAIL 항목으로 지적.
- **결론**: `_serialize_frontmatter(meta: dict) -> str` 추가. `---\nkey: value\n---\n` 형식 반환, 빈 dict 시 `''` 반환.

**Q3. 에러 처리 방식?**

- **결론**: 존재하지 않는 리소스 접근 시 `FileNotFoundError` raise. 호출자(MCP 서버 레이어)가 핸들링하는 구조.

**Q4. `raw_save` / `raw_read` 타입?**

- **결론**: bytes 처리 (Round 4 결정 유지). Streamlit `UploadedFile.read()`가 bytes 반환하므로 변환 없이 그대로 저장.

**Q5. slug 루트 레벨 처리?**

- **결론**: `index`, `log` 같은 루트 slug는 `wiki/index.md`, `wiki/log.md`로 매핑. 카테고리 레벨(`concepts/rag`)과 동일 로직으로 처리.

### 구현 결과

- `mcp_server/__init__.py` 신규 생성
- `mcp_server/wiki_store.py` 신규 작성 (209줄), 7개 public API + 5개 내부 헬퍼
- impl-agent → verify-agent 1회 FAIL 후 재시도 → PASS (frontmatter 직렬화 추가, dead import 제거)

**영향 받은 파일:**
- `mcp_server/__init__.py` — 신규
- `mcp_server/wiki_store.py` — 신규

---

## Round 17 — orchestrate 스킬 PR 자동 생성 적용

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자: "앞으로 매번 'PR 만들어줘'라고 입력하기 귀찮다. 자동으로 만들어지게 해달라."

### 결정

orchestrate 스킬 Phase 3(PASS 처리)에서 커밋 직후 `gh pr create`를 자동 실행한다.

**변경 전:** 커밋 후 "PR을 생성하려면: 'PR 만들어줘'" 안내
**변경 후:** 커밋 후 즉시 PR 생성, URL 사용자에게 보고

**원칙 변경:**
- 기존: "사용자 승인 없이 `git push` 또는 PR 생성 금지"
- 변경: "커밋 후 PR은 자동으로 생성한다. `git push --force` 또는 머지는 여전히 금지"

**영향 받은 파일:**
- `.claude/skills/orchestrate/SKILL.md` — Phase 3 PASS 절차 및 원칙 수정

---

## Round 18 — raw/ 디렉토리 Git 관리 정책 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자: "raw 폴더 안에 있는 내용은 업로드 안되게 하되, 뭘 저장해야 하는지 설명하는 md 파일은 남기고 싶다."

### 결정

`.gitignore` 규칙 변경:
- 기존: `raw/` (디렉토리 전체 무시)
- 변경: `raw/*` (내용물 무시) + `!raw/README.md` (README 예외 추적)

`raw/README.md` 신규 생성 — 저장 대상 파일 형식, 추가 방법, 주의사항 기술.

**근거:**
- PDF 등 원본 파일은 용량이 크고 민감할 수 있어 Git 추적 불필요
- README는 협업자(또는 새 세션의 에이전트)가 `raw/` 용도를 파악하기 위해 Git 추적 필요

**영향 받은 파일:**
- `.gitignore` — `raw/` → `raw/*` + `!raw/README.md`
- `raw/README.md` — 신규 생성

---

## Round 19 — server.py FastMCP 구현 세부 결정

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

이슈 #2 작업 중 `mcp_server/server.py` 구현 과정에서 세부 설계를 결정함.

### 결정 사항

**Q1. FastMCP 패키지 선택: `fastmcp` vs 공식 `mcp` SDK?**

- **결론**: 공식 MCP Python SDK(`mcp[cli]`) 채택. `from mcp.server.fastmcp import FastMCP` 사용.
- **근거**: Anthropic 공식 패키지로 장기 지원 가능성이 높음. `fastmcp` 단독 패키지보다 호환성 우수.

**Q2. `raw_save` MCP 레이어 타입 처리?**

- MCP 프로토콜은 JSON 기반이므로 bytes를 직접 전달 불가.
- **결론**: MCP 레이어에서 `str` 수신 후 `UTF-8 bytes`로 인코딩하여 `wiki_store.raw_save`에 전달. MVP 범위에서 충분.

**Q3. `settings.json` PYTHONPATH 설정 방식?**

- `server.py`가 `from wiki_store import ...` 형태로 같은 디렉토리 내 모듈을 임포트하는 구조.
- **결론**: `settings.json`의 `env`에 `PYTHONPATH: mcp_server/` 설정. Python 실행 경로는 절대경로 사용.
- **한계**: Python 절대경로가 로컬 환경에 종속됨. 다른 환경에서는 수정 필요 (이슈 범위 허용).

**Q4. `requirements.txt` 신규 생성?**

- 기존에 `requirements.txt` 없음.
- **결론**: `mcp[cli]>=1.0.0` 명시한 `requirements.txt` 신규 생성. 이후 이슈에서 의존성 추가 예정.

### 구현 결과

- `requirements.txt` 신규 생성
- `mcp_server/server.py` 신규 작성 (7개 도구 전부 Must + Should 충족)
- `.claude/settings.json` 신규 생성 (MCP 서버 등록)
- impl → verify 1회 PASS

**영향 받은 파일:**
- `requirements.txt` — 신규
- `mcp_server/server.py` — 신규
- `.claude/settings.json` — 신규

---

## Round 20 — GUI 채팅 백엔드 아키텍처 전면 변경

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자: "GUI에서 Anthropic API를 직접 호출하면 API 키가 필요하고 비용이 발생한다. 개인 Claude Code(구독)를 사용하는 방법이 없는가?"

### 논의

**기존 설계(Round 4 B안)의 한계:**
- Streamlit → `anthropic.messages.create()` → Claude API (유료, API 키 필요)
- 사용자 입장에서 LLM Wiki를 사용하려면 Claude 구독과 별도로 API 키가 필요
- "LLM Wiki의 장점이 사라진다"는 사용자 지적

**대안 후보:**
| 방식 | API 키 필요 | MCP 연동 | 구현 난이도 |
|------|------------|---------|------------|
| Anthropic API 직접 호출 | ✅ 필요 | ✗ (별도 구현) | 낮음 |
| `claude -p` subprocess (기본 cwd) | ✗ 불필요 | ✗ (미연동 확인) | 낮음 |
| `claude -p` subprocess (cwd=root, .mcp.json) | ✗ 불필요 | ✅ 자동 로드 | 낮음 |

**검증 실험:**
- `claude -p "wiki_list 도구 호출해줘"` (cwd 미지정) → "llm-wiki MCP 서버가 연결되어 있지 않습니다" (실패)
- `subprocess.run(["claude", "-p", query], cwd=project_root)` 방식 + 프로젝트 루트의 `.mcp.json` → Claude Code가 `.mcp.json`을 읽어 MCP 서버 자동 로드 (성공 예정)

**핵심 인사이트:**
`claude -p`가 MCP를 로드하지 못했던 이유는 실행 디렉토리에 MCP 설정 파일이 없었기 때문.
`cwd`를 프로젝트 루트(`.mcp.json` 위치)로 지정하면 자동 로드된다.

**GUI 프레임워크 변경:**
- 기존: Streamlit (채팅 UI 어색, API 종속)
- 변경: **Flask + HTML** (자유도 높음, Markdown 렌더링 품질 우수, 3패널 레이아웃 정밀 제어)
- 근거: wiki/ 페이지 Markdown 렌더링(`markdown2`), 3패널 CSS Grid 레이아웃, 과제 제출용 스크린샷 품질

### 결정

1. **채팅 백엔드**: Anthropic API 직접 호출 → `subprocess(["claude", "-p", query], cwd=project_root)` 로 변경
2. **MCP 로드 방법**: 프로젝트 루트에 `.mcp.json` 신규 생성 (`.claude/settings.json`과 동일 내용)
3. **GUI 프레임워크**: Streamlit → **Flask + HTML/CSS** 로 변경
4. **페이지 열람(목록/읽기)**: MCP 경유 불필요 — `wiki_store.py` 직접 import 사용 (응답 속도 최적화)
5. **파일 업로드**: MCP `raw_save` 경유 불필요 — `wiki_store.raw_save()` 직접 호출
6. **채팅 스트리밍**: MVP 비스트리밍 (AJAX fetch → JSON 응답) 확정

**영향 받은 파일:**
- `docs/PRD.md` — v1.2, 시나리오·기능 요구사항·구조도·비기능 요구사항 전면 수정
- `docs/issues-plan.md` — Issue 6(Streamlit → Flask), Issue 7(Claude API → subprocess) 재작성
- `.mcp.json` — 신규 생성 예정 (이슈 #6 작업 시)
- `requirements.txt` — `streamlit`, `anthropic` 제거 / `flask`, `markdown2` 추가 예정

---

## Round 22 — 최초 인제스트 소스 선정 및 PDF 지원 추가

**날짜**: 2026-06-03
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

이슈 #4 작업 중 `raw/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf` (Lewis et al., 2021 원저 RAG 논문)를 인제스트 소스로 선정하여 최초 Wiki 빌드를 수행함.

### 문제 발견

`mcp_server/server.py`의 `raw_read` 도구가 `data.decode("utf-8")`로만 구현되어 있어 바이너리 PDF 파일 읽기 불가.

### 결정 사항

**Q1. 인제스트 소스 선정?**

- **결론**: `raw/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf` 사용 — RAG 개념·프레임워크·패턴이 풍부하여 LLM Wiki 도메인에 최적
- `raw/` 디렉토리에 이미 존재하는 파일 활용

**Q2. PDF 지원 방식?**

- **결론**: `mcp_server/server.py`의 `raw_read` 도구에 `.pdf` 확장자 감지 분기 추가. `pypdf.PdfReader`로 텍스트 추출 후 문자열 반환. 비-PDF 파일은 기존 UTF-8 decode 경로 유지.
- `requirements.txt`에 `pypdf>=3.0.0` 추가.
- `wiki_store.raw_read`는 bytes 반환 유지 — MCP 레이어에서만 PDF 처리 (계층 분리)

### 구현 결과

- Wiki 페이지 21개 생성 (sources/1, concepts/10, frameworks/3, patterns/7)
- 모든 페이지 YAML frontmatter + `[[slug]]` 내부 링크 포함
- `wiki/index.md`, `wiki/log.md` 갱신 완료

**영향 받은 파일:**
- `requirements.txt` — `pypdf>=3.0.0` 추가
- `mcp_server/server.py` — `raw_read` PDF 분기 추가
- `wiki/` — 21개 페이지 신규 생성 + index.md, log.md 갱신

---

## Round 21 — Flask 뷰어 기본 레이아웃 구현

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

이슈 #6 작업: Wiki 열람이 가능한 기본 Flask 앱 구현 (Round 20 결정 실행)

### 결정 사항

**Q1. 사이드바 페이지 목록 — MCP 경유 vs 직접 import?**

- **결론**: `wiki_store.wiki_list()` / `wiki_store.wiki_read()` 직접 import 사용 (MCP 경유 없음)
- **근거**: Round 20 결정 유지. 뷰어 내부 열람은 응답 속도 최적화를 위해 MCP 우회.

**Q2. `_parse_frontmatter` 내부 함수 노출?**

- `viewer/app.py`가 `wiki_store._parse_frontmatter`(내부 헬퍼)를 직접 import
- **결론**: MVP 범위에서 허용. 뷰어가 frontmatter 파싱 로직을 재사용하는 가장 단순한 방법.

**Q3. `.mcp.json` 위치 및 내용?**

- **결론**: 프로젝트 루트에 신규 생성. `.claude/settings.json`과 동일한 MCP 서버 설정 복사.
- **근거**: `claude -p` subprocess 실행 시 cwd=프로젝트루트 + `.mcp.json` 자동 로드 (Round 20 핵심 인사이트)

### 구현 결과

- `viewer/app.py` — Flask 라우팅, wiki_store 직접 import, 카테고리 그룹핑, Markdown 렌더링
- `viewer/templates/layout.html` — 사이드바 + 본문 2패널 Jinja2 템플릿
- `viewer/templates/page.html` — frontmatter 메타 + wiki-body 렌더링
- `viewer/static/style.css` — GitHub 스타일 2패널 CSS, Markdown 스타일, 반응형
- `.mcp.json` — 프로젝트 루트 신규 생성
- `requirements.txt` — flask>=3.0.0, markdown2>=2.4.0 추가

**영향 받은 파일:**
- `viewer/app.py` — 신규
- `viewer/templates/layout.html` — 신규
- `viewer/templates/page.html` — 신규
- `viewer/static/style.css` — 신규
- `.mcp.json` — 신규
- `requirements.txt` — 의존성 추가

---

## Round 23 — 채팅 패널 subprocess 설계 세부 결정

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

이슈 #7 작업: Flask 파일 업로드 + claude -p subprocess 채팅 패널 구현 (Round 20 결정 실행)

### 결정 사항

**Q1. subprocess timeout 값?**

- **결론**: `timeout=120` (2분). 인제스트처럼 MCP 도구를 여러 번 호출하는 작업이 길어질 수 있음.
- TimeoutExpired, FileNotFoundError, 일반 Exception 세 경우를 각각 처리하여 한국어 오류 메시지 반환.

**Q2. 파일 업로드 — MCP `raw_save` 경유 vs 직접 호출?**

- **결론**: `wiki_store.raw_save(filename, bytes)` 직접 호출 (MCP 불필요). Round 20 결정 유지.
- 근거: 뷰어 서버가 같은 프로세스에서 wiki_store를 import하므로 MCP 경유는 오버헤드.

**Q3. 채팅 패널 스트리밍 여부?**

- **결론**: MVP 비스트리밍 유지. AJAX fetch → JSON 응답 방식.
- 근거: Round 20 결정 유지. 스트리밍은 SSE/WebSocket 추가 구현 필요, 현재 범위 초과.

**Q4. 3패널 레이아웃 반응형 처리?**

- **결론**: 1024px 이하 화면에서 채팅 패널 숨김. 모바일에서는 2패널(사이드바 + 본문)로 fallback.

### 구현 결과

- `viewer/app.py` — /upload, /chat 라우트 추가
- `viewer/templates/layout.html` — 3패널 레이아웃 (sidebar + main + chat-panel)
- `viewer/static/style.css` — 채팅 버블, 스피너, 업로드 폼 스타일
- `viewer/static/chat.js` — 신규 생성, fetch 기반 채팅·업로드 처리

**영향 받은 파일:**
- `viewer/app.py` — /upload, /chat 라우트 추가
- `viewer/templates/layout.html` — 3패널 구조로 변경
- `viewer/static/style.css` — 채팅 패널 스타일 추가
- `viewer/static/chat.js` — 신규 생성

---

## Round 24 — 파일 업로드 UI를 채팅 패널로 통합

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자: "파일 업로드를 채팅에서 같이 진행할 수 있도록 디자인 변경. 전송 height와 메시지 box height가 맞지 않기 때문에 사이즈 조정."

### 논의

**기존 구조의 문제:**
- 파일 업로드 폼이 사이드바 하단에 분리되어 있어 "업로드 → 채팅 인제스트 요청" 흐름이 단절됨
- 채팅 입력 영역이 `textarea + 전송버튼`을 flex 행으로 배치 → 높이 불일치

**개선 방향:**
- 파일 업로드를 채팅 패널 입력 영역으로 이동 → 업로드 후 바로 채팅으로 인제스트 요청 가능
- 레이아웃 구조를 flex 행(textarea + 버튼)에서 열(textarea 위, 툴바 아래)로 변경

### 결정

**레이아웃 변경:**
- `textarea` (전체 너비) + `[📎 파일 첨부] [전송]` 툴바 행으로 분리
- 파일 선택 시 textarea 위에 파란 칩(📄 파일명 ✕) 표시
- 전송 클릭 시: 파일 있으면 `POST /upload` 먼저 → 결과를 채팅 버블로 표시 → 메시지 있으면 `POST /chat`

**UX 흐름 통합:**
- 파일 업로드 성공·실패 결과가 채팅 버블로 표시되어 대화 맥락 유지

**영향 받은 파일:**
- `viewer/templates/layout.html` — 사이드바 업로드 폼 제거, 채팅 패널 입력 영역에 파일 첨부 버튼·칩 추가
- `viewer/static/style.css` — 업로드 섹션 스타일 제거, chat-toolbar·chat-file-chip·chat-bubble.system 추가
- `viewer/static/chat.js` — 업로드·채팅 단일 submit 핸들러로 통합

---

## Round 25 — subprocess MCP 도구 권한 처리 방식 결정

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

채팅 패널에서 인제스트 요청 시 Claude subprocess가 MCP 도구 사용 권한을 요청하는 메시지를 응답으로 반환함.

> "MCP 도구 권한이 필요합니다. 사용자 설정에서 `mcp__llm-wiki__*` 도구들을 허용해 주시면 인제스트를 진행할 수 있습니다."

### 논의

**후보 A: `--dangerously-skip-permissions`**
- 모든 도구 권한을 일괄 허용 (Bash 포함)
- 비대화형 subprocess 표준 패턴
- 단점: Bash·Write 등 파일시스템/실행 도구까지 열림 → 보안 위험

**후보 B: `--allowedTools <도구목록>`**
- 필요한 MCP 도구 7개만 명시적으로 허용
- 나머지 도구(Bash, Write, Edit 등)는 차단 상태 유지
- 단점: 목록 관리 필요

### 결정

**`--allowedTools` 채택** (후보 B)

허용 목록: `mcp__llm-wiki__wiki_list`, `wiki_read`, `wiki_write`, `wiki_search`, `wiki_delete`, `raw_save`, `raw_read` 7개.

**근거:** 채팅 패널은 Wiki 관련 작업만 수행해야 함. `--dangerously-skip-permissions`는 이 프로젝트 범위 이상의 권한을 열어주므로 부적절.

**영향 받은 파일:**
- `viewer/app.py` — `/chat` 라우트의 subprocess 호출에 `--allowedTools` 인수 추가

---

## Round 26 — AJAX 네비게이션 도입으로 채팅 패널 상태 유지

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 문제 제기

사용자: "다른 페이지로 이동하면 chat도 리렌더링이 되어 이전 대화는 사라지지만 claude 코드는 계속 돌아간다."

### 논의

**근본 원인:**
사이드바·본문 내 링크 클릭이 전체 페이지 리로드를 발생시켜 채팅 패널 DOM이 초기화됨.

**해결 후보:**
| 방식 | 구현 복잡도 | 채팅 유지 | URL 갱신 | 뒤로가기 |
|------|-----------|---------|---------|---------|
| localStorage 저장 후 복원 | 낮음 | 지연 복원 (flash 있음) | ✅ | ✅ |
| AJAX 네비게이션 | 중간 | ✅ (DOM 유지) | ✅ (pushState) | ✅ (popstate) |

**AJAX 방식 설계:**
- `GET /api/page/<slug>` — 본문 HTML만 JSON으로 반환 (레이아웃 없음)
- 사이드바 `.nav-link` 클릭 인터셉트 → fetch → `.main-content` innerHTML 교체
- 마크다운 본문 내 `/page/*` 링크: **이벤트 위임**으로 처리 (AJAX 교체 후에도 동작)
- URL: `history.pushState` / 뒤로가기: `popstate` 이벤트 처리

**`_content.html` partial 분리 이유:**
`/api/page/` 엔드포인트와 기존 `/page/` 라우트가 동일한 본문 HTML을 공유하기 위해 Jinja2 partial(`_content.html`)로 추출. `page.html`은 이를 `{% include %}`로 사용.

### 결정

**AJAX 네비게이션 채택**

1. `viewer/templates/_content.html` — 본문 렌더링 partial (신규)
2. `viewer/app.py` — `/api/page/<path:slug>` JSON 엔드포인트 추가
3. `viewer/static/chat.js` — 사이드바 링크 인터셉트 + 본문 내 링크 이벤트 위임 추가
4. `viewer/templates/page.html` — `_content.html` include로 단순화

**영향 받은 파일:**
- `viewer/templates/_content.html` — 신규
- `viewer/templates/page.html` — _content.html include로 교체
- `viewer/app.py` — /api/page/ 엔드포인트 추가
- `viewer/static/chat.js` — AJAX 네비게이션 로직 추가

---

## Round 27 — 키워드 검색 구현 설계 결정

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

이슈 #8 작업: 사이드바 키워드 검색 기능 구현 (V-05)

### 결정 사항

**Q1. 검색 백엔드 — MCP `wiki_search` 호출 vs 직접 import?**

- **결론**: `wiki_store.wiki_search()` 직접 import 사용. MCP 경유 없음.
- **근거**: Round 20 방침 유지 — 뷰어 내부 열람·검색은 응답 속도 최적화를 위해 MCP 우회.

**Q2. 검색 UX — 버튼 클릭 vs 실시간 디바운스?**

- **결론**: 300ms 디바운스 실시간 검색. 별도 전송 버튼 없음.
- **근거**: 검색 결과가 수백 ms 내에 반환되므로 버튼이 불필요. 타이핑 중 즉시 피드백이 UX에 더 자연스러움.

**Q3. 결과 클릭 시 페이지 이동 방식?**

- **결론**: Round 26에서 확립한 `navigateTo(slug)` AJAX 함수 그대로 재사용.
- **근거**: 전체 페이지 리로드 없이 본문만 교체되어 채팅 패널 상태가 유지됨. 코드 중복 없음.

**Q4. 결과 표시 영역 위치?**

- **결론**: 사이드바 검색 입력창 아래 `position: absolute` 드롭다운으로 표시. `z-index: 100`으로 nav 목록 위에 오버레이.
- **근거**: 별도 패널 분할 없이 공간 효율적으로 결과 표시 가능. 외부 클릭·Escape 키로 닫힘.

**Q5. 내부 slug(`index`, `log`) 처리?**

- **결론**: 기존 `_HIDDEN_SLUGS` 상수 재사용하여 검색 결과에서도 제외.
- **근거**: 사이드바 네비게이션과 동일한 필터링 기준을 검색에도 적용하여 일관성 유지.

### 구현 결과

- `viewer/app.py` — `GET /api/search?q=<query>` 엔드포인트 추가
- `viewer/templates/layout.html` — 사이드바 헤더 아래 검색 입력창 + 결과 영역 추가
- `viewer/static/style.css` — 검색창, 드롭다운 결과 스타일 추가
- `viewer/static/chat.js` — 디바운스 검색 로직, 결과 렌더링, 클릭 핸들러 추가

**영향 받은 파일:**
- `viewer/app.py` — /api/search 엔드포인트 추가
- `viewer/templates/layout.html` — 검색 UI 추가
- `viewer/static/style.css` — 검색 스타일 추가
- `viewer/static/chat.js` — 검색 로직 추가

---

## Round 28 — wiki-check 스킬 신설 및 CLAUDE.md 문서 정합성 정리

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

M4 완료 후 Wiki 콘텐츠 상태를 자연어로 점검할 수 있는 스킬이 필요하다는 요청. 동시에 CLAUDE.md에 Streamlit·FastMCP 등 구현 변경 이전의 표현이 남아 있어 정리.

### 결정 사항

**Q1. wiki-check 스킬의 점검 대상?**

- **결론**: Wiki 콘텐츠 데이터(페이지 수·카테고리·frontmatter·내부 링크·검색 기능)를 대상으로 한다.
- **근거**: 기존 `/health` 커맨드는 하네스 파일 구조(스킬·에이전트·CLAUDE.md 일관성)를 점검. wiki-check는 그와 별개로 Wiki 데이터 품질을 점검하는 역할로 명확히 분리.

**Q2. wiki-check 스킬의 도구 사용 원칙?**

- **결론**: 모든 조회를 MCP 도구(`wiki_list`, `wiki_read`, `wiki_search`)로만 수행. 내장 Read 도구 사용 금지.
- **근거**: CLAUDE.md 운영 규칙 1번 유지 — 에이전트는 파일시스템에 직접 접근하지 않는다.

**Q3. wiki-check 결과 처리 — 자동 수정 vs 보고만?**

- **결론**: 보고만 수행. 수정 금지.
- **근거**: 점검과 수정을 분리해야 사용자가 판단 후 `wiki-edit` 스킬로 선택적으로 수정 가능. 자동 수정은 의도치 않은 페이지 변경 위험이 있음.

**Q4. CLAUDE.md 잔재 표현 정리 범위?**

- **결론**: 구현과 직접 관련된 설명 3곳만 수정.
  - `mcp_server/` 설명: "FastMCP 기반" → "mcp[cli] 기반"
  - `viewer/` 설명: "Streamlit Wiki 뷰어 (구현 예정)" → "Flask Wiki 뷰어 (3패널)"
  - `raw/` 설명: "Streamlit 업로드로만 추가" → "Flask 채팅 패널 업로드로만 추가"
  - `raw_save` MCP 도구 설명: "Streamlit 호출" → "Flask viewer 호출"

### 구현 결과

- `.claude/skills/wiki-check/SKILL.md` — 신규 생성 (5단계 점검 절차)
- `CLAUDE.md` — wiki-check 스킬 테이블 등록, Streamlit·FastMCP 잔재 표현 4곳 수정

**영향 받은 파일:**
- `.claude/skills/wiki-check/SKILL.md` — 신규 생성
- `CLAUDE.md` — 스킬 테이블 추가, 문서 표현 정리

---

## Round 29 — M5 제출용 README.md 전면 개편

**날짜**: 2026-06-04
**참여자**: 사용자, Claude Sonnet 4.6

### 맥락

M5(문서화) 단계에서 과제 제출 요건 충족을 위해 README.md를 전면 재편성. 기존 README는 시스템 아키텍처 중심으로 작성되어 있어, 프로젝트 소개·환경 세팅·실행 방법·개발 워크플로·MCP 도구 동작 흐름이 불완전하거나 분산되어 있었음.

### 결정 사항

**Q1. README 섹션 구성 기준?**

- **결론**: 독자 여정 순서로 재편성. 프로젝트 소개 → 아키텍처 → 환경 세팅 → 실행 방법 → 사용 방법 → 개발 방법 → MCP 도구 → 폴더 구조 순.
- **근거**: 처음 보는 독자(과제 채점자 포함)가 위에서 아래로 읽으면 전체 맥락을 순서대로 파악할 수 있어야 함.

**Q2. MCP 도구 섹션에 동작 흐름 추가 여부?**

- **결론**: 인제스트·질의응답·Wiki 편집 3가지 흐름을 의사코드 형태로 추가.
- **근거**: 도구 목록만으로는 "MCP 서버가 어떻게 작동하는지"를 설명하지 못함. 호출 주체(에이전트 vs Flask 뷰어)와 순서를 명시해야 과제 요구사항인 "MCP 도구 동작 방식 기술"을 충족.

**Q3. 개발 워크플로(github-issue-work, orchestrate 등)를 README에 포함할 것인가?**

- **결론**: 포함. "프로젝트 개발 방법" 섹션으로 독립.
- **근거**: 이 프로젝트는 코드 산출물뿐 아니라 에이전트 기반 개발 프로세스 자체가 과제의 평가 대상. impl-agent → verify-agent 핑퐁 구조, 이슈 단위 작업 방식을 명시적으로 문서화.

### 구현 결과

- `README.md` — 전면 개편 (140줄 추가, 44줄 제거)
  - 프로젝트 소개: 기술 스택 표, 주요 기능 표 신설
  - 환경 세팅: git clone + 사전 설치 요구사항 분리
  - MCP 도구: 호출 주체 컬럼 추가, 동작 흐름 3종 추가
  - 프로젝트 개발 방법: 이슈 등록 → 이슈 작업 → 건강 체크 → PR 리뷰 섹션 신설

**영향 받은 파일:**
- `README.md` — 전면 개편
