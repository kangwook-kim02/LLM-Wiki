---
type: source
title: "LangChain 기초: 프롬프트 + 모델 + 출력 파서"
source_type: 블로그 포스트
author: mandu (mandu.log)
url: https://velog.io/@mandu/Langchain-기본적인-사용법-프롬프트-모델-출력-파서
published: 2025-11-04
ingested: 2026-06-04
---

# LangChain 기초: 프롬프트 + 모델 + 출력 파서

출처: mandu.log (2025-11-04), `raw/LangChain 기초.pdf`

## 개요

LangChain의 가장 기본적인 구성 요소인 LLM 모델([[frameworks/chatopenai]]), 프롬프트([[concepts/prompt-template]]), 출력 파서, 체인([[concepts/lcel]])의 사용법을 다루는 한국어 튜토리얼.

## 다루는 핵심 주제

| 주제 | 연결 페이지 |
|------|------------|
| ChatOpenAI 클래스 사용법 | [[frameworks/chatopenai]] |
| 스트리밍 응답 | [[concepts/streaming]] |
| 토큰 캐싱(prefix caching) | [[concepts/prompt-caching]] |
| 멀티모달 입력 | [[frameworks/chatopenai]] |
| PromptTemplate | [[concepts/prompt-template]] |
| LCEL (pipe 체인) | [[concepts/lcel]] |
| Batch / async 실행 | [[concepts/lcel]] |
| RunnablePassthrough | [[patterns/runnable-passthrough]] |
| RunnableParallel | [[patterns/runnable-parallel]] |
| RunnableLambda | [[patterns/runnable-lambda]] |
| LangSmith 추적 | [[frameworks/langsmith]] |

## 환경 설정 요약

```
OPENAI_API_KEY=
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
```

패키지 설치: `pip install -r https://raw.githubusercontent.com/teddylee777/langchain-kr/main/requirements.txt`

## 생성된 Wiki 페이지

**Frameworks (3)**: [[frameworks/langchain]], [[frameworks/chatopenai]], [[frameworks/langsmith]]

**Concepts (5)**: [[concepts/lcel]], [[concepts/runnable]], [[concepts/prompt-template]], [[concepts/prompt-caching]], [[concepts/streaming]]

**Patterns (3)**: [[patterns/runnable-passthrough]], [[patterns/runnable-parallel]], [[patterns/runnable-lambda]]
