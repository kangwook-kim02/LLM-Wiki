---
type: source
tags: [강의자료, subprocess, CLI, python, CSE3308]
created: 2026-05-24
---

# Agents Subprocess Calling

**파일:** `raw/3. Agents subprocess calling.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Week 3)

## 핵심 주장

- **Coding은 SDLC의 극히 일부**: AI가 코드를 빠르게 생성하지만, 좋은 시스템을 만들기 위해서는 그것만으로 충분하지 않다.
- **CLI 호출 두 가지 방식**: (1) 터미널에서 명령줄 인자로 직접 실행, (2) Python `subprocess.run()`으로 stdin 파이프를 통해 프롬프트 전달.
- **에이전트 권한 수준의 트레이드오프**: YOLO Mode(`--dangerously-skip-permissions`)는 편리하지만, 에이전트가 사용자의 의도와 무관하게 파일을 삭제하는 사고가 발생할 수 있다.
- **세션 관리**: `claude -c`, `claude --resume`, `codex resume`, `gemini --resume` 등으로 이전 세션을 이어갈 수 있다.

## 주요 개념

- [[Subprocess]], [[CLI 에이전트]], [[세션 관리]], [[에이전트 권한]], [[YOLO Mode]]

## 주목할 인사이트

- Gemini는 `-p` 플래그에 프롬프트가 필수(stdin 전달 불가)인 반면, Claude/Codex는 stdin으로 프롬프트를 전달한다 → 에이전트마다 호출 방식이 다름.
- `subprocess.run()` 핵심 파라미터: `input`(stdin), `capture_output`(stdout/stderr 캡처), `text`(문자열 처리), `timeout`(최대 대기 시간).
- Python으로 에이전트를 호출할 때는 OS별 바이너리 이름 차이(`codex.cmd` vs `codex`)를 처리해야 한다.

## 에이전트별 subprocess 호출 패턴

```python
# Claude
subprocess.run(["claude", "-p"], input="프롬프트", capture_output=True, text=True)

# Codex (Windows)
subprocess.run(["codex.cmd", "exec"], input="프롬프트", capture_output=True, text=True)

# Gemini (Windows)
subprocess.run(["gemini.cmd", "-p", "프롬프트"], capture_output=True, text=True)
```

## Wiki 업데이트 내역

- 생성: [[source: source-03-subprocess-calling]]
- 생성: [[Subprocess]] (wiki/concepts/subprocess.md)
- 업데이트: [[Claude Code]] (wiki/entities/claude-code.md)
- 업데이트: [[Codex CLI]] (wiki/entities/codex-cli.md)
- 업데이트: [[Gemini CLI]] (wiki/entities/gemini-cli.md)
