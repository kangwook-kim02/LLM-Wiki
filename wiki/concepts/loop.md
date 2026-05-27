---
type: concept
tags: [loop, 자동화, 반복실행, claude]
created: 2026-05-27
sources: [9. Loop and Hooks.pdf]
---

# Loop (루프)

## 정의

에이전트가 특정 작업을 일정 간격 또는 조건에 따라 반복적으로 자동 실행하는 기능. Claude Code에서 거의 독점적으로 지원된다.

## 상세 설명

Loop는 에이전트에게 "계속 확인하고 행동하라"는 자동화 메커니즘이다. Codex와 Gemini에서는 Loop 기능이 없어 OS 스케줄러(cron, Task Scheduler)를 활용해야 한다.

**Loop 활용 패턴:**

```
[Claude Loop 예시]
/loop 5m /lint          ← 5분마다 wiki lint 실행
/loop check-build       ← 빌드 상태 계속 확인
```

**비용 주의사항:**

Loop가 Read/Write를 수반하면 반복마다 토큰 비용이 발생한다. 권장 사용법:
- ✅ 단순 Status Checking (파일 존재 여부, 조건 확인)
- ✅ 경량 모니터링
- ❌ 매 반복마다 LLM 추론이 필요한 복잡한 작업

**비용 절감 전략 — 로컬 모델 분리:**

```
fire (트리거 감지)  → 상용 에이전트 (Claude)
action (실제 작업) → 로컬 에이전트 (Qwen3.5 27b 등)
```

개인 GPU로 로컬 모델을 호출하면 action 비용을 크게 줄일 수 있다.

**[[Hook]]과의 관계:**

| | Loop | Hook |
|---|---|---|
| 트리거 | 시간 간격 | 에이전트 생애 주기 이벤트 |
| 주도권 | 에이전트가 주기적으로 실행 | 특정 이벤트 발생 시 자동 실행 |
| 지원 | Claude 독점 | Claude, 일부 다른 에이전트 |
| 용도 | 반복 모니터링·자동화 | 결정론적 보정·로깅 |

## 관련 개념

- [[Hook]] — 생애 주기 이벤트 기반 자동 실행 (Loop와 상호 보완)
- [[Claude Code]] — Loop 기능을 지원하는 주요 에이전트
- [[Contract-Driven Iteration]] — Loop의 종료 조건을 Contract가 정의

## 출처

- [[source: 9. Loop and Hooks.pdf]] — "Loop: Claude에서 거의 독점적으로 지원하는 기능. Codex 및 Gemini에서는 OS 스케줄러를 활용해야 함."
