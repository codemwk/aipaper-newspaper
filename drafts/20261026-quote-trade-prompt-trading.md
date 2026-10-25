---
title: "AI 트레이딩: Quote.Trade Pro — 말로 주문 전략을 짜면 AI가 ‘계획서’를 내고 사람이 승인해야 실행. 손절·익절 위치는 거래소에 끝까지 숨긴다"
date: 2026-10-26T07:08:00+09:00
category: "AI 트레이딩"
slug: "quote-trade-prompt-trading"
summary: "AI 에이전트용 크립토 ‘다크풀’ 거래소 Quote.Trade가 10/22(미 동부) 텔레그램 기반 Quote.Trade Pro를 출시. 내장 AI에게 ‘차트에 지표 넣어 줘’, ‘내 진입·청산 조건으로 고급 주문 만들어 줘’라고 말하면 거래 계획 초안을 만들고, 사용자가 검토·승인해야 실행된다. 지정가·손절·트레일링 스톱·OCO·브래킷 주문은 거래소 밖에서 관리하다 조건이 맞을 때만 즉시체결(FOK) 요청을 보낸다. API 문서상 ‘프롬프트’ 엔드포인트는 리서치·미리보기 전용."
---

> 지난번 저장하신 MT5 + 에이전트 안전장치 기사들(RiskGate·MT5 MCP 권한 설정)과 이어지는 소식입니다 — ‘AI는 제안, 사람은 승인’ 구조가 크립토 거래소에도 들어왔습니다.

## 한줄 요약
AI에게 매매를 맡길 때 두 가지가 무섭다. **AI가 멋대로 주문하는 것**, 그리고 **내 손절 위치가 남에게 보이는 것**. Quote.Trade Pro는 둘 다 막는 설계를 내세웠다([GlobeNewswire 보도자료](https://www.globenewswire.com/news-release/2026/10/23/3387001/0/en/quote-trade-launches-prompt-trading-and-advanced-order-suite-bringing-institutional-grade-ai-native-strategy-execution-to-the-dark-pool.html)).

## 어떻게 쓰나
- **텔레그램 안에서** 차트를 보며 내장 AI 에이전트와 대화한다.
  - “이 차트에 지표 추가해 줘” / “내 진입·청산 조건으로 고급 주문 만들어 줘” / “이 시장의 신호 아이디어 제안해 줘”
- AI는 지시를 **거래 계획 초안**으로 바꾸고, 사용자가 **검토·승인한 뒤에만** 실행된다.
- API 문서 기준으로도 `/api/v3/prompt/` 계열은 **리서치·미리보기만** 하고, 승인된 주문은 별도 주문 엔드포인트로 들어간다([API 문서](https://doc.quote.trade/v3-advanced-orders.html)).

## ‘전략을 숨기는’ 구조
| 일반 거래소 | Quote.Trade Pro |
|---|---|
| 손절·익절 주문을 거래소가 보관 → 거래소는 내가 어디서 나갈지 안다 | 지정가·손절·트레일링 스톱·OCO·브래킷·조건부 전략을 **거래소 밖**에서 관리 |
| 주문이 호가창에 대기 | 조건 충족 시 **즉시체결 아니면 취소(FOK)** 요청만 거래소로 |
- CEO 크리스 맥: “손절 주문을 쥔 거래소는 당신이 어디서 나갈지 정확히 안다. 우리 다크풀은 FOK 실행 요청만 받는다.”
- 회사 주장 수치: 초당 10만 주문 처리, 1,500개+ 시장, 올해 초 400만 달러 투자 유치. (외부 검증 수치 아님)

## 읽을 때 주의할 점
- **‘다크풀 DEX’**는 주문 정보를 공개 호가창에 드러내지 않는 탈중앙 거래소라는 뜻. 한국 사용자에겐 규제·세금·서비스 제공 범위를 먼저 확인해야 할 해외 크립토 서비스다.
- 보도자료엔 “AI 에이전트는 제한 없이 거래한다”는 문구도 있다. 즉 **승인 단계는 Pro 앱의 프롬프트 기능에 해당**하고, API로 직접 붙는 봇·에이전트는 스스로 주문할 수 있다. 내 에이전트를 붙일 땐 승인 단계를 내 쪽에서 따로 만들어야 한다.
- 같은 주 Virtuals Protocol은 에이전트용 BTC·ETH **옵션 자동매매**를 추가했다([TokenPost, 10/25](https://www.tokenpost.com/news/technology/40602)). 에이전트가 다룰 수 있는 상품이 현물→무기한 선물→옵션으로 빠르게 넓어지는 중이라, 권한 설계의 중요성은 더 커진다.

## MT5 사용자에게 주는 힌트
- MT5 내장 AI 어시스턴트도 매매 권한을 **실행 / 확인 요청 / 매매 금지** 중에서 고르게 돼 있다([MT5 도움말](https://www.metatrader5.com/en/terminal/help/mcp_and_ai/configuration)). Quote.Trade의 ‘초안→승인’은 그중 **‘확인 요청’ 모드를 기본으로 만든 것**과 같다.
- 차용할 아이디어: 손절·익절을 브로커에 미리 걸지 않고 **내 쪽(EA·에이전트)에서 보관하다 조건 시 시장가로 보내는 방식**은 노출은 줄이지만, 연결이 끊기면 손절이 안 나가는 위험이 생긴다. 안전장치(서버 측 비상 손절)와 함께 써야 한다.

출처: [Quote.Trade 보도자료 (10/22 ET)](https://www.globenewswire.com/news-release/2026/10/23/3387001/0/en/quote-trade-launches-prompt-trading-and-advanced-order-suite-bringing-institutional-grade-ai-native-strategy-execution-to-the-dark-pool.html) · [Quote.Trade API — Advanced Orders](https://doc.quote.trade/v3-advanced-orders.html) · [TokenPost — Virtuals 옵션 (10/25)](https://www.tokenpost.com/news/technology/40602) · [MetaTrader 5 도움말 — MCP and AI](https://www.metatrader5.com/en/terminal/help/mcp_and_ai/configuration)
