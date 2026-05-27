# Wiki Log

> append-only 작업 이력. LLM이 자동으로 기록합니다.
> 파싱 팁: `grep "^## \[" wiki/log.md | tail -10` 으로 최근 10개 확인.

---

## [2026-05-24] init | Wiki 초기화

- CLAUDE.md 스키마 생성
- AGENTS.md 스키마 생성 (Multi-Agent 호환)
- wiki/index.md 생성
- wiki/log.md 생성
- raw/, wiki/, wiki/concepts/, wiki/entities/, wiki/sources/, wiki/topics/ 디렉토리 생성

---

## [2026-05-24] ingest | 초기 일괄 인제스트 (9개 PDF)

### 처리된 소스

| 파일 | 소스 요약 페이지 |
|------|----------------|
| `1. Vibe coding and Agent coding.pdf` | `wiki/sources/source-01-vibe-coding-agent-coding.md` |
| `2. SDLC pipeline in Vibe coding.pdf` | `wiki/sources/source-02-sdlc-pipeline.md` |
| `3. Agents subprocess calling.pdf` | `wiki/sources/source-03-subprocess-calling.md` |
| `4. Plan_mode Sequential and Parallel agents.pdf` | `wiki/sources/source-04-plan-mode-sequential-parallel.md` |
| `5. Agent Specifications.pdf` | `wiki/sources/source-05-agent-specifications.md` |
| `6. Agent pool and Orchestrator.pdf` | `wiki/sources/source-06-agent-pool-orchestrator.md` |
| `7. Harness and Skills.pdf` | `wiki/sources/source-07-harness-skills.md` |
| `8. Model Context Protocol.pdf` | `wiki/sources/source-08-mcp.md` |
| `9. Loop and Hooks.pdf` | `wiki/sources/source-09-loop-hooks.md` |

### 생성된 개념 페이지

- `wiki/concepts/vibe-coding.md`
- `wiki/concepts/agentic-coding.md`
- `wiki/concepts/harness-engineering.md`
- `wiki/concepts/plan-mode.md`
- `wiki/concepts/mcp.md`
- `wiki/concepts/hook.md`

### 생성된 엔티티 페이지

- `wiki/entities/claude-code.md`
- `wiki/entities/codex-cli.md`
- `wiki/entities/gemini-cli.md`

### 생성된 주제 개요 페이지

- `wiki/topics/agentic-coding-overview.md`
- `wiki/topics/agent-architecture-patterns.md`

### 업데이트

- `wiki/index.md` 전체 업데이트 (20개 페이지 등록)

### 미생성 페이지 (향후 인제스트 시 생성 권장)

~~다음 개념들이 소스에서 언급되었으나 아직 개별 페이지가 없음~~ → 2026-05-27 전체 생성 완료.

---

## [2026-05-27] 미생성 페이지 13개 보완

### 생성된 개념 페이지 (11개)

- `wiki/concepts/sdlc.md`
- `wiki/concepts/prd.md`
- `wiki/concepts/sequential-agent.md`
- `wiki/concepts/parallel-agent.md`
- `wiki/concepts/agent-specification.md`
- `wiki/concepts/orchestrator.md`
- `wiki/concepts/agent-pool.md`
- `wiki/concepts/contract-driven-iteration.md`
- `wiki/concepts/skill.md`
- `wiki/concepts/subprocess.md`
- `wiki/concepts/loop.md`

### 생성된 엔티티 페이지 (2개)

- `wiki/entities/andrej-karpathy.md`
- `wiki/entities/fastmcp.md`

### 업데이트

- `wiki/index.md` 전체 업데이트 (20 → 33개 페이지 등록)
