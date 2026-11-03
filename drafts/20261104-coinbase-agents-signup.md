---
title: "AI 트레이딩: Coinbase ‘에이전트용 가입 페이지’ — ChatGPT·Claude·Grok이 주식·코인·선물까지 주문. 같은 날 CFD 브로커 Century는 정반대로 ‘읽기만’"
date: 2026-11-04T07:01:00+09:00
category: "AI 트레이딩"
slug: "coinbase-agents-signup"
summary: "Coinbase가 11/2 coinbase.com/agents에 ‘나를 위해 / 내 에이전트를 위해’ 가입 흐름을 열었다. MCP로 연결한 AI가 시세·보유 확인과 크립토·주식·24시간 선물 주문까지(지역·등급별). 안전장치는 별도 샌드박스 포트폴리오, 지출 한도, 거래별 수동 승인, Coinbase 밖 출금 금지. x402 마이크로결제는 건당 5달러·하루 50달러 상한(미국). 11/3 Century Financial은 MCP 도구 50개+를 주면서도 주문·출금은 막았다."
---

## 한줄 요약
10/25에 “Coinbase가 에이전트에게 문을 열었다”고 짧게 전했는데, 이번엔 그 문의 **구체적 구조**가 나왔다. 계좌를 만들 때부터 **“이 계좌는 내 에이전트용”**을 고르게 한 것이다([Techiexpert 11/3](https://techiexpert.com/coinbase-launches-sign-up-page-allowing-ai-agents-to-trade-crypto-stocks-and-futures/)).

## Coinbase가 연 것
- **연결**: ChatGPT, Claude, Grok, Perplexity, Hermes, Cursor 등 MCP 지원 도구를 코드·API 키 없이 연결. MCP가 없는 도구용 CLI도 제공.
- **할 수 있는 일**(지역·계정 등급에 따라): 시세·뉴스 조사, 보유 확인, 크립토·주식·24시간 선물/파생 주문. 예시 명령은 “BTC 80%·S&P 500 20%로 리밸런싱, 5% 넘게 벗어나면 알림”, “매주 수요일 TSLA 50달러 매수, RSI 70 넘으면 25달러만”.
- **안전장치**: 에이전트 전용 **샌드박스 포트폴리오**, **하드 지출 한도**, 체결 전 **수동 승인** 옵션, 언제든 연결 해제. 무엇보다 에이전트는 **Coinbase 밖으로 송금·출금 불가**.
- **에이전트가 직접 돈을 쓰는 길**: x402 프로토콜로 유료 데이터·리포트를 USDC로 결제, 미국 기준 **건당 5달러·하루 50달러** 상한. 에이전트 사용 추가 수수료는 없다.

## 같은 날 정반대 선택: Century Financial
CFD 브로커 Century Financial의 ‘Century AI Connect’(11/3)는 원격 MCP로 6개 그룹 **도구 50개+**(포지션·거래 내역·관심종목, 중간가, Trading Central 리서치, 뉴스 심리, 경제 캘린더)를 주지만, **주문·수정·청산·자금 이동·설정 변경은 전부 금지**. 실행은 자사 앱에서만 한다([TradeInformer](https://tradeinformer.com/tech-news/century-financial-launches-claude-connector)).

## 왜 중요한가 (MT5 쪽에서 보면)
지난번 저장하신 **MT5 + MCP 안전 레이어** 소식들과 바로 이어진다. 이제 브로커마다 **권한 사다리**가 상품 사양이 됐다: 읽기 전용(Century) → 주문 준비 후 사람 확인(Webull) → 승인 단계 붙은 실행(Match-Trader) → 한도·샌드박스 안에서 실행(Coinbase). MT5 Build 6060+의 내장 MCP도 ‘AI 거래 허용/금지/수동 확인’ 스위치를 두고 있다([MetaTrader 5 도움말](https://www.metatrader5.com/en/terminal/help/mcp_and_ai/capabilities)). 내 에이전트를 붙일 때 볼 체크리스트는 결국 같다: **별도 계좌(샌드박스), 금액 한도, 출금 차단, 수동 승인 기본값**.

## 주의
- 자연어 지시는 해석이 틀릴 수 있다. Coinbase도 “AI는 실수할 수 있고 투자 조언이 아니며 책임은 계정 소유자”라고 명시.
- 파생·선물 접근은 지역과 등급에 따라 다르다. 한국 사용자에게 어떤 기능이 열리는지는 확인되지 않았다.
