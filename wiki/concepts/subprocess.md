---
type: concept
tags: [subprocess, CLI, python, 에이전트호출]
created: 2026-05-27
sources: [3. Agents subprocess calling.pdf]
---

# Subprocess (서브프로세스)

## 정의

Python의 `subprocess.run()`을 통해 Claude, Codex, Gemini 등의 CLI 에이전트를 외부 프로세스로 호출하는 방식.

## 상세 설명

Subprocess 호출은 에이전트를 프로그래밍 방식으로 자동화할 때 핵심 패턴이다. 두 가지 방식이 있다:

1. **터미널 직접 실행**: CLI에서 명령줄 인자로 프롬프트 전달
2. **Python subprocess**: `subprocess.run()`으로 stdin 파이프를 통해 프롬프트 전달

**에이전트별 호출 패턴:**

```python
import subprocess

# Claude — stdin으로 프롬프트 전달
result = subprocess.run(
    ["claude", "-p"],
    input="프롬프트 내용",
    capture_output=True,
    text=True,
    timeout=180
)

# Codex — stdin으로 프롬프트 전달 (Windows)
result = subprocess.run(
    ["codex.cmd", "exec"],
    input="프롬프트 내용",
    capture_output=True,
    text=True
)

# Gemini — -p 플래그에 프롬프트 직접 전달 (stdin 불가)
result = subprocess.run(
    ["gemini.cmd", "-p", "프롬프트 내용"],
    capture_output=True,
    text=True
)
```

**`subprocess.run()` 핵심 파라미터:**

| 파라미터 | 역할 |
|---------|------|
| `input` | stdin으로 전달할 프롬프트 문자열 |
| `capture_output` | stdout/stderr 캡처 여부 |
| `text` | 문자열(str)로 처리 여부 |
| `timeout` | 최대 대기 시간 (초) |

**주의사항:**
- OS별 바이너리 이름 차이 처리 필요 (`codex.cmd` vs `codex`)
- Gemini는 stdin 전달 불가, `-p` 플래그 필수
- YOLO Mode(`--dangerously-skip-permissions`)는 편리하지만 사고 위험 있음

## 관련 개념

- [[Claude Code]] — subprocess 호출 시 `claude -p` 패턴 사용
- [[Codex CLI]] — subprocess 호출 시 `codex.cmd exec` 패턴 사용
- [[Gemini CLI]] — subprocess 호출 시 `-p` 플래그 필수
- [[Orchestrator]] — subprocess를 통해 에이전트를 동적으로 실행

## 출처

- [[source: 3. Agents subprocess calling.pdf]] — "Python subprocess.run()으로 stdin 파이프를 통해 프롬프트 전달"
