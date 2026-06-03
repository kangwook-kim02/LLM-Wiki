# LLM Wiki — Agent Schema

이 파일은 에이전트 운영 규칙을 정의합니다. 에이전트와 협의 없이 직접 수정하지 마세요.

---

## 프로젝트 개요

**도메인**: LLM Application Frameworks & Agent Systems (RAG, LangChain, LangGraph)
**목표**: MCP 서버 기반 Wiki 도구를 통해 지식을 자동으로 축적·서빙

---

## 디렉토리 구조

```
.
├── CLAUDE.md              ← 이 파일
├── README.md
├── .gitignore
│
├── docs/                  ← 설계 문서
│   ├── domain-definition.md
│   ├── PRD.md
│   ├── decision-log.md
│   ├── issues-plan.md     ← GitHub 이슈 계획 (M2~M5)
│   ├── wiki-schema.md     ← Wiki 페이지 유형별 템플릿
│   └── health/            ← /health 커맨드 실행 로그 (날짜별)
│
├── mcp_server/            ← FastMCP 기반 MCP 서버 (구현 예정)
│   ├── server.py
│   └── wiki_store.py
│
├── viewer/                ← Streamlit Wiki 뷰어 (구현 예정)
│   └── app.py
│
├── wiki/                  ← 에이전트가 생성·관리하는 Markdown 페이지
│   ├── index.md           ← 전체 페이지 카탈로그 (자동 관리)
│   ├── log.md             ← 작업 이력 (append-only)
│   ├── concepts/
│   ├── frameworks/
│   ├── patterns/
│   └── sources/
│
├── raw/                   ← 원본 소스 파일 (불변, Streamlit 업로드로만 추가)
│
├── .claude/
│   ├── skills/            ← 스킬 정의 (각 스킬: skillname/SKILL.md)
│   ├── agents/            ← 에이전트 명세
│   └── commands/          ← 슬래시 커맨드
│
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
```

---

## MCP 도구 명세

에이전트는 파일 시스템에 직접 접근하지 않는다. 반드시 아래 MCP 도구만 사용한다.

| 도구 | 시그니처 | 역할 |
|------|----------|------|
| `wiki_list` | `wiki_list()` | 전체 페이지 slug 목록 반환 |
| `wiki_read` | `wiki_read(slug: str)` | 특정 페이지 내용 반환 |
| `wiki_write` | `wiki_write(slug: str, content: str)` | 페이지 생성/덮어쓰기 |
| `wiki_search` | `wiki_search(query: str)` | 제목·본문 키워드 검색 |
| `wiki_delete` | `wiki_delete(slug: str)` | 페이지 삭제 |
| `raw_save` | `raw_save(filename: str, content: bytes)` | 업로드 파일을 `raw/`에 저장 (Streamlit 호출) |
| `raw_read` | `raw_read(filename: str)` | `raw/` 파일 내용 반환 (인제스트용) |

페이지 유형별 템플릿 → `docs/wiki-schema.md` 참조

---

## 스킬

### Wiki 운영 스킬

| 스킬 | 파일 | 트리거 |
|------|------|--------|
| **ingest** | `.claude/skills/ingest/SKILL.md` | 소스 파일 추가/인제스트 요청 |
| **query** | `.claude/skills/query/SKILL.md` | 개념·기술 질문 |
| **wiki-edit** | `.claude/skills/wiki-edit/SKILL.md` | 특정 페이지 편집 요청 |

### 개발 전용 스킬

| 스킬 | 파일 | 트리거 |
|------|------|--------|
| **github-issue-create** | `.claude/skills/github-issue-create/SKILL.md` | 이슈 등록 요청 |
| **github-issue-work** | `.claude/skills/github-issue-work/SKILL.md` | 특정 이슈 번호 작업 시작 |
| **pr-review** | `.claude/skills/pr-review/SKILL.md` | 특정 PR 번호 리뷰 요청 |
| **orchestrate** | `.claude/skills/orchestrate/SKILL.md` | impl-agent → verify-agent 조율 *(github-issue-work 내부 호출, 직접 트리거 금지)* |

---

## 커맨드

| 커맨드 | 파일 | 역할 |
|--------|------|------|
| `/health` | `.claude/commands/health.md` | 하네스 구조 점검 및 `docs/health/YYYY-MM-DD.md` 로그 저장 |

---

## 운영 규칙

1. Wiki 읽기/쓰기와 raw 파일 접근은 **MCP 도구만 사용한다** (내장 Read/Write 도구 사용 금지).
2. `raw/` 파일은 절대 수정하지 않는다. 읽기는 `raw_read`를 사용한다.
3. 페이지 생성 후 반드시 `wiki_write("index", …)`로 인덱스를 업데이트한다.
4. 모든 Wiki 작업 후 `wiki_write("log", …)`로 이력을 append한다.
5. 설계·구조·방향 결정이 생길 때마다 `docs/decision-log.md`에 라운드를 추가한다.
6. 모든 내부 링크는 `[[slug]]` 형식으로 작성한다.
7. YAML frontmatter 필수, 출처 없는 주장 작성 금지.
8. 날짜는 `YYYY-MM-DD`, 한국어 우선·기술 용어 영어 병기 허용.
9. 새 세션 시작 시 `docs/decision-log.md`를 읽어 이전 의사결정 컨텍스트를 파악한다.
