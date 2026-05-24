---
type: source
tags: [강의자료, loop, hook, automation, lifecycle, CSE3308]
created: 2026-05-24
---

# Loop and Hooks

**파일:** `raw/9. Loop and Hooks.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Week 12)

## 핵심 주장

- **Hook 정의**: Agent의 생애 주기 동안 특정 시점/조건 만족 시마다 자동으로 실행 가능한 스크립트.
- **Hook의 주 목적**: AI Agent가 확률에 따른 잘못된 결정을 내릴 수 있는 부분들을 Hook을 이용하여 결정론적인 결과물을 낼 수 있도록 하는 것.
- **Loop**: Claude에서 거의 독점적으로 지원하는 기능. Codex 및 Gemini에서는 OS 스케줄러를 활용해야 함.
- **비용 주의**: Loop가 Read/Write를 수반하면 일정 시간마다 작업 비용이 발생하므로, 단순 Status Checking 위주로 활용 권장.
- **로컬 모델 비용 절감**: 개인 GPU로 로컬 모델(Qwen3.5 27b 등)을 호출하면 fire는 상용 에이전트, action은 로컬 에이전트로 분리하여 비용 절감 가능.

## Hook 이벤트 종류

| 이벤트 | 설명 |
|--------|------|
| `UserPromptSubmit` | 사용자가 프롬프트를 제출했을 때 |
| `PreToolUse` | Codex가 도구를 쓰기 직전 |
| `PostToolUse` | 도구 실행이 끝난 직후 |
| `PermissionRequest` | 권한 요청이 발생할 때 |
| `Stop` | 한 turn이 끝나려 할 때 |
| `SessionStart` | 세션 시작/재개 시점 |

## Hook 유의미한 사용 패턴

- **At Stop**: 에이전트에게 셸 스크립트 실행, 작업 완료 보고. 특정 에이전트 작업 완료 시 SDK/subprocess로 다른 에이전트 작동.
- **At PostToolUse**: 어떤 도구를 사용했는지 기록 남기기(LOG).
- **At UserPromptSubmit**: `/docs`와 같은 지식 베이스에 이미 존재하는지 체크, 추가 프롬프트 강제 주입.

## 주요 개념

- [[Loop]], [[Hook]], [[에이전트 생애 주기]], [[결정론적 결과]], [[비용 최적화]]

## 주목할 인사이트

- Hook의 핵심 철학: "AI Agent가 확률에 따른 잘못된 결정을 내릴 수 있는 부분들을 Hook을 이용하여 결정론적인 결과물을 낼 수 있도록" — 에이전트 신뢰성의 핵심 메커니즘.
- Loop의 Claude 독점성: Codex/Gemini에서는 OS 스케줄러를 써야 하므로, 자동화 루프가 필요한 경우 Claude Code가 유리한 선택.
- `UserPromptSubmit` Hook + 지식 베이스 검색: 이 LLM Wiki 프로젝트와 직접 연결되는 패턴. 사용자의 지시가 wiki에 이미 있는지 Hook으로 체크 가능.

## Wiki 업데이트 내역

- 생성: [[source: source-09-loop-hooks]]
- 생성: [[Loop]] (wiki/concepts/loop.md)
- 생성: [[Hook]] (wiki/concepts/hook.md)
- 업데이트: [[Harness Engineering]] (wiki/concepts/harness-engineering.md)
- 업데이트: [[Claude Code]] (wiki/entities/claude-code.md)
