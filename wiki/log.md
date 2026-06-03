---
type: log
---

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
