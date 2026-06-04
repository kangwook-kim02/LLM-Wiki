# LLM Wiki — RAG & Agent Frameworks Knowledge Base

> MCP 서버를 기반으로 RAG, LangChain, LangGraph 생태계 지식을 자동으로 축적하고 서빙하는 Wiki 시스템.

---

## 프로젝트 소개

**도메인**: LLM Application Frameworks & Agent Systems (RAG, LangChain, LangGraph)
**대상 독자**: RAG·LangChain·LangGraph를 학습하거나 실무에 적용하려는 개발자

Andrej Karpathy의 LLM Wiki 패턴을 확장하여, **MCP(Model Context Protocol) 서버**를 중간 계층으로 두는 구조입니다. Claude Code 에이전트는 파일 시스템에 직접 접근하지 않고, MCP 도구를 통해서만 Wiki를 읽고 씁니다.

### 기술 스택

| 영역 | 기술 |
|------|------|
| AI 에이전트 | Claude Code (Anthropic) |
| 에이전트 프로토콜 | MCP (Model Context Protocol) |
| Wiki 뷰어 | Flask + markdown2 |
| MCP 서버 | Python (`mcp[cli]`) |
| 소스 파싱 | pypdf |

### 주요 기능

| 기능 | 설명 |
|------|------|
| **채팅** | 우측 채팅 패널에서 Claude Code 에이전트와 대화 — 인제스트, 질의응답, 페이지 편집 |
| **키워드 검색** | 좌측 사이드바 검색창으로 Wiki 페이지 제목·본문 실시간 검색 (제목 매칭 우선) |
| **MD 렌더링** | 중앙 패널에서 Wiki 페이지를 Markdown → HTML로 변환하여 렌더링 |
| **소스 업로드** | 사이드바 하단 파일 업로드 → `raw/`에 저장 후 채팅으로 인제스트 트리거 |

---

## 시스템 아키텍처

```
┌──────────────────────────────────────────────────────────────┐
│           Flask 뷰어 (viewer/app.py :5000)                   │
│  [좌: 사이드바]       [중: 본문 패널]    [우: 채팅 패널]    │
│  페이지 목록/검색     MD 렌더링          claude -p 연결      │
│  파일 업로드                             인제스트/질의응답   │
└──────┬────────────────────────────────────────┬──────────────┘
       │ wiki_store 직접 import                  │ subprocess
       │ raw_save(file)                          │ claude -p
       ▼                                         ▼
┌──────────────────────┐          ┌────────────────────────────┐
│    MCP 서버           │◄─────────│   Claude Code 에이전트     │
│  wiki_list/read      │  MCP 도구 │   ingest / query           │
│  wiki_write/search   │  호출     │   wiki-edit                │
│  wiki_delete         │           │   github-issue-work        │
│  raw_save / raw_read │           └────────────────────────────┘
└──────────┬───────────┘
           │
     ┌─────┴──────┐
     ▼            ▼
┌─────────┐  ┌─────────┐
│  wiki/  │  │  raw/   │
│  *.md   │  │  소스   │
└─────────┘  └─────────┘
```

> 뷰어의 페이지 열람·파일 업로드는 `wiki_store.py`를 직접 import하여 처리합니다 (MCP 불필요).
> 채팅 패널은 `subprocess(["claude", "-p", query], cwd=project_root)`로 Claude Code를 호출하며,
> 프로젝트 루트의 `.mcp.json`을 통해 MCP 도구가 자동 로드됩니다.

---

## 환경 세팅

### 사전 설치 요구사항

