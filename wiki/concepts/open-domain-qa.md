---
type: concept
tags: [QA, open-domain, question-answering, NLP, benchmark]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Open-Domain QA (오픈 도메인 질의응답)

## 정의
특정 도메인이나 사전 제공된 문서에 제한되지 않고, 임의의 질문에 대해 외부 지식 소스를 검색하여 답변하는 NLP 태스크.

## 상세 설명
Open-Domain QA는 두 가지 접근 방식으로 나뉜다:

**Open-Book 방식 (검색 기반)**:
- 검색 시스템으로 관련 문서를 찾은 뒤 답변을 추출하거나 생성
- DPR + extractive reader 방식이 대표적 (Karpukhin et al., 2020)
- 답변이 반드시 검색 문서에 포함되어야 하는 한계

**Closed-Book 방식 (파라미터 기반)**:
- 외부 검색 없이 모델 파라미터에 저장된 지식만으로 답변 생성
- T5-11B 등이 해당
- 학습 데이터 이후 지식 반영 불가

[[concepts/rag]]는 두 방식을 결합하여 검색 결과가 없어도 parametric knowledge로 답변을 생성할 수 있다. RAG는 NQ, TriviaQA, WebQuestions, CuratedTrec 4개 벤치마크에서 state-of-the-art 달성(2021년 기준).

주요 평가 지표: **Exact Match (EM)** — 예측 답변이 정답과 완전히 일치하는 비율.

## 관련 개념
- [[concepts/rag]] — Open-Domain QA의 state-of-the-art 방법
- [[concepts/knowledge-intensive-nlp]] — Open-Domain QA가 속하는 태스크 유형
- [[concepts/dense-passage-retrieval]] — Open-Domain QA를 위한 검색 방법

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
