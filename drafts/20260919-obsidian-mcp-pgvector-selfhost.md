---
title: "GitHub 해설: maxkuminov/obsidian-mcp — Postgres·벡터·OAuth 붙인 셀프호스트 볼트 메모리"
date: 2026-09-19T07:50:00+09:00
category: "GitHub"
slug: "obsidian-mcp-pgvector-selfhost"
summary: "maxkuminov/obsidian-mcp. 옵시디언 볼트를 에이전트 공유 메모리로: 시맨틱+전문검색, wikilink 그래프, CRUD, OAuth, vault guide. Docker+Postgres 비용 대신 멀티유저·감사 로그."
---

## 한줄 요약
[maxkuminov/obsidian-mcp](https://github.com/maxkuminov/obsidian-mcp)는 옵시디언 볼트를 **에이전트 공유 메모리**로 만드는 **셀프호스트 MCP**다. 가벼운 filesystem MCP와 달리 **Postgres 인덱스·pgvector·OAuth·관리 UI**를 전제로 한다.

## 무엇이 의미 있나 (코드 덤프 없이)
- **도구 패밀리 ~25개**: 시맨틱/전문 검색, wikilink 그래프 질의, 노트 CRUD, 원자적 쓰기·dry-run diff, 볼트 가이드(`get_vault_guide` — 일반 Obsidian 문법 + 해당 vault의 `CLAUDE.md`를 라이브로).
- **왜 무거운가**: Docker+DB 세팅 세금 대신, 인덱스가 유지되고 멀티유저·사용 로그·토큰 기반 클라이언트가 가능하다. Obsidian REST 플러그인에 묶인 서버와 달리 **앱을 안 켜도** 동작.
- 포지션 비교(README 표 요지): MarkusPfundstein식 REST 브리지·순수 Python 파일 MCP·플러그인 MCP 대비, **영속 인덱스 + 시맨틱 + OAuth** 축이 차별점.

## 왜 중요한가
어제 obsidian-second-brain v0.16(침묵 실패 수정)·vault-bridge와 같이 읽으면, PKM 스택이 (1) 에이전트 훅 안전장치 (2) 가벼운 MCP (3) **팀용 백엔드 MCP**로 분화 중이다. 개인 볼트면 librarian/Ar9av로 충분하고, 팀·감사·권한이 필요하면 이쪽이다.

## 기억할 것
- [maxkuminov/obsidian-mcp](https://github.com/maxkuminov/obsidian-mcp)
