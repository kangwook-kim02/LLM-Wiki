---
type: source
tags: [강의자료, MCP, model-context-protocol, tool-calling, CSE3308]
created: 2026-05-24
---

# Model Context Protocol (MCP)

**파일:** `raw/8. Model Context Protocol.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Week 11)

## 핵심 주장

- **MCP 정의**: Anthropic이 만들고 OpenAI, Google 등이 참여하며 표준화된 프로토콜. Claude, Codex, Gemini 같은 AI 에이전트가 다양한 외부 시스템과 동일한 방식으로 연결될 수 있도록 만드는 "AI용 USB 인터페이스".
- **MCP의 필요성**: 기존에는 DB/System/API 연결마다 별도의 커넥터 코드 작성이 필요했으나, 표준화된 프로토콜 사용으로 연동 비용이 줄고 성능이 개선됨.
- **OOP 관점**: 캡슐화·추상화·다형성 — MCP를 사용하면 Tool Calling 내부의 일에 대해 AI Agent가 신경 쓸 필요가 없음.
- **Context Explosion 트레이드오프**: MCP 도구가 많을수록 각 도구에 대한 기능 추론이 필요해 컨텍스트가 폭발적으로 증가.
- **MCP는 append/read만**: MCP에 execute 도구를 추가하면 외부 wrapper가 되어 제어권을 잃음. Journal 용도로는 append/read만 사용 권장.

## 주요 개념

- [[MCP (Model Context Protocol)]], [[Tool Calling]], [[Context Explosion]], [[FastMCP]], [[AgentMEMO]]

## 주목할 인사이트

- "결국엔 OOM이다": MCP는 OOP의 캡슐화·추상화·다형성 원칙을 AI 도구 연동에 적용한 것.
- FastMCP를 이용한 AgentMEMO 서버 구현: `memo.create`, `memo.get`, `memo.list`, `memo.update`, `memo.append` 툴을 SQLite에 저장.
- Orchestrator-Worker 패턴과 MCP: Sub-agent가 MCP 서버를 통해 외부 도구를 표준화된 방식으로 활용.

## MCP 실습 흐름

1. AgentMEMO 클론 → 프로젝트 목표 분석
2. AI 에이전트와 논의하여 입력 스키마 결정
3. FastMCP로 `agentmemo.server`의 tools 구현
4. 검증: 서버 실행 → /mcp POST 수신 → tools/list → tools/call → SQLite 저장 확인

## Wiki 업데이트 내역

- 생성: [[source: source-08-mcp]]
- 생성: [[MCP (Model Context Protocol)]] (wiki/concepts/mcp.md)
- 생성: [[Tool Calling]] (wiki/concepts/tool-calling.md)
- 생성: [[FastMCP]] (wiki/entities/fastmcp.md)
- 업데이트: [[Orchestrator]] (wiki/concepts/orchestrator.md)
