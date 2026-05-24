---
type: concept
tags: [agentic-coding, llm, SDLC, agent]
created: 2026-05-24
sources: [1. Vibe coding and Agent coding.pdf, 2. SDLC pipeline in Vibe coding.pdf]
---

# Agentic Coding (에이전틱 코딩)

## 정의
코딩 에이전트를 통해 SDLC가 보장되는 개발 프로세스를 수행하는 방식으로, 인간이 Orchestrator 역할을 맡아 단일→순차→병렬 에이전트 구조로 복잡한 시스템을 개발한다.

## 상세 설명

2025년 4분기부터 부상한 개발 패러다임. [[Vibe Coding]]이 소규모 애플리케이션에 적합하다면, Agentic Coding은 대규모 제품 수준의 시스템 개발까지 확장 가능하다.

**Vibe Coding과의 차이:**

| | Vibe Coding | Agentic Coding |
|---|---|---|
| 접근 방식 | One-Shot Generation | Description per each Agents |
| 문서화 | PRD/SRS 링크 또는 없음 | 적절한 Prompt + PRD/SRS |
| 인간의 역할 | Prompt Engineering | Orchestrator |
| 에이전트 구조 | Single Conversation | Single → Sequential → Multi-Agent |
| 적합한 규모 | Small-Size Application | Up to Large-Scale Product |
| SDLC 단계 | Simple Loop | SDLC 단계별 AI 협업 |

**에이전트 구조의 발전:**

1. **Single Agent**: 사용자의 요청이 명확하고 구조화되어 있어야 함
2. **Sequential Agent**: 각 에이전트는 독립적으로 작동하되 앞 단계가 완료되어야 다음 단계 시작. SDLC Analysis 단계의 작업 분해와 동일한 원리.
3. **Parallel Agent**: 하나의 입력을 여러 전문화된 서브 에이전트가 동시에 처리. Research에서 강력한 접근(WebSearch).

## 관련 개념

- [[Vibe Coding]] — 선행 패러다임, 소규모에 적합
- [[SDLC]] — Agentic Coding이 보장하려는 개발 프로세스
- [[Orchestrator]] — 인간 또는 상위 에이전트의 역할
- [[Sequential Agent]], [[Parallel Agent]] — 에이전트 구조 유형
- [[Harness Engineering]] — Agentic Coding을 안정적으로 실행하는 실행 구조

## 출처

- [[source: 1. Vibe coding and Agent coding.pdf]] — "코딩 에이전트를 통해 SDLC가 보장되는 개발 프로세스를 수행 가능"
- [[source: 2. SDLC pipeline in Vibe coding.pdf]] — Vibe Coding vs Agentic Coding 비교 표
