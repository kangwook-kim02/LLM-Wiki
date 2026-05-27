# LLM Wiki — Agentic Coding Basics

> Andrej Karpathy의 LLM Wiki 패턴을 기반으로 구축한 **개인 지식 베이스**.  
> RAG(검색 증강 생성) 대신 LLM이 Markdown 위키를 직접 유지·진화시키는 방식입니다.

---

## 🧠 LLM Wiki란?

일반적인 RAG는 질문할 때마다 원본 문서를 검색해서 답을 만듭니다.  
LLM Wiki는 다릅니다 — **LLM이 지식을 한 번 읽고, Markdown 파일로 정리해두면** 이후 질문은 그 위키를 참고합니다.

| | RAG | LLM Wiki |
|---|---|---|
| 지식 저장 방식 | 원본 문서 벡터 DB | 정리된 Markdown 파일 |
| 질문 시 동작 | 원본 검색 → 매번 재생성 | 위키 읽기 → 합성 |
| 지식 누적 | ✗ (매번 처음부터) | ✅ (위키가 점점 성장) |
| 사람이 읽을 수 있나 | ✗ (벡터는 불투명) | ✅ (Markdown 파일) |

**핵심 아이디어**: 위키는 점점 성장하는 영구적인 산출물입니다.

---

## 📁 폴더 구조

```
.
├── README.md               ← 이 파일 (시작점)
├── CLAUDE.md               ← Claude Code용 에이전트 운영 스키마
├── AGENTS.md               ← Codex CLI / Gemini CLI용 에이전트 스키마
│
├── raw/                    ← 원본 소스 파일 (PDF 등, 불변 / git 미추적)
│
├── .claude/
│   ├── skills/             ← 자연어 트리거 스킬
│   │   ├── ingest.md       ← 소스 인제스트 스킬
│   │   └── query.md        ← 질의응답 스킬
│   └── commands/           ← 슬래시 커맨드
│       └── lint.md         ← /lint (위키 건강 검사)
│
└── wiki/                   ← LLM이 생성·유지하는 Markdown 위키
    ├── index.md            ← 전체 페이지 목록 (자동 관리)
    ├── log.md              ← 작업 이력 (자동 append)
    ├── sources/            ← 소스별 요약 페이지
    ├── concepts/           ← 개념 설명 페이지
    ├── entities/           ← 도구·사람·프레임워크 페이지
    └── topics/             ← 여러 개념을 묶는 주제 개요 페이지
```

---

## 🚀 시작하기

### 필요한 것

