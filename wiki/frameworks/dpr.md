---
type: framework
tags: [DPR, dense-retrieval, BERT, bi-encoder, open-domain-qa, Facebook-AI]
created: 2026-06-03
---

# DPR (Dense Passage Retrieval)

## 요약
Facebook AI Research가 제안한 Open-Domain QA를 위한 고밀도 문서 검색 프레임워크로, BERT 기반 bi-encoder 아키텍처를 사용한다.

## 핵심 컴포넌트
- **문서 인코더** (BERT_d) — 각 문서 청크를 고정 밀집 벡터로 인코딩, 사전에 오프라인 처리
- **질의 인코더** (BERT_q) — 쿼리를 실시간으로 밀집 벡터로 인코딩
- **문서 인덱스** — [[frameworks/faiss]] 기반 MIPS 인덱스, [[concepts/non-parametric-memory]] 역할

## 주요 사용 패턴
검색 점수 계산:


[[concepts/rag]] 모델에서의 DPR 사용:
- 초기화: TriviaQA + Natural Questions 검색 감독으로 사전학습된 DPR 모델 사용
- 파인튜닝: 문서 인코더(BERT_d)는 고정, 질의 인코더(BERT_q)만 BART와 함께 학습
- 검색: FAISS HNSW 근사 탐색으로 top-K 문서 반환

## 관련 항목
- [[concepts/dense-passage-retrieval]] — DPR이 구현하는 검색 방법론
- [[concepts/mips]] — DPR이 사용하는 탐색 알고리즘
- [[frameworks/faiss]] — DPR 인덱싱에 사용되는 라이브러리
- [[frameworks/bart]] — RAG에서 DPR과 함께 사용되는 generator

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.2
