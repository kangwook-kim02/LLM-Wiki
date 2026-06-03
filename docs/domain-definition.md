# 지식 도메인 정의 문서

**프로젝트**: LLM Wiki — RAG & Agent Frameworks
**작성일**: 2026-06-03
**버전**: 1.0

---

## 1. 도메인 선정 이유

### 왜 이 도메인인가?

RAG(Retrieval-Augmented Generation), LangChain, LangGraph는 현재 LLM 기반 애플리케이션 개발의 핵심 생태계입니다. 이 기술들은:

- 빠르게 진화하여 공식 문서만으로는 전체 맥락을 파악하기 어렵다
- 개념 간 의존 관계가 복잡하다 (예: LangGraph는 LangChain 위에 구축)
- 실무 패턴과 이론적 개념 사이의 간극이 크다

이 세 가지 특성이 LLM Wiki 패턴이 가장 효과적으로 작동하는 조건입니다. Wiki가 점진적으로 성장하면서 개념 간 연결이 축적될수록 학습 가치가 높아집니다.

### CSE-3308 강의 내용과의 관계

본 위키는 강의에서 *다루는 방법론*을 적용하되, 강의 *내용 자체*를 위키화하지 않습니다. 강의 내용(Agentic Coding, MCP 등)은 1번 과제에서 이미 구현했으며, 이번 과제는 별도의 기술 도메인에 그 방법론을 적용합니다.

---

## 2. 도메인 범위

### 2.1 핵심 도메인

```
LLM Application Frameworks & Agent Systems
│
├── RAG (Retrieval-Augmented Generation)
│   ├── 기본 RAG 파이프라인
│   ├── Advanced RAG 기법 (HyDE, RAPTOR, Self-RAG 등)
│   ├── 평가 방법론 (RAGAS 등)
│   └── 구성 요소 (Embedding, Vector Store, Retriever)
│
├── LangChain
│   ├── LCEL (LangChain Expression Language)
│   ├── Chains
│   ├── Agents & Tools
│   ├── Memory
│   └── Callbacks & Tracing
│
└── LangGraph
    ├── 그래프 기본 개념 (Node, Edge, State)
    ├── 멀티에이전트 패턴
    ├── Human-in-the-loop
    ├── Persistence & Checkpointing
    └── LangGraph Platform
```

### 2.2 포함 범위

| 카테고리 | 포함 항목 |
|----------|-----------|
| **개념** (concepts/) | RAG, Embedding, Vector Store, Retriever, Chain, Agent, Tool, State, Graph, Node, Edge, Memory, Checkpointing |
| **프레임워크** (frameworks/) | LangChain, LangGraph, LangSmith, FAISS, Chroma, Pinecone |
| **패턴** (patterns/) | Basic RAG, Agentic RAG, ReAct, Plan-and-Execute, Multi-Agent Supervisor, Hierarchical Agents |
| **소스** (sources/) | 공식 문서, 튜토리얼, 논문 요약 |

### 2.3 제외 범위

- LLM 모델 자체 (GPT-4, Claude 등) — 프레임워크 도구로만 언급
- 파인튜닝, 사전훈련 방법론
- LangChain 이외의 프레임워크 (LlamaIndex, Haystack 등) — 비교 언급은 허용

---

## 3. 예상 위키 페이지 목록

### 개념 페이지 (concepts/)

- `rag` — Retrieval-Augmented Generation 개요
- `embedding` — 텍스트 임베딩 개념
- `vector-store` — 벡터 저장소 개념
- `retriever` — 검색기 유형과 동작
- `chain` — LangChain의 Chain 개념
- `agent` — LLM 에이전트 개념
- `tool` — 에이전트 도구 개념
- `memory` — 대화 메모리 유형
- `state` — LangGraph State 개념
- `graph` — LangGraph Graph 구조
- `node` — 그래프 노드 개념
- `edge` — 그래프 엣지 (조건부 분기)
- `checkpointing` — 상태 영속성

### 프레임워크 페이지 (frameworks/)

- `langchain` — LangChain 프레임워크 개요
- `langgraph` — LangGraph 프레임워크 개요
- `langsmith` — LLM 관찰가능성 도구
- `faiss` — Facebook AI Similarity Search
- `chroma` — Chroma 벡터 DB

### 패턴 페이지 (patterns/)

- `basic-rag` — 기본 RAG 파이프라인
- `advanced-rag` — 고급 RAG 기법
- `react` — ReAct 에이전트 패턴
- `plan-and-execute` — 계획-실행 패턴
- `multi-agent-supervisor` — 슈퍼바이저 멀티에이전트
- `human-in-the-loop` — 인간 개입 패턴

---

## 4. 위키 성장 전략

### 인제스트 우선순위

1. **1순위**: LangChain, LangGraph 공식 문서 핵심 섹션
2. **2순위**: RAG 관련 논문 (Lewis et al. 2020 등)
3. **3순위**: 실무 튜토리얼 및 블로그 포스트

### 페이지 성장 기대값

| 단계 | 소스 수 | 예상 페이지 수 |
|------|---------|---------------|
| MVP | 3~5개 | 20~30개 |
| 완성 | 10개+ | 50개+ |

---

## 5. 도메인 특수 컨벤션

- 코드 예시는 Python으로 작성 (LangChain/LangGraph 생태계 기준)
- API 변경이 잦으므로 **버전 명시** 필수 (예: `langchain>=0.2`)
- 개념 설명 시 **언제 사용하는가**를 반드시 포함
- 프레임워크 간 비교는 객관적 트레이드오프 형식으로 작성
