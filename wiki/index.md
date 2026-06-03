---
type: index
created: 2026-06-03
updated: 2026-06-03
---

# Wiki 페이지 인덱스

전체 Wiki 페이지 카탈로그 (자동 관리). 최종 갱신: 2026-06-03

총 페이지 수: 21 (index, log 제외)

---

## Sources (소스 요약)

| slug | 제목 | 유형 | 날짜 |
|------|------|------|------|
| [[sources/rag-paper-lewis-2020]] | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | 논문 | 2026-06-03 |

---

## Concepts (개념)

| slug | 설명 |
|------|------|
| [[concepts/rag]] | RAG (Retrieval-Augmented Generation) — parametric + non-parametric 메모리 결합 생성 모델 |
| [[concepts/parametric-memory]] | Parametric Memory — 신경망 파라미터에 저장된 암묵적 지식 |
| [[concepts/non-parametric-memory]] | Non-Parametric Memory — 외부 문서 인덱스 기반 검색 가능 지식 |
| [[concepts/dense-passage-retrieval]] | Dense Passage Retrieval (DPR) — BERT 기반 bi-encoder 밀집 검색 |
| [[concepts/mips]] | MIPS (Maximum Inner Product Search) — 벡터 최대 내적 탐색 알고리즘 |
| [[concepts/knowledge-intensive-nlp]] | Knowledge-Intensive NLP Tasks — 외부 지식이 필수인 NLP 태스크 유형 |
| [[concepts/seq2seq]] | Seq2Seq — 입력 시퀀스를 출력 시퀀스로 변환하는 encoder-decoder 아키텍처 |
| [[concepts/open-domain-qa]] | Open-Domain QA — 제한 없는 도메인에서의 질의응답 태스크 |
| [[concepts/hallucination]] | Hallucination — 언어 모델의 사실과 다른 내용 생성 현상 |
| [[concepts/retriever-generator-architecture]] | Retriever-Generator Architecture — 검색기와 생성기를 결합한 2단계 아키텍처 |

---

## Frameworks (프레임워크)

| slug | 설명 |
|------|------|
| [[frameworks/bart]] | BART — Facebook AI의 사전학습 seq2seq 변환기, RAG generator 역할 |
| [[frameworks/dpr]] | DPR — Dense Passage Retrieval 구현 프레임워크, RAG retriever 역할 |
| [[frameworks/faiss]] | FAISS — Facebook AI의 고성능 벡터 유사도 탐색 라이브러리 |

---

## Patterns (패턴)

| slug | 설명 |
|------|------|
| [[patterns/rag-sequence]] | RAG-Sequence — 동일 문서로 전체 시퀀스 생성하는 RAG 변형 |
| [[patterns/rag-token]] | RAG-Token — 토큰마다 다른 문서를 사용하는 RAG 변형 |
| [[patterns/index-hot-swapping]] | Index Hot-Swapping — 재학습 없이 non-parametric 메모리 갱신 |
| [[patterns/end-to-end-retrieval-training]] | End-to-End Retrieval Training — 검색 감독 없이 retriever+generator 동시 학습 |
| [[patterns/parametric-nonparametric-hybrid]] | Parametric-Nonparametric Hybrid — 두 메모리 방식의 결합 아키텍처 패턴 |
| [[patterns/thorough-decoding]] | Thorough Decoding — 모든 (y,z) 쌍 forward pass로 정확한 확률 추정 |
| [[patterns/fast-decoding]] | Fast Decoding — beam search 결과만 사용하는 빠른 RAG-Sequence 디코딩 |
