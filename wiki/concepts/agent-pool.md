---
type: concept
tags: [agent-pool, 에이전트레지스트리, JSON]
created: 2026-05-27
sources: [6. Agent pool and Orchestrator.pdf]
---

# Agent Pool (에이전트 풀)

## 정의

개별 에이전트의 설정값을 JSON으로 관리하는 에이전트 레지스트리. Orchestrator가 동적으로 에이전트를 선택·실행할 수 있도록 한다.

## 상세 설명

Agent Pool은 `.pool/` 디렉토리 아래 에이전트마다 하나의 JSON 파일로 관리된다. Orchestrator는 이 파일들을 읽어 사용 가능한 에이전트 목록을 파악하고 목표에 맞는 에이전트를 선택한다.

**에이전트 JSON 명세 구조:**

```json
{
  "id": "에이전트 파일명과 동일",
  "role": "에이전트의 한 줄 역할 설명",
  "system_prompt": "에이전트에게 전달될 전체 시스템 프롬프트",
  "input": {
    "description": "입력 설명",
    "format": "입력 형식",
    "source": "입력 출처"
  },
  "output": {
    "description": "출력 설명",
    "format": "출력 형식",
    "files": []
  },
  "tools": [],
  "constraints": {
    "max_attempts": 3,
    "timeout_seconds": 180,
    "sandbox": ""
  }
}
```

**Pool 디렉토리 구조 예시:**

```
.pool/
├── planner.json
├── reviewer.json
├── coder.json
└── tester.json
```

**대시보드**: `.pool/` 디렉토리의 에이전트들을 테이블 형태로 보여주는 동적 대시보드 — 에이전트 추가/삭제 시 자동 반영, 실행 이력 누적.

## 관련 개념

- [[Orchestrator]] — Agent Pool을 읽고 에이전트를 선택·실행하는 관리자
- [[Agent Specification]] — 각 JSON 파일에 담긴 에이전트 명세
- [[Harness Engineering]] — Agent Pool은 Preference 구성 요소에 해당

## 출처

- [[source: 6. Agent pool and Orchestrator.pdf]] — "개별 에이전트의 설정값을 XML/TOML/JSON으로 관리하고, 필요한 에이전트를 Pool에 등록하여 Orchestrator가 유동적으로 활용"
