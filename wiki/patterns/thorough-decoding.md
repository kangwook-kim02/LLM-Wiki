---
type: pattern
tags: [decoding, thorough-decoding, RAG-Sequence, beam-search, inference]
created: 2026-06-03
---

# Thorough Decoding (철저 디코딩)

## 문제 상황
RAG-Sequence 모델에서 전체 출력 시퀀스 y의 확률을 계산하려면 모든 후보 y에 대해 각 문서 z와의 결합 확률을 계산해야 한다. 일부 후보 y는 특정 문서의 beam search에서 생성되지 않을 수 있어 확률 추정이 불완전할 수 있다.

## 해결 방법
각 문서 z에 대해 beam search를 수행하여 후보 집합 Y를 생성한 뒤, Y의 각 후보에 대해 Y를 생성하지 않은 모든 문서 z에 대해 추가 forward pass를 수행한다.

절차:
1. 각 문서 z_1, ..., z_K에 대해 별도로 beam search 실행
2. 전체 후보 집합 Y 구성 (모든 beam search 결과 합집합)
3. 후보 y가 문서 z의 beam에서 생성되지 않았다면, 추가 forward pass 실행
4. 각 y에 대해 p(y|x) = sum_z p_eta(z|x) * p_theta(y|x,z) 계산

## 구현 예시
Fast Decoding과 비교:
- Thorough Decoding: 모든 (y, z) 쌍에 대해 forward pass 실행, 정확하지만 느림
- [[patterns/fast-decoding]]: y가 z의 beam에 없으면 p_theta(y|x,z) ≈ 0으로 근사, 빠름

## 트레이드오프
- 장점: 후보 확률의 더 정확한 추정
- 단점: 출력 길이가 길어질수록 후보 집합 |Y|가 커져 forward pass 횟수 증가
- 단점: Fast Decoding보다 추론 비용이 높음

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.5
