---
type: concept
tags: [plan-mode, read-only, planning, agent]
created: 2026-05-24
sources: [4. Plan_mode Sequential and Parallel agents.pdf]
---

# Plan Mode (플랜 모드)

## 정의
Agent CLI에서 계획만 세우고 코드는 건드리지 않는 모드로, 진입 시 read-only 도구만 활성화되어 파일 수정·생성·삭제·명령 실행이 차단된다.

## 상세 설명

Plan Mode는 에이전트가 코드를 작성하기 전에 충분한 분석과 계획을 수립하도록 강제하는 메커니즘이다. 사용자가 계획을 검토하고 승인하면 그때 구현 모드로 전환된다.

**활성화 도구:**
- ✅ 파일 읽기
- ✅ 검색
- ✅ 웹 조회

**비활성화 도구:**
- ❌ 파일 수정·생성·삭제
- ❌ 명령 실행

**산출물:** 마크다운 파일 (At Memory space)

**EPCC 패턴에서의 위치:**
```
Explore → Plan (← Plan Mode 사용) → Code → Commit
```

Plan Mode는 EPCC 패턴의 "Plan" 단계를 구현하는 도구다. "바로 코딩하지 않고 먼저 읽고 계획한다"는 원칙을 기계적으로 강제한다.

## 관련 개념

- [[Agentic Coding]] — Plan Mode를 통해 SDLC 계획 단계 보장
- [[Sequential Agent]] — Plan Mode 결과물이 Sequential Agent의 첫 번째 산출물이 됨
- [[Hand-off 파일]] — Plan Mode의 마크다운 산출물
- [[Contract-Driven Iteration]] — Plan Mode로 생성된 계획이 Contract 역할을 함

## 출처

- [[source: 4. Plan_mode Sequential and Parallel agents.pdf]] — "Agent CLI에서 계획만 세우고, 코드는 건드리지 않는 모드"
