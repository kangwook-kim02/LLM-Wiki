---
type: concept
tags: [sequential-agent, pipeline, 에이전트아키텍처]
created: 2026-05-27
sources: [2. SDLC pipeline in Vibe coding.pdf, 4. Plan_mode Sequential and Parallel agents.pdf]
---

# Sequential Agent (순차 에이전트)

## 정의

앞 단계가 완료되어야 다음 단계가 시작되는 에이전트 체인. 단계 간 의존성이 있는 작업에 사용한다.

## 상세 설명

Sequential Agent는 각 에이전트가 독립적으로 작동하되, 이전 에이전트의 출력이 다음 에이전트의 입력이 되는 구조다. SDLC의 단계별 의존 관계를 그대로 구현한다.

**전형적인 파이프라인 구조:**

```
Planner → Reviewer → Coder → Tester
   ↓          ↓         ↓        ↓
planning.md  review.md  code/  test_results/
```

**Hand-off 파일 패턴**: 각 에이전트는 작업 완료 후 결과를 마크다운 파일로 저장하고, 다음 에이전트는 그 파일을 읽어 작업을 이어간다.

```
workspace/
├── 00_planning.md
├── 01_review.md
├── 02_revised_plan.md
└── 03_final_report.md
```

**[[Parallel Agent]]와 비교:**

| | Sequential | Parallel |
|---|---|---|
| 실행 방식 | 순서대로 | 동시에 |
| 단계 간 의존성 | 있음 | 없음 |
| 적합한 상황 | SDLC 단계 분리 | 독립적 리서치 |
| 속도 | 느림 | 빠름 |

## 관련 개념

- [[Parallel Agent]] — 의존성 없는 작업에 사용하는 대안 패턴
- [[Orchestrator]] — Sequential Pipeline을 동적으로 구성하는 관리자
- [[Plan Mode]] — Sequential 파이프라인의 첫 단계에 사용
- [[Agent Specification]] — 각 에이전트의 역할·입출력 정의

## 출처

- [[source: 2. SDLC pipeline in Vibe coding.pdf]] — "각 에이전트는 독립적으로 작동하되 앞 단계가 완료되어야 다음 단계가 시작."
- [[source: 4. Plan_mode Sequential and Parallel agents.pdf]] — "Hand-off 파일 패턴: 각 Round마다 작업 내용을 기록하는 핸드오프 파일 저장"