- [Claude Code](https://claude.ai/code) (CLI 또는 데스크탑 앱)
- 또는 Codex CLI / Gemini CLI (AGENTS.md 참고)

### 처음 시작 (빠른 시작)

1. **이 저장소를 클론합니다**
   ```bash
   git clone https://github.com/kangwook-kim02/LLM-Wiki.git
   cd LLM-Wiki
   ```

2. **raw/ 폴더에 소스 파일을 넣습니다** (PDF, 텍스트 등)
   ```
   raw/
   ├── my-paper.pdf
   └── my-article.md
   ```

3. **Claude Code를 열고 자연어로 인제스트합니다**
   ```
   my-paper.pdf 업로드 했어, 위키 만들어줘!
   ```
   Claude가 자동으로:
   - 소스 요약 페이지 생성 (`wiki/sources/`)
   - 새 개념 페이지 생성 (`wiki/concepts/`)
   - 위키 인덱스 업데이트 (`wiki/index.md`)
   - 작업 이력 기록 (`wiki/log.md`)

4. **질문합니다**
   ```
   Plan Mode란 무엇인가요?
   ```
   Claude가 위키 페이지를 참고해서 답합니다.

---

## 💬 스킬 & 커맨드

### 🔵 Ingest 스킬 — 새 소스 추가 (자연어 트리거)

파일명과 함께 위키 생성을 요청하면 자동으로 발동됩니다:

```
my-research-paper.pdf 업로드 했어, 위키 만들어줘!
```
```
새 자료 추가했어 — article.pdf 인제스트해줘
```
```
10. NewTopic.pdf 위키에 넣어줘
```

LLM이 소스를 읽고 위키 페이지를 자동으로 생성·업데이트합니다.  
**한 소스당 보통 10~15개 페이지가 생성되거나 업데이트됩니다.**

---

### 🔵 Query 스킬 — 질문하기 (자연어 트리거)

Ingest 트리거에 해당하지 않는 모든 질문에 자동으로 발동됩니다:

```
Hook과 Loop의 차이가 뭔가요?
```
```
Orchestrator-Workers 패턴을 언제 사용하나요?
```
```
MCP의 장단점을 설명해주세요
```

LLM이 `wiki/index.md`를 먼저 읽고, 관련 페이지를 찾아 답을 합성합니다.  
답변 내용이 보존할 가치가 있으면 새 페이지로 자동 저장됩니다.

---

### 🟣 /lint 커맨드 — 위키 건강 검사 (슬래시 커맨드)

의도적으로 실행할 때 슬래시 커맨드로 호출합니다:

```
/lint
```

LLM이 모든 페이지를 스캔하여 다음을 탐지합니다:
- 페이지 간 **모순**
- 링크가 없는 **고아 페이지**
- 언급은 되었지만 **페이지가 없는 개념**
- 새 소스로 인해 **구식이 된 내용**

---

## 📄 위키 페이지 유형

위키는 4가지 유형의 페이지로 구성됩니다:

| 유형 | 위치 | 설명 |
|------|------|------|
| **소스 요약** | `wiki/sources/` | 원본 파일 하나당 1개, 핵심 주장 정리 |
| **개념** | `wiki/concepts/` | 특정 기술·아이디어 설명 |
| **엔티티** | `wiki/entities/` | 도구, 사람, 프레임워크 등 고유 개체 |
| **주제 개요** | `wiki/topics/` | 여러 개념을 묶는 고수준 정리 |

모든 페이지는 `[[위키링크]]` 형식으로 서로 연결됩니다 (Obsidian 호환).

---

## 📚 현재 위키 콘텐츠

이 저장소에는 **Agentic Coding Basics** 시리즈 9개 강의 자료를 인제스트한 위키가 포함되어 있습니다.

| 소스 | 주제 |
|------|------|
| Vibe Coding and Agent Coding | 패러다임 전환 개요 |
| SDLC Pipeline in Vibe Coding | SDLC 단계별 AI 협업 |
| Agents Subprocess Calling | Python으로 CLI 에이전트 호출 |
| Plan Mode, Sequential and Parallel Agents | 계획 모드, 에이전트 협력 패턴 |
| Agent Specifications | 에이전트 명세 구성요소 |
| Agent Pool and Orchestrator | 동적 에이전트 관리 |
| Harness and Skills | 에이전트 실행 환경 구조화 |
| Model Context Protocol | 외부 시스템 연동 표준 |
| Loop and Hooks | 자동화와 결정론적 제어 |

👉 **[wiki/index.md](wiki/index.md)** 에서 전체 페이지 목록을 확인하세요.

---

## 🔧 에이전트별 사용 방법

### Claude Code
```bash
# 프로젝트 폴더에서 Claude Code를 열면 CLAUDE.md를 자동으로 읽습니다
claude
```

### Codex CLI
```bash
codex --approval-mode full-auto "ingest my-paper.pdf"
```

### Gemini CLI
```bash
gemini -p "ingest my-paper.pdf"
```

자세한 내용은 **[AGENTS.md](AGENTS.md)** 를 참고하세요.

---

## 📖 참고

- **원작**: [Andrej Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **위키 스키마**: [CLAUDE.md](CLAUDE.md) (Claude Code용), [AGENTS.md](AGENTS.md) (범용)
- **작업 이력**: [wiki/log.md](wiki/log.md)

---

> 💡 **팁**: `wiki/index.md`는 LLM이 자동으로 관리합니다. 직접 수정하지 마세요.  
> 새 소스를 추가할 때마다 위키가 성장하고 더 풍부해집니다.
