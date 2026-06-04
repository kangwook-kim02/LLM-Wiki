---
type: pattern
title: RunnableParallel
tags: [langchain, runnable, parallel, pattern, lcel]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# RunnableParallel

여러 [[concepts/runnable]] 체인을 병렬로 실행하고 결과를 하나의 dict로 합치는 패턴.

## 기본 사용법

```python
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()

chain1 = (
    PromptTemplate.from_template("{country}의 수도는 어디야?")
    | model
    | StrOutputParser()
)
chain2 = (
    PromptTemplate.from_template("{country}의 면적은 얼마야?")
    | model
    | StrOutputParser()
)

combined = RunnableParallel(capital=chain1, area=chain2)

result = combined.invoke({"country": "대한민국"})
# → {"capital": "서울", "area": "약 100,363 km²"}
```

## RunnablePassthrough와 조합

```python
from langchain_core.runnables import RunnablePassthrough

chain1 = (
    {"country": RunnablePassthrough()}
    | PromptTemplate.from_template("{country}의 수도는?")
    | ChatOpenAI()
)
chain2 = (
    {"country": RunnablePassthrough()}
    | PromptTemplate.from_template("{country}의 면적은?")
    | ChatOpenAI()
)

combined_chain = RunnableParallel(capital=chain1, area=chain2)
combined_chain.invoke("대한민국")
```

## async batch 지원

```python
# 4.5 async batch
my_process = chain.ainvoke({"topic": "NVDA"})
await my_process
```

## 사용 시나리오

- 동일 입력으로 여러 질문에 동시 답변이 필요할 때
- RAG에서 검색과 다른 처리를 병렬로 수행할 때
- 여러 체인의 결과를 합산하는 앙상블 패턴

## 관련 패턴

- [[patterns/runnable-passthrough]] — 입력 통과
- [[patterns/runnable-lambda]] — 사용자 정의 변환
- [[concepts/lcel]] — LCEL 체인 조립
- [[concepts/runnable]] — Runnable 인터페이스