- Python 3.11+
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- [GitHub CLI](https://cli.github.com/) (`gh`) — 개발 스킬(이슈·PR) 사용 시

### 저장소 클론

```bash
git clone https://github.com/kangwook-kim02/LLM-Wiki.git
cd LLM-Wiki
```

### 의존성 설치

```bash
pip install -r requirements.txt
```

`requirements.txt` 포함 패키지: `mcp[cli]`, `pypdf`, `flask`, `markdown2`

---

## 실행 방법

### 1. MCP 서버 등록

`.claude/settings.json`과 `.mcp.json` 두 파일 모두에 Python 및 프로젝트 **절대경로**를 환경에 맞게 수정합니다.

```json
{
  "mcpServers": {
    "llm-wiki": {
      "command": "<python 절대경로>",
      "args": ["<프로젝트 절대경로>/mcp_server/server.py"],
      "env": {
        "PYTHONPATH": "<프로젝트 절대경로>/mcp_server"
      }
    }
  }
}
```

> `.claude/settings.json` — Claude Code CLI용 / `.mcp.json` — Flask 뷰어 채팅 패널용

### 2. Claude Code 실행

```bash
claude
```

Claude Code가 자동으로 `CLAUDE.md`를 읽고 MCP 도구를 사용할 수 있는 상태가 됩니다.

### 3. Wiki 뷰어 실행 (별도 터미널)

```bash
python -m flask --app viewer/app.py run
```

브라우저에서 `http://localhost:5000` 접속.

---

## LLM Wiki 사용 방법

### 소스 인제스트

1. 뷰어 사이드바 하단 **"소스 업로드"** 에서 PDF/MD/TXT 파일 선택
2. 업로드 완료 후 우측 채팅 패널에 입력:
   ```
   langchain-docs.pdf 인제스트해줘
   ```
3. 에이전트가 Wiki 페이지 자동 생성 → 중앙 패널에서 즉시 열람 가능

### 개념 질문

채팅 패널에서 자연어로 질문하면 Wiki 기반으로 답변합니다.

```
RAG와 Fine-tuning의 차이가 뭔가요?
```

### Wiki 편집

```
LangGraph 페이지에 StateGraph 설명 추가해줘
```

### Wiki 상태 점검

`wiki-check` 스킬로 Wiki 콘텐츠의 구성과 품질을 점검합니다. `/health` 커맨드가 하네스 구조를 점검하는 것과 달리, 이 스킬은 Wiki **페이지 데이터** 자체를 대상으로 합니다.

```
위키 점검해줘
```

점검 항목:

| 항목 | 설명 |
|------|------|
| 인덱스 일관성 | `wiki_list()` 결과와 `index.md` 등재 목록 대조 — 누락·유령 항목 탐지 |
| 페이지 품질 | YAML frontmatter, `title`·`tags` 필드, 빈 페이지 여부 확인 |
| 내부 링크 유효성 | `[[slug]]` 형식 링크 대상이 실제로 존재하는지 검사 |
| 검색 기능 | `wiki_search` 정상 동작 여부 확인 |

결과는 ✅ / ⚠️ / ❌ 형태로 요약되며, 이상 항목은 slug와 함께 수정 권고가 제시됩니다. 점검 후 수정이 필요하면 `wiki-edit` 스킬로 후속 조치합니다.

---

## 프로젝트 개발 방법

이 프로젝트는 Claude Code 스킬 기반으로 이슈 단위 개발 워크플로를 따릅니다.

### 1. 이슈 등록

`github-issue-create` 스킬로 구조화된 이슈를 생성합니다.

```
이슈 등록해줘: 키워드 검색 시 제목 우선 정렬 기능
```

GitHub 이슈 템플릿에 맞춰 제목·설명·완료 기준을 포함한 이슈가 자동 생성됩니다.

### 2. 이슈 작업

`github-issue-work` 스킬로 이슈 번호를 지정해 작업을 시작합니다.

```
이슈 #8번 작업하자
```

내부적으로 `orchestrate` 스킬이 두 전문 에이전트를 순차 호출합니다:

```
impl-agent (구현) → verify-agent (검증) → 필요 시 재구현 핑퐁
```

- **impl-agent**: 이슈 요구사항을 코드로 구현하고 PR 생성
- **verify-agent**: 구현 결과를 이슈 완료 기준 대비 검증, 미달 시 impl-agent에 재작업 요청

### 3. 하네스 건강 체크

`/health` 커맨드로 스킬·에이전트·MCP 도구 등 하네스 구조 전체를 점검합니다.

```
/health
```

점검 결과는 `docs/health/YYYY-MM-DD.md`에 자동 저장됩니다.

### 4. PR 리뷰 (선택)

`pr-review` 스킬로 머지 전 PR을 검토합니다. 매 PR마다 필수는 아니며 필요할 때 활용합니다.

```
PR #12번 리뷰해줘
```

완료 기준 준수, 규칙 위반, 코드 품질 4관점에서 리뷰 리포트를 생성합니다.

---

## MCP 도구

MCP 서버(`mcp_server/server.py`)가 제공하는 7가지 도구입니다. Claude Code 에이전트는 파일 시스템에 직접 접근하지 않고 반드시 이 도구들만 사용합니다.

### 도구 목록

| 도구 | 호출 주체 | 설명 |
|------|----------|------|
| `wiki_list()` | 에이전트 | 전체 위키 페이지 목록(slug) 반환 |
| `wiki_read(slug)` | 에이전트 | 특정 페이지의 Markdown 내용 반환 |
| `wiki_write(slug, content)` | 에이전트 | 페이지 생성 또는 수정 |
| `wiki_search(query)` | 에이전트 | 제목·본문 키워드 검색 (제목 매칭 우선) |
| `wiki_delete(slug)` | 에이전트 | 페이지 삭제 |
| `raw_save(filename, content)` | Flask 뷰어 | 업로드 파일을 `raw/`에 저장 |
| `raw_read(filename)` | 에이전트 | `raw/` 파일 내용 반환 (인제스트용) |

**slug 형식**: `카테고리/페이지명` — 예) `concepts/rag`, `frameworks/langchain`

