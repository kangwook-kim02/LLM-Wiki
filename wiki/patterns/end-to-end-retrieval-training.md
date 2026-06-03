---
type: pattern
tags: [end-to-end, training, retrieval, joint-learning, latent-variable]
created: 2026-06-03
---

# End-to-End Retrieval Training (엔드투엔드 검색 학습)

## 문제 상황
검색기와 생성기를 별도로 학습하면 두 컴포넌트 간의 최적화 목표가 맞지 않아 전체 시스템 성능이 저하될 수 있다. 어떤 문서를 검색해야 하는지에 대한 직접적인 감독(supervision) 신호가 없는 경우가 많다.

## 해결 방법
검색 문서를 잠재 변수(latent variable)로 취급하여, 입출력 쌍 (x, y)만으로 검색기와 생성기를 동시에 end-to-end 학습한다.

학습 목표:
- 각 입출력 쌍 (x_j, y_j)에 대해 negative marginal log-likelihood 최소화
- sum_j -log p(y_j|x_j)를 Adam optimizer로 최적화

RAG의 구체적 구현:
- 문서 인코더(BERT_d): 고정 (재학습 비용이 너무 크기 때문)
- 질의 인코더(BERT_q): BART generator와 함께 학습
- 직접적인 검색 감독(retrieval supervision) 불필요

## 구현 예시
학습 시 각 미니배치에서:
1. 질의 인코더로 쿼리 임베딩 생성
2. FAISS 인덱스로 top-K 문서 검색
3. 각 문서에 대해 BART로 생성 확률 계산
4. top-K에 대해 marginalize하여 최종 확률 계산
5. negative log-likelihood 역전파

## 트레이드오프
- 장점: 검색 감독 신호 없이도 학습 가능, 더 다양한 태스크에 적용 가능
- 장점: RAG 논문 실험에서 학습된 검색기가 모든 태스크에서 고정 검색기보다 우수
- 단점: 문서 인코더 고정으로 인한 학습 근사 오차 존재
- 단점: REALM 방식의 주기적 인덱스 업데이트보다 메모리 효율이 낮을 수 있음

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.4
