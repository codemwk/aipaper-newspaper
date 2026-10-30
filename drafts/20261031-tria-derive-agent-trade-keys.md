---
title: "AI 트레이딩: ‘거래는 되고 출금은 안 되는 열쇠’ — Tria는 만료되는 에이전트 전용 키, Derive는 기계용 옵션 거래 API"
date: 2026-10-31T07:01:00+09:00
category: "AI 트레이딩"
slug: "tria-derive-agent-trade-keys"
summary: "10/30 자가수탁 금융앱 Tria(사용자 60만+)가 Claude·ChatGPT·Codex·Cursor 같은 에이전트에 하이퍼리퀴드·Decibel 무기한 선물 거래를 맡기는 Agentic Trading을 출시했다. 에이전트는 ‘포지션 열기·닫기만 되고 출금은 불가’한 전용 트레이딩 키로 접근하며, 키에 만료 기간을 걸고 언제든 회수할 수 있다. 같은 날 옵션 거래소 Derive는 에이전트가 복합 옵션 전략을 거래하는 Agent Trading API를 열었다."
---

## 한줄 요약
에이전트에게 계좌를 맡길 때 가장 무서운 건 “돈이 빠져나가는 것”이다. Tria의 답은 **거래 전용·출금 불가·만료되는 키**다([Chainwire](https://chainwire.org/2026/10/30/tria-launches-agentic-trading-allowing-ai-agents-to-execute-crypto-trades-without-giving-up-control-of-funds/)).

## Tria Agentic Trading — 구조
- **연결**: Claude, ChatGPT, Codex, Cursor 등 → Tria Trade SDK → 하이퍼리퀴드·Decibel 무기한 선물. 별도 AI 지갑으로 돈을 옮기지 않고 **기존 Tria 계좌에서 바로** 실행.
- **키 설계**: 거래소별 전용 트레이딩 키 발급 → 권한 설정 → AI 도구에 연결.
  - 할 수 있는 것: 지원 포지션 **열기·닫기**
  - 할 수 없는 것: **출금**
  - 관리: **만료 기간 설정**, 앱에서 에이전트 거래 모니터링, **언제든 회수**
- **사용 예**: “BTC가 진입가에 오면 포지션을 열고, 목표가에 닫아라” — 차트를 계속 볼 필요가 없다.
- 회사가 인용한 Investing.com 4월 조사: 미국 개인투자자 **62%가 AI를 투자 판단에 썼지만**, 그중 자동매매 알고리즘을 쓰는 사람은 **4.5%**뿐.

## Derive — 기계가 읽는 옵션 거래소
- 10/30 Derive가 에이전트용 문서·API를 공개해 **복합 옵션 전략을 에이전트가 직접 거래**할 수 있게 했다. Virtuals 등 에이전트 플랫폼이 이미 연결됐다고 밝혔다([TradingView 뉴스](https://www.tradingview.com/news/coinmarketcal:d66066ac9094b:0-derive-agent-trading-apis-give-ai-agents-access-to-complex-options-strategies-30-oct-2026/)).

## 꼭 읽어야 할 한 줄
Tria 스스로 공지에 적었다: **“거래 전용 권한은 출금을 막을 뿐, 거래 손실은 막지 못한다.”** 무기한 선물은 증거금 전액을 잃을 수 있는 상품이다. 출금 불가 키는 해킹·오작동 피해의 상한을 줄일 뿐, 전략이 틀렸을 때의 손실은 그대로다.

## 왜 중요한가
- 어제 다룬 B2TRADER(브로커가 권한 단계를 정함)·eToro(매 행동 승인)에 이어, **“권한을 열쇠 단위로 쪼개고 시간 제한을 거는”** 세 번째 설계가 나왔다. MT5의 내장 MCP도 ‘AI 거래 금지/허용/확인 필요’ 3단계를 둔다([MetaTrader 5 도움말](https://www.metatrader5.com/en/terminal/help/mcp_and_ai/configuration)).
- 지난번 저장하신 MT5 에이전트 거래 안전장치(RiskGate·MT5 MCP) 기사들과 이어지는 소식이다.
