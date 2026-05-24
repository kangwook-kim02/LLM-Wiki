---
type: entity
tags: [도구, CLI, Google, LLM-agent]
created: 2026-05-24
sources: [3. Agents subprocess calling.pdf]
---

# Gemini CLI

## 요약
Google이 개발한 CLI 기반 LLM 에이전트로, `-p` 플래그에 프롬프트를 직접 전달해야 하며 GEMINI.md 스키마를 지원한다.

## 주요 특징

- **프롬프트 전달 방식 차이**: Gemini는 stdin 전달이 불가하며 `-p` 플래그에 프롬프트 문자열이 필수.
- **Subprocess 호출**: Windows에서는 `gemini.cmd -p "프롬프트" --output-format json`.
- **세션 관리**: `gemini --resume`(최근 세션), `gemini --resume <index>`, `gemini --list-sessions`.
- **YOLO 모드**: `gemini --yolo` (무제한 권한).
- **Loop 미지원**: Loop 기능이 없어 OS 스케줄러를 활용해야 함.
- **GEMINI.md**: Gemini의 에이전트 스키마 파일.

## 관련 항목

- [[Claude Code]], [[Codex CLI]]
- [[Subprocess]] — Python에서 Gemini 호출 방법

## 출처

- [[source: 3. Agents subprocess calling.pdf]] — "Gemini는 -p에 프롬프트가 필수 (stdin으로 전달 불가)"
