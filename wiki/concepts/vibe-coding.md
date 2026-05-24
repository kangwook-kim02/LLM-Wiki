---
type: concept
tags: [vibe-coding, llm, development-paradigm]
created: 2026-05-24
sources: [1. Vibe coding and Agent coding.pdf]
---

# Vibe Coding (바이브 코딩)

## 정의
자연어로 목표와 제약을 전달하고 LLM이 코드를 생성하게 하는 개발 방식으로, 개발자의 역할이 코드 작성에서 청사진 설계·프롬프트 엔지니어링·검증으로 전환된다.

## 상세 설명

Vibe Coding은 2024년 4분기에서 2025년 3분기 사이를 풍미한 개발 트렌드다. Andrej Karpathy가 명명한 개념으로, 개발자가 구체적인 코드 구문을 직접 작성하는 대신 자연어로 "분위기(vibe)"를 전달하면 LLM이 그에 맞는 코드를 생성한다.

**기존 코딩 방식과의 차이:**

| | 기존 코딩 | Vibe Coding |
|---|---|---|
| 입력 | 코드 구문/로직 직접 작성 | 자연어 지시 (목표, 제약) |
| 개발자 역할 | 코드 작성 + 테스트 | 청사진 설계 + 프롬프트 엔지니어링 + 검증 |
| 진행 방식 | 컴파일·테스트로 반복 개선 | 개념적 개요와 구조를 전달하며 점진적 개선 |

**Vibe Coding의 인지적 전환:** 저수준 구현 세부 사항의 부담을 덜어주고, 창의적인 문제 해결·사용자 경험 디자인·시스템 아키텍처에 더 집중할 수 있게 한다. 단, 구문 암기보다는 개념적 표현과 전략적 상호작용을 강조한다.

**한계:** 코드 규모가 커질수록 일관성/검증/운영에서 기술 부채가 빠르게 쌓인다. Karpathy 본인도 "AI가 만든 변경을 Accept All로 밀어붙이는 방식"이라고 표현했다.

## 관련 개념

- [[Agentic Coding]] — Vibe Coding의 한계를 보완하는 다음 단계
- [[PRD]] — Vibe Coding의 핵심 산출물 패턴 "Spec First, Code Later"
- [[SDLC]] — Vibe Coding이 단순화했던 개발 생명주기

## 출처

- [[source: 1. Vibe coding and Agent coding.pdf]] — "바이브 코딩이란? 자연어로 목표/제약을 말하고, LLM이 코드를 만들게 하는 방식"
- [[source: 1. Vibe coding and Agent coding.pdf]] — Sapkota et al., "Vibe coding vs. agentic coding", arXiv:2505.19443 (2025)
