# /health

현재 하네스 구조가 올바르게 설계됐는지 점검한다.
문제가 있는 항목은 ❌, 정상은 ✅, 경고는 ⚠️ 로 표시한다.

---

## 점검 항목

### 1. 필수 파일 존재 여부

다음 파일이 모두 존재하는지 확인한다:

```
CLAUDE.md
README.md
.gitignore
docs/domain-definition.md
docs/PRD.md
docs/decision-log.md
docs/wiki-schema.md
wiki/index.md
wiki/log.md
.claude/skills/ingest.md
.claude/skills/query.md
.claude/skills/wiki-edit.md
.claude/skills/github-issue-create.md
.claude/skills/github-issue-work.md
.claude/skills/orchestrate.md
.claude/agents/impl-agent.md
.claude/agents/verify-agent.md
.github/PULL_REQUEST_TEMPLATE.md
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md
```

### 2. 스킬 파일 frontmatter 검증

`.claude/skills/` 의 모든 `.md` 파일을 읽어 확인한다:
- `name` 필드가 YAML frontmatter에 존재하는가?
- `description` 필드가 YAML frontmatter에 존재하는가?
- `description`이 트리거 조건을 명확히 서술하는가? (빈 값 또는 1단어 이하 ❌)

### 3. 에이전트 파일 frontmatter 검증

`.claude/agents/` 의 모든 `.md` 파일을 읽어 확인한다:
- `name` 필드 존재 여부
- `description` 필드 존재 여부
- **허용된 기능**과 **제한** 섹션이 모두 존재하는가?

### 4. CLAUDE.md 일관성 검증

`CLAUDE.md`를 읽어 스킬 테이블에 등재된 항목과 실제 파일을 대조한다:
- 테이블에 있는 스킬 파일이 실제로 존재하는가?
- 실제 스킬 파일 중 테이블에 누락된 것이 있는가?

MCP 도구 명세도 확인한다:
- `raw_save`, `raw_read`, `wiki_list`, `wiki_read`, `wiki_write`, `wiki_search`, `wiki_delete` 7개가 모두 명시되어 있는가?

### 5. orchestrate 연결 검증

`github-issue-work.md`를 읽어 확인한다:
- Step 4에서 orchestrate 스킬을 호출하도록 명시되어 있는가?
- "직접 구현 금지" 원칙이 명시되어 있는가?

`orchestrate.md`를 읽어 확인한다:
- impl-agent 스폰 → verify-agent 스폰 순서가 명시되어 있는가?
- 재시도 횟수 제한(1회)이 명시되어 있는가?
- 실패 시 사용자 보고 흐름이 존재하는가?

### 6. decision-log 최신성 검증

`docs/decision-log.md`를 읽어 확인한다:
- 마지막 Round 번호가 `CLAUDE.md`의 최근 변경 이력과 일치하는가?
- "향후 라운드 예정" 섹션이 존재하는가?

---

## 출력 및 로그 저장

### 출력 형식

```
## 하네스 검증 결과 — YYYY-MM-DD

### 1. 필수 파일
✅ 모두 존재  /  ❌ 누락: {파일명}

### 2. 스킬 frontmatter
✅ {스킬명} — name/description 정상
❌ {스킬명} — {문제점}

### 3. 에이전트 frontmatter
✅ {에이전트명} — 정상
❌ {에이전트명} — {문제점}

### 4. CLAUDE.md 일관성
✅ 스킬 테이블 일치
⚠️ 누락된 파일: {파일명}

### 5. orchestrate 연결
✅ github-issue-work → orchestrate 연결 확인
✅ impl → verify 순서 확인
✅ 재시도 1회 제한 확인

### 6. decision-log
✅ 최신 Round: Round N
⚠️ {불일치 항목이 있을 경우}

---
총 ✅ N개 / ⚠️ N개 / ❌ N개
{❌ 또는 ⚠️ 가 있을 경우 수정 권고 항목 요약}
```

### 로그 저장

점검 완료 후 위 결과를 `docs/health/YYYY-MM-DD.md` 파일로 저장한다.

- 같은 날짜에 여러 번 실행된 경우: `YYYY-MM-DD-2.md`, `YYYY-MM-DD-3.md` 순으로 저장
- `docs/health/` 폴더가 없으면 생성 후 저장
- 저장 후 사용자에게 파일 경로를 알린다: `📄 로그 저장: docs/health/YYYY-MM-DD.md`
