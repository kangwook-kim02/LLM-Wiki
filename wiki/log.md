---
type: log
---

## 2026-06-04 — LangChain 기초 인제스트 완료 (누락 페이지 보완)

- **소스:** `raw/LangChain 기초.pdf`
- **작업:** 이전 세션에서 미생성된 7개 페이지 생성 완료
- **소스:** [[sources/langchain-basics-mandu]]

### 신규 생성 페이지 (7개)

**Frameworks (3개)**
- `frameworks/langchain` — LangChain 프레임워크
- `frameworks/chatopenai` — ChatOpenAI 래퍼 클래스
- `frameworks/langsmith` — LangSmith 추적/모니터링 플랫폼

**Concepts (1개)**
- `concepts/streaming` — 스트리밍 응답

**Patterns (3개)**
- `patterns/runnable-passthrough` — RunnablePassthrough 패턴
- `patterns/runnable-parallel` — RunnableParallel 패턴
- `patterns/runnable-lambda` — RunnableLambda 패턴

### 현재 Wiki 총 페이지 수: 33개 (index, log 제외)

---

## 2026-06-04 — LangChain 기초 인제스트

- **소스:** `raw/LangChain 기초.pdf` (mandu.log, 2025-11-04)
- **생성:** 12개 페이지
- **업데이트:** `index` (21 → 33페이지)
- **소스:** [[sources/langchain-basics-mandu]]

### 생성된 페이지

**Sources (1개)**
- `sources/langchain-basics-mandu` — LangChain 기초 블로그 포스트 소스 요약

**Concepts (5개)**
- `concepts/lcel` — LCEL (LangChain Expression Language)
- `concepts/runnable` — Runnable 인터페이스
- `concepts/prompt-template` — PromptTemplate
- `concepts/prompt-caching` — 프롬프트 캐싱 (Token Caching / Prefix Caching)
- `concepts/streaming` — 스트리밍 응답

**Frameworks (3개)**
- `frameworks/langchain` — LangChain 프레임워크
- `frameworks/langsmith` — LangSmith 추적/모니터링 플랫폼
- `frameworks/chatopenai` — ChatOpenAI 래퍼 클래스

**Patterns (3개)**
- `patterns/runnable-passthrough` — RunnablePassthrough 패턴
- `patterns/runnable-parallel` — RunnableParallel 패턴
- `patterns/runnable-lambda` — RunnableLambda 패턴

---

## 2026-06-03 -- [M3] query 스킬 동작 검증 (이슈 #5)

**작업자:** impl-agent
**작업 유형:** query 스킬 동작 검증 (wiki_search -> wiki_read 순서 테스트)

### 테스트 질의 결과

**Q1: RAG란 무엇인가?**
- 사용 도구: wiki_search(RAG) -> wiki_read(concepts/rag), wiki_read(concepts/retriever-generator-architecture)
- 답변 출처: [[concepts/rag]], [[concepts/retriever-generator-architecture]], [[concepts/parametric-memory]], [[concepts/non-parametric-memory]]
- 답변 요약: RAG는 사전학습된 parametric 메모리(BART seq2seq)와 non-parametric 메모리(DPR 기반 문서 인덱스)를 결합하여 언어 생성을 수행하는 파인튜닝 방법론이다. 입력 x가 주어지면 retriever가 top-K 문서 z를 검색하고, generator가 x와 z를 조건으로 출력 y를 생성한다. [[patterns/rag-sequence]]와 [[patterns/rag-token]] 두 가지 변형이 있다.
- 결과: PASS (Wiki 기반 답변, 출처 slug 포함)

**Q2: RAG-Sequence와 RAG-Token의 차이는?**
- 사용 도구: wiki_search(RAG-Sequence) -> wiki_search(RAG-Token) -> wiki_read(patterns/rag-sequence), wiki_read(patterns/rag-token)
- 답변 출처: [[patterns/rag-sequence]], [[patterns/rag-token]], [[sources/rag-paper-lewis-2020]]
- 답변 요약: RAG-Sequence는 전체 출력 시퀀스에 동일한 문서를 사용하여 marginalization하며(수식: sum_{z} p(z|x) * p(y|x,z)), 문서 일관성이 높아 Open-Domain QA에 유리하지만 디코딩이 느리다. RAG-Token은 각 출력 토큰마다 다른 문서를 참조할 수 있어(수식: prod_i sum_{z} p(z|x) * p(y_i|x,z,...)) 여러 문서 정보 결합이 필요한 Jeopardy 생성 태스크에 우수하며 표준 beam decoder로 효율적으로 디코딩 가능하다.
- 결과: PASS (두 패턴 비교 답변, 출처 slug 포함)

