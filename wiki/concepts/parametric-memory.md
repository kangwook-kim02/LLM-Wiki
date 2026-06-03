---
type: concept
tags: [parametric-memory, language-model, knowledge-storage, NLP]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Parametric Memory (파라미터 기억)

## 정의
신경망 모델의 가중치(파라미터) 안에 암묵적으로 저장된 지식으로, 사전학습 과정에서 데이터로부터 학습된다.

## 상세 설명
대형 언어 모델은 방대한 텍스트 코퍼스를 사전학습하면서 사실적 지식을 파라미터 안에 저장한다. 이를 parametric memory 또는 parametric implicit knowledge base라고 부른다.

Parametric memory의 장점은 입력 시퀀스와 함께 즉시 활용 가능하며, 외부 검색 인프라가 필요 없다는 것이다. 그러나 중요한 한계도 있다:
- 지식 확장이나 수정이 어렵다 (추가 학습 필요)
- 예측 근거를 직접 제시하기 어렵다
- hallucination(환각) 현상이 발생할 수 있다
- 학습 데이터 이후의 세계 변화를 반영하지 못한다

[[concepts/rag]] 모델에서 parametric memory는 BART-large seq2seq 변환기로 구현된다. Generator 파라미터 θ가 이에 해당하며, 검색된 문서와 함께 출력을 생성한다.

T5, GPT-3 등 closed-book 모델들은 오직 parametric memory만 사용한다. RAG는 이를 [[concepts/non-parametric-memory]]와 결합하여 두 방식의 장점을 취한다.

## 관련 개념
- [[concepts/non-parametric-memory]] — 외부 검색 기반 메모리, parametric memory와 대비
- [[concepts/rag]] — parametric과 non-parametric memory를 결합한 모델
- [[concepts/hallucination]] — parametric-only 모델의 주요 문제
- [[frameworks/bart]] — RAG에서 parametric memory로 사용되는 모델

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