### 도구 동작 흐름

**인제스트 흐름** (소스 파일 → Wiki 페이지 생성)

```
사용자 파일 업로드
  → Flask 뷰어: raw_save(filename, content)        # raw/ 에 파일 저장
  → 사용자: 채팅 패널에서 "파일명 인제스트해줘"
  → 에이전트: raw_read(filename)                   # 원본 내용 읽기
  → 에이전트: wiki_write(slug, content)            # 새 페이지 생성
  → 에이전트: wiki_read("index")                   # 인덱스 읽기
  → 에이전트: wiki_write("index", updated)         # 인덱스 업데이트
  → 에이전트: wiki_write("log", appended)          # 작업 이력 기록
```

**질의응답 흐름** (개념·기술 질문)

```
사용자: "RAG와 Fine-tuning의 차이가 뭔가요?"
  → 에이전트: wiki_search(query)                   # 관련 페이지 검색
  → 에이전트: wiki_read(slug) × N                  # 관련 페이지 내용 읽기
  → 에이전트: 답변 합성 후 응답
```

**Wiki 편집 흐름**

```
사용자: "LangGraph 페이지에 StateGraph 설명 추가해줘"
  → 에이전트: wiki_search("LangGraph")             # 페이지 slug 탐색
  → 에이전트: wiki_read(slug)                      # 현재 내용 읽기
  → 에이전트: wiki_write(slug, updated_content)    # 수정 내용 저장
  → 에이전트: wiki_write("log", appended)          # 작업 이력 기록
```

---

## 폴더 구조

```
LLM-Wiki/
├── CLAUDE.md                    ← 에이전트 운영 스키마
├── README.md                    ← 이 파일
├── requirements.txt             ← Python 의존성
├── .mcp.json                    ← Flask 뷰어용 MCP 서버 설정
├── .gitignore
│
├── docs/
│   ├── domain-definition.md     ← 지식 도메인 정의
│   ├── PRD.md                   ← 제품 요구사항 문서
│   ├── decision-log.md          ← 의사결정 이력
│   ├── issues-plan.md           ← GitHub 이슈 계획 (M2~M5)
│   ├── wiki-schema.md           ← Wiki 페이지 유형별 템플릿
│   └── health/                  ← /health 점검 로그 (날짜별)
│
├── mcp_server/
│   ├── server.py                ← MCP 서버 (7개 도구)
│   └── wiki_store.py            ← Wiki I/O 레이어
│
├── viewer/
│   ├── app.py                   ← Flask 뷰어 (라우팅)
│   ├── templates/
│   │   ├── layout.html          ← 3패널 기본 템플릿
│   │   └── page.html            ← Wiki 페이지 뷰
│   └── static/
│       ├── style.css            ← 레이아웃·채팅 스타일
│       └── chat.js              ← 채팅·업로드 AJAX 처리
│
├── wiki/                        ← Wiki 콘텐츠 (에이전트 관리)
│   ├── index.md
│   ├── log.md
│   ├── concepts/
│   ├── frameworks/
│   ├── patterns/
│   └── sources/
│
├── raw/                         ← 원본 소스 파일 (뷰어 업로드로만 추가)
│
├── .claude/
│   ├── settings.json            ← MCP 서버 등록 + 권한 설정
│   ├── skills/                  ← 스킬 정의 (7개)
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
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [LangChain Documentation](https://python.langchain.com)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph)
