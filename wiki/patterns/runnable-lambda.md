---
type: pattern
title: RunnableLambda
tags: [langchain, runnable, lambda, pattern, lcel]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# RunnableLambda

일반 Python 함수를 [[concepts/runnable]] 인터페이스로 래핑하는 패턴. 체인 안에 사용자 정의 변환 로직을 삽입할 때 사용한다.

## 기본 사용법

```python
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from datetime import datetime

def get_today(_):  # 파라미터를 반드시 하나 받아야 함
    return datetime.today().strftime("%b-%d")

prompt = PromptTemplate.from_template(
    "{today}가 생일인 유명인 {n}명을 나열하세요. 생년월일을 표기해 주세요."
)
llm = ChatOpenAI(temperature=0, model_name="gpt-4.1-mini")

chain = (
    {"today": RunnableLambda(get_today), "n": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

chain.invoke(5)
```

## itemgetter와 조합

복잡한 입력 변환이 필요할 때 `operator.itemgetter`와 조합한다:

```python
from operator import itemgetter
from langchain_core.runnables import RunnableLambda

def length_function(text):
    return len(text)

chain = (
    {
        "a": itemgetter("word1") | RunnableLambda(length_function),
        "b": {"text1": itemgetter("word1"), "text2": itemgetter("word2")}
             | RunnableLambda(lambda d: len(d["text1"]) * len(d["text2"])),
    }
    | ChatPromptTemplate.from_template("{a} + {b}는 무엇인가요?")
    | ChatOpenAI()
)
```

## 주의 사항

- 함수는 반드시 파라미터를 **하나** 받아야 한다 (체인 입력값이 전달됨)
- 입력값을 사용하지 않더라도 `_` 로 받는 파라미터가 필요하다

## 사용 시나리오

- 현재 날짜·시간 주입 등 동적 값 삽입
- 외부 API 호출 결과를 체인에 통합
- 복잡한 전처리/후처리 로직을 체인에 삽입

## 관련 패턴

- [[patterns/runnable-passthrough]] — 입력 통과
- [[patterns/runnable-parallel]] — 병렬 실행
- [[concepts/lcel]] — LCEL 체인 조립
- [[concepts/runnable]] — Runnable 인터페이스
