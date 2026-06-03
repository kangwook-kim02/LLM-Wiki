---
type: concept
tags: [seq2seq, encoder-decoder, transformer, generation, NLP]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Seq2Seq (Sequence-to-Sequence)

## 정의
입력 시퀀스를 받아 출력 시퀀스를 생성하는 encoder-decoder 신경망 아키텍처.

## 상세 설명
Seq2seq 모델은 입력 시퀀스 x를 인코더로 처리한 후, 디코더가 조건부 확률 p(y|x)를 최대화하는 방식으로 출력 시퀀스 y를 생성한다. 기계 번역, 요약, 질의응답 등 다양한 생성 태스크에 사용된다.

트랜스포머 기반 사전학습 seq2seq 모델의 대표 예시:
- **BART**: 디노이징 목적함수로 학습된 seq2seq 변환기. [[frameworks/bart]] 참조
- **T5** (Text-to-Text Transfer Transformer): 모든 NLP 태스크를 텍스트 생성으로 변환
- **mT5**: 다국어 T5

[[concepts/rag]] 모델에서 seq2seq는 generator 역할을 담당한다. BART-large(400M 파라미터)가 사용되며, 검색된 문서 z와 입력 x를 연결(concatenate)하여 조건으로 삼아 출력 y를 생성한다.

## 관련 개념
- [[frameworks/bart]] — RAG에서 사용되는 seq2seq 모델
- [[concepts/parametric-memory]] — seq2seq 모델이 구현하는 parametric memory
- [[concepts/rag]] — seq2seq를 generator로 사용하는 모델

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
