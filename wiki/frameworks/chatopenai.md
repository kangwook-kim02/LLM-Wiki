---
type: framework
title: ChatOpenAI
tags: [langchain, openai, llm, chatopenai]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# ChatOpenAI

LangChain에서 OpenAI의 ChatGPT 모델을 사용하기 위한 래퍼 클래스. `langchain_openai` 패키지에서 제공한다.

## 기본 사용법

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model_name="gpt-4.1-nano",  # 모델명
    temperature=0.1,             # 창의성 (0.0 ~ 2.0)
)

response = llm.invoke("대한민국의 수도는 어디인가요?")
# response는 AIMessage 객체
```

## 주요 파라미터

| 파라미터 | 타입 | 설명 |
|---------|------|------|
| `model_name` | str | 사용할 OpenAI 모델명 |
| `temperature` | float | 창의성 (0–2) |
| `max_tokens` | int | 생성할 최대 토큰 수 |
| `top_p` | float | nucleus sampling (0–1) |
| `frequency_penalty` | float | 반복 단어 억제 |
| `presence_penalty` | float | 새로운 토픽 유도 |
| `n` | int | 생성 결과 개수 |
| `stop` | list[str] | 생성을 멈출 토큰 |
| `api_key` | str | OpenAI API key |
| `base_url` | str | custom OpenAI endpoint |
| `timeout` | float | 요청 timeout |
| `max_retries` | int | 실패 시 재시도 횟수 |
| `streaming` | bool | 스트림 모드 |

## 호출 방식

```python
# 동기 invoke
response = llm.invoke(question)

# 스트리밍
for token in llm.stream(question):
    print(token.content, end="", flush=True)

# 비동기
await llm.ainvoke(question)
```

- `.bind(logprobs=True)` — 각 토큰의 확률 로그값 반환

## 멀티모달

```python
from langchain_teddynote.models import MultiModal

multimodal_llm = MultiModal(
    ChatOpenAI(model_name="gpt-4.1-nano"),
    system_prompt="...",
    user_prompt="..."
)
answer = multimodal_llm.stream(IMAGE_URL)
```

## 인증

환경변수 `OPENAI_API_KEY` 또는 생성자 `api_key` 인자에 API 키를 제공해야 한다.

## 관련 개념

- [[concepts/lcel]] — LCEL 체인에서 ChatOpenAI 사용
- [[concepts/streaming]] — 스트리밍 응답
- [[concepts/prompt-caching]] — 토큰 캐싱
- [[frameworks/langsmith]] — API 호출 추적
