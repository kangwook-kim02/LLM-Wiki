"""
setup.py — LLM-Wiki 환경별 MCP 서버 설정 자동 생성 스크립트

사용법:
    1. .env.example을 복사해 .env를 생성한다.
       cp .env.example .env   (Windows: copy .env.example .env)
    2. .env를 열어 PYTHON_CMD, PROJECT_ROOT를 현재 환경에 맞게 수정한다.
    3. 프로젝트 루트에서 실행한다.
       python setup.py

생성되는 파일:
    .claude/settings.json   — Claude Code CLI 및 Flask 뷰어 채팅 패널 공용 MCP 서버 설정
"""

import json
import os
from pathlib import Path


def load_env(env_path: Path) -> dict:
    """
    .env 파일을 파싱하여 key=value 딕셔너리로 반환한다.
    주석(#)과 빈 줄은 무시한다.
    """
    env = {}
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            env[key.strip()] = value.strip()
    return env


def build_mcp_config(python_cmd: str, project_root: str) -> dict:
    """MCP 서버 설정 딕셔너리를 생성한다."""
    server_script = str(Path(project_root) / "mcp_server" / "server.py")
    pythonpath = str(Path(project_root) / "mcp_server")
    return {
        "mcpServers": {
            "llm-wiki": {
                "command": python_cmd,
                "args": [server_script],
                "env": {
                    "PYTHONPATH": pythonpath
                }
            }
        }
    }


def write_json(path: Path, data: dict) -> None:
    """딕셔너리를 JSON 파일로 저장한다. 상위 디렉토리가 없으면 생성한다."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  생성 완료: {path}")


def main():
    project_root = Path(__file__).parent.resolve()
    env_path = project_root / ".env"

    # .env 파일 존재 여부 확인
    if not env_path.exists():
        print("[오류] .env 파일을 찾을 수 없습니다.")
        print("  .env.example을 복사하여 .env를 생성한 후 값을 수정하세요.")
        print("    Windows: copy .env.example .env")
        print("    macOS/Linux: cp .env.example .env")
        raise SystemExit(1)

    env = load_env(env_path)

    # 필수 변수 확인
    missing = [k for k in ("PYTHON_CMD", "PROJECT_ROOT") if k not in env or not env[k]]
    if missing:
        print(f"[오류] .env에 다음 변수가 없거나 비어 있습니다: {', '.join(missing)}")
        raise SystemExit(1)

    python_cmd = env["PYTHON_CMD"]
    root = env["PROJECT_ROOT"]

    print(f"PYTHON_CMD   = {python_cmd}")
    print(f"PROJECT_ROOT = {root}")
    print()

    config = build_mcp_config(python_cmd, root)

    write_json(project_root / ".claude" / "settings.json", config)

    print()
    print("설정 완료. 이제 'claude' 명령으로 Claude Code를 실행하세요.")


if __name__ == "__main__":
    main()
