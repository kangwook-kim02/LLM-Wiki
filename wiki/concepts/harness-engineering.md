---
type: concept
tags: [harness, engineering, contract, skill, journal]
created: 2026-05-24
sources: [7. Harness and Skills.pdf]
---

# Harness Engineering (하네스 엔지니어링)

## 정의
AI 에이전트가 복잡한 작업을 안전하고 효율적으로 완수할 수 있도록, 프롬프트나 모델을 넘어선 외부 실행 환경(도구, 데이터, 검증 파이프라인, 안전장치)을 구조적으로 설계하고 통제하는 기술.

## 상세 설명

Harness Engineering은 단순히 프롬프트를 잘 작성하는 것이 아니라, 작업의 목표·절차·기록·선호를 **분리**해 관리한다.

**4가지 핵심 구성 요소:**

| 책임 | 질문 | 파일 예시 |
|------|------|-----------|
| **Contract** | 무엇이 끝났는가? | `TASK.md` |
| **Procedure** | 어떻게 진행하는가? | `Skill` (마크다운 파일) |
| **Journal** | 지금까지 무엇을 했는가? | `log.md` 또는 MCP |
| **Preference** | 어떤 방식으로 일하는가? | `PROFILE.md`, `AGENTS.md`, `CLAUDE.md` |

> "Contract가 없는 Procedure는 무한 루프이고, Procedure가 없는 Contract는 죽은 문서다."

**Ralph Ruf의 루프 패턴:**
- Phase 1: Jobs To Be Done → AI Agent와 사람이 대화하며 `/spec` 폴더에 명세서를 만든다
- Phase 2: AI 에이전트가 기존 코드 구현체와 명세서를 비교한 뒤 Plan을 세운다
- Phase 3 (while loop): AI 에이전트가 1개의 Plan 체크리스트에 대해 작업 → 검증 → 계획 업데이트 → 커밋 → 종료

**AGENTS.md 절대 금지 사항:**
- ❌ 한 반복에서 두 개 이상의 작업을 처리하기
- ❌ 실패한 테스트를 주석 처리하거나 skip 처리하기
- ❌ `specs/` 없이 코드를 작성하기
- ❌ `journal.md`를 수정하거나 삭제하기 (오직 append)
- ❌ 사용자의 명시적 승인 없이 새 의존성 추가하기
- ❌ 같은 접근을 3번 실패한 뒤에도 시도 계속하기 → 멈추고 보고

## 관련 개념

- [[Contract-Driven Iteration]] — Harness의 핵심 반복 메커니즘
- [[Skill]] — Procedure를 구현하는 마크다운 파일
- [[Hook]] — 에이전트 생애 주기의 결정론적 실행
- [[Loop]] — 반복 자동화
- [[MCP (Model Context Protocol)]] — Journal을 세션을 넘어 저장하는 방법

## 출처

- [[source: 7. Harness and Skills.pdf]] — "AI 에이전트가 복잡한 작업을 안전하고 효율적으로 완수할 수 있도록... 외부 실행 환경을 구조적으로 설계하고 통제하는 기술"
