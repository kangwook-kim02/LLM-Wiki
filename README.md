# LLM Wiki — RAG & Agent Frameworks Knowledge Base

> MCP 서버를 기반으로 RAG, LangChain, LangGraph 생태계 지식을 자동으로 축적하고 서빙하는 Wiki 시스템.

---

## 프로젝트 개요

**도메인**: LLM Application Frameworks & Agent Systems
**대상 독자**: RAG·LangChain·LangGraph를 학습하거나 실무에 적용하려는 개발자

Andrej Karpathy의 LLM Wiki 패턴을 확장하여, **MCP(Model Context Protocol) 서버**를 중간 계층으로 두는 구조입니다. Claude Code 에이전트는 파일 시스템에 직접 접근하지 않고, MCP 도구를 통해서만 Wiki를 읽고 씁니다.

---

## 시스템 아키텍처

```
┌──────────────────────────────────────────────────────────┐
│         Streamlit 뷰어 (viewer/app.py :8501)             │
│  [좌: 사이드바]      [중: 본문 패널]    [우: 채팅 패널]  │
│  페이지 목록/검색    MD 렌더링          Claude API 연결   │
│  파일 업로드                            인제스트/질의응답  │
└──────┬──────────────────────────────────────┬────────────┘
       │ raw_save(file)                        │ Claude API 호출
       ▼                                       ▼
┌──────────────────────┐          ┌────────────────────────┐
│    MCP 서버           │◄─────────│   Claude Code 에이전트  │
│  wiki_list/read      │  MCP 도구 │   ingest / query       │
│  wiki_write/search   │  호출     │   wiki-edit            │
│  wiki_delete         │           │   github-issue-work    │
│  raw_save / raw_read │           └────────────────────────┘
└──────────┬───────────┘
           │
     ┌─────┴──────┐
     ▼            ▼
┌─────────┐  ┌─────────┐
│  wiki/  │  │  raw/   │
│  *.md   │  │  소스   │
└─────────┘  └─────────┘
```

---

## MCP 도구 목록

MCP 서버(`mcp_server/server.py`)가 제공하는 7가지 도구:

| 도구 | 호출 주체 | 설명 |
|------|----------|------|
| `wiki_list()` | 에이전트 / 뷰어 | 전체 위키 페이지 목록(slug) 반환 |
| `wiki_read(slug)` | 에이전트 / 뷰어 | 특정 페이지의 Markdown 내용 반환 |
| `wiki_write(slug, content)` | 에이전트 | 페이지 생성 또는 수정 |
| `wiki_search(query)` | 에이전트 / 뷰어 | 제목·본문 키워드 검색 |
| `wiki_delete(slug)` | 에이전트 | 페이지 삭제 |
| `raw_save(filename, content)` | Streamlit 뷰어 | 업로드 파일을 `raw/`에 저장 |
| `raw_read(filename)` | 에이전트 | `raw/` 파일 내용 반환 (인제스트용) |

**slug 형식**: `카테고리/페이지명` — 예) `concepts/rag`, `frameworks/langchain`

---

## 실행 방법

### 요구 환경

- Python 3.11+
- Claude Code CLI
- GitHub CLI (`gh`) — 개발 스킬 사용 시

### 의존성 설치

```bash
pip install fastmcp streamlit markdown anthropic
```

### 1. MCP 서버 등록

프로젝트 `.claude/settings.json`에 추가:

```json
{
  "mcpServers": {
    "llm-wiki": {
      "command": "python",
      "args": ["mcp_server/server.py"],
      "cwd": "<이 프로젝트 절대 경로>"
    }
  }
}
```

### 2. Claude Code 실행

```bash
claude
```

Claude Code가 자동으로 `CLAUDE.md`를 읽고 MCP 도구를 사용할 수 있는 상태가 됩니다.

### 3. Wiki 뷰어 실행 (별도 터미널)

```bash
streamlit run viewer/app.py
```

브라우저에서 `http://localhost:8501` 접속.

---

## 사용 방법

### 새 소스 인제스트

1. Streamlit 사이드바 **"소스 업로드"** 에서 PDF/MD 파일 선택
2. 업로드 완료 후 우측 채팅 패널에 입력:
   ```
   langchain-docs.pdf 인제스트해줘
   ```
3. 에이전트가 Wiki 페이지 자동 생성 → 중앙 패널에서 즉시 열람 가능

### 개념 질문

```
RAG와 Fine-tuning의 차이가 뭔가요?
```

### Wiki 편집

```
LangGraph 페이지에 StateGraph 설명 추가해줘
```

---

## 스킬 & 커맨드

### Wiki 운영 스킬

| 스킬 | 트리거 | 동작 |
|------|--------|------|
| **ingest** | 파일 추가/인제스트 요청 | raw_read → 분석 → wiki_write로 페이지 생성 |
| **query** | 개념·기술 질문 | wiki_search → wiki_read → 답변 합성 |
| **wiki-edit** | 특정 페이지 편집 요청 | wiki_read → 수정 → wiki_write |

### 개발 전용 스킬

| 스킬 | 트리거 | 동작 |
|------|--------|------|
| **github-issue-create** | "이슈 등록해줘" | gh issue create (이슈 템플릿 기반) |
| **github-issue-work** | "이슈 #N번 작업하자" | 파악 → 브랜치 생성 → orchestrate 위임 |
| **orchestrate** | github-issue-work 내부 호출 | impl-agent → verify-agent 순차 실행 |

### 커맨드

| 커맨드 | 동작 |
|--------|------|
| `/health` | 하네스 구조 점검 + `docs/health/YYYY-MM-DD.md` 로그 저장 |

---

## 폴더 구조

```
LLM-Wiki/
├── CLAUDE.md                    ← 에이전트 운영 스키마
├── README.md                    ← 이 파일
├── .gitignore
│
├── docs/
│   ├── domain-definition.md     ← 지식 도메인 정의
│   ├── PRD.md                   ← 제품 요구사항 문서
│   ├── decision-log.md          ← 의사결정 이력
│   ├── wiki-schema.md           ← Wiki 페이지 유형별 템플릿
│   └── health/                  ← /health 점검 로그 (날짜별)
│
├── mcp_server/
│   ├── server.py                ← FastMCP 기반 MCP 서버
│   └── wiki_store.py            ← Wiki I/O 레이어
│
├── viewer/
│   └── app.py                   ← Streamlit Wiki 뷰어
│
├── wiki/                        ← Wiki 콘텐츠 (에이전트 관리)
│   ├── index.md
│   ├── log.md
│   ├── concepts/
│   ├── frameworks/
│   ├── patterns/
│   └── sources/
│
├── raw/                         ← 원본 소스 파일 (Streamlit 업로드로만 추가)
│
├── .claude/
│   ├── skills/                  ← 스킬 정의 (6개)
│   ├── agents/                  ← 에이전트 명세 (impl, verify)
│   └── commands/                ← 슬래시 커맨드 (/health)
│
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

---

## 참고

- [Andrej Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [LangChain Documentation](https://python.langchain.com)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph)
