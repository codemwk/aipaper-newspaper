---
title: "MCPVault — Obsidian 볼트 MCP가 v2 스펙으로, 읽기전용·wiki_link·보안 denylist"
date: 2026-09-22T07:11:00+09:00
category: "Second Brain"
slug: "mcpvault-obsidian-mcp-v2"
summary: "@bitbonsai/mcpvault(MCPVault). v0.16.0(2026-08)이 MCP v2(2026-07-28 스펙)로 이동. --read-only, wiki_link, .git/.obsidian 등 denylist, frontmatter 안전 편집. npx 설치·문서는 mcpvault.org. Obsidian 닫아도 로컬 파일 MCP."
---

## 한줄 요약
[MCPVault](https://mcpvault.org/)(`@bitbonsai/mcpvault`)는 로컬 Obsidian 볼트를 **MCP 클라이언트에 연결**한다. **v0.16.0**(2026-08)에서 공식 SDK 기준 **MCP v2(2026-07-28 스펙)** 로 옮겼고, 한 프로세스가 구·신 프로토콜을 받는다고 밝힌다.

## 지금 뭐가 뜨나
- **읽기 전용**: `--read-only`로 변형 툴을 끄고 조회만(v0.15.0).
- **wiki_link**: `[[Note]]` · `[[Note|Display]]` · 경로형 링크를 해석해 컨텍스트로 반환.
- **보안**: `.git` / `.obsidian` / `node_modules`·닷파일 등 **깊이 무관 denylist**. 심링크 탈출 차단 이력.
- **편집**: frontmatter는 AST 보존(날짜·따옴표·HH:MM 오인 방지). Obsidian을 켜지 않아도 파일 단위 동작.
- **설치**: `npx -y @bitbonsai/mcpvault` 계열 · 문서 [mcpvault.org](https://mcpvault.org/).

## 왜 중요한가
어제 enquire-mcp가 “검색 결과 신선도”였다면, 오늘은 **볼트 파일을 에이전트 표준 포트(MCP v2)로 여는 게이트웨이**다. 세컨드브레인×에이전트에서 스펙 세대가 갈리면 클라이언트가 끊긴다 — v2 이동은 그 신호다. 읽기전용·denylist가 기본 옵션으로 드러난 것도, 에이전트에게 노트북을 통째로 맡기기 전 **최소 권한** 체크리스트로 바로 쓰인다.

## 기억할 것
- [mcpvault.org](https://mcpvault.org/) · `@bitbonsai/mcpvault` · v0.16.0 MCP v2 · read-only 옵션
