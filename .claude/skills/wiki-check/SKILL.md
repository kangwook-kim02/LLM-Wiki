---
name: wiki-check
description: "위키 점검해줘", "위키 상태 확인해줘", "위키 점검" 등 Wiki 콘텐츠 상태 점검을 요청할 때 실행한다.
---

# Skill: wiki-check

Wiki 콘텐츠의 구성과 품질을 점검하고 이상 여부를 보고한다.
하네스 구조 점검(`/health`)과 달리 **Wiki 페이지 데이터** 자체를 대상으로 한다.

---

## 절차

### Step 1 — 전체 페이지 목록 수집

```
MCP: wiki_list()
→ 전체 slug 목록 저장
```

전체 페이지 수, 카테고리별 분포 집계:
- `concepts/`, `frameworks/`, `patterns/`, `sources/`, 루트(`index`, `log`) 분류

---

### Step 2 — 인덱스 일관성 점검

```
MCP: wiki_read("index")
```

- `wiki_list()` 결과와 `index.md` 등재 목록 대조
- `index.md`에 없는 페이지(누락) → ⚠️
- `index.md`에 있지만 실제 파일이 없는 항목(유령 항목) → ❌

---

### Step 3 — 페이지 품질 점검

`wiki_list()`로 얻은 모든 slug를 순회하며 각 페이지를 읽고 확인한다.
(`index`, `log` 제외)

```
MCP: wiki_read("{slug}")
```

각 페이지에서 확인할 항목:

| 항목 | 정상 | 이상 |
|------|------|------|
| YAML frontmatter 존재 | `---` 블록으로 시작 | ❌ 없음 |
| `title` 필드 | frontmatter에 존재 | ⚠️ 누락 |
| `tags` 필드 | frontmatter에 존재 | ⚠️ 누락 |
| 본문 존재 | frontmatter 이후 내용 있음 | ❌ 빈 페이지 |
| 내부 링크 유효성 | `[[slug]]` 형식의 모든 링크 대상이 `wiki_list()` 목록에 존재 | ⚠️ 깨진 링크 |

---

### Step 4 — 검색 기능 점검

```
MCP: wiki_search("RAG")
```

- 결과가 1개 이상 반환되면 ✅
- 결과가 0개이면 ⚠️ (인제스트 필요 가능성)

---

### Step 5 — 결과 보고

아래 형식으로 출력한다:

```
## Wiki 점검 결과 — YYYY-MM-DD

### 전체 현황
- 총 페이지 수: N개
- concepts: N개 / frameworks: N개 / patterns: N개 / sources: N개

### 1. 인덱스 일관성
✅ index.md 누락 없음
⚠️ index.md 미등재 페이지: {slug}, ...
❌ 유령 항목 (파일 없음): {slug}, ...

### 2. 페이지 품질
✅ frontmatter 정상: N개
❌ frontmatter 누락: {slug}, ...
⚠️ title 누락: {slug}, ...
⚠️ tags 누락: {slug}, ...
❌ 빈 페이지: {slug}, ...

### 3. 내부 링크
✅ 깨진 링크 없음
⚠️ 깨진 링크: {slug} → [[{대상 slug}]] (존재하지 않음), ...

### 4. 검색 기능
✅ wiki_search 정상 동작

---
총 ✅ N개 / ⚠️ N개 / ❌ N개

{이상 항목이 있을 경우 수정 권고 요약}
```

---

## 원칙

- 모든 데이터 조회는 MCP 도구만 사용한다 (내장 Read 도구 사용 금지)
- 점검 결과를 수정하지 않는다 — 보고만 수행
- 수정이 필요한 항목은 구체적인 slug와 문제를 명시하여 사용자가 후속 조치를 취할 수 있게 한다
- 페이지 수가 많아 시간이 걸릴 경우 중간 진행 상황을 짧게 알린다
