---
type: concept
tags: [hallucination, factuality, reliability, language-model, generation]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Hallucination (환각)

## 정의
언어 모델이 사실과 다르거나 근거 없는 내용을 그럴듯하게 생성하는 현상.

## 상세 설명
Hallucination은 대형 언어 모델의 핵심적인 한계 중 하나다. 모델은 실제 존재하지 않는 인물, 사건, 인용문 등을 마치 실제인 것처럼 생성할 수 있다. 이는 [[concepts/parametric-memory]]만 사용하는 closed-book 모델에서 특히 두드러진다.

Hallucination의 주요 원인:
- 학습 데이터에 포함되지 않은 지식에 대해 추측으로 응답
- 빈번하지 않은 사실에 대한 불확실성
- 언어적 유창성과 사실 정확성 간의 trade-off

[[concepts/rag]] 모델은 실제 문서에서 검색한 내용을 조건으로 텍스트를 생성하기 때문에 hallucination을 줄이는 데 효과적이다. RAG 논문의 인간 평가에서 RAG-Token이 BART보다 42.7% 더 사실적이라고 평가받았으며, BART가 더 사실적인 경우는 7.1%에 불과했다.

또한 RAG의 non-parametric memory는 검색된 문서를 명시적으로 접근할 수 있어 예측 근거(provenance)를 제공할 수 있다.

## 관련 개념
- [[concepts/parametric-memory]] — hallucination이 주로 발생하는 컴포넌트
- [[concepts/rag]] — hallucination을 완화하는 접근법
- [[concepts/knowledge-intensive-nlp]] — hallucination이 특히 문제가 되는 태스크

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
