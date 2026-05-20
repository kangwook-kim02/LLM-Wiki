# LLM Wiki — Personal Knowledge Base Schema

이 파일은 LLM 에이전트(Claude Code)가 이 wiki를 어떻게 관리해야 하는지 정의하는 스키마입니다.
**이 파일을 직접 수정하지 마세요** — wiki 운영 중 LLM과 협의하여 공동 진화시킵니다.

---

## 디렉토리 구조

```
.
├── raw/          ← 원본 소스 (불변, LLM이 읽기만 함)
├── wiki/         ← LLM이 생성·유지하는 Markdown 페이지들
│   ├── index.md  ← 전체 페이지 카탈로그
│   ├── log.md    ← 작업 이력 (append-only)
│   └── ...       ← 개념/엔티티/주제 페이지들
└── CLAUDE.md     ← 이 스키마 파일
```

**규칙:**
- `raw/` 파일은 절대 수정하지 않는다.
- `wiki/` 파일만 생성·수정한다.
- 모든 wiki 페이지는 Markdown(`.md`)으로 작성한다.

---

## Wiki 페이지 유형

### 1. 개념 페이지 (`wiki/concepts/`)
특정 기술·아이디어를 설명하는 페이지.

```markdown
# [개념 이름]

## 정의
한 문장 정의.

## 상세 설명
2~5 문단.

## 관련 개념
- [[다른 개념]]
- [[또 다른 개념]]

## 출처
- [[source: 파일명]] — 인용 내용
```

### 2. 엔티티 페이지 (`wiki/entities/`)
사람, 도구, 프레임워크, 조직 등 고유 개체.

```markdown
# [엔티티 이름]

## 요약
한 줄 설명.

## 주요 특징
- 특징 1
- 특징 2

## 관련 항목
- [[개념]], [[다른 엔티티]]

## 출처
- [[source: 파일명]]
```

### 3. 소스 요약 페이지 (`wiki/sources/`)
각 원본 소스에 대한 요약.

```markdown
# [소스 제목]

**파일:** `raw/파일명`
**인제스트 날짜:** YYYY-MM-DD
**유형:** 논문 | 강의 자료 | 아티클 | 책 챕터

## 핵심 주장
3~5개 bullet.

## 주요 개념
- [[개념1]], [[개념2]]

## 주목할 인사이트
중요하거나 놀라운 내용.

## Wiki 업데이트 내역
이 소스로 인해 수정된 페이지 목록.
```

### 4. 주제 개요 페이지 (`wiki/topics/`)
여러 개념/엔티티를 아우르는 고수준 주제 페이지.

```markdown
# [주제 이름]

## 개요
이 주제가 무엇인지, 왜 중요한지.

## 핵심 구성 요소
- [[개념1]] — 한 줄 설명
- [[개념2]] — 한 줄 설명

## 관계도
개념들이 어떻게 연결되는지 텍스트로 서술.

## 미해결 질문
아직 명확하지 않은 부분.

## 출처
- [[source: 파일명]]
```

---

## 워크플로

### Ingest (새 소스 추가)

사용자가 "이 파일 인제스트해줘" 또는 `ingest [파일명]`이라고 하면:

1. `raw/` 에서 파일을 읽는다.
2. 핵심 주장과 개념을 사용자와 논의한다.
3. `wiki/sources/` 에 소스 요약 페이지를 생성한다.
4. 새로 등장한 개념마다 `wiki/concepts/` 페이지를 생성하거나 기존 페이지를 업데이트한다.
5. 관련 엔티티 페이지를 생성하거나 업데이트한다.
6. 관련 주제 페이지를 업데이트한다.
7. `wiki/index.md` 를 업데이트한다.
8. `wiki/log.md` 에 항목을 추가한다: `## [YYYY-MM-DD] ingest | 파일명`

**원칙:** 한 소스 인제스트 시 10~15개 페이지를 건드리는 것이 정상. 서로 모순되는 내용은 명시적으로 flagging한다.

### Query (질문)

사용자가 질문하면:

1. `wiki/index.md` 를 읽어 관련 페이지를 파악한다.
2. 관련 페이지들을 읽는다.
3. 인용과 함께 답변을 합성한다.
4. 답변이 wiki 페이지로 보존할 가치가 있으면 `wiki/topics/` 또는 `wiki/concepts/` 에 파일링한다.
5. `wiki/log.md` 에 항목 추가: `## [YYYY-MM-DD] query | 질문 요약`

### Lint (건강 검사)

사용자가 "wiki lint해줘" 또는 "wiki 점검해줘"라고 하면:

1. 모든 wiki 페이지를 스캔한다.
2. 다음을 탐지한다:
   - 페이지 간 모순
   - 인바운드 링크가 없는 고아 페이지
   - 언급은 되었지만 페이지가 없는 개념
   - 누락된 교차 참조
   - 새 소스로 인해 구식이 된 클레임
3. 발견 사항을 목록으로 보고하고 수정 여부를 사용자에게 묻는다.
4. `wiki/log.md` 에 항목 추가: `## [YYYY-MM-DD] lint | 발견 N건`

---

## 현재 소스 목록

현재 `raw/` 에 있어야 할 파일들 (프로젝트 루트에서 이동 필요):

| 파일 | 주제 |
|------|------|
| `Vibe coding and Agent coding.pdf` | Vibe Coding vs Agentic Coding 개요 |
| `SDLC pipeline in Vibe coding.pdf` | SDLC 파이프라인 |
| `Agents subprocess calling.pdf` | 에이전트 서브프로세스 |
| `Plan_mode Sequential and Parallel agents.pdf` | Plan 모드, 병렬 에이전트 |
| `Agent Specifications.pdf` | 에이전트 명세 |
| `Agent pool and Orchestrator.pdf` | 에이전트 풀 & 오케스트레이터 |
| `Harness and Skills.pdf` | 하네스 & 스킬 |
| `Model Context Protocol.pdf` | MCP |
| `Loop and Hooks.pdf` | 루프 & 훅 |

---

## 컨벤션

- 모든 페이지 제목은 `# 제목` 형식 (H1).
- 내부 링크는 `[[페이지명]]` 형식 (Obsidian 호환).
- 날짜는 `YYYY-MM-DD` 형식.
- 한국어 우선, 기술 용어는 영어 원문 병기 허용.
- 출처 없는 주장을 작성하지 않는다.
- 각 페이지 상단에 YAML frontmatter 선택적 추가:

```yaml
---
type: concept | entity | source | topic
tags: [태그1, 태그2]
created: YYYY-MM-DD
sources: [파일명1, 파일명2]
---
```

---

## 진화 규칙

이 스키마는 고정이 아닙니다. 새로운 도메인이 추가되거나 더 나은 구조가 발견되면:
1. 사용자에게 변경 제안을 먼저 설명한다.
2. 동의를 받은 후 이 `CLAUDE.md` 를 업데이트한다.
3. `wiki/log.md` 에 스키마 변경 사항을 기록한다.
