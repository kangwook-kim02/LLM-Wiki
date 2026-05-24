---
type: entity
tags: [도구, CLI, Anthropic, LLM-agent]
created: 2026-05-24
sources: [1. Vibe coding and Agent coding.pdf, 3. Agents subprocess calling.pdf, 9. Loop and Hooks.pdf]
---

# Claude Code

## 요약
Anthropic이 개발한 CLI 기반 LLM 에이전트로, CLAUDE.md 스키마 기반 작업 자동화, Plan Mode, Loop/Hook, Skill 등을 지원하는 에이전틱 코딩 도구.

## 주요 특징

- **CLAUDE.md**: 에이전트의 행동 방식을 정의하는 스키마 파일. 프로젝트 루트에 위치하며 세션마다 자동으로 로드됨.
- **Plan Mode**: read-only 도구만 활성화하여 계획 단계를 강제 분리.
- **Loop 기능**: 반복 자동화를 지원하는 Claude 거의 독점 기능. Codex/Gemini는 OS 스케줄러 활용 필요.
- **Hook 지원**: `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart` 등 생애 주기 이벤트에 스크립트 연결 가능.
- **세션 관리**: `claude -c`(최근 세션 이어감), `claude --resume`(세션 목록 선택), `claude --resume <session-id>`.
- **Subprocess 호출**: `subprocess.run(["claude", "-p", "--no-session-persistence", "--output-format", "json"], input=prompt)`.

## 관련 항목

- [[Codex CLI]], [[Gemini CLI]] — 경쟁/보완 도구
- [[Harness Engineering]] — Claude Code를 활용한 하네스 구축
- [[CLAUDE.md]] — Claude Code의 에이전트 스키마 파일
- [[Hook]], [[Loop]] — Claude Code가 독점적으로 지원하는 자동화 기능

## 출처

- [[source: 1. Vibe coding and Agent coding.pdf]] — "(추천) Anthropic Claude"
- [[source: 3. Agents subprocess calling.pdf]] — subprocess 호출 방식
- [[source: 9. Loop and Hooks.pdf]] — "Loop 기능은 Claude에서만 거의 독점적으로 지원"
