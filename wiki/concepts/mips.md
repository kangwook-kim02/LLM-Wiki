---
type: concept
tags: [MIPS, maximum-inner-product-search, approximate-nearest-neighbor, retrieval]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# MIPS (Maximum Inner Product Search)

## 정의
주어진 질의 벡터에 대해 벡터 집합 중 내적(inner product)이 최대인 항목을 sub-linear 시간에 탐색하는 알고리즘.

## 상세 설명
MIPS는 대규모 벡터 데이터베이스에서 가장 관련성 높은 항목을 효율적으로 찾기 위해 사용된다. 정확한 최대 내적 탐색은 선형 시간이 필요하지만, 근사 알고리즘을 통해 sub-linear 시간에 높은 품질의 결과를 얻을 수 있다.

[[frameworks/faiss]] 라이브러리는 MIPS의 대표적 구현체로, Hierarchical Navigable Small World(HNSW) 알고리즘 등 다양한 근사 탐색 방법을 제공한다.

RAG 논문의 실험에서는 FAISS의 HNSW 근사 알고리즘을 사용하여 위키피디아 21M 청크에 대한 MIPS 인덱스를 구축했다.

수식으로 표현하면:
top-k(p_η(·|x)) = argmax_z p_η(z|x) ≈ argmax_z exp(d(z)^T q(x))

코사인 유사도 기반 Approximate Nearest Neighbor(ANN) 탐색과 유사하지만, 정규화되지 않은 벡터에서의 내적을 최대화한다는 점이 다르다.

## 관련 개념
- [[concepts/dense-passage-retrieval]] — MIPS를 활용한 검색 방법
- [[frameworks/faiss]] — MIPS의 주요 구현 라이브러리
- [[concepts/non-parametric-memory]] — MIPS로 접근하는 외부 메모리

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
