---
type: concept
tags: [contract-driven, iteration, TASK.md, harness]
created: 2026-05-27
sources: [7. Harness and Skills.pdf]
---

# Contract-Driven Iteration (계약 기반 반복)

## 정의

에이전트가 Contract(TASK.md)를 읽고 `Done when` 조건을 만족할 때까지 반복하는 실행 방식. 명시적인 달성 조건과 최대 작업 상한이 있어야 한다.

## 상세 설명

Contract-Driven Iteration은 [[Harness Engineering]]의 핵심 원리다. 에이전트에게 "무엇이 끝난 상태인지"를 명확히 정의해야 루프가 종료될 수 있다.

**TASK.md (Contract 파일) 구조:**

```markdown
# Task: [작업명]

## Goal
달성해야 할 목표

## Done when
- [ ] 조건 1
- [ ] 조건 2
- [ ] 조건 3

## Max attempts
10

## Constraints
- 해서는 안 되는 것들
```

**Ralph Ruf의 Loop 패턴:**

```
Phase 1: 명세 작성 (TASK.md 생성)
Phase 2: Plan 수립
while (Done when 조건 미충족 AND attempts < max):
    Phase 3: 작업 → 검증 → 커밋
```

**핵심 경구:**

> "Contract가 없는 Procedure는 무한 루프이고,  
> Procedure가 없는 Contract는 죽은 문서다."

**Contract의 필수 요소:**
- `Done when` 조건: 언제 작업이 완료되었는지 검증 가능한 기준
- `Max attempts`: 무한 루프 방지를 위한 상한선
- `Constraints`: 에이전트가 해서는 안 되는 행동 명시

## 관련 개념

- [[Harness Engineering]] — Contract는 하네스의 4가지 구성 요소 중 하나
- [[Skill]] — Contract와 함께 동작하는 Procedure 파일
- [[Hook]] — Contract 조건 달성 시 트리거되는 메커니즘
- [[Agent Specification]] — 에이전트별 Contract에 해당하는 문서

## 출처

- [[source: 7. Harness and Skills.pdf]] — "에이전트가 Contract(TASK.md)를 읽고 Done when 조건을 만족할 때까지 반복하는 방식. 명시적인 달성 조건과 최대 작업 상한이 있어야 한다."
