---
type: pattern
tags: [RAG-Sequence, marginalization, decoding, retrieval-augmented]
created: 2026-06-03
---

# RAG-Sequence Model

## 문제 상황
검색 결과 문서를 활용하여 텍스트를 생성할 때, 어떤 문서를 참조하여 전체 출력 시퀀스를 생성할지 결정해야 한다. 전체 시퀀스를 일관된 문서로 생성하는 것이 유리한 태스크가 있다.

## 해결 방법
RAG-Sequence는 동일한 검색 문서를 사용하여 전체 출력 시퀀스를 생성한다. 검색 문서를 잠재 변수로 취급하여 top-K 문서에 대해 marginalization한다.

수식:
p_RAG-Sequence(y|x) ≈ sum_{z in top-k} p_eta(z|x) * p_theta(y|x,z)
                     = sum_{z in top-k} p_eta(z|x) * prod_i p_theta(y_i|x,z,y_{1:i-1})

디코딩 방식: 각 문서 z에 대해 별도로 beam search를 수행한 뒤, 후보 집합 Y에 대해 점수를 합산한다.
- **Thorough Decoding**: 모든 후보에 대해 추가 forward pass 수행 (느리지만 정확)
- **Fast Decoding**: beam search 중 생성되지 않은 후보의 확률을 0으로 근사 (빠름)

## 구현 예시
RAG-Sequence는 각 문서별로 독립적인 beam search를 실행하므로, 병렬 처리가 가능하다.

## 트레이드오프
- 장점: 긴 출력 시퀀스에서 문서 일관성 유지, MSMARCO에서 RAG-Token보다 높은 BLEU 점수
- 단점: 여러 번의 forward pass 필요로 RAG-Token보다 느린 디코딩
- [[patterns/rag-token]]에 비해 Jeopardy 질문 생성에서는 성능이 낮음 (여러 문서 정보를 결합하는 태스크에 불리)

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.1
