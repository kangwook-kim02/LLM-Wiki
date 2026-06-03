---
name: github-issue-create
description: "이슈 등록해줘", "이슈 만들어줘", "이슈 올려줘" 등 GitHub 이슈 생성을 요청할 때 실행한다. 개발 작업 등록 전용 스킬.
---

# Skill: github-issue-create

## 절차

### Step 1 — 이슈 유형 확인

사용자가 유형을 명시하지 않은 경우 질문한다:
- `bug` — 버그 리포트 (`.github/ISSUE_TEMPLATE/bug_report.md`)
- `feature` — 기능 요청 (`.github/ISSUE_TEMPLATE/feature_request.md`)

### Step 2 — 이슈 내용 수집

사용자 메시지에서 추출하거나, 부족한 경우 질문한다:

| 항목 | bug | feature |
|------|-----|---------|
| 제목 | 필수 | 필수 |
| 설명 | 버그 재현 방법 | 기능 동기 및 설명 |
| 영향 범위 | MCP/스킬/뷰어 중 해당 체크 | 도구 추가/스킬/뷰어 중 해당 체크 |

### Step 3 — 이슈 생성

```bash
gh issue create \
  --title "[BUG] {제목}"  또는  "[FEAT] {제목}" \
  --body "{템플릿 기반 본문}" \
  --label "bug"  또는  "enhancement"
```

### Step 4 — 결과 보고

생성된 이슈 URL과 번호를 사용자에게 알린다.

```
이슈 #N이 생성되었습니다: https://github.com/{repo}/issues/N
작업을 시작하려면: "이슈 #N번 작업하자"
```

---

## 원칙

- 제목은 반드시 `[BUG]` 또는 `[FEAT]` 접두사를 붙인다
- `gh` CLI가 인증되어 있지 않으면 `gh auth login` 안내 후 중단
- 이슈 생성 전 내용을 요약해서 사용자 확인을 받는다
