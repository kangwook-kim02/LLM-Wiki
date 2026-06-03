---
type: source
created: 2026-06-03
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**파일:** `raw/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
**인제스트 날짜:** 2026-06-03
**유형:** 논문

**저자:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
**소속:** Facebook AI Research, University College London, New York University
**arXiv:** 2005.11401v4 (2021-04-12)

## 핵심 주장
- 사전학습된 parametric 메모리(seq2seq 모델)와 non-parametric 메모리(위키피디아 밀집 벡터 인덱스)를 결합한 RAG 모델 제안
- RAG-Sequence와 RAG-Token 두 가지 변형 모델을 제안하며, Open-Domain QA 3개 태스크에서 state-of-the-art 달성
- 검색 기반 접근으로 hallucination을 줄이고 더 사실적이고 다양한 텍스트 생성
- non-parametric 메모리는 재학습 없이 인덱스 교체만으로 지식 업데이트 가능

## 주요 개념
- [[concepts/rag]], [[concepts/parametric-memory]], [[concepts/non-parametric-memory]]
- [[concepts/dense-passage-retrieval]], [[concepts/mips]], [[concepts/knowledge-intensive-nlp]]
- [[frameworks/bart]], [[frameworks/dpr]], [[frameworks/faiss]]
- [[patterns/rag-sequence]], [[patterns/rag-token]], [[patterns/index-hot-swapping]]

## 주목할 인사이트
RAG는 검색 결과가 없는 경우에도 정답을 생성할 수 있으며(NQ에서 11.8% 정확도), 이는 parametric 메모리와 non-parametric 메모리의 상호 보완적 역할 덕분이다. 또한 인덱스 교체(Index Hot-Swapping)를 통해 모델 재학습 없이 세계 지식을 갱신할 수 있다는 점이 실용적으로 중요하다.

## Wiki 업데이트 내역
이 소스로 생성된 페이지:
- [[concepts/rag]]
- [[concepts/parametric-memory]]
- [[concepts/non-parametric-memory]]
- [[concepts/dense-passage-retrieval]]
- [[concepts/mips]]
- [[concepts/knowledge-intensive-nlp]]
- [[concepts/seq2seq]]
- [[concepts/open-domain-qa]]
- [[concepts/hallucination]]
- [[concepts/retriever-generator-architecture]]
- [[frameworks/bart]]
- [[frameworks/dpr]]
- [[frameworks/faiss]]
- [[patterns/rag-sequence]]
- [[patterns/rag-token]]
- [[patterns/index-hot-swapping]]
- [[patterns/end-to-end-retrieval-training]]
- [[patterns/parametric-nonparametric-hybrid]]
- [[patterns/thorough-decoding]]
- [[patterns/fast-decoding]]
