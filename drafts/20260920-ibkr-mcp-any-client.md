---
title: "IBKR MCP 개방 — ChatGPT·Claude 말고 Cursor·Perplexity도 계좌에 붙인다"
date: 2026-09-20T07:08:00+09:00
category: "AI Trading"
slug: "ibkr-mcp-any-client"
summary: "2026-07-28 IBKR 공식. 인증 마켓플레이스(ChatGPT/Claude/Grok) 밖 MCP 클라이언트(Claude Code·Cursor·Perplexity·Windsurf 등)도 https://api.ibkr.com/v1/api/mcp-public 로 연결. 에이전트는 지시서만 작성, 체결은 IBKR 화면에서 사람 제출."
---

## 한줄 요약
[Interactive Brokers](https://www.interactivebrokers.com/en/general/about/mediaRelations/7-28-26.php)는 AI 연동을 **MCP 표준**으로 열어, 기존 ChatGPT·Claude·Grok 인증 커넥터뿐 아니라 **임의의 MCP 호환 도구**가 계좌에 붙게 했다. 엔드포인트: `https://api.ibkr.com/v1/api/mcp-public`.

## 지금 뭐가 뜨나
- 연결 흐름: 클라이언트에서 MCP 서버 URL 추가 → IBKR 로그인 화면 → **단일 계좌** 권한 승인. API 키를 AI에 넘기지 않는 설계.
- 에이전트가 할 수 있는 것: 포트폴리오·리스크·시나리오 질의, 투자 리서치, **자연어로 거래 지시서 초안**.
- 에이전트가 **못** 하는 것(이 릴리즈): 주문을 호가창에 직접 넣기. 초안을 IBKR Client Portal / Desktop / Mobile / TWS 등에서 사람이 검토·제출.
- Gemini 지원은 “곧”이라고만 발표. Ask IBKR·AI Screener·테마 검색·뉴스 요약 등 **플랫폼 내장 AI**는 MCP와 별개 제품군.

## 왜 중요한가
MT5·cTrader·TradingView MCP 물결 옆에서 IBKR는 **“분석은 에이전트, 체결은 브로커 UI”**라는 안전 설계를 분명히 했다. 실시간 돈에서는 “에이전트가 얼마나 똑똑한가”보다 **어느 레이어에서 주문을 막느냐**가 먼저다.

## 기억할 것
- [IBKR 보도](https://www.interactivebrokers.com/en/general/about/mediaRelations/7-28-26.php) · [AI Hub](https://www.interactivebrokers.com/en/trading/ai-hub.php) · MCP URL `api.ibkr.com/v1/api/mcp-public`
