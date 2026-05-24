---
type: source
tags: [강의자료, agent-specification, system-prompt, context-engineering, CSE3308]
created: 2026-05-24
---

# Agent Specifications

**파일:** `raw/5. Agent Specifications.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Practical Session 02 — Context Engineering)

## 핵심 주장

- **Agent Specification 구성 요소**: System Prompt + Context(Session ID, Project Information, Hand-Off) + Inputs + Outputs. 각 에이전트는 명확한 Role, Input/Output을 가져야 한다.
- **System Prompt의 역할**: 에이전트의 행동 방식을 결정하는 핵심. Claude는 `--system-prompt` 플래그로 간단하게 전달 가능하지만, 다른 에이전트의 경우 마크다운 파일 활용이 필요하다.
- **Planner-Reviewer 패턴**: AGENT1(Planner)은 분석·분해·계획·TODO 생성, AGENT2(Reviewer)는 유효성 검사·기술적 검토·점수 평가·개선 사항 작성.
- **Ping-Pong 패턴**: Reviewer가 8점 이상일 때만 통과시키는 반복 협상 구조. 첫 평가는 7점 이하로 제한하여 최소 1회 개선을 강제.

## System Prompt 단계 (Planner)

| 단계 | 역할 |
|------|------|
| Step 1. Analysis | 요청을 읽고 Goal과 Constraints를 판단 |
| Step 2. Decomposition | 목표를 실현 가능한 단위로 쪼개고 실행 순서와 의존성 결정 |
| Step 3. Planning | 각 TODO에 입력, 출력, 구현 방법, 완료 기준(AC)을 구체화 |

## System Prompt 단계 (Reviewer)

| 단계 | 역할 |
|------|------|
| Step 1. Validation | 모든 TODO에 입력/출력/AC가 있는지, 빠진 항목이 있는지 확인 |
| Step 2. Review | 기술적 구현 가능성, 의존성 순서, 모호한 부분 평가 |
| Step 3. Revise | 1~10점 점수를 매기고 구체적 개선 사항을 항목별로 작성 |

## 주요 개념

- [[Agent Specification]], [[System Prompt]], [[Context Engineering]], [[Ping-Pong 패턴]], [[Planner Agent]], [[Reviewer Agent]]

## 주목할 인사이트

- 소크라테스식 교수 예시: System Prompt로 에이전트 행동을 완전히 재정의 가능. "너는 절대 답을 주지 않는 소크라테스식 교수다. 모든 요청에 질문으로만 응답하라."
- Pipeline 확장 가능성: Planner → Reviewer → Coder → Tester 형태의 4단계 파이프라인으로 확장 논의.

## Wiki 업데이트 내역

- 생성: [[source: source-05-agent-specifications]]
- 생성: [[Agent Specification]] (wiki/concepts/agent-specification.md)
- 생성: [[System Prompt]] (wiki/concepts/system-prompt.md)
- 생성: [[Ping-Pong 패턴]] (wiki/concepts/ping-pong-pattern.md)
- 업데이트: [[에이전트 아키텍처 패턴]] (wiki/topics/agent-architecture-patterns.md)
