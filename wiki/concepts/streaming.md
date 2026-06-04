---
type: concept
title: 스트리밍 (Streaming)
tags: [streaming, langchain, async, realtime]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# 스트리밍 (Streaming)

LLM 응답을 생성 완료까지 기다리지 않고 토큰 단위로 실시간 출력하는 방식. 긴 응답에서 사용자 경험(UX)을 크게 개선한다.

## 동기 스트리밍

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4.1-nano")

answer = llm.stream("대한민국의 아름다운 관광지 10곳과 주소를 알려주세요!")

for token in answer:
    print(token.content, end="", flush=True)
```

`langchain_teddynote`의 `stream_response` 유틸로 간소화:

```python
from langchain_teddynote.messages import stream_response

answer = llm.stream(question)
answer_text = stream_response(answer, return_output=True)
```

## 비동기 스트리밍

```python
# astream: 비동기 for 루프
async for token in chain.astream({"topic": "YouTube"}):
    print(token, end="", flush=True)
```

## [[concepts/lcel]] 체인에서의 스트리밍

LCEL 체인(`prompt | model | parser`)은 `.stream()`, `.astream()` 모두 지원한다.

## 관련 개념

- [[frameworks/chatopenai]] — 스트리밍을 지원하는 모델 래퍼
- [[concepts/lcel]] — 스트리밍 가능한 체인 조립
- [[concepts/runnable]] — Runnable 인터페이스의 스트리밍 메서드
