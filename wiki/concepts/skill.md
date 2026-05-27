---
type: concept
tags: [skill, procedure, harness, 재사용]
created: 2026-05-27
sources: [7. Harness and Skills.pdf]
---

# Skill (스킬)

## 정의

에이전트가 특정 작업을 어떻게 수행할지 정의한 마크다운 파일. 에이전트는 작업 맥락에 맞는 Skill을 자동으로 찾아 적용한다.

## 상세 설명

Skill은 [[Harness Engineering]]의 4가지 구성 요소 중 **Procedure**에 해당한다. "어떻게 수행하는가"를 명문화한 재사용 가능한 절차서다.

**Skill 파일의 구성 요소:**

```markdown
---
name: skill-name
description: 언제 이 스킬을 사용하는지 (트리거 정의)
---

# Skill: [이름]

## 입력
- $ARGUMENT 등 입력 변수

## 절차
Step 1 — ...
Step 2 — ...

## 출력
- 생성·수정되는 파일 목록
```

**트리거 방식에 따른 분류:**

| 유형 | 트리거 | 위치 | 예시 |
|------|--------|------|------|
| 자연어 스킬 | `description` 매칭 | `.claude/skills/` | ingest, query |
| 슬래시 커맨드 | `/명령어` 직접 입력 | `.claude/commands/` | /lint |

**Skill vs Contract:**

> "Contract가 없는 Procedure(Skill)는 무한 루프이고,  
> Procedure(Skill)가 없는 Contract는 죽은 문서다."

Skill은 반드시 [[Contract-Driven Iteration]]의 Contract(TASK.md)와 함께 동작해야 한다.

**이 프로젝트의 Skill 목록:**

- `.claude/skills/ingest.md` — 소스 인제스트
- `.claude/skills/query.md` — 위키 질의응답
- `.claude/commands/lint.md` — 위키 건강 검사 (`/lint`)

## 관련 개념

- [[Harness Engineering]] — Skill은 하네스의 Procedure 구성 요소
- [[Contract-Driven Iteration]] — Skill과 함께 동작하는 Contract
- [[Hook]] — Skill 실행 전후에 결정론적으로 주입되는 메커니즘
- [[Orchestrator]] — 상황에 맞는 Skill을 선택하는 관리자

## 출처

- [[source: 7. Harness and Skills.pdf]] — "에이전트가 특정 작업을 어떻게 수행할지 정의한 마크다운 파일. AI Agent는 작업 맥락에 맞는 Skill을 자동으로 찾아 적용할 수 있다."
