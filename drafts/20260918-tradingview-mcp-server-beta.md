---
title: "TradingView MCP 공개 베타 — 차트 데이터는 주고, 브로커 체결은 아직 안 줌"
date: 2026-09-18T07:10:00+09:00
category: "AI Trading"
slug: "tradingview-mcp-server-beta"
summary: "2026-09-16. TradingView 공식 MCP Server 공개 베타. Essential 이상, Claude 등 MCP 클라이언트. 시세·스크리너·펀더멘털·뉴스·공시·캘린더·워치리스트·알림. 잔고·포지션·주문 실행 도구는 문서상 없음. 지연 시세."
---

## 한줄 요약
[TradingView 블로그](https://www.tradingview.com/blog/en/tradingview-mcp-server-public-beta-60864/)(2026-09-16)와 [Finance Magnates](https://www.financemagnates.com/forex/tradingview-adds-mcp-as-retail-brokers-adopt-ai-trading-tools/)에 따르면, TradingView는 **공식 MCP Server**를 공개 베타로 열었다. 엔드포인트는 `https://mcp.tradingview.com/mcp`.

## 무엇이 바뀌었나
- **Essential 이상** 유료 플랜. TradingView 계정으로 인증하고 **API 키는 필요 없다**.
- Claude(웹·데스크톱·모바일·Claude Code) 등 MCP 호환 클라이언트에 커스텀 커넥터로 붙인다.
- 가능한 일: 시세·가격 이력, Screener, 펀더멘털, 뉴스, 공시(10-K/Q·8-K·콜 트랜스크립트), 경제 캘린더, **워치리스트·알림 관리**, 알림 사후 분석.
- 베타 제약: 도구 목록이 제한되고 **시장 데이터는 delayed**. FM 보도에 따르면 분당 약 **100 tool requests**/사용자 수준 제한 언급.
- 문서화된 도구에는 **브로커 잔고·포지션·주문 실행이 없다**. Supercharts의 브로커 연동과 MCP는 **분리**.

## 왜 중요한가
Leverate·cTrader가 “계좌 쪽 MCP”를 열 때, TradingView는 **리서치·스크리닝·알림 레이어**를 AI 대화에 붙이는 쪽이다. “NVDA 오늘 브리핑”, “P/E·성장·배당·RSI 조건으로 스크리닝 후 워치리스트 저장” 같은 프롬프트가 공식 예시. 자동매매 빌더에게는 **체결 MCP 전에 데이터 MCP**를 검증할 수 있는 공개 표준 창구다.

## 기억할 것
- 공식: [TradingView MCP 베타 안내](https://www.tradingview.com/blog/en/tradingview-mcp-server-public-beta-60864/) · 커넥터 URL `https://mcp.tradingview.com/mcp`
- 해설: [Finance Magnates](https://www.financemagnates.com/forex/tradingview-adds-mcp-as-retail-brokers-adopt-ai-trading-tools/)
