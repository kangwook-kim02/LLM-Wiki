---
type: framework
title: LangSmith
tags: [langsmith, langchain, observability, tracing]
source: [[sources/langchain-basics-mandu]]
created: 2026-06-04
---

# LangSmith

LangChain 애플리케이션의 API 호출 이력(토큰 수, 비용, 입출력 등)을 추적·모니터링하는 도구. 토큰 발급 후 한도 내에서 무료 사용 가능하다.

- 공식 사이트: https://smith.langchain.com/

## 환경 변수 설정

```bash
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your-key>
LANGSMITH_PROJECT=<project-name>
```

`.env` 파일에 작성 후 `python-dotenv`로 로드한다.

## 추적 설정

```python
from langchain_teddynote import logging

# 추적 시작
logging.langsmith("CH01-Basic")

# 추적 비활성화
logging.langsmith("CH01-Basic", set_enable=False)
```

## 주요 기능

- API 호출별 토큰 수, 비용, 응답 시간 추적
- 입출력 내용 시각화
- 프로젝트별 실행 이력 관리
- 디버깅 및 성능 최적화 지원

## 관련 개념

- [[frameworks/langchain]] — LangChain 프레임워크
- [[frameworks/chatopenai]] — 추적 대상 모델
- [[concepts/prompt-caching]] — 캐싱 토큰 확인
