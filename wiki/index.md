# Wiki Index

> 이 파일은 LLM이 자동으로 유지합니다. 직접 수정하지 마세요.
> 마지막 업데이트: 2026-05-27

---

## 소스 요약 (`wiki/sources/`)

| 페이지 | 요약 | 인제스트 날짜 |
|--------|------|--------------|
| [Vibe Coding and Agent Coding](sources/source-01-vibe-coding-agent-coding.md) | 소프트웨어 엔지니어링 패러다임 전환, Vibe Coding vs Agentic Coding 개요 | 2026-05-24 |
| [SDLC Pipeline in Vibe Coding](sources/source-02-sdlc-pipeline.md) | SDLC 단계별 AI 협업, Spec-Driven Development, 에이전트 구조 비교 | 2026-05-24 |
| [Agents Subprocess Calling](sources/source-03-subprocess-calling.md) | Python subprocess로 CLI 에이전트 호출, 세션 관리, 권한 트레이드오프 | 2026-05-24 |
| [Plan Mode, Sequential and Parallel Agents](sources/source-04-plan-mode-sequential-parallel.md) | Plan Mode, Hand-off 파일 패턴, 도구 간 협업 | 2026-05-24 |
| [Agent Specifications](sources/source-05-agent-specifications.md) | Agent Specification 구성요소, System Prompt, Ping-Pong 패턴 | 2026-05-24 |
| [Agent Pool and Orchestrator](sources/source-06-agent-pool-orchestrator.md) | 에이전트 상태 관리, Agent Pool JSON 구조, Orchestrator 역할 | 2026-05-24 |
| [Harness and Skills](sources/source-07-harness-skills.md) | Harness Engineering, Contract-Driven Iteration, Skill, 에이전틱 코딩 패턴 | 2026-05-24 |
| [Model Context Protocol](sources/source-08-mcp.md) | MCP 정의, Tool Calling, Context Explosion 트레이드오프 | 2026-05-24 |
| [Loop and Hooks](sources/source-09-loop-hooks.md) | Hook 이벤트 종류, Loop 자동화, 결정론적 실행 | 2026-05-24 |

---

## 개념 (`wiki/concepts/`)

| 페이지 | 요약 |
|--------|------|
| [Vibe Coding](concepts/vibe-coding.md) | 자연어로 코드를 생성하는 LLM 개발 방식 (2024.4Q~2025.3Q) |
| [Agentic Coding](concepts/agentic-coding.md) | SDLC가 보장되는 에이전트 기반 개발 패러다임 (2025.4Q~) |
| [SDLC](concepts/sdlc.md) | Planning~Maintenance까지 소프트웨어 개발 전 단계를 아우르는 체계적 프로세스 |
| [PRD](concepts/prd.md) | "Spec First, Code Later"의 핵심 산출물. 코드 작성 전 시스템 요구사항 정의 문서 |
| [Sequential Agent](concepts/sequential-agent.md) | 앞 단계 완료 후 다음 단계가 시작되는 의존성 기반 에이전트 체인 |
| [Parallel Agent](concepts/parallel-agent.md) | 독립 작업을 동시에 처리하는 에이전트 구조 |
| [Harness Engineering](concepts/harness-engineering.md) | Contract+Procedure+Journal+Preference로 에이전트 실행 환경을 구조화하는 기술 |
| [Plan Mode](concepts/plan-mode.md) | read-only 도구만 활성화하여 계획 단계를 강제 분리하는 모드 |
| [Agent Specification](concepts/agent-specification.md) | 에이전트의 역할·입출력·완료 조건을 정의한 명세 문서 |
| [Orchestrator](concepts/orchestrator.md) | Agent Pool에서 목표에 맞는 에이전트를 동적으로 선택·실행하는 관리자 |
| [Agent Pool](concepts/agent-pool.md) | 에이전트 설정을 JSON으로 관리하는 레지스트리 (.pool/*.json) |
| [Contract-Driven Iteration](concepts/contract-driven-iteration.md) | TASK.md의 Done when 조건을 만족할 때까지 반복하는 실행 방식 |
| [Skill](concepts/skill.md) | 에이전트가 특정 작업을 수행하는 절차를 정의한 Markdown 파일 |
| [Subprocess](concepts/subprocess.md) | Python subprocess.run()으로 CLI 에이전트를 프로그래밍 방식으로 호출 |
| [Loop](concepts/loop.md) | 에이전트가 작업을 주기적으로 자동 반복 실행하는 기능 (Claude 독점) |
| [MCP (Model Context Protocol)](concepts/mcp.md) | AI 에이전트와 외부 시스템 연결을 표준화한 "AI용 USB 인터페이스" |
| [Hook](concepts/hook.md) | 에이전트 생애 주기에 결정론적 스크립트를 주입하는 메커니즘 |

---

## 엔티티 (`wiki/entities/`)

| 페이지 | 요약 |
|--------|------|
| [Andrej Karpathy](entities/andrej-karpathy.md) | Vibe Coding 용어 창시자, LLM Wiki 패턴 제안자 |
| [Claude Code](entities/claude-code.md) | Anthropic의 CLI LLM 에이전트. Loop/Hook 지원, CLAUDE.md 스키마 |
| [Codex CLI](entities/codex-cli.md) | OpenAI의 CLI LLM 에이전트. Git sandbox 필수, AGENTS.md 스키마 |
| [Gemini CLI](entities/gemini-cli.md) | Google의 CLI LLM 에이전트. -p 플래그 필수, GEMINI.md 스키마 |
| [FastMCP](entities/fastmcp.md) | Python으로 MCP 서버를 빠르게 구현하는 프레임워크 |

---

## 주제 개요 (`wiki/topics/`)

| 페이지 | 요약 |
|--------|------|
| [Agentic Coding 개요](topics/agentic-coding-overview.md) | 패러다임 전환부터 Harness까지 전체 그림 |
| [에이전트 아키텍처 패턴](topics/agent-architecture-patterns.md) | Sequential/Parallel/Orchestrator-Workers 등 패턴 선택 가이드 |

---

## 통계

- 총 소스: **9**
- 총 wiki 페이지: **33** (9 sources + 17 concepts + 5 entities + 2 topics)
- 마지막 인제스트: 2026-05-24 (초기 일괄 인제스트)
- 마지막 페이지 보완: 2026-05-27 (미생성 13개 페이지 작성)
- 마지막 lint: —
