---
type: concept
tags: [SDLC, 개발방법론, 소프트웨어공학]
created: 2026-05-27
sources: [1. Vibe coding and Agent coding.pdf, 2. SDLC pipeline in Vibe coding.pdf]
---

# SDLC (Software Development Life Cycle)

## 정의

소프트웨어를 기획부터 폐기까지 체계적으로 개발·운영하기 위한 단계별 프로세스 모델.

## 상세 설명

SDLC는 Planning → Analysis → Design → Implementation → Testing → Deployment → Maintenance 단계로 구성된다. AI 협업 시대에는 각 단계에 에이전트가 참여하는 방식으로 재해석된다.

**Agentic Coding에서의 SDLC 재해석:**

| 단계 | 전통 방식 | AI 협업 방식 |
|------|----------|------------|
| Planning | 회의, 일정 수립 | PRD 작성 → Plan Mode에서 에이전트가 분해 |
| Analysis | 요구사항 문서 | [[PRD]] → SRS → User Story 자동 생성 |
| Design | 아키텍처 설계 | Sequential/Parallel Agent 구조 결정 |
| Implementation | 코드 작성 | EPCC 패턴으로 에이전트가 코딩 |

Vibe Coding은 Implementation만 AI에 맡기지만, Agentic Coding은 SDLC 전 단계에 에이전트가 참여하여 체계적인 프로세스를 보장한다.

## 관련 개념

- [[PRD]] — SDLC Analysis 단계의 핵심 산출물
- [[Agentic Coding]] — SDLC 전 단계를 에이전트가 보장하는 패러다임
- [[Plan Mode]] — SDLC Planning 단계를 코드 실행과 분리하는 메커니즘
- [[Sequential Agent]] — SDLC 단계 간 의존성을 구현하는 구조

## 출처

- [[source: 1. Vibe coding and Agent coding.pdf]] — "코딩 에이전트를 통해 SDLC가 보장되는 개발 프로세스를 수행 가능"
- [[source: 2. SDLC pipeline in Vibe coding.pdf]] — "Planning → Analysis → Design → Implementation 단계를 AI 협업 방식으로 재구성"
