---
type: concept
tags: [PRD, 요구사항, spec-driven-development]
created: 2026-05-27
sources: [2. SDLC pipeline in Vibe coding.pdf]
---

# PRD (Product Requirements Document)

## 정의

"Spec First, Code Later" 원칙의 핵심 산출물. 시스템이 무엇을 해야 하는지를 코드 작성 이전에 명확히 정의하는 문서.

## 상세 설명

PRD는 Vibe Coders의 작업 패턴에서 최우선 단계다. PRD 없이 코딩을 시작하면 복잡한 시스템에서 기대하는 결과를 내기 어렵다.

**PRD의 구성 요소:**

- **Goal**: 시스템이 달성해야 하는 목표
- **Stakeholders**: 사용자, 운영자, 비즈니스 이해관계자
- **Functional Requirements**: 시스템이 해야 하는 것
- **Non-Functional Requirements**: 성능, 보안, 확장성
- **Constraints**: 기술적·예산적 제약

**작업 분해 흐름:**

```
PRD → Plan → SRS (Software Requirements Specification)
           → User Story
           → 에이전트별 작업 할당
```

**Quick Sort 시각화 예시**: PRD 요소를 프롬프트에 포함시키자 결과물이 월등히 향상됨. "단순한 도구 하나도 체계적인 Requirements가 없으면 기대하는 결과를 내기 힘들다."

## 관련 개념

- [[SDLC]] — PRD는 SDLC Analysis 단계의 산출물
- [[Agentic Coding]] — "Spec First, Code Later"를 실천하는 패러다임
- [[Plan Mode]] — PRD를 바탕으로 계획을 세우는 모드
- [[Agent Specification]] — 에이전트별 PRD에 해당하는 문서

## 출처

- [[source: 2. SDLC pipeline in Vibe coding.pdf]] — "Vibe Coders의 패턴은 'Spec First, Code Later'. PRD → Plan → SRS → User Story 순서로 작업을 분해한다."
