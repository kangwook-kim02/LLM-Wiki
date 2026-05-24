---
type: source
tags: [강의자료, plan-mode, sequential-agent, parallel-agent, CSE3308]
created: 2026-05-24
---

# Plan Mode, Sequential and Parallel Agents

**파일:** `raw/4. Plan_mode Sequential and Parallel agents.pdf`
**인제스트 날짜:** 2026-05-24
**유형:** 강의자료 (CSE3308 Week 4)

## 핵심 주장

- **Plan Mode**: Agent CLI에서 계획만 세우고 코드는 건드리지 않는 모드. 진입 시 read-only 도구만 활성화되며 파일 수정·생성·삭제·명령 실행이 차단된다. 산출물은 마크다운 파일로 저장된다.
- **Hand-off 파일 패턴**: 각 Round 또는 에이전트마다 작업 내용을 기록하는 핸드오프 파일을 저장. (예: `workspace/00_planning.md`, `01_review.md`, ..., `04_final_plan_report.md`)
- **Pipeline 구조 설계**: 프롬프트 입력 → Plan 생성 → Review → Revised Plan → TODO의 순차적 파이프라인.
- **도구 간 협업**: Claude Skill에 Codex를 Implementation 담당으로, Codex Skill에 Claude를 Review 담당으로 등록하면 CLI 레벨에서 간단한 에이전틱 코딩 체계를 확보할 수 있다.

## 주요 개념

- [[Plan Mode]], [[Sequential Agent]], [[Parallel Agent]], [[Hand-off 파일]], [[Pipeline]]

## 주목할 인사이트

- Plan Mode에서 Python 기반 프로토타입 요청 시 에이전트가 Tkinter를 선택하는 경향이 있음 (추가 라이브러리 불필요, 낮은 Fault 확률, 단 성능 이슈 있음).
- Excalidraw를 이용한 러프한 파이프라인 구조 정의 → CLI에게 image와 API Document를 drag & drop으로 전달하여 파이프라인 스크립트 생성 가능.
- "파이프라인 스크립트의 명세를 재사용 가능하도록 구조화한 문서를 작성" — 재사용 가능한 스크립트가 핵심 산출물.

## Wiki 업데이트 내역

- 생성: [[source: source-04-plan-mode-sequential-parallel]]
- 생성: [[Plan Mode]] (wiki/concepts/plan-mode.md)
- 업데이트: [[Sequential Agent]] (wiki/concepts/sequential-agent.md)
- 업데이트: [[Parallel Agent]] (wiki/concepts/parallel-agent.md)
- 생성: [[Hand-off 파일]] (wiki/concepts/handoff-file.md)
- 업데이트: [[에이전트 아키텍처 패턴]] (wiki/topics/agent-architecture-patterns.md)
