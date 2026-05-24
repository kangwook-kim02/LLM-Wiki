---
type: source
tags: [강의자료, harness, skills, contract-driven, TASK.md, CSE3308]
created: 2026-05-24
---

# Harness and Skills

**파일:** `raw/7. Harness and Skills.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Week 10)

## 핵심 주장

- **Harness Engineering 정의**: AI 에이전트가 복잡한 작업을 안전하고 효율적으로 완수할 수 있도록, 프롬프트나 모델을 넘어선 외부 실행 환경(도구, 데이터, 검증 파이프라인, 안전장치)을 구조적으로 설계하고 통제하는 기술.
- **4가지 핵심 구성 요소**: Contract(TASK.md), Procedure(Skill), Journal(log.md or MCP), Preference(PROFILE.md, AGENTS.md, CLAUDE.md).
- **Contract-Driven Iteration**: 에이전트가 Contract(TASK.md)를 읽고 `Done when` 조건을 만족할 때까지 반복하는 방식. 명시적인 달성 조건과 최대 작업 상한이 있어야 한다.
- **Skill**: 에이전트가 특정 작업을 어떻게 수행할지 정의한 마크다운 파일. AI Agent는 작업 맥락에 맞는 Skill을 자동으로 찾아 적용할 수 있다.
- **에이전틱 코딩 기본 패턴 5가지**: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer.

## 하네스 4가지 구성 요소

| 책임 | 질문 | 파일 예시 |
|------|------|-----------|
| Contract | 무엇이 끝났는가? | TASK.md |
| Procedure | 어떻게 진행하는가? | Skill |
| Journal | 지금까지 무엇을 했는가? | log.md 또는 MCP |
| Preference | 어떤 방식으로 일하는가? | PROFILE.md, AGENTS.md, CLAUDE.md |

## 에이전틱 코딩 패턴

| 패턴 | 의미 | 예시 |
|------|------|------|
| Prompt Chaining | 앞 단계 결과를 다음 단계 입력으로 사용 | 스펙 작성 → 테스트 작성 → 구현 |
| Routing | 입력 종류에 따라 다른 경로 선택 | 문서 수정은 가벼운 모델, 보안 이슈는 강한 모델 |
| Parallelization | 독립 작업을 동시에 실행 | 여러 파일을 나누어 수정 |
| Orchestrator-Workers | 관리자가 작업을 쪼개 워커에게 배분 | 영향받는 파일을 찾고 각 워커에게 할당 |
| Evaluator-Optimizer | 만들고 평가하고 다시 고침 | 테스트 통과할 때까지 구현 반복 |

## 코딩에서 자주 쓰는 패턴

| 이름 | 흐름 | 핵심 |
|------|------|------|
| EPCC | Explore → Plan → Code → Commit | 바로 코딩하지 않고 먼저 읽고 계획 |
| TDD | Red → Green → Refactor | 실패 테스트를 먼저 만들고 통과 |
| Visual Iteration | 생성 → 화면 확인 → 수정 | UI는 실제 화면으로 검증 |
| Three-Agent Harness | Planner → Generator → Evaluator | 계획, 구현, 평가를 분리 |

## 주요 개념

- [[Harness Engineering]], [[Contract-Driven Iteration]], [[Skill]], [[TASK.md]], [[Journal]], [[에이전틱 코딩 패턴]], [[EPCC 패턴]]

## 주목할 인사이트

- "Contract가 없는 Procedure는 무한 루프이고, Procedure가 없는 Contract는 죽은 문서다."
- AGENTS.md의 3가지 절대 금지: ❌ 한 반복에서 두 개 이상의 작업, ❌ 실패한 테스트를 skip, ❌ `specs/` 없이 코드 작성.
- OpenAI `/goal` 기능: 사용자가 목표 설정 후 끝날 때까지 계속 작업을 이어가는 기능 (현재 UnderDevelopment).
- Ralph Ruf의 Loop: Phase 1(명세 작성) → Phase 2(Plan 수립) → while loop: Phase 3(작업→검증→커밋).

## Wiki 업데이트 내역

- 생성: [[source: source-07-harness-skills]]
- 생성: [[Harness Engineering]] (wiki/concepts/harness-engineering.md)
- 생성: [[Contract-Driven Iteration]] (wiki/concepts/contract-driven-iteration.md)
- 생성: [[Skill]] (wiki/concepts/skill.md)
- 생성: [[에이전틱 코딩 패턴]] (wiki/concepts/agentic-coding-patterns.md)
- 업데이트: [[에이전트 아키텍처 패턴]] (wiki/topics/agent-architecture-patterns.md)
