---
title: "GitTrends AI v5.0 — 스타 ‘속도’로 MCP·스킬을 에이전트에게 바로 찾게"
date: 2026-09-20T07:38:00+09:00
category: "GitHub Hot"
slug: "gittrends-ai-v50"
summary: "2026-09-10 DEV. jastfan/github-trending v5.0. Star Velocity Radar(24h 순증) + Agent Skills/MCP/마켓플레이스 보드. npm gittrends-mcp로 Claude/Cursor에 1클릭. JSON·RSS 공개. Agent-Leaderboard(누적 스타)와 보완 축."
---

## 한줄 요약
[DEV 소개](https://dev.to/aman_social/introducing-gittrends-ai-v50-real-time-github-velocity-1-click-mcp-discovery-for-coding-agents-405e)의 **GitTrends AI v5.0**은 GitHub Trending의 맹점 — **누적 스타에 묻히는 신규 폭주** — 를 **24시간 스타 속도(velocity)**로 풀어, MCP·Agent Skills를 코딩 에이전트가 쿼리하게 만든다.

## 지금 뭐가 뜨나
- 라이브: [jastfan.github.io/github-trending](https://jastfan.github.io/github-trending/) · 소스 [jastfan/github-trending](https://github.com/jastfan/github-trending)
- 네 보드: Agent Skills / MCP Servers / Ecosystem Marketplaces / **Star Velocity Radar**
- 에이전트 연결: `claude mcp add gittrends -- npx -y gittrends-mcp` 또는 Cursor `mcp.json`에 `npx -y gittrends-mcp`
- 자동화: Actions가 UTC 00:20·12:20에 갱신, 트렌딩 페이지 막히면 Search API 폴백. `data/latest.json`·`feed.xml` 공개.

## 왜 중요한가
[jaychempan/Agent-Leaderboard](https://github.com/jaychempan/Agent-Leaderboard)가 **누적 인기**라면, GitTrends는 **오늘 뭐가 터지나**다. 에이전트에게 “지금 클론할 MCP”를 맡길 때 두 보드를 같이 보는 편이 덜 다친다.

## 기억할 것
- [DEV 글](https://dev.to/aman_social/introducing-gittrends-ai-v50-real-time-github-velocity-1-click-mcp-discovery-for-coding-agents-405e) · 패키지 `gittrends-mcp`
