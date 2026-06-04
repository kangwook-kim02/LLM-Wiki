---
type: framework
title: LangChain
tags: [langchain, llm, framework]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# LangChain

LLM 기반 애플리케이션을 구축하기 위한 오픈소스 프레임워크. 프롬프트, 모델, 출력 파서, 체인, 에이전트 등의 구성 요소를 제공한다.

## 핵심 개념

| 구성 요소 | 설명 |
|----------|------|
| [[concepts/prompt-template]] | 입력 변수를 포함한 프롬프트 템플릿 |
| [[frameworks/chatopenai]] | OpenAI ChatGPT 모델 래퍼 |
| [[concepts/lcel]] | 체인을 선언형으로 조립하는 표현 언어 |
| [[concepts/runnable]] | 모든 구성 요소가 구현하는 공통 인터페이스 |
| [[frameworks/langsmith]] | API 호출 추적 및 모니터링 도구 |

## 설치

```bash
pip install -r https://raw.githubusercontent.com/teddylee777/langchain-kr/main/requirements.txt
```

`langchain-teddynote` 패키지는 한국어 튜토리얼(teddylee777)이 제공하는 유틸 패키지로, 불편한 기능을 보완하고 추가 기능을 제공한다.

## 패키지 구조

- `langchain_core` — 핵심 추상화 (Runnable, PromptTemplate, OutputParser 등)
- `langchain_openai` — OpenAI 통합 (ChatOpenAI)
- `langchain_community` — 서드파티 통합 모음
- `langchain_teddynote` — 한국어 튜토리얼 유틸 패키지

## 관련 개념

- [[concepts/lcel]] — 체인 조립 문법
- [[concepts/runnable]] — Runnable 인터페이스
- [[patterns/runnable-passthrough]] — 입력 통과 패턴
- [[patterns/runnable-parallel]] — 병렬 실행 패턴
- [[patterns/runnable-lambda]] — 사용자 정의 함수 래핑
