---
type: framework
tags: [BART, seq2seq, transformer, pre-trained, generation, Facebook-AI]
created: 2026-06-03
---

# BART (Bidirectional and Auto-Regressive Transformers)

## 요약
Facebook AI Research가 제안한 사전학습 seq2seq 변환기 모델로, 디노이징 목적함수로 학습되어 텍스트 생성 태스크에서 탁월한 성능을 보인다.

## 핵심 컴포넌트
- **인코더** — 양방향 트랜스포머(BERT 유사), 손상된 입력을 이해
- **디코더** — 자동회귀 트랜스포머(GPT 유사), 좌-우 방향 생성
- **디노이징 사전학습** — 텍스트 마스킹, 문장 치환, 문서 회전 등 다양한 노이즈 함수 사용

## 주요 사용 패턴
BART-large: 12개 레이어 인코더/디코더, 400M 파라미터, 1024 은닉 차원

[[concepts/rag]]에서 BART-large가 generator로 사용된다:


입력 x와 검색된 문서 z를 단순 연결(concatenation)하여 BART에 공급한다.

## 관련 항목
- [[concepts/seq2seq]] — BART가 구현하는 아키텍처 유형
- [[concepts/parametric-memory]] — BART 파라미터가 저장하는 지식
- [[concepts/rag]] — BART를 generator로 사용하는 모델
- [[frameworks/dpr]] — RAG에서 BART와 함께 사용되는 retriever

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021), Section 2.3
