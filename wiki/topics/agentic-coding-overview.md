---
type: topic
tags: [agentic-coding, overview, paradigm]
created: 2026-05-24
sources: [1. Vibe coding and Agent coding.pdf, 2. SDLC pipeline in Vibe coding.pdf, 7. Harness and Skills.pdf]
---

# Agentic Coding 개요

## 개요

Agentic Coding은 소프트웨어 엔지니어링의 세 번째 패러다임 전환이다. 하드웨어 종속 시대(1940~) → 추상화/프레임워크 시대(~2024) → 지능형 시스템 시대(2024~)의 흐름에서, AI 에이전트가 SDLC 전 단계에 걸쳐 협력하는 방식으로 발전했다.

[[Vibe Coding]]이 "분위기"로 코드를 생성하는 단순한 LLM 활용이었다면, Agentic Coding은 에이전트가 역할을 분담하고 SDLC를 보장하는 체계적인 개발 프로세스다.

## 핵심 구성 요소

- [[Vibe Coding]] — 선행 패러다임. 소규모에 적합하지만 기술 부채 문제 존재
- [[Agentic Coding]] — SDLC를 보장하는 에이전트 기반 개발 방식
- [[SDLC]] — Planning → Analysis → Design → Implementation 단계
- [[PRD]] — "Spec First, Code Later"의 핵심 산출물
- [[Plan Mode]] — 계획 단계를 코드 실행과 분리하는 메커니즘
- [[Sequential Agent]] — 단계적 의존관계를 가진 에이전트 체인
- [[Parallel Agent]] — 독립 작업을 동시에 처리하는 에이전트 구조
- [[Harness Engineering]] — 에이전트를 안정적으로 운영하는 실행 환경
- [[Hook]] — 에이전트 생애 주기의 결정론적 보정
- [[MCP (Model Context Protocol)]] — 외부 시스템 연동 표준 인터페이스

## 관계도

```
[인간 (Orchestrator)]
        │
        ▼
[Plan Mode] ──→ [PRD/SRS 명세]
        │
        ▼
[Sequential Pipeline]
  Agent1(Planner) → Agent2(Reviewer) → Agent3(Coder) → Agent4(Tester)
        │                                                      │
        ▼                                                      ▼
 [Hand-off 파일]                                        [최종 산출물]
        
[Parallel Research]
  Agent1(WebSearch) ──┐
  Agent2(WebSearch) ──┤──→ [통합 결과]
  Agent3(WebSearch) ──┘

[Harness]
  Contract(TASK.md) + Procedure(Skill) + Journal(log.md) + Preference(AGENTS.md)
  
[Hook] ─ UserPromptSubmit, PostToolUse, Stop ...
[Loop] ─ 반복 자동화 (Claude 전용)
[MCP]  ─ 외부 시스템 연동
```

## 미해결 질문

- Agentic Coding 체계에서 인간이 개입해야 하는 최소 단위는 무엇인가?
- Multi-Agent 시스템에서 에이전트 간 모순되는 결과가 나올 때 어떻게 해결해야 하는가?
- Loop + Hook 조합으로 완전 자동화가 가능한 SDLC 단계는 어디까지인가?

## 출처

- [[source: 1. Vibe coding and Agent coding.pdf]]
- [[source: 2. SDLC pipeline in Vibe coding.pdf]]
- [[source: 7. Harness and Skills.pdf]]
