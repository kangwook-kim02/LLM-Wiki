# Wiki 페이지 스키마

Wiki 페이지는 4가지 유형으로 구성됩니다. 각 유형의 위치와 템플릿은 아래를 참조합니다.

---

## 1. 개념 페이지 (`wiki/concepts/`)

기술 개념·아이디어를 설명하는 페이지.

```markdown
---
type: concept
tags: [태그1, 태그2]
created: YYYY-MM-DD
sources: [소스파일명]
---

# [개념 이름]

## 정의
한 문장 정의.

## 상세 설명
2~5 문단.

## 관련 개념
- [[concepts/관련개념]]

## 출처
- [[sources/소스명]] — 인용 내용
```

---

## 2. 프레임워크 페이지 (`wiki/frameworks/`)

도구·라이브러리·프레임워크를 설명하는 페이지.

```markdown
---
type: framework
tags: [태그1, 태그2]
created: YYYY-MM-DD
---

# [프레임워크 이름]

## 요약
한 줄 설명.

## 핵심 컴포넌트
- 컴포넌트 1 — 역할
- 컴포넌트 2 — 역할

## 주요 사용 패턴
코드 예시 또는 다이어그램.

## 관련 항목
- [[concepts/관련개념]]

## 출처
- [[sources/소스명]]
```

---

## 3. 패턴 페이지 (`wiki/patterns/`)

아키텍처 패턴·설계 방법론을 설명하는 페이지.

```markdown
---
type: pattern
tags: [태그1, 태그2]
created: YYYY-MM-DD
---

# [패턴 이름]

## 문제 상황
어떤 상황에서 이 패턴이 필요한가.

## 해결 방법
패턴의 구조와 동작 방식.

## 구현 예시
코드 또는 다이어그램.

## 트레이드오프
장점과 단점.

## 출처
- [[sources/소스명]]
```

---

## 4. 소스 요약 페이지 (`wiki/sources/`)

인제스트된 원본 소스 하나당 1개 생성.

```markdown
---
type: source
created: YYYY-MM-DD
---

# [소스 제목]

**파일:** `raw/파일명`
**인제스트 날짜:** YYYY-MM-DD
**유형:** 논문 | 공식문서 | 튜토리얼 | 아티클

## 핵심 주장
- 주장 1
- 주장 2

## 주요 개념
- [[concepts/개념1]], [[frameworks/프레임워크1]]

## 주목할 인사이트
중요하거나 놀라운 내용.

## Wiki 업데이트 내역
이 소스로 인해 생성/수정된 페이지 목록.
```

---

## 슬러그 규칙

- 형식: `카테고리/페이지명`
- 소문자, 하이픈 구분
- 예) `concepts/rag`, `frameworks/langchain`, `patterns/basic-rag`
