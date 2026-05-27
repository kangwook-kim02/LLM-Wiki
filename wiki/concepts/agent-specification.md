---
type: concept
tags: [agent-specification, system-prompt, context-engineering]
created: 2026-05-27
sources: [5. Agent Specifications.pdf]
---

# Agent Specification (에이전트 명세)

## 정의

에이전트가 수행할 역할, 입출력, 완료 조건을 명확히 정의한 문서. 에이전트가 일관되고 예측 가능하게 동작하도록 보장한다.

## 상세 설명

Agent Specification은 4가지 핵심 구성 요소로 이루어진다:

| 구성 요소 | 설명 |
|----------|------|
| **System Prompt** | 에이전트의 행동 방식과 역할 정의 |
| **Context** | Session ID, Project Info, Hand-Off 파일 경로 |
| **Inputs** | 에이전트가 받는 입력의 형식과 출처 |
| **Outputs** | 에이전트가 생성하는 산출물의 형식과 저장 위치 |

**Planner-Reviewer 패턴에서의 명세:**

```
AGENT1 (Planner)
  Role: 요청 분석 → 목표 분해 → TODO 생성
  Input: 사용자 요청, 이전 Reviewer 피드백
  Output: workspace/planning.md (TODO 목록 + AC)

AGENT2 (Reviewer)
  Role: 유효성 검사 → 기술 검토 → 점수 평가
  Input: workspace/planning.md
  Output: workspace/review.md (점수 + 개선사항)
```

**System Prompt 단계 (Planner):**
1. Analysis — Goal과 Constraints 판단
2. Decomposition — 목표를 실현 가능한 단위로 분해
3. Planning — 각 TODO에 입력·출력·완료 기준(AC) 구체화

**System Prompt 단계 (Reviewer):**
1. Validation — 모든 TODO에 입력/출력/AC 존재 확인
2. Review — 기술적 구현 가능성·의존성 순서·모호한 부분 평가
3. Revise — 1~10점 점수 + 구체적 개선사항 작성

## 관련 개념

- [[Harness Engineering]] — Specification은 Preference 구성 요소에 해당
- [[Contract-Driven Iteration]] — Specification의 Done when 조건으로 반복 종료
- [[Ping-Pong 패턴]] — Planner ↔ Reviewer가 Specification 기반으로 협상
- [[Agent Pool]] — JSON으로 저장된 에이전트 Specification 레지스트리

## 출처

- [[source: 5. Agent Specifications.pdf]] — "Agent Specification 구성 요소: System Prompt + Context + Inputs + Outputs"
