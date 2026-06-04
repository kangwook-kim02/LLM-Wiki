---
type: concept
title: PromptTemplate
aliases: [Prompt Template, ChatPromptTemplate]
tags: [langchain, prompt, template]
created: 2026-06-04
source: [[sources/langchain-basics-mandu]]
---

# PromptTemplate

사용자의 입력 변수를 사용하여 완전한 프롬프트 문자열을 만드는 데 사용되는 템플릿 클래스.

## 핵심 파라미터

| 파라미터 | 타입 | 설명 |
|----------|------|------|
| `template` | str | 템플릿 문자열. `{변수명}`으로 변수 표기 |
| `input_variables` | list[str] | 중괄호 안에 들어갈 변수 이름 목록 |

## 사용법

```python
from langchain_core.prompts import PromptTemplate

# 방법 1: from_template 클래스 메서드
template = "{country}의 수도는 어디인가요?"
prompt_template = PromptTemplate.from_template(template)

# 프롬프트 문자열 생성
prompt = prompt_template.format(country="대한민국")
# → '대한민국의 수도는 어디인가요?'
```

## LCEL에서 사용

[[concepts/lcel]]의 pipe 체인에서 첫 번째 단계로 자주 사용됨:

```python
chain = PromptTemplate.from_template("{topic}에 대해 설명해주세요.") | model | output_parser
```

## 중괄호 이스케이프

템플릿에서 중괄호 자체를 출력하려면 이중 중괄호 `{{ }}` 사용:

```python
template = """
양식은 [FORMAT]을 참고하여 {{ 작성 }}해주세요.
# 상황: {question}
"""
```

## 관련 개념

- [[concepts/lcel]] — LCEL 파이프라인의 첫 단계로 활용
- [[concepts/runnable]] — PromptTemplate은 Runnable 인터페이스 구현체
- [[frameworks/langchain]] — LangChain 프레임워크
