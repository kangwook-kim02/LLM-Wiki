---
type: pattern
tags: [hybrid-model, parametric, non-parametric, memory, knowledge-retrieval]
created: 2026-06-03
---

# Parametric-Nonparametric Hybrid (파라메트릭-비파라메트릭 하이브리드)

## 문제 상황
순수 parametric 모델은 지식 업데이트가 어렵고 hallucination이 발생하며, 순수 extractive 검색 모델은 검색 결과 내에만 답변이 제한되어 생성 유연성이 떨어진다.

## 해결 방법
Parametric memory(신경망 파라미터에 저장된 지식)와 non-parametric memory(외부 문서 인덱스)를 결합하여 두 방식의 장점을 취한다.

결합 방식:
- **Non-parametric**: 검색기가 관련 문서를 찾아 사실적 근거 제공
- **Parametric**: 생성기가 언어적 유창성과 추론 능력으로 최종 출력 생성

두 메모리는 상호보완적으로 작동한다:
- 검색 문서가 없어도 parametric 지식으로 답변 가능 (NQ에서 11.8%)
- Parametric 지식이 부족한 경우 non-parametric 검색으로 보완
- Jeopardy 생성 예시: non-parametric 메모리가 책 제목을 유도하고, parametric 메모리가 제목을 완성

## 구현 예시
관련 패턴들:
- [[patterns/rag-sequence]] — 시퀀스 단위 hybrid 생성
- [[patterns/rag-token]] — 토큰 단위 hybrid 생성
- [[patterns/end-to-end-retrieval-training]] — hybrid 학습 방법
- [[patterns/index-hot-swapping]] — non-parametric 컴포넌트 갱신

## 트레이드오프
- 장점: Closed-book 방식보다 사실적이고 다양한 텍스트 생성
- 장점: Extractive 방식보다 생성 유연성이 높음
- 장점: 지식 갱신이 상대적으로 용이 (인덱스 교체)
- 단점: 두 컴포넌트 관리 필요, 검색 지연 발생
- 단점: 검색 품질이 전체 성능에 영향

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
