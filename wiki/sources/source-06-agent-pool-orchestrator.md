---
type: source
tags: [강의자료, agent-pool, orchestrator, state-management, CSE3308]
created: 2026-05-24
---

# Agent Pool and Orchestrator

**파일:** `raw/6. Agent pool and Orchestrator.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Week 6)

## 핵심 주장

- **에이전트의 상태(State)**: 에이전틱 코딩 워크플로우에서 각 에이전트는 상태(Processing | Idle)와 상태 전이, 입력과 출력, 시간의 개념을 가진다.
- **Workflow(Pipeline)의 한계**: Main Orchestrator에게 과도한 부담이 집중되고, 단일 작업에만 활용 가능하며 재사용이 어렵다.
- **Agent Pool**: 개별 에이전트의 설정값을 XML/TOML/JSON으로 관리하고, 필요한 에이전트를 Pool에 등록하여 Orchestrator가 유동적으로 활용할 수 있도록 처리.
- **Orchestrator의 역할**: `pool/*.json`의 에이전트 정의를 읽고, 목표에 맞는 에이전트를 선택하여 독립 subprocess를 통해 실행.
- **컨텍스트 파일로 에이전트 행동 제한**: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`를 이용하여 Subprocess로 실행되는 에이전트의 행동을 제한.

## 에이전트 JSON 명세 구조

```json
{
  "id": "에이전트 파일명과 동일",
  "role": "에이전트의 한 줄 역할 설명",
  "system_prompt": "에이전트에게 전달될 전체 시스템 프롬프트",
  "input": { "description": "", "format": "", "source": "" },
  "output": { "description": "", "format": "", "files": [] },
  "tools": [],
  "constraints": { "max_attempts": 3, "timeout_seconds": 180, "sandbox": "" }
}
```

## 주요 개념

- [[Agent Pool]], [[Orchestrator]], [[에이전트 상태 관리]], [[대시보드]], [[컨텍스트 파일]]

## 주목할 인사이트

- Ping-Pong 패턴의 발전: Planner가 Reviewer에게 자료를 전달 후 대기, Reviewer는 작업 후 Review 반환 → 이후 Sleep(또는 Terminate). 이것이 상태 기반 에이전트의 기본 패턴.
- 대시보드: `.pool/` 디렉토리의 에이전트들을 테이블 형태로 보여주는 동적 대시보드 — 에이전트 추가/삭제 시 자동 반영, 실행 이력 누적.
- "파이프라인 순서는 고정하지 말고, 어떤 에이전트든 풀에 등록되면 테이블에 나타나게" — 동적 에이전트 관리의 핵심.

## Wiki 업데이트 내역

- 생성: [[source: source-06-agent-pool-orchestrator]]
- 생성: [[Agent Pool]] (wiki/concepts/agent-pool.md)
- 생성: [[Orchestrator]] (wiki/concepts/orchestrator.md)
- 생성: [[에이전트 상태 관리]] (wiki/concepts/agent-state-management.md)
- 업데이트: [[에이전트 아키텍처 패턴]] (wiki/topics/agent-architecture-patterns.md)
