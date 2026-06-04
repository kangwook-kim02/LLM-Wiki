---
type: concept
title: 프롬프트 캐싱 (Prompt Caching / Token Caching)
aliases: [Prompt Caching, Token Caching, Prefix Caching]
tags: [langchain, openai, caching, optimization, cost]
created: 2026-06-04
source: [[sources/langchain-basics-mandu]]
---

# 프롬프트 캐싱 (Prompt Caching / Token Caching)

매 요청마다 바뀌지 않는 "프롬프트의 고정 앞부분(prefix)"을 캐싱하여 토큰 비용과 응답 속도를 개선하는 최적화 기법.

## 동작 조건

- 프롬프트가 **동일한 prefix**를 가져야 함
- **일정 길이 이상**에서만 작동 (OpenAI 기준 약 1,024 토큰 이상)
- 캐싱 판단은 **OpenAI 서버가 자동**으로 처리 (명시적 설정 불필요)

## 사용 예시

```python
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    answer = llm.invoke(
        very_long_prompt.format("프롬프트 캐싱 기능에 대해 2문장으로 설명하세요")
    )
    print(cb)  # 토큰 사용량 확인
    
    # 캐싱된 토큰 수 확인
    cached_tokens = answer.response_metadata["token_usage"]["prompt_tokens_details"]["cached_tokens"]
    print(f"캐싱된 토큰: {cached_tokens}")
```

## 효과

- 캐시 히트 시 동일 prefix 토큰 처리 비용 절감
- 응답 지연(latency) 감소
- 긴 시스템 프롬프트나 문서를 반복 사용하는 RAG 패턴([[concepts/rag]])에 특히 유리

## 관련 개념

- [[frameworks/chatopenai]] — ChatOpenAI에서 캐싱 적용
- [[concepts/rag]] — RAG 패턴에서 고정 컨텍스트 캐싱에 활용
