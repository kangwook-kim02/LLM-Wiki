---
type: concept
tags: [knowledge-intensive, NLP, QA, open-domain, fact-verification]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Knowledge-Intensive NLP Tasks (지식 집약적 NLP 태스크)

## 정의
외부 지식 소스 없이는 인간도 합리적으로 수행하기 어려운 NLP 태스크 유형.

## 상세 설명
Knowledge-intensive NLP tasks는 모델이 방대한 사실적 지식에 접근해야 제대로 수행할 수 있는 태스크다. 단순 패턴 매칭이나 언어 이해만으로는 부족하며, 특정 도메인 지식이나 세계 지식이 필요하다.

주요 유형:
- **Open-Domain QA**: 검색 엔진 없이 임의의 질문에 답변 (NQ, TriviaQA, WebQuestions, CuratedTrec)
- **Abstractive QA**: 검색 결과를 바탕으로 자유형식 답변 생성 (MSMARCO NLG)
- **Fact Verification**: 주장이 위키피디아에서 지지되는지 반박되는지 분류 (FEVER)
- **Knowledge-Intensive Generation**: 사실적 지식이 필요한 텍스트 생성 (Jeopardy 질문 생성)

[[concepts/rag]] 모델은 parametric memory와 non-parametric memory를 결합하여 이러한 태스크에서 탁월한 성능을 보인다. 순수 parametric 모델(T5, GPT-3 등 closed-book 방식)보다 사실 정확도가 높고, hallucination이 적다.

## 관련 개념
- [[concepts/rag]] — knowledge-intensive 태스크를 위한 핵심 접근법
- [[concepts/open-domain-qa]] — 대표적 knowledge-intensive 태스크
- [[concepts/hallucination]] — knowledge-intensive 태스크에서의 주요 문제
- [[concepts/parametric-memory]] — 지식을 파라미터에 저장하는 방식

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
