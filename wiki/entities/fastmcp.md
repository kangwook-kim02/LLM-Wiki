---
type: entity
tags: [도구, MCP, Python, 프레임워크]
created: 2026-05-27
sources: [8. Model Context Protocol.pdf]
---

# FastMCP

## 요약
Python으로 MCP 서버를 빠르게 구현할 수 있는 프레임워크. AgentMEMO 등 MCP 기반 도구 구현에 활용된다.

## 주요 특징

- **간단한 MCP 서버 구축**: FastAPI 스타일의 데코레이터로 MCP Tool을 선언
- **AgentMEMO 구현에 사용**: `memo.create`, `memo.get`, `memo.list`, `memo.update`, `memo.append` 툴을 SQLite에 저장하는 서버 구현
- **표준 MCP 프로토콜 준수**: `/mcp POST` 수신 → `tools/list` → `tools/call` 흐름 지원

## AgentMEMO 구현 흐름

```python
from fastmcp import FastMCP

mcp = FastMCP("AgentMEMO")

@mcp.tool()
def memo_create(title: str, content: str) -> dict:
    # SQLite에 저장
    ...

@mcp.tool()
def memo_get(id: int) -> dict:
    ...

if __name__ == "__main__":
    mcp.run()
```

**MCP 실습 흐름:**
1. AgentMEMO 클론 → 프로젝트 목표 분석
2. AI 에이전트와 논의하여 입력 스키마 결정
3. FastMCP로 `agentmemo.server`의 tools 구현
4. 검증: 서버 실행 → `/mcp` POST 수신 → `tools/list` → `tools/call` → SQLite 저장 확인

## 관련 항목

- [[MCP (Model Context Protocol)]] — FastMCP가 구현하는 표준 프로토콜
- [[Harness Engineering]] — FastMCP로 구현한 MCP가 Journal 구성 요소로 활용됨

## 출처

- [[source: 8. Model Context Protocol.pdf]] — "FastMCP를 이용한 AgentMEMO 서버 구현: memo.create, memo.get, memo.list, memo.update, memo.append 툴을 SQLite에 저장"
