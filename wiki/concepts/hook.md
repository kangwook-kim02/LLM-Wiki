---
type: concept
tags: [hook, automation, lifecycle, deterministic]
created: 2026-05-24
sources: [9. Loop and Hooks.pdf]
---

# Hook (훅)

## 정의
Agent의 생애 주기 동안 특정 시점 또는 조건 만족 시마다 자동으로 실행 가능한 스크립트로, AI 에이전트의 확률적 결정을 결정론적 결과로 보정하는 메커니즘.

## 상세 설명

Hook의 핵심 목적은 **결정론화**다. AI 에이전트는 확률 기반으로 작동하기 때문에 동일한 입력에도 다른 결과가 나올 수 있다. Hook은 이런 불확실한 지점에 결정론적 스크립트를 주입하여 신뢰성을 높인다.

**Hook 이벤트 종류:**

| 이벤트 | 실행 시점 | 활용 예시 |
|--------|-----------|-----------|
| `UserPromptSubmit` | 사용자가 프롬프트를 제출했을 때 | 지식 베이스 중복 체크, 추가 프롬프트 주입 |
| `PreToolUse` | 도구를 쓰기 직전 | 권한 확인, 로깅 |
| `PostToolUse` | 도구 실행이 끝난 직후 | 도구 사용 이력 기록(LOG) |
| `PermissionRequest` | 권한 요청이 발생할 때 | 권한 정책 자동 처리 |
| `Stop` | 한 turn이 끝나려 할 때 | 셸 스크립트 실행, 작업 완료 보고, 다른 에이전트 트리거 |
| `SessionStart` | 세션 시작/재개 시점 | 상태 복원, 초기화 |

**이 LLM Wiki와의 연결:**
`UserPromptSubmit` Hook에 wiki 검색을 연결하면, 사용자의 질문이 이미 wiki에 존재하는지 자동으로 체크하는 시스템을 구축할 수 있다.

## 관련 개념

- [[Loop]] — Hook과 함께 자동화의 두 축
- [[Harness Engineering]] — Hook은 하네스의 결정론적 안전장치
- [[에이전트 생애 주기]] — Hook이 개입하는 시점들의 집합

## 출처

- [[source: 9. Loop and Hooks.pdf]] — "AI Agent가 확률에 따른 잘못된 결정을 내릴 수 있는 부분들을 Hook을 이용하여 결정론적인 결과물을 낼 수 있도록 하는 것이 주 목적"
