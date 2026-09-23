---
title: "Second Brain: ai-memory — 벤더 넘나드는 git 백업 마크다운 장기기억"
date: 2026-09-24T07:07:00+09:00
category: "Second Brain / PKM"
slug: "ai-memory-cross-agent-wiki"
summary: "akitaonrails/ai-memory(~8.2k★). Rust MCP/HTTP. git 백업 .md 위키가 소스 오브 트루스, SQLite FTS5는 파생 인덱스. 기본 제로-LLM. 훅 캡처·클레임원스 핸드오프. Claude Code/Cursor/Codex 등."
---

## 한줄 요약
[ai-memory](https://github.com/akitaonrails/ai-memory)는 코딩 에이전트들의 **벤더 사일로 기억**을 깨려는 로컬 퍼스트 서버다. 메모리는 **git으로 버전 관리되는 Markdown 위키**가 원본이고, 검색용 DB는 언제든 재빌드 가능한 파생물이다.

## 어떻게 동작하나
- **캡처**: 에이전트 라이프사이클 훅으로 관찰을 조용히 수집.
- **원본**: 사람이 Obsidian/VS Code/`rg`로 읽고 고칠 수 있는 `.md`.
- **리콜**: 기본은 SQLite FTS5 등 **제로-LLM**(API 비용 없음). 임베딩/LLM 통합은 옵션.
- **핸드오프**: 세션이 끊길 때 미해결을 기록하고, 다음 에이전트가 **클레임원스**로 이어받음.
- 지원(프로젝트·DEV 소개 기준): Claude Code, Codex, Cursor, OpenCode, Gemini CLI 등. MIT. Docker로 `127.0.0.1:49374` 예시.

## 왜 중요한가
도구를 Claude↔Cursor로 바꿔도 **같은 장기기억**을 들고 가게 한다. LLM Wiki 철학(사람이 소유하는 마크다운 지식)을 멀티 에이전트 코딩 워크플로로 확장한 형태다. 스타 스냅샷 약 **8,205★**(2026-09-24).

## 기억할 것
- [github.com/akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) · [DEV 개요(2026-09-22)](https://dev.to/terminalchai/ai-memory-persistent-cross-agent-long-term-memory-for-coding-clis-3c40)
