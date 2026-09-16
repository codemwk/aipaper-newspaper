---
title: "llm-wiki-agent — raw/에 넣으면 에이전트가 위키를 키우는 스킬"
date: 2026-09-17T07:40:00+09:00
category: "Second Brain"
slug: "llm-wiki-agent-samuraigpt"
summary: "SamurAIGPT/llm-wiki-agent. Karpathy LLM Wiki 패턴. Claude Code·Codex·OpenCode·Gemini CLI. API 키 불필요(에이전트 파일시스템). Obsidian wikilink 그래프. ★3.5k대(조회 시점)."
---

## 한줄 요약
[SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)는 소스를 `raw/`에 두고 에이전트에게 ingest를 시키면, **지속·상호링크 마크다운 위키**를 스스로 키우는 코딩 에이전트 스킬이다.

## 무엇이 되나
- Claude Code / Codex / OpenCode / Gemini CLI 등 **설정 파일을 읽는 에이전트**면 동작. “별도 API 키 서버”가 아니라 에이전트 세션이 파일을 읽고 쓴다.
- 슬래시(예: Claude Code `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/wiki-graph`)와 자연어 트리거.
- Obsidian: `[[wikilink]]` 일관 유지 → 그래프가 자연 성장. Web Clipper·`raw/` 드롭으로 큐잉.
- Karpathy [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 패턴 — 매번 RAG 재검색 대신 **한 번 컴파일해 갱신**.
- 조회 시점 GitHub ★ **약 3.5k**, 최근 푸시 활발(2026-09-16 전후). 어제 Ar9av/obsidian-wiki·vault-bridge와 **같은 가족, 다른 진입점**(에이전트 스킬 중심).

## 왜 중요한가
세컨드브레인 사용자는 플러그인·MCP·스킬 중 무엇을 고를지 헷갈린다. 이 레포는 “에이전트가 이미 있는 사람”용 **최소 설치 위키 루프**다. LLM Wiki를 직접 짓겠다는 계획(사용자 관심)과 바로 맞닿는다.

## 기억할 것
- 레포: [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)
- 관련: [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki)(어제) · Karpathy gist
