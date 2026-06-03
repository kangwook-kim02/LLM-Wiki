---
type: pattern
tags: [RAG-Token, marginalization, decoding, token-level, retrieval-augmented]
created: 2026-06-03
---

# RAG-Token Model

## 문제 상황
단일 문서보다 여러 문서에서 정보를 결합해야 하는 생성 태스크에서, 각 토큰마다 다른 문서를 참조할 수 있는 유연성이 필요하다.

## 해결 방법
RAG-Token은 각 출력 토큰을 생성할 때마다 다른 검색 문서를 사용할 수 있다. 각 토큰에서 top-K 문서에 대해 marginalization한다.

수식:
p_RAG-Token(y|x) ≈ prod_i sum_{z in top-k} p_eta(z|x) * p_theta(y_i|x,z,y_{1:i-1})

이는 표준 자동회귀 seq2seq와 동일한 전환 확률 구조를 가지므로, 표준 beam decoder로 디코딩할 수 있다.

## 구현 예시
각 토큰 생성 시 top-K 문서에 대한 확률 분포를 계산하여 가중 합산(marginalization)한다. 표준 beam search로 디코딩 가능하여 RAG-Sequence보다 디코딩이 효율적이다.

## 트레이드오프
- 장점: 여러 문서의 정보를 토큰 단위로 결합 가능, Jeopardy 질문 생성에서 RAG-Sequence보다 우수
- 장점: 표준 beam decoder로 효율적 디코딩
- 단점: 전체 시퀀스의 문서 일관성이 낮을 수 있음
- [[patterns/rag-sequence]]에 비해 Open-Domain QA 일부 태스크에서 성능 소폭 낮음

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.1
