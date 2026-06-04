---
type: pattern
title: RunnablePassthrough
tags: [langchain, runnable, pattern, lcel]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# RunnablePassthrough

입력값을 그대로 통과시키는 [[concepts/runnable]]. dict가 아닌 단일 값을 체인에 넘길 때 유용하다.

## 기본 사용법

```python
from langchain_core.runnables import RunnablePassthrough

# 단일 값을 dict 포맷으로 체인에 주입
runnable_chain = {"num": RunnablePassthrough()} | prompt | ChatOpenAI()

# dict 대신 단일 값 10을 invoke
runnable_chain.invoke(10)
# → {"num": 10} 으로 변환되어 프롬프트에 전달됨
```

## assign: 새 키 추가

```python
# 기존 입력 dict에 새 키를 추가
result = (
    RunnablePassthrough.assign(new_num=lambda x: x["num"] * 3)
).invoke({"num": 1})
# → {"num": 1, "new_num": 3}
```

## 사용 시나리오

- RAG 체인에서 사용자 질의(query)를 retriever와 generator 모두에 전달할 때
- 체인 중간에 원본 입력을 보존하면서 새 키를 추가할 때
- 입력 포맷을 고정하여 체인 재사용성을 높일 때

## 관련 패턴

- [[patterns/runnable-parallel]] — 병렬 실행 시 RunnablePassthrough와 함께 사용
- [[patterns/runnable-lambda]] — 사용자 정의 변환
- [[concepts/lcel]] — LCEL 체인 조립
- [[concepts/runnable]] — Runnable 인터페이스
