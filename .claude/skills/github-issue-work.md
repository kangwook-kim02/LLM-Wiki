---
name: github-issue-work
description: "이슈 #N번 작업하자", "이슈 #N 시작해", "#N번 작업해줘" 등 특정 이슈 번호로 작업 시작을 요청할 때 실행한다. 개발 작업 실행 전용 스킬.
---

# Skill: github-issue-work

## 입력

| 변수 | 설명 | 예시 |
|------|------|------|
| `$N` | 이슈 번호 | `3` |

## 절차

### Step 1 — 컨텍스트 파악

`docs/decision-log.md`를 읽어 이 이슈와 관련된 과거 의사결정 라운드를 확인한다.

```bash
gh issue view $N
```

이슈 제목, 레이블, 본문(영향 범위·설명·재현 방법 등) 전체 파악.

### Step 2 — 작업 브랜치 생성

```bash
git checkout -b issue-$N/{slug}
```

`{slug}`: 이슈 제목을 소문자 kebab-case로 변환.
예) `issue-3/add-raw-save-tool`

### Step 3 — 작업 계획 수립 후 사용자 확인

이슈 내용을 바탕으로 작업 계획을 요약하고 사용자에게 보여준 뒤 승인받고 진행한다.

```
## 작업 계획 — 이슈 #N: {제목}

### 변경 대상 파일
- `{파일1}` — {변경 내용}
- `{파일2}` — {변경 내용}

### 순서
1. ...
2. ...

진행할까요?
```

### Step 4 — 구현 및 검증 (orchestrate 스킬에 위임)

사용자 승인 후 orchestrate 스킬을 실행한다.
아래 컨텍스트를 전달한다:

- `$ISSUE_N` = 이슈 번호
- `$ISSUE_TITLE` = 이슈 제목
- `$ISSUE_BODY` = 이슈 본문
- `$WORK_PLAN` = Step 3에서 사용자가 승인한 작업 계획

orchestrate 스킬이 impl-agent → verify-agent 순으로 실행하고
커밋까지 처리한다. 결과를 기다린다.

### Step 5 — PR 생성 (사용자 요청 시)

orchestrate가 커밋 완료를 보고한 뒤, 사용자가 PR을 요청하면:

```bash
gh pr create \
  --title "{이슈 제목}" \
  --body "$(cat <<'EOF'
## Summary
- closes #{$N}
- {변경 내용 bullet}

## Test plan
- [ ] {테스트 항목}

EOF
)"
```

---

## 원칙

- 작업 전 반드시 계획을 사용자에게 보여주고 확인받는다
- 브랜치 없이 main에서 직접 작업하지 않는다
- Step 4는 반드시 orchestrate 스킬을 통해 실행한다 (직접 구현 금지)
- PR은 사용자가 명시적으로 요청할 때만 생성한다
