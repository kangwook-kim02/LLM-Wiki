---
type: concept
tags: [DPR, dense-retrieval, bi-encoder, BERT, retrieval]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Dense Passage Retrieval (DPR)

## 정의
BERT 기반 bi-encoder 아키텍처를 사용하여 질의와 문서를 각각 밀집 벡터로 인코딩하고 내적 유사도로 관련 문서를 검색하는 방법.

## 상세 설명
Dense Passage Retrieval(DPR)은 Karpukhin et al.(2020)이 제안한 검색 방법으로, 기존의 희소 벡터 기반(BM25, TF-IDF) 검색과 달리 밀집 표현(dense representation)을 사용한다.

DPR의 bi-encoder 구조:
- **문서 인코더** d(z) = BERT_d(z): 각 문서를 고정 벡터로 인코딩하여 사전에 인덱싱
- **질의 인코더** q(x) = BERT_q(x): 쿼리를 실시간으로 인코딩

검색 점수는 두 인코더 출력의 내적으로 계산된다:
p_η(z|x) ∝ exp(d(z)^T q(x))

[[concepts/mips]](Maximum Inner Product Search)를 통해 sub-linear 시간에 top-K 문서를 검색한다. [[frameworks/faiss]]가 이를 위해 사용된다.

RAG에서는 DPR 사전학습 모델을 검색기 초기값으로 사용하며, 파인튜닝 시 문서 인코더(BERT_d)는 고정하고 질의 인코더(BERT_q)만 BART generator와 함께 end-to-end로 학습한다.

DPR은 TriviaQA와 Natural Questions에서의 검색 감독으로 사전학습되어 있다.

## 관련 개념
- [[concepts/mips]] — DPR 검색에서 사용하는 유사도 탐색 알고리즘
- [[concepts/non-parametric-memory]] — DPR 인덱스가 구현하는 외부 메모리
- [[frameworks/dpr]] — DPR 구현 프레임워크
- [[frameworks/faiss]] — DPR 인덱싱에 사용되는 라이브러리
- [[concepts/rag]] — DPR을 검색기로 사용하는 모델

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
