---
name: query
description: ingest·wiki-edit 트리거가 아닌 모든 개념·기술 질문 시 실행한다. "RAG란?", "LangGraph에서 State를 어떻게 써?", "Retriever 유형 설명해줘" 등.
---

# Skill: query

## 절차

### Step 1 — 관련 페이지 검색

```
MCP: wiki_search("{질문에서 추출한 핵심 키워드}")
→ 관련 페이지 슬러그 목록 확인
```

결과가 없으면 상위 카테고리 키워드로 재시도. 그래도 없으면 Step 3으로.

### Step 2 — 관련 페이지 읽기

```
MCP: wiki_read("{슬러그}")  ← 검색 결과 상위 3개까지
```

### Step 3 — 인덱스 참조 (검색 결과 불충분 시)

```
MCP: wiki_read("index")
→ 전체 목록에서 관련 항목 탐색 후 wiki_read
```

### Step 4 — 답변 합성

- 출처 페이지를 `[[슬러그]]` 형식으로 명시
- Wiki에 없는 내용은 "Wiki에 해당 내용이 아직 없습니다"로 명시

### Step 5 — 답변 저장 (선택)

기존 Wiki에 없는 새로운 인사이트가 담겼다면:
```
MCP: wiki_write("{적절한 슬러그}", 새_페이지_내용)
```

---

## 원칙

- 항상 `wiki_search`부터 시작한다 (기억에만 의존하지 않음)
- Wiki에 없는 내용을 임의로 생성하지 않는다
- 출처 없는 주장 금지
