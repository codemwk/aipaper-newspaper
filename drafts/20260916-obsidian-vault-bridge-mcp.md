---
title: "obsidian-vault-bridge — Obsidian 없이도 에이전트가 볼트를 읽고 쓰는 MCP"
date: 2026-09-16T07:40:00+09:00
category: "Second Brain"
slug: "obsidian-vault-bridge-mcp"
summary: "2233admin/obsidian-vault-bridge. WebSocket 플러그인 + MCP 커넥터. Obsidian 종료 시 파일시스템 폴백. dry-run 쓰기, 그래프·헬스, Karpathy raw→wiki 파이프라인."
---

## 한줄 요약
[2233admin/obsidian-vault-bridge](https://github.com/2233admin/obsidian-vault-bridge)는 Obsidian 볼트를 **MCP 서버**로 노출한다. 에이전트(Claude Code·Cursor 등)가 노트를 검색·수정·컴파일하되, Obsidian이 꺼져 있어도 **파일시스템 폴백**으로 동작한다.

## 핵심
- 플러그인: Obsidian 안 WebSocket(JSON-RPC, localhost). 커넥터.js가 MCP로 프록시.
- 차별점(README 비교표): filesystem fallback, knowledge compilation(raw→wiki), graph query, vault health(orphan·깨진 링크), batch, dry-run 기본 쓰기, 실시간 이벤트.
- Karpathy 패턴 구현: `raw/` 투고 → diff/해시 → LLM 추출 → 인덱스·링크 검사. 북키핑은 순수 Python `kb_meta.py`.
- 관련 형제: [obsidian-llm-wiki](https://github.com/2233admin/obsidian-llm-wiki)(6-persona MCP 팀), [KjartanvanDriel/obsidian-wiki-mcp](https://github.com/KjartanvanDriel/obsidian-wiki-mcp)(스키마·승인형 ingest).

## 왜 중요한가
“세컨브레인”이 채팅 메모리에 남지 않고 **파일 단위 감사·Git**로 남으려면, 에이전트↔볼트 다리가 필요하다. 브리지는 그 다리이고, dry-run·헬스는 **에이전트가 볼트를 망가뜨리지 않게** 하는 운영 장치다. LLM Wiki를 실제로 돌리는 사람에게 플러그인 검색엔진 다음 체크리스트다.

## 기억할 것
- [obsidian-vault-bridge](https://github.com/2233admin/obsidian-vault-bridge)
- 패턴 출처: Karpathy LLM Wiki / 관련 YouTube·gist
