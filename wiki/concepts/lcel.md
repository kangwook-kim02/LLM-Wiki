---
type: concept
title: LCEL (LangChain Expression Language)
aliases: [LangChain Expression Language, LCEL]
tags: [langchain, chain, runnable, dsl]
created: 2026-06-04
source: [[sources/langchain-basics-mandu]]
---

# LCEL (LangChain Expression Language)

LangChain에서 체인(Chain)을 **선언형**으로 쉽게 조립하고 실행할 수 있도록 만든 DSL(Domain-Specific Language).

## 핵심 개념

- **[[concepts/runnable]]**: 모든 구성 요소(Prompt, LLM, Parser 등)는 `Runnable` 인터페이스를 따름
- **Pipe(`|`) composition**: `chain = A | B | C` 처럼 Runnable을 연결
- **Strong typing**: 입력/출력 타입을 명확하게 유지

## 기본 사용법

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("{topic}에 대해 {how} 설명해주세요.")
model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
output_parser = StrOutputParser()

chain = prompt | model | output_parser  # LCEL pipe composition
chain.invoke({"topic": "인공지능 모델의 학습 원리", "how": "매우 어렵게"})
```

## 실행 메서드

| 메서드 | 설명 |
|--------|------|
| `chain.invoke(input)` | 단일 입력 동기 실행 |
| `chain.stream(input)` | 스트리밍([[concepts/streaming]]) 동기 실행 |
| `chain.batch(inputs)` | 여러 입력 일괄 처리 |
| `chain.ainvoke(input)` | 단일 입력 비동기 실행 |
| `chain.astream(input)` | 비동기 스트리밍 실행 |
| `chain.abatch(inputs)` | 비동기 배치 처리 |

### Batch 예시

```python
# max_concurrency로 동시 처리 수 제어
answers = chain.batch(
    [{"topic": "ChatGPT"}, {"topic": "Instagram"}, {"topic": "멀티모달"}],
    config={"max_concurrency": 3},
)
```

### Async Stream 예시

```python
async for token in chain.astream({"topic": "YouTube"}):
    print(token, end="", flush=True)
```

## 관련 개념

- [[concepts/runnable]] — Runnable 인터페이스
- [[patterns/runnable-passthrough]] — 입력을 그대로 전달
- [[patterns/runnable-parallel]] — 병렬 체인 실행
- [[patterns/runnable-lambda]] — 사용자 정의 함수 체인
- [[frameworks/langchain]] — LangChain 프레임워크