**Q3: DPR이 RAG 시스템에서 어떤 역할을 하는가?**
- 사용 도구: wiki_search(DPR) -> wiki_read(concepts/dense-passage-retrieval), wiki_read(frameworks/dpr)
- 답변 출처: [[concepts/dense-passage-retrieval]], [[frameworks/dpr]], [[frameworks/faiss]], [[concepts/mips]], [[concepts/rag]]
- 답변 요약: DPR은 RAG의 retriever 컴포넌트로서, BERT 기반 bi-encoder(질의 인코더 BERT_q + 문서 인코더 BERT_d)를 사용해 입력 질의와 문서를 밀집 벡터로 인코딩하고 내적 유사도([[concepts/mips]])로 top-K 관련 문서를 검색한다. RAG 파인튜닝 시 문서 인코더는 고정하고 질의 인코더만 BART generator와 함께 end-to-end로 학습되며, [[frameworks/faiss]] HNSW 인덱스를 통해 sub-linear 시간에 검색이 수행된다.
- 결과: PASS (DPR-RAG 관계 답변, 출처 slug 포함)

### 검증 결과 요약
- wiki_search -> wiki_read 순서로 MCP 도구가 정상 동작함을 확인
- 3개 질의 모두 Wiki 기반 답변 생성 및 [[slug]] 출처 포함
- 완료 기준 3/3 충족


# Wiki 작업 이력

append-only. 최신 항목이 위에 위치한다.

---

## 2026-06-03 — [M3] ingest 스킬 엔드투엔드 검증 (이슈 #4)

**작업자:** impl-agent
**소스:** `raw/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
**작업 유형:** ingest (PDF → Wiki 페이지 생성)

### 생성된 페이지 목록 (21개)

**Sources (1개)**
- `sources/rag-paper-lewis-2020` — RAG 논문 (Lewis et al., 2021) 소스 요약

**Concepts (10개)**
- `concepts/rag` — RAG (Retrieval-Augmented Generation) 개념
- `concepts/parametric-memory` — Parametric Memory 개념
- `concepts/non-parametric-memory` — Non-Parametric Memory 개념
- `concepts/dense-passage-retrieval` — Dense Passage Retrieval (DPR) 개념
- `concepts/mips` — MIPS (Maximum Inner Product Search) 개념
- `concepts/knowledge-intensive-nlp` — Knowledge-Intensive NLP Tasks 개념
- `concepts/seq2seq` — Seq2Seq 아키텍처 개념
- `concepts/open-domain-qa` — Open-Domain QA 개념
- `concepts/hallucination` — Hallucination 개념
- `concepts/retriever-generator-architecture` — Retriever-Generator 아키텍처 개념

**Frameworks (3개)**
- `frameworks/bart` — BART 프레임워크
- `frameworks/dpr` — DPR 프레임워크
- `frameworks/faiss` — FAISS 라이브러리

**Patterns (7개)**
- `patterns/rag-sequence` — RAG-Sequence 패턴
- `patterns/rag-token` — RAG-Token 패턴
- `patterns/index-hot-swapping` — Index Hot-Swapping 패턴
- `patterns/end-to-end-retrieval-training` — End-to-End 검색 학습 패턴
- `patterns/parametric-nonparametric-hybrid` — Parametric-Nonparametric Hybrid 패턴
- `patterns/thorough-decoding` — Thorough Decoding 패턴
- `patterns/fast-decoding` — Fast Decoding 패턴

### 코드 변경 사항
- `requirements.txt`: `pypdf>=3.0.0` 추가
- `mcp_server/server.py`: `raw_read` 도구에 PDF 텍스트 추출 분기 추가 (pypdf 사용)

### 완료 기준 충족 여부
- [x] Wiki 페이지 21개 생성 (요구사항: 20개 이상)
- [x] 모든 페이지에 YAML frontmatter 포함
- [x] 내부 링크 `[[slug]]` 형식 사용
- [x] `wiki/index.md` 갱신
- [x] `wiki/log.md` 갱신 (현재 항목)
