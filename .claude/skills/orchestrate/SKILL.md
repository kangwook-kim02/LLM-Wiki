---
name: orchestrate
description: impl-agent와 verify-agent를 순차적으로 조율하는 오케스트레이션 스킬. github-issue-work 스킬의 작업 실행 단계에서 호출된다. 직접 트리거하지 않는다.
---

# Skill: orchestrate

## 입력 (github-issue-work로부터)

- `$ISSUE_N` — 이슈 번호
- `$ISSUE_TITLE` — 이슈 제목
- `$ISSUE_BODY` — 이슈 본문 (요구사항)
- `$WORK_PLAN` — 사용자가 승인한 작업 계획

---

## 실행 흐름

### Phase 1 — impl-agent 스폰

아래 컨텍스트를 전달하여 impl-agent를 실행한다:

```
[impl-agent 에게]
이슈 #$ISSUE_N: $ISSUE_TITLE

요구사항:
$ISSUE_BODY

승인된 작업 계획:
$WORK_PLAN

위 내용을 구현하고 완료 보고서를 작성해줘.
agents/impl-agent.md 의 절차를 따른다.
```

impl-agent의 완료 보고를 수신하고 `$IMPL_REPORT`로 저장한다.

### Phase 2 — verify-agent 스폰

impl-agent 완료 후 즉시 verify-agent를 실행한다:

```
[verify-agent 에게]
이슈 #$ISSUE_N 구현 검증 요청

원래 요구사항:
$ISSUE_BODY

impl-agent 구현 보고:
$IMPL_REPORT

위 구현이 요구사항을 충족하는지 검증하고 결과를 보고해줘.
agents/verify-agent.md 의 절차를 따른다.
```

### Phase 3 — 결과 처리

**PASS인 경우:**

```bash
git add {impl-agent가 변경한 파일들}
git commit -m "#{$ISSUE_N} {$ISSUE_TITLE}"
gh pr create \
  --title "{$ISSUE_TITLE}" \
  --body "$(cat <<'EOF'
## Summary
- closes #{$ISSUE_N}
- {변경 파일 및 구현 내용 bullet}

## Test plan
- [ ] {verify-agent 검증 항목}
EOF
)"
```

사용자에게 보고:
```
✅ 이슈 #$ISSUE_N 구현 및 검증 완료
커밋: #{SHA}
PR: {PR URL}
```

**FAIL인 경우 (1회 재시도):**

verify-agent의 수정 제안을 포함하여 impl-agent를 재스폰한다:

```
[impl-agent 에게 — 재시도]
검증에서 다음 문제가 발견되었습니다:
{verify-agent의 FAIL 보고}

위 항목을 수정해줘. 다른 부분은 건드리지 않는다.
```

재시도 후 verify-agent를 다시 실행한다.

**재시도 후에도 FAIL인 경우:**

자동 커밋하지 않고 사용자에게 보고한다:

```
⚠️ 이슈 #$ISSUE_N 검증 2회 실패

구현 내용은 브랜치에 저장되어 있습니다.
검증 실패 이유:
{verify-agent 최종 보고}

다음 중 선택해주세요:
1. 직접 수정 후 "다시 검증해줘"
2. 현재 상태로 커밋 "그냥 커밋해줘"
3. 작업 취소 "브랜치 버려줘"
```

---

## 원칙

- impl → verify 순서는 반드시 지킨다 (역방향 불가)
- 자동 재시도는 최대 1회
- 재시도 후 실패 시 사용자 판단에 위임한다
- 커밋 후 PR은 자동으로 생성한다 (사용자 요청 불필요)
- 사용자 승인 없이 `git push --force` 또는 머지 금지
