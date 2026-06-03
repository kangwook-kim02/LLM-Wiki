---
type: framework
tags: [FAISS, vector-search, approximate-nearest-neighbor, MIPS, Facebook-AI]
created: 2026-06-03
---

# FAISS (Facebook AI Similarity Search)

## 요약
Facebook AI Research가 개발한 고성능 밀집 벡터 유사도 탐색 라이브러리로, 수십억 개 규모의 벡터에서 효율적인 MIPS와 최근접 이웃 탐색을 지원한다.

## 핵심 컴포넌트
- **Flat 인덱스** — 완전 탐색, 정확하지만 느림
- **IVF (Inverted File Index)** — 클러스터 기반 근사 탐색
- **HNSW (Hierarchical Navigable Small World)** — 그래프 기반 고속 근사 탐색
- **PQ (Product Quantization)** — 벡터 압축으로 메모리 효율화

## 주요 사용 패턴
RAG 논문에서 FAISS HNSW 인덱스 사용:
- 위키피디아 21M 청크를 BERT 임베딩(768차원)으로 인덱싱
- 쿼리 임베딩과 최대 내적 기반 top-K 문서 검색
- sub-linear 시간 복잡도로 대규모 코퍼스 탐색 가능

## 관련 항목
- [[concepts/mips]] — FAISS가 구현하는 탐색 알고리즘
- [[frameworks/dpr]] — FAISS로 문서 인덱스를 구축하는 검색 프레임워크
- [[concepts/non-parametric-memory]] — FAISS 인덱스가 저장하는 외부 메모리

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 3
