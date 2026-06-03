---
type: concept
tags: [retriever, generator, architecture, hybrid-model, NLP]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Retriever-Generator Architecture (검색기-생성기 아키텍처)

## 정의
검색기(retriever)가 관련 문서를 찾고, 생성기(generator)가 이를 조건으로 텍스트를 생성하는 2-단계 신경망 아키텍처.

## 상세 설명
Retriever-Generator 아키텍처는 [[concepts/non-parametric-memory]](검색 기반)와 [[concepts/parametric-memory]](생성 기반)를 결합한다.

**Retriever 컴포넌트** p_η(z|x):
- 입력 x에 대해 관련 문서 z를 top-K 방식으로 반환
- [[frameworks/dpr]] bi-encoder로 구현: BERT 문서 인코더 + BERT 질의 인코더
- [[concepts/mips]]로 sub-linear 시간에 top-K 탐색

**Generator 컴포넌트** p_θ(y_i|x, z, y_1:i-1):
- 입력 x, 검색 문서 z, 이전 토큰들 y_1:i-1을 조건으로 현재 토큰 y_i 생성
- [[frameworks/bart]]-large (400M 파라미터) seq2seq로 구현
- x와 z를 단순 연결(concatenation)하여 BART에 입력

**End-to-End 학습**:
- 검색 문서를 잠재 변수(latent variable)로 처리
- 입출력 쌍 (x, y)에 대해 negative marginal log-likelihood 최소화
- Adam optimizer, 문서 인코더 고정, 질의 인코더와 BART만 학습

두 변형 모델([[patterns/rag-sequence]], [[patterns/rag-token]])이 문서 marginalization 방식에서 차이를 보인다.

## 관련 개념
- [[concepts/rag]] — retriever-generator 아키텍처의 대표 구현
- [[frameworks/dpr]] — retriever 구현체
- [[frameworks/bart]] — generator 구현체
- [[patterns/rag-sequence]] — 시퀀스 단위 marginalization
- [[patterns/rag-token]] — 토큰 단위 marginalization

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
