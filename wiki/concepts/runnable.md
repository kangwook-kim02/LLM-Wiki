---
type: concept
title: Runnable 인터페이스
aliases: [Runnable, Runnable Interface]
tags: [langchain, lcel, interface, abstraction]
created: 2026-06-04
source: [[sources/langchain-basics-mandu]]
---

# Runnable 인터페이스

LangChain의 모든 구성 요소(Prompt, LLM, OutputParser 등)가 구현하는 공통 인터페이스. [[concepts/lcel]]의 기반이 되는 추상화.

## 핵심 속성

- `invoke(input)` 메서드를 가진 모든 객체가 Runnable
- Pipe(`|`) 연산자로 다른 Runnable과 합성(composition) 가능
- 입력/출력 타입이 명확하게 정의됨

## Runnable 구현체

| 클래스 | 역할 |
|--------|------|
| `PromptTemplate` | 템플릿 기반 프롬프트 생성 |
| `ChatOpenAI` | LLM 추론 |
| `StrOutputParser` | AIMessage → str 변환 |
| `RunnablePassthrough` | 입력 그대로 전달 ([[patterns/runnable-passthrough]]) |
| `RunnableParallel` | 여러 체인 병렬 실행 ([[patterns/runnable-parallel]]) |
| `RunnableLambda` | 사용자 함수 래핑 ([[patterns/runnable-lambda]]) |

## 합성 예시

```python
from langchain_core.runnables import RunnablePassthrough

# dict 입력 없이 raw value를 넘길 때
runnable_chain = {"num": RunnablePassthrough()} | prompt | ChatOpenAI()
runnable_chain.invoke(10)  # {"num": 10}으로 자동 변환
```

## 관련 개념

- [[concepts/lcel]] — LCEL에서 Runnable을 pipe로 연결
- [[patterns/runnable-passthrough]] — 입력 그대로 통과
- [[patterns/runnable-parallel]] — 병렬 실행
- [[patterns/runnable-lambda]] — 함수 래핑
