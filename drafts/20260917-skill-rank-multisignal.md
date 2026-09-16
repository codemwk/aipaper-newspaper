---
title: "SkillRank — 스타만이 아닌 GitHub·npm·HN 신호로 스킬 일일 순위"
date: 2026-09-17T07:50:00+09:00
category: "GitHub Hot"
slug: "skill-rank-multisignal"
summary: "davidcjw/skill-rank. Claude·에이전트 스킬을 0–100 점수로 매일 재랭크. GitHub 0.58·npm 0.25·커뮤니티(HN·awesome) 0.17. Agent-Leaderboard(스타순) 보완 레이어."
---

## 한줄 요약
[davidcjw/skill-rank](https://github.com/davidcjw/skill-rank)는 Claude Code·AI 에이전트 **스킬**을 GitHub·npm·Hacker News·awesome 리스트 신호로 묶어 **0–100** 인기 점수를 매일 다시 매긴다. 사이트: [skill-rank-ten.vercel.app](https://skill-rank-ten.vercel.app).

## 무엇이 다른가
- 가중치(README): **GitHub**(스타·포크·최근 푸시) 0.58 · **npm** 주간 다운로드 0.25 · **커뮤니티**(HN·큐레이션 리스트 포함) 0.17.
- 관련성 게이트: claude / mcp / subagent / agent-skill 등 허용어, n8n류 오탐 차단 덴ylist.
- 옵션으로 Supabase 스냅샷 → **전일 대비 화살표**(상승·하락). Cron으로 24시간 재검증.
- [jaychempan/Agent-Leaderboard](https://github.com/jaychempan/Agent-Leaderboard)가 **스타 순 보드**라면, SkillRank는 **다중 신호 온도계**. 레포 자체 스타는 아직 작아도, 방법론이 포인트다.
- 별도로 [AgentRank](https://agentrank-ai.com/)류는 MCP에 freshness·이슈 건강·dependents를 섞는 축 — “스타 거짓말” 문제 의식은 공유.

## 왜 중요한가
스킬·MCP가 폭증하면 스타 1등만 따라가다 **죽은 레포**에 시간을 쓴다. 자동화·세컨드브레인 사용자는 Leaderboard로 지도를 보고, SkillRank·AgentRank로 **신선도·실제 설치 신호**를 교차하면 고르기 비용이 줄어든다.

## 기억할 것
- 레포·앱: [skill-rank](https://github.com/davidcjw/skill-rank) · [skill-rank-ten.vercel.app](https://skill-rank-ten.vercel.app)
- 보완: [Agent-Leaderboard](https://github.com/jaychempan/Agent-Leaderboard) · [agentrank-ai.com](https://agentrank-ai.com/)
