---
type: topic
tags: [agent-architecture, patterns, orchestrator, pipeline]
created: 2026-05-24
sources: [4. Plan_mode Sequential and Parallel agents.pdf, 5. Agent Specifications.pdf, 6. Agent pool and Orchestrator.pdf, 7. Harness and Skills.pdf]
---

# 에이전트 아키텍처 패턴

## 개요

에이전틱 코딩 시스템에서 에이전트들이 어떻게 구성되고 협력하는지를 정의하는 패턴들의 집합. 작업의 복잡도와 독립성에 따라 적절한 패턴을 선택한다.

## 핵심 구성 요소

### 기본 에이전트 유형

- [[Sequential Agent]] — 앞 단계가 완료되어야 다음 단계 시작. 단계 간 의존성이 있을 때.
- [[Parallel Agent]] — 독립 작업을 동시 처리. Research, 독립 파일 수정에 강력.
- [[Orchestrator]] — 에이전트 풀에서 적절한 에이전트를 선택하여 실행.
- [[Agent Pool]] — 에이전트 설정을 JSON으로 관리하는 에이전트 레지스트리.

### 협력 패턴

| 패턴 | 구조 | 적합한 상황 |
|------|------|------------|
| **Prompt Chaining** | A → B → C (결과 전달) | 단계 간 의존성이 있음 |
| **Routing** | Input → [모델 선택] → 실행 | 입력 종류에 따라 다른 처리 필요 |
| **Parallelization** | Input → [A, B, C 동시] → 통합 | 독립 작업이 여러 개 |
| **Orchestrator-Workers** | Orchestrator → [Worker 배분] | 작업 수를 미리 모름 |
| **Evaluator-Optimizer** | Generate → Evaluate → Improve | 품질 기준이 있는 반복 작업 |
| **Ping-Pong** | Planner ↔ Reviewer (점수 기준) | 품질 보증이 필요한 계획 수립 |

### 고급 패턴

- **Three-Agent Harness**: Planner → Generator → Evaluator. 계획, 구현, 평가를 완전히 분리.
- **EPCC**: Explore → Plan → Code → Commit. 탐색 없이 코딩하지 않는 원칙.
- **TDD**: Red → Green → Refactor. 테스트 우선 개발.

## 관계도

```
작업 복잡도
    │
    ▼ 낮음
[Single Agent]
    │
    ▼
[Sequential Agent Pipeline]
  Planner → Reviewer → Coder → Tester
  (Hand-off 파일로 컨텍스트 전달)
    │
    ▼
[Agent Pool + Orchestrator]
  .pool/plan.json
  .pool/review.json     ← Orchestrator가 동적으로 선택
  .pool/code.json
    │
    ▼ 높음
[Multi-Agent + MCP]
  Parallel Research + Sequential Implementation + MCP Storage
```

## 패턴 선택 가이드

| 상황 | 선택 패턴 |
|------|----------|
| 단계 간 의존성이 있다 | Prompt Chaining / Sequential |
| 독립 작업이 여러 개다 | Parallelization |
| 작업 수를 미리 모른다 | Orchestrator-Workers |
| 품질 기준이 있는 반복이다 | Evaluator-Optimizer / Ping-Pong |
| 완전한 분리가 필요하다 | Three-Agent Harness |

## 미해결 질문

- Agent Pool의 크기가 늘어날 때 Orchestrator의 컨텍스트 비용을 어떻게 관리하는가?
- Ping-Pong 패턴에서 무한 루프를 방지하는 최적의 종료 조건은?

## 출처

- [[source: 4. Plan_mode Sequential and Parallel agents.pdf]]
- [[source: 5. Agent Specifications.pdf]]
- [[source: 6. Agent pool and Orchestrator.pdf]]
- [[source: 7. Harness and Skills.pdf]]
