---
type: concept
tags: [parallel-agent, 병렬처리, 에이전트아키텍처]
created: 2026-05-27
sources: [2. SDLC pipeline in Vibe coding.pdf, 4. Plan_mode Sequential and Parallel agents.pdf]
---

# Parallel Agent (병렬 에이전트)

## 정의

서로 독립적인 작업들을 동시에 처리하는 에이전트 구조. 작업 간 의존성이 없을 때 속도를 극대화하기 위해 사용한다.

## 상세 설명

Parallel Agent는 여러 에이전트가 동시에 작동하여 결과를 통합하는 방식이다. 주로 리서치, 독립적인 파일 수정, 다각도 분석에 강력하다.

**전형적인 구조:**

```
         Input
           │
   ┌───────┼───────┐
   ▼       ▼       ▼
Agent1  Agent2  Agent3
(WebSearch)(WebSearch)(WebSearch)
   │       │       │
   └───────┼───────┘
           ▼
        통합 결과
```

**적합한 사용 사례:**

- 동일한 주제를 여러 관점에서 동시에 리서치
- 서로 관련 없는 여러 파일을 동시에 수정
- 다수의 독립적인 테스트 케이스를 병렬 실행
- Orchestrator-Workers 패턴에서 Worker들의 실행

**[[Sequential Agent]]와 비교:**

| | Sequential | Parallel |
|---|---|---|
| 실행 방식 | 순서대로 | 동시에 |
| 단계 간 의존성 | 있음 | 없음 |
| 적합한 상황 | SDLC 단계 분리 | 독립적 리서치·수정 |
| 속도 | 느림 | 빠름 |

## 관련 개념

- [[Sequential Agent]] — 의존성이 있을 때 사용하는 대안 패턴
- [[Orchestrator]] — Parallel Worker들을 조율하는 관리자
- [[Agent Pool]] — 병렬 실행할 에이전트들의 레지스트리

## 출처

- [[source: 2. SDLC pipeline in Vibe coding.pdf]] — "독립 작업이 여러 개일 때 Parallelization 패턴 사용"
- [[source: 4. Plan_mode Sequential and Parallel agents.pdf]] — "Parallel Agent: 독립 작업을 동시 처리. Research, 독립 파일 수정에 강력"
