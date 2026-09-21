---
title: "MT5 Build 6060 — 터미널에 네이티브 MCP·에이전트 AI가 들어왔다"
date: 2026-09-22T07:03:00+09:00
category: "AI Trading"
slug: "mt5-build-6060-native-mcp"
summary: "MetaQuotes MT5 Build 6060(릴리즈 노트 2026-07-23). Tools>Options>MCP. 로컬 엔드포인트 예: http://127.0.0.1:22346/mcp, 토큰+Bearer. 내장 Assistant 또는 Codex·Claude Code 등 외부 에이전트. 거래 기본은 권한·수동 확인. ProreX 고객은 ProreX MCP와 병행 가능."
---

## 한줄 요약
[MetaTrader 5 Build 6060](https://www.metatrader5.com/en/releasenotes/terminal/2447)(MetaQuotes, 2026-07-23 릴리즈 노트)은 터미널에 **네이티브 MCP**와 에이전트형 AI 연결을 넣었다. 시세·차트·주문을 로컬 MCP로 열고, 내장 Assistant나 외부 코딩 에이전트가 같은 프로토콜로 붙는다.

## 지금 뭐가 뜨나
- 설정: **Tools → Options → MCP**. 로컬 엔드포인트는 흔히 `http://127.0.0.1:22346/mcp` 형태(환경·빌드에 따라 확인).
- 인증: **토큰 + Bearer**. 외부 에이전트(예: Codex, Claude Code)도 동일 엔드포인트로 연결.
- 거래 기본값: 실주문·위험 작업은 **권한 게이트·수동 확인**이 기본이라는 가이드가 강조된다([연동 해설](https://trasignal.com/blog/forex/connect-chatgpt-claude-ai-metatrader-5/)).
- ProreX: 자격 있는 고객은 **ProreX MCP**(스크리너·Smart Score·아이디어·뉴스·캘린더)를 MT5 데이터 옆에 병행할 수 있다 — “브로커 인텔 + 터미널 실행” 이중 층.

## 왜 중요한가
어제 consent/audit형 커뮤니티 MCP가 “안전층”이었다면, 오늘은 **플랫폼 벤더가 MCP를 공식 표면으로 연 신호**다. 에이전트 트레이딩의 병목은 모델이 아니라 **어디에 권한이 박혀 있는가**로 이동한다.

## 기억할 것
- [MT5 릴리즈 노트 6060](https://www.metatrader5.com/en/releasenotes/terminal/2447) · [연동 가이드](https://trasignal.com/blog/forex/connect-chatgpt-claude-ai-metatrader-5/) · 데모·권한부터
