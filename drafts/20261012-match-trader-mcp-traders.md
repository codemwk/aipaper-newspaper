---
title: "AI 트레이딩: Match-Trader ‘트레이더용 MCP’ — 브로커 데스크용에 이어, 개인 계좌 조회·주문(승인형)까지"
date: 2026-10-12T07:07:00+09:00
category: "AI 트레이딩"
slug: "match-trader-mcp-traders"
summary: "10/5 Finance Magnates: Match-Trade가 브로커 Manager MCP에 이어 Match-Trader MCP for Traders를 출시. 포지션·스왑·노출·이력 자연어 조회, 주문 생성·수정·취소는 클라이언트가 승인 UI를 띄울 수 있음. 토큰 권한·레이트 리밋·투자자문 아님 고지."
---

## 한줄 요약
10/5 AiPaper가 다룬 것은 **브로커·프롭펌 내부**용 Broker Management MCP였다. 같은 시기 Match-Trade는 **개인/트레이더 계좌**를 Claude·ChatGPT·Cursor·VS Code에 붙이는 [MCP for Traders](https://www.financemagnates.com/forex/match-trade-adds-retail-traders-to-mcp-after-brokers-and-prop-firms/)를 냈다. **조회 + (승인형) 주문**이 한 서버에 있다.

## 어떻게 동작하나
- **읽기**: 오픈 포지션, 스왑 비용, 포트폴리오 노출, 대기 주문, 거래 이력. 손실 패턴·손절 없는 포지션 찾기 같은 질의 예시가 보도에 등장.
- **쓰기**: 포지션 오픈·수정·클로즈, 대기 주문 생성·수정·취소. 호환 클라이언트는 **파라미터를 보여 주고 트레이더 승인 후** 실행할 수 있다고 한다.
- **통제**: Match-Trader API 경유, 읽기/거래 기능 분리, **계좌 단위 토큰**, 기능별 권한 제한·철회, 토큰·유저 레이트 리밋, API 액션이 **거래 이력에 남음**.
- **고지**: 투자 조언 아님, 승인 주문 책임은 트레이더.

## 같은 주의 다른 MCP와 비교
- **브로커 MCP**(10/1·10/5 보도): Full Server License 사업자, Manager/Admin, 주로 **운영 데이터**.
- **트레이더 MCP**: 고객 계좌, **주문 경로 포함**.
- **Axi MT5↔Claude**(10/8): 브로커별 MT5 권한 모델. Match-Trader는 **자사 멀티에셋 스택** 안의 원격 MCP.

## 왜 중요한가
리테일 FX·CFD에서 MCP가 “차트 설명해 줘”를 넘어 **계좌 행위 계층**으로 내려왔다. 실무 체크리스트는 (1) 토큰을 읽기 전용으로 쪼갤 수 있는지 (2) 승인 UI가 클라이언트 기본값인지 (3) 레이트 리밋·감사 로그가 분쟁 시 증거로 쓰이는지다.

출처: [Finance Magnates — MCP for Traders](https://www.financemagnates.com/forex/match-trade-adds-retail-traders-to-mcp-after-brokers-and-prop-firms/) · 브로커편: [Match-Trader Broker MCP](https://match-trader.com/match-trader-brings-ai-assistants-directly-to-broker-data-via-model-context-protocol/)
