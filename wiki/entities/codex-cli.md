---
type: entity
tags: [도구, CLI, OpenAI, LLM-agent]
created: 2026-05-24
sources: [3. Agents subprocess calling.pdf, 4. Plan_mode Sequential and Parallel agents.pdf]
---

# Codex CLI

## 요약
OpenAI가 개발한 CLI 기반 LLM 에이전트로, Git sandbox 환경에서 작동하며 AGENTS.md 스키마를 지원한다.

## 주요 특징

- **Sandbox 필수**: Codex CLI 호출 시에는 프로젝트가 Sandbox(git repo)로 감싸져 있어야 한다. `git init` 필요.
- **Subprocess 호출**: Windows에서는 `codex.cmd exec --ephemeral --json --skip-git-repo-check`.
- **`--skip-git-repo-check`**: Git 저장소 밖에서도 실행 가능하게 하는 플래그.
- **AGENTS.md**: Codex의 에이전트 스키마 파일. `CLAUDE.md`와 동일한 역할.
- **세션 관리**: `codex resume`(세션 picker), `codex resume <id>`, `codex resume --last`.
- **권한 모드**: `codex --dangerously-bypass-approvals-and-sandbox`.
- **stdin 방식**: Claude와 동일하게 stdin으로 프롬프트 전달.

## 관련 항목

- [[Claude Code]], [[Gemini CLI]]
- [[AGENTS.md]] — Codex의 에이전트 스키마
- [[Subprocess]] — Python에서 Codex 호출 방법

## 출처

- [[source: 3. Agents subprocess calling.pdf]] — subprocess 호출 방식
- [[source: 4. Plan_mode Sequential and Parallel agents.pdf]] — "Claude와 Codex를 동시에 사용하는 경우... CLI 레벨에서 간단한 에이전틱 코딩 체계를 확보"
