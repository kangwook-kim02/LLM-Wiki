---
type: concept
tags: [orchestrator, 에이전트관리, 동적실행]
created: 2026-05-27
sources: [6. Agent pool and Orchestrator.pdf]
---

# Orchestrator (오케스트레이터)

## 정의

Agent Pool에서 목표에 맞는 에이전트를 선택하고 독립 subprocess를 통해 실행하는 관리자 에이전트.

## 상세 설명

Orchestrator는 단순한 파이프라인 실행자와 달리, **동적으로** 에이전트를 선택하고 조율한다. 미리 정해진 순서가 없고, 목표에 따라 어떤 에이전트를 쓸지 런타임에 결정한다.

**Orchestrator의 핵심 역할:**

1. `pool/*.json` 에서 사용 가능한 에이전트 목록을 읽는다
2. 현재 목표에 맞는 에이전트를 선택한다
3. 선택한 에이전트를 독립 subprocess로 실행한다
4. 각 에이전트의 상태(Processing | Idle)를 추적한다
5. 결과를 수집하고 다음 단계를 결정한다

**단순 Pipeline과의 비교:**

| | Pipeline | Orchestrator |
|---|---|---|
| 에이전트 순서 | 고정 | 동적 |
| 재사용성 | 낮음 (단일 작업) | 높음 (모든 작업에 활용) |
| 확장성 | 에이전트 추가 시 파이프라인 수정 | Pool에 등록만 하면 됨 |
| 복잡도 | 낮음 | 높음 |

**인간이 Orchestrator가 되는 경우**: Agentic Coding에서 인간의 역할은 프롬프트 엔지니어에서 Orchestrator로 변화한다 — 목표를 정의하고 에이전트들에게 작업을 배분한다.

## 관련 개념

- [[Agent Pool]] — Orchestrator가 에이전트를 선택하는 레지스트리
- [[Sequential Agent]] — Orchestrator가 순서를 정해 실행하는 패턴
- [[Parallel Agent]] — Orchestrator가 동시에 실행하는 패턴
- [[MCP (Model Context Protocol)]] — Orchestrator-Worker 패턴에서 외부 도구 연결에 활용

## 출처

- [[source: 6. Agent pool and Orchestrator.pdf]] — "pool/*.json의 에이전트 정의를 읽고, 목표에 맞는 에이전트를 선택하여 독립 subprocess를 통해 실행"
