---
title: "AI 트레이딩: ‘보기는 되고, 사고팔기는 안 된다’가 표준이 되는 중 — Alpaca의 ChatGPT 플러그인은 모의매매만 주문, Schwab은 외부 에이전트를 매주 수십 건 차단"
date: 2026-10-18T07:10:00+09:00
category: "AI 트레이딩"
slug: "agents-read-only-trading"
summary: "Alpaca(10/12): ChatGPT 플러그인 2종 — Paper Trading(모의 계좌로 주식·ETF·옵션·크립토 시뮬레이션 주문 가능), Live(실계좌 잔고·포지션·체결 조회만, 주문·수정·취소 불가). Schwab CEO 릭 워스터(10/16 Bloomberg TV, Forkast 10/17): 무단 AI 에이전트의 고객 자금 접근을 매주 ‘수십 건’ 차단, 자체 비서 ‘Charley’는 정보 업무만, 외부 LLM엔 읽기 전용 MCP. JPMorgan도 외부 에이전트 차단. 대조: IBKR은 전용 계좌 파티션으로 자율매매 시범(10/15), Robinhood는 전용 에이전트 계좌·주문 승인 기본 ON."
---

## 한줄 요약
“AI가 내 계좌로 대신 매매한다”는 그림은 매력적이지만, 이번 주 증권업계가 그은 선은 꽤 분명하다. **에이전트는 보고, 분석하고, 연습까지는 해도 된다. 진짜 돈을 움직이는 건 아직 사람 손이다.**

## Alpaca: 주문은 ‘모의 계좌’에서만
API 중심 증권사 **Alpaca**는 2026-10-12 ChatGPT 플러그인 두 개를 냈다([Alpaca 블로그](https://alpaca.markets/blog/paper-trading-and-live-portfolio-monitoring-now-available-in-chatgpt-with-alpaca/)).
- **Alpaca Paper Trading**: 모의 계좌에 연결해 잔고·포지션 확인, 시장 분석, 그리고 **주식·ETF·옵션·크립토 시뮬레이션 주문**까지 자연어로.
- **Alpaca Live**: 실계좌의 잔고·매수 가능액·포지션·체결 내역 **조회와 리서치만**. **실주문·수정·취소는 불가** — 실거래는 Alpaca API나 대시보드에서 직접 해야 한다.
- 회사가 강조한 주의점이 실전적이다: “주문이 **접수됐다는 응답**이 **체결됐다는 뜻은 아니다**. 상태를 다시 조회하라.” 모의매매는 시장 충격·지연 슬리피지·주문 대기 순서·규제 수수료를 반영하지 못한다는 것도 명시했다.

## Schwab·JPMorgan: 외부 에이전트 차단
Charles Schwab CEO **릭 워스터**는 10/16 Bloomberg TV 인터뷰에서 무단 AI 에이전트가 고객 계좌에 접근해 거래하려는 시도를 **매주 ‘수십 건’ 차단**하고 있으며 주간 보고를 받는다고 밝혔다([Forkast, 10/17](https://forkast.news/schwab-and-jpmorgan-block-unauthorized-ai-agents-from-moving-money-as-private-ordering-reaches-financial-core/)).
- 자체 AI 비서 **‘Charley’는 관리·정보 업무만** 하고 매매 기능이 없다.
- 외부 LLM에는 **읽기 전용 MCP 서버**를 준다 — 잔고 확인·리서치는 되지만 자금 이동은 금지.
- 그의 말: “누군가 비밀번호를 에이전트에게 넘겨 고객 대신 행동하게 하면, 우리도 고객도 통제할 수 없다. 뭔가 잘못되면 **누가 책임지나?**”
- **JPMorgan**의 제이미 다이먼도 외부 에이전트의 고객 계좌 접근을 막고 있다고 확인했다. 미국엔 아직 에이전트 책임을 정한 연방법이 없어(관련 법안들은 위원회 계류), 회사들이 **‘배제’로 스스로 규칙을 만드는** 중이라는 게 Forkast의 분석이다.

## 반대편: 울타리를 치고 문을 연 곳
- **IBKR**: 초대한 약 3천 명에게 **전용 자금 파티션** 안에서만 자율매매를 시범 개방(10/15 실적 발표, 지난 호 기사).
- **Robinhood**: 전용 에이전트 계좌에 든 돈만 쓰게 하고, **매 거래 수동 승인이 기본값(ON)**([Robinhood, 9/29](https://robinhood.com/us/en/newsroom/hood-summit-2026/)).

## 왜 중요한가
자동매매를 준비하는 개인에게 이번 주 흐름이 주는 실전 지침은 세 가지다. ① **연습은 모의 계좌 + AI**로 충분히 — Alpaca처럼 주문 흐름까지 그대로 연습할 수 있다. ② 실전에 넣을 땐 **‘전용 계좌·한도·승인’ 3종 세트**를 제공하는 곳을 고를 것. ③ 에이전트에 **비밀번호를 직접 넘기는 방식은 피할 것** — 증권사가 막는 이유가 곧 내 책임 문제다. 결국 AI 트레이딩의 승부는 모델 성능보다 **“얼마나 안전하게 권한을 나눠 주는가”**에서 갈리고 있다.

출처: [Alpaca — Paper Trading and Live Portfolio Monitoring in ChatGPT (10/12)](https://alpaca.markets/blog/paper-trading-and-live-portfolio-monitoring-now-available-in-chatgpt-with-alpaca/) · [Forkast — Schwab and JPMorgan Block Unauthorized AI Agents (10/17)](https://forkast.news/schwab-and-jpmorgan-block-unauthorized-ai-agents-from-moving-money-as-private-ordering-reaches-financial-core/) · [Yahoo Finance — Schwab CEO 인터뷰](https://finance.yahoo.com/markets/article/charles-schwab-ceo-ai-agents-trading-on-your-behalf-need-rules-of-the-road-203402357.html) · [Robinhood HOOD Summit 2026](https://robinhood.com/us/en/newsroom/hood-summit-2026/)
