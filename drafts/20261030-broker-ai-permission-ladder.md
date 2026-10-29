---
title: "AI 트레이딩: 같은 주에 갈린 두 답 — B2TRADER는 ‘전체 권한 에이전트는 주문마다 확인 없이 실행’, eToro는 ‘모든 행동마다 승인’"
date: 2026-10-30T07:06:00+09:00
category: "AI 트레이딩"
slug: "broker-ai-permission-ladder"
summary: "10/29 B2BROKER가 B2TRADER에 MCP 연결과 터미널 내 AI 채팅을 정식 추가했다. 브로커가 권한을 ‘읽기 전용/전체’로 정하고, 전체 권한 외부 에이전트는 허용된 거래를 주문별 확인 없이 실행할 수 있다(터미널 내 채팅은 매번 확인). 같은 날 eToro는 Claude·Grok·ChatGPT용 Connector를 출시했는데, 모든 행동 전에 승인을 받고 입금·출금은 불가. 지난주 IBKR은 주문별 승인 없는 자율 주문을 허용했다."
---

## 한줄 요약
AI가 내 계좌에서 주문을 낼 수 있게 되는 건 이제 기정사실이다. 남은 질문은 **“누가, 어디까지 허락하나”**다. 같은 날 나온 두 발표가 이 질문에 정반대로 답했다.

## B2TRADER: 브로커가 문을 정하고, 열린 문 안에서는 자동
- B2BROKER의 트레이딩 플랫폼 B2TRADER에 **MCP 지원 + 터미널 내 AI 채팅**이 붙었다. Claude·ChatGPT나 직접 만든 에이전트를 계좌에 연결해 시세·포트폴리오·거래 내역을 보고, “수익 난 포지션 정리”, “손절 주문 걸기” 같은 지시를 수행한다([Finance Magnates](https://www.financemagnates.com/forex/b2trader-adds-chatgpt-and-claude-for-ai-trade-execution-but-brokers-set-the-limits/)).
- **권한은 브로커가 정한다**: 읽기 전용(분석·모니터링만) / 전체(주문·수정·청산). 브로커는 MCP를 아예 끌 수도 있고, 에이전트는 허락한 본인 계좌에만 접근한다.
- 차이점 하나: **터미널 안 채팅이 제안한 주문은 매번 확인**을 받지만, **전체 권한을 받은 외부 에이전트는 허용 범위 안에서 주문마다 확인 없이 실행**한다.
- CEO Arthur Azizov: “터미널에 AI를 넣으면 바로 이 질문이 생긴다 — 이 비서가 실제로 뭘 할 수 있는지 누가 정하나?”

## eToro Connector: 매번 묻는다, 돈은 못 옮긴다
- 10/29 출시. Claude·Grok·ChatGPT를 eToro 포트폴리오에 연결해 보유 종목을 묻고, 대화 안에서 행동을 승인한다([TradeInformer](https://tradeinformer.com/tech-news/etoro-launches-ai-portfolio-connectors)).
- **보기만 / 행동까지** 중 사용자가 고르고 언제든 바꾼다. **모든 행동 전에 승인**, 연결 해제 즉시 접근 종료.
- **입금·송금은 AI가 할 수 없다.** 미국·호주·싱가포르 고객은 제외, Claude Desktop은 당분간 읽기 전용.

## 권한 사다리 한눈에
| 단계 | 사례 |
|---|---|
| 읽기 전용 | CMC Markets(영국 CFD·ChatGPT), Kraken ChatGPT 앱 |
| 주문 준비 → 사람이 확정 | Leverate MCP, eToro Connector(행동마다 승인) |
| 허용 범위 내 자율 실행 | B2TRADER 전체 권한 외부 에이전트, IBKR 자율 주문(지난주) |

## 왜 중요한가
- 지난번 저장하신 **MT5 + MCP 안전장치** 기사들과 이어지는 소식이다. 개인 자동매매를 짤 때도 이 사다리를 그대로 쓰면 된다: **처음엔 읽기 전용 → 주문 준비까지만 → 손실 한도·종목 제한을 건 뒤에야 자율 실행**.
- “확인 없이 실행”은 편하지만, 프롬프트 한 줄 오해가 바로 체결로 이어진다. 브로커가 아니라 **내가 먼저 한도를 정해 두는 쪽**이 안전하다.
