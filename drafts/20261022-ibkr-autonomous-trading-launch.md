---
title: "AI 트레이딩: IBKR ‘자율 매매’ 정식 발표 — AI는 별도 칸(AI Partition)에서만, 자기자본 10%·최대 2만 5천 달러, ‘승인 매매 10건’을 먼저 거쳐야 열린다"
date: 2026-10-22T07:04:00+09:00
category: "AI 트레이딩"
slug: "ibkr-autonomous-trading-launch"
summary: "Interactive Brokers가 10/21 ‘IBKR Autonomous Trading’ 공식 발표(BusinessWire): 자격 고객이 MCP로 연결한 AI(ChatGPT·Claude·Grok·Perplexity·Claude Code 등)에게 7만 5천여 종 주식·옵션·ETF 감시와 주문 제출을 건별 승인 없이 위임. 단 별도 ‘AI Partition’ 안에서만 — 주계좌에서 이체해 운용, 자기자본의 최대 10%, 최소 $1,000, 모든 파티션 합계 최대 $25,000. 허용: 주식·ETF·상장 주식/ETF/지수 옵션, 시장가·지정가·스톱·스톱지정가, Day/Overnight. 금지: 페니주식, 복잡한 레버리지 상품, 소수점 주식, 공매도, 증거금 필요한 옵션 전략. 자격: ‘검토·승인’ 모드로 2주간 $100 이상 거래 10건 이상(향후 자격 시험으로 대체 예정). 클라이언트 포털 ‘킬 스위치’로 즉시 해제. 주문 빈도·최대 주문 크기 제한은 예고."
---

## 한줄 요약
10/15 실적 발표에서 ‘제한 출시’로 예고됐던 IBKR의 AI 자율 매매가 10/21 **정식 이름과 규칙**을 달고 나왔다. 핵심은 “AI에게 계좌 전체가 아니라 **작은 별도 칸**만 준다”는 설계다([BusinessWire](https://www.businesswire.com/news/home/20261021902894/en/Interactive-Brokers-Introduces-Autonomous-Trading), [IBKR Traders’ Insight](https://www.interactivebrokers.com/campus/traders-insight/ibkr-toolbox/traders-toolbox-ai-order-placement-is-here/)).

## 무엇이 달라졌나
기존 **AI Integration**은 AI가 ‘주문 지시서’만 쓰고 사람이 건마다 승인해 제출하는 방식이었다. **Autonomous Trading**은 고객이 정한 조건을 만족하면 연결된 AI가 **건별 승인 없이 주문을 제출**한다. 연결은 IBKR 공개 **MCP 서버** — MCP를 지원하는 어떤 AI든(Claude Desktop·Claude Code·ChatGPT 등) 엔드포인트만 넣으면 된다.

IBKR이 든 지시 예시:
- “오전 9:45, 30일 내재변동성이 전일 대비 3포인트 넘게 바뀐 종목을 크기순으로 표시해.”
- “매일 아침, 포트폴리오의 10%를 넘는 종목은 8%로 줄여.”
- “보유 종목의 내재변동성이 52주 90퍼센타일에 닿으면 30일 커버드콜을 팔아.”

## 안전장치 — 숫자로
| 항목 | 규칙 |
|---|---|
| 자금 | 주계좌에서 이체한 **AI Partition** 안에서만. 자기자본의 **최대 10%**, 평생 최소 **$1,000**, 모든 파티션 합계 **최대 $25,000** |
| 상품 | 주식·ETF·상장 주식/ETF/지수 옵션 |
| 주문 | 시장가·지정가·스톱·스톱지정가 / Day·Overnight·Overnight+Day |
| 금지 | 페니주식, 복잡한 레버리지 상품, 소수점 주식, **공매도**, 증거금 차입이 필요한 옵션 전략 |
| 자격 | ‘검토·승인’ 모드에서 **2주간 $100 이상 거래 10건 이상** 직접 승인(향후 자격 시험으로 대체 예정) + 계좌 유형·법인·국가 요건 |
| 중단 | 클라이언트 포털의 **킬 스위치**로 즉시 연결 해제 |
| 예고 | 주문 빈도 제한, 최대 주문 크기, 최소 계좌 잔고 기준 등 사용자 정의 가드레일 |

예: 자산 $2,000 계좌는 $1,000까지, 수백만 달러 계좌도 $25,000에서 멈춘다.

## 왜 중요한가
지난주 정리했던 업계 지형(Schwab·JPMorgan은 외부 에이전트 차단, Alpaca는 실계좌 읽기 전용, Binance는 분리된 ‘AI 전략 계좌’)에서 IBKR이 **가장 멀리 간 대형 증권사**가 됐다. 그러면서도 답은 같다: **분리된 계좌 + 상한 + 금지 목록 + 킬 스위치 + 사람 승인 이력**.
MT5·MCP로 자동매매를 실험하는 독자라면 이 표를 **자기 봇의 체크리스트**로 써도 된다 — 봇 전용 계좌, 자기자본 대비 상한, 공매도·레버리지 금지, 처음엔 ‘승인 모드’로 10건 이상 검증, 한 번에 끊는 스위치. 자율 매매의 손실은 여전히 고객 몫이라는 점(IBKR의 위험 고지)도 잊지 말 것.

출처: [BusinessWire — Interactive Brokers Introduces Autonomous Trading (10/21)](https://www.businesswire.com/news/home/20261021902894/en/Interactive-Brokers-Introduces-Autonomous-Trading) · [IBKR Traders’ Insight — AI Order Placement Is Here (10/21)](https://www.interactivebrokers.com/campus/traders-insight/ibkr-toolbox/traders-toolbox-ai-order-placement-is-here/)
