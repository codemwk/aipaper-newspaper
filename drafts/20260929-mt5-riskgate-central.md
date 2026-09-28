---
title: "AI 트레이딩: MT5 RiskGate — 시그널과 리스크를 분리하는 ‘계정 단위 문지기’"
date: 2026-09-29T07:06:00+09:00
category: "AI 트레이딩"
slug: "mt5-riskgate-central"
summary: "MQL5 Articles(Douglas Rechia). 다중 EA가 계정을 터뜨리는 패턴(USD 중복·상관 페어·EA별 일손실). RiskGate 서비스가 intent→approved/lot/reason. 일손실 2%·심볼당 2포지션·일 6트레이드 예시. AI 에이전트에도 같은 분리 원칙."
---

## 한줄 요약
[MQL5 Articles — RiskGate](https://www.mql5.com/en/articles/21720)는 MetaTrader 5에서 **여러 EA가 같은 계정을 쓸 때** 개별 백테스트로는 안 보이는 포트폴리오 리스크를 지적한다. 해법은 EA를 **시그널 생성기**로 두고, 주문 전 **중앙 RiskGate 서비스**에 intent를 보내 `approved` / `lot` / `reason`을 받는 구조다. AI·MCP 에이전트를 붙일 때도 동일한 **시그널↔리스크 분리**가 핵심이다.

## 무엇이 깨지나
- **USD 중복**: EURUSD·GBPUSD·USDJPY EA가 각자 “풀 사이즈”로 달러 롱 → 계정 단위 환노출 폭발.
- **상관 페어**: 유럽 리스크오프에 EUR·GBP가 같이 무너져 이중 타격.
- **EA별 일손실**: 각 EA 2% 스톱이어도 다섯 개가 따로 먹으면 계정은 6–8% 손실 가능.

## RiskGate가 하는 일
- localhost TCP+JSON. EA는 symbol/side/SL(또는 sl_points)·magic만 보내고, 서비스가 **일손실·심볼 노출·일간 트레이드 수·상관 그룹 로트 절반** 등을 적용.
- 예시 규칙(글 속 prop 스타일): 일손실 **2%**, 트레이드당 리스크 **0.5%**, 심볼당 오픈 **2**, 일 **6** 트레이드, 서비스 다운 시 **전부 거부(fail-closed)**.
- 핸들러는 인터페이스 주입으로 **단위 테스트** 가능 — Strategy Tester가 서비스를 못 돌리는 한계를 우회.

## 왜 중요한가
어제 다룬 “권한 삼각형”이 **누가 주문할 수 있나**라면, RiskGate는 **계정이 감당할 수 있나**다. LLM이 시그널을 내더라도 **마지막 문지기는 결정론적 리스크 엔진**이어야 한다.

## 기억할 것
- [RiskGate 기사](https://www.mql5.com/en/articles/21720) · 키워드: intent / approved·lot·reason / fail-closed
