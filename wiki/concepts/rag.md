---
type: concept
tags: [RAG, retrieval, generation, NLP, language-model]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# RAG (Retrieval-Augmented Generation)

## 정의
사전학습된 parametric 메모리(seq2seq 생성 모델)와 non-parametric 메모리(검색 가능한 문서 인덱스)를 결합하여 언어 생성을 수행하는 일반목적 파인튜닝 방법론.

## 상세 설명
RAG는 대형 언어 모델이 파라미터 내에 저장된 지식만으로는 한계가 있다는 문제를 해결하기 위해 제안되었다. 모델은 두 가지 메모리 컴포넌트를 결합한다: (1) 파라미터 안에 지식을 저장하는 seq2seq 변환기(BART), (2) 위키피디아 등 외부 문서를 밀집 벡터 인덱스로 저장하는 non-parametric 메모리.

입력 시퀀스 x가 주어지면 검색기(retriever)가 관련 문서 z를 top-K 방식으로 검색하고, 생성기(generator)가 x와 z를 조건으로 출력 y를 생성한다. 검색 문서를 잠재 변수(latent variable)로 취급하여 end-to-end로 학습한다.

RAG는 [[patterns/rag-sequence]]와 [[patterns/rag-token]] 두 가지 변형이 있다. RAG-Sequence는 전체 출력 시퀀스에 동일한 문서를 사용하고, RAG-Token은 각 토큰마다 다른 문서를 사용할 수 있다.

Open-Domain QA(NQ, TQA, WQ, CT), Abstractive QA(MSMARCO), Jeopardy 질문 생성, FEVER 사실 검증 등 다양한 knowledge-intensive NLP 태스크에서 state-of-the-art 성능을 달성하였다.

## 관련 개념
- [[concepts/parametric-memory]] — RAG의 생성기 컴포넌트
- [[concepts/non-parametric-memory]] — RAG의 검색기 컴포넌트
- [[concepts/dense-passage-retrieval]] — RAG 검색기 구현체
- [[concepts/knowledge-intensive-nlp]] — RAG가 해결하는 태스크 유형
- [[concepts/hallucination]] — RAG로 완화 가능한 문제

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Facebook AI Research
