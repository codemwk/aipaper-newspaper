---
title: "AI 트레이딩: IBKR, ‘승인 없이 사고파는’ AI 에이전트 첫 개방 — 전용 계좌 파티션·초대 3천 명, 같은 주 Schwab CEO “열쇠를 통째로 넘기는 건 지나치다”"
date: 2026-10-17T07:08:00+09:00
category: "AI 트레이딩"
slug: "ibkr-autonomous-ai-trading"
summary: "IBKR 3분기 실적 콜(10/15): 자격 고객이 호환 AI 에이전트에 ‘전용 계좌 파티션’ 안에서 자율 매매를 위임하는 기능 제한 출시. 사람 승인형 AI Connector 사용자 약 3,000명 먼저 초대, 수주 내 확대. Connector엔 Perplexity 공식 파트너·MCP 호환 확대, 계좌 손익·알림·관심종목·2-leg 옵션 추가. Schwab CEO(10/16): ‘규칙을 정해 준 에이전트만’, 새 비서 Charley는 매매 봇 아님. Sparkling(10/14): 에이전트는 주문 카드만, 서명은 사용자."
---

## 한줄 요약
10/15 본지는 IBKR Connector 1.2.0을 “검색은 열리고, 실행은 아직 조심스럽다”고 정리했다. 바로 그날(미국 시간 10/15) 3분기 실적 발표에서 **Interactive Brokers(IBKR)**가 한 발 더 나갔다 — 고객이 AI 에이전트에게 **사람 승인 없이 매매하도록 권한을 위임**하는 기능의 제한 출시를 공식화한 것이다([MarketBeat 콜 요약](https://www.marketbeat.com/instant-alerts/transcript-interactive-brokers-group-q3-earnings-call-highlights-2026-10-15/)).

## IBKR: 무엇을, 누구에게
- **자율 AI 매매(제한 출시)**: 자격을 갖춘 고객이 호환 AI 에이전트에 매매를 허락하되, 거래는 **전용 계좌 파티션(dedicated account partitions)** 안에서만 일어난다. 본 계좌와 칸막이를 친 ‘에이전트 전용 지갑’ 구조.
- **대상**: 사람이 매번 승인하는 기존 **AI Connector**를 써 본 고객 약 **3,000명**을 먼저 초대, 자격은 **향후 수주에 걸쳐 확대**(창업자 Thomas Peterffy). Zacks는 글로벌 주식·옵션을 여러 거래 세션에 걸쳐 지원한다고 전했다([Yahoo/Zacks](https://finance.yahoo.com/markets/stocks/articles/ibkr-q3-earnings-call-highlights-130000189.html)).
- **AI Connector 확장**: **Perplexity**를 공식 파트너로 추가, **MCP** 쓰는 AI 도구로 호환 확대, 계좌 단위 손익·알림·관심종목·**2-leg 옵션 전략** 추가.
- **회사의 계산**: Peterffy는 투자자가 AI로 더 많은 정보와 종목을 감시하게 되면서 **거래량이 늘 것**으로 본다. 3분기 커미션은 $6.02억(+12%), 고객 계좌는 558만(+35%).

## Schwab: “열쇠를 넘기진 말라”
다음 날(10/16) Charles Schwab CEO Rick Wurster는 Yahoo Finance에 반대편 원칙을 말했다. “에이전트가 당신 대신 거래하려면 당신이 **‘도로 규칙(rules of the road)’**을 줘야 한다… ‘알아서 주식 사 줘’는 위험하다. **열쇠를 통째로 넘기는 건 지나친 도약**이다.” Schwab이 곧 내놓을 대화형 비서 **Charley**는 매매 에이전트가 아니며, 처음엔 주소 변경·신뢰 연락처 지정 같은 행정 업무만 대신한다([Yahoo Finance](https://finance.yahoo.com/markets/article/charles-schwab-ceo-ai-agents-trading-on-your-behalf-need-rules-of-the-road-203402357.html)).

## 크립토 쪽 답: ‘에이전트는 서명 못 한다’
같은 주 자기수탁형 트레이딩 앱 **Sparkling**(10/14 웹앱 출시)은 세 번째 모델을 보여 줬다. 자연어로 원하는 거래를 말하면 에이전트가 **주문 카드(Pre-Executed Flow)**를 만들고, 사용자가 검토·수정·거절 후 직접 확정한다. 에이전트는 **개인키에 접근도, 서명도 못 한다**. 무기한 선물은 Hyperliquid, 토큰화 미국 주식은 xStocks, 스왑은 Bebop RFQ로 실행되며 미국·영국에선 쓸 수 없다([TechFinancials](https://techfinancials.co.za/2026/10/16/sparkling-launches-web-app-bringing-a-full-trading-terminal-and-ai-agent-to-the-browser-2/)).

## 왜 중요한가
한 주 사이 업계의 세 가지 설계가 선명해졌다: **① 칸막이 친 자율(IBKR)**, **② 규칙 먼저·실행은 아직(Schwab)**, **③ 준비는 AI·서명은 사람(Sparkling, Axi·Match-Trader 계열)**. 어제(10/16) 본지가 다룬 MEXC 설문에서 트레이더 54%가 “계좌의 20% 이하만 맡기겠다”고 답한 것과 IBKR의 ‘전용 파티션’은 정확히 같은 발상이다. 개인 자동매매를 설계한다면 지금 바로 따라 할 수 있는 원칙: **에이전트용 소액 계좌를 따로 두고, 최대 손실·레버리지 한도를 에이전트 밖(브로커 설정)에 건다.** 단, IBKR 자율 매매의 세부 한도·적용 국가는 아직 공개 문서로 확인되지 않았다.

출처: [MarketBeat — IBKR Q3 Call Highlights](https://www.marketbeat.com/instant-alerts/transcript-interactive-brokers-group-q3-earnings-call-highlights-2026-10-15/) · [Yahoo Finance/Zacks — IBKR Q3](https://finance.yahoo.com/markets/stocks/articles/ibkr-q3-earnings-call-highlights-130000189.html) · [Yahoo Finance — Schwab CEO](https://finance.yahoo.com/markets/article/charles-schwab-ceo-ai-agents-trading-on-your-behalf-need-rules-of-the-road-203402357.html) · [TechFinancials — Sparkling](https://techfinancials.co.za/2026/10/16/sparkling-launches-web-app-bringing-a-full-trading-terminal-and-ai-agent-to-the-browser-2/)
