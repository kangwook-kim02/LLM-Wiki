---
type: pattern
tags: [decoding, fast-decoding, RAG-Sequence, approximation, inference]
created: 2026-06-03
---

# Fast Decoding (빠른 디코딩)

## 문제 상황
RAG-Sequence의 Thorough Decoding은 출력 시퀀스가 길어질수록 추가 forward pass 횟수가 급증하여 추론 속도가 크게 저하된다.

## 해결 방법
후보 y가 문서 z의 beam search에서 생성되지 않은 경우, p_theta(y|x,z) ≈ 0으로 근사하여 추가 forward pass를 생략한다.

절차:
1. 각 문서 z_1, ..., z_K에 대해 beam search 실행
2. 전체 후보 집합 Y 구성
3. 각 y에 대해 y를 생성한 문서들의 확률만 합산 (나머지는 0으로 처리)
4. p(y|x) ≈ sum_{z: y in beam(z)} p_eta(z|x) * p_theta(y|x,z) 계산

## 구현 예시
[[patterns/thorough-decoding]]과 비교:
- Fast Decoding은 추가 forward pass 없이 이미 계산된 확률만 사용
- 출력 길이에 무관하게 일정한 forward pass 횟수 유지

## 트레이드오프
- 장점: 추론 속도 대폭 향상
- 장점: 출력 길이가 길어져도 계산 비용이 증가하지 않음
- 단점: 일부 후보의 확률 추정이 부정확할 수 있음 (과소 추정)
- 단점: 희귀한 정답이 모든 문서의 beam에서 생성되지 않으면 손실 가능

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.5
