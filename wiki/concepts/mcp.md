---
type: concept
tags: [MCP, protocol, tool-calling, integration]
created: 2026-05-24
sources: [8. Model Context Protocol.pdf]
---

# MCP (Model Context Protocol)

## 정의
Anthropic이 만들고 OpenAI, Google 등이 참여하여 표준화한 프로토콜로, AI 에이전트가 다양한 외부 시스템(DB, API, 서비스)과 동일한 방식으로 연결될 수 있도록 하는 "AI용 USB 인터페이스".

## 상세 설명

MCP 이전에는 AI 에이전트가 DB/System/API에 연결하려면 매번 별도의 커넥터 코드를 작성하거나, AI가 긴 시간 동안 직접 분석해야 했다. MCP는 이 연동 작업을 표준화함으로써 비용과 복잡성을 줄인다.

**OOP 관점의 MCP:**
- **캡슐화**: Tool Calling 내부의 구현 세부사항을 숨긴다
- **추상화**: 다양한 외부 시스템을 동일한 인터페이스로 접근
- **다형성**: 어떤 AI 에이전트든 동일한 방식으로 도구를 호출

**트레이드오프 — Context Explosion:**
MCP 도구가 많을수록 에이전트가 각 도구의 기능을 추론해야 하므로, 컨텍스트 사용량이 폭발적으로 증가할 수 있다.

**MCP 사용 원칙 (Journal용):**
- MCP는 `append`/`read`만 사용할 것
- `execute` 도구를 MCP에 추가하면 외부 wrapper가 되어 에이전트 제어권을 잃음

## 관련 개념

- [[Tool Calling]] — MCP의 핵심 동작 메커니즘
- [[Orchestrator]] — MCP를 활용하여 외부 시스템에 연결하는 상위 에이전트
- [[Harness Engineering]] — Journal 저장소로 MCP 활용 가능
- [[FastMCP]] — Python MCP 서버 구현 라이브러리

## 출처

- [[source: 8. Model Context Protocol.pdf]] — "Claude, Codex, Gemini 같은 AI 에이전트가 다양한 외부 시스템과 동일한 방식으로 연결될 수 있도록 만드는 'AI용 USB 인터페이스'"
