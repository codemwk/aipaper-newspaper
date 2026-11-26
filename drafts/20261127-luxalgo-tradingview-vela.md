---
title: "AI 트레이딩: TradingView 최대 지표 제작사 LuxAlgo의 스크립트 409개가 검색에서 사라졌다 — LuxAlgo는 ‘Pine Script를 그대로 돌리는’ 자체 차트 Vela와 백테스트 에이전트로 맞불"
date: 2026-11-27T07:05:00+09:00
category: "AI 트레이딩"
slug: "luxalgo-tradingview-vela"
summary: "11/25 LuxAlgo는 TradingView 커뮤니티 스크립트 검색에서 자사 지표 409개가 전부 빠졌다고 밝혔다(삭제는 아님). 좋아요 18만 4천 개의 Smart Money Concepts도 포함. TradingView는 이 건에 대해 공식 설명을 내지 않았다. 같은 주 LuxAlgo는 자체 차트 Vela를 모바일로 내고, Pine Script를 1:1로 실행하는 PineTS, 몇 시간씩 혼자 백테스트하는 코딩 에이전트 Quant 2.0, cTrader 브로커 실거래 연결을 밀고 있다."
---

## 한줄 요약
지표를 **어느 플랫폼에 두느냐**가 갑자기 리스크가 됐다. TradingView 안에서만 사는 Pine 지표는, 플랫폼이 노출을 끄면 **사라진 것과 비슷해진다**([LuxAlgo X, 11/25](https://x.com/LuxAlgo)).

## 무슨 일이 있었나
- LuxAlgo(팔로워 150만 — TradingView 공식 계정 81만 3천보다 많다고 회사 주장)는 11/25 **“TradingView가 1위 퍼블리셔를 숨겼다”**고 게시했다. 지표 **409개가 커뮤니티 스크립트 검색에서 빠졌고**, 삭제는 아니라고 했다.
- 대표 지표 **Smart Money Concepts**는 좋아요 18만 4천 개로 플랫폼 1위였다.
- **TradingView는 이 건에 대해 공식 입장을 내지 않았다.** 다만 규정상 공개 스크립트는 *Suggested(검색·피드 노출)*, *Unsuggested(프로필에서만 보임, 검색 불가)*, *Hidden(작성자·모더레이터만)* 세 상태가 있고, 품질·규정 위반 정도에 따라 모더레이터가 바꿀 수 있다([TradingView 스크립트 게시 규정](https://www.tradingview.com/support/solutions/43000590599-script-publishing-rules/)). 이번 증상은 ‘Unsuggested’와 같은 모양이다.
- 배경: LuxAlgo는 11월 내내 자체 차트 **Vela**를 “TradingView를 넘는 차트”로 홍보해 왔다. 무료 사용자 알림 3개 제한, 그리기 도구 유료화 같은 TradingView 정책을 직접 비교하는 게시물도 많았다.

## LuxAlgo가 내민 대안: Vela
- **PineTS:** Pine Script를 **TradingView 밖에서 1:1로 실행**하는 엔진. 지표를 붙여 넣으면 다시 짜지 않고 돈다고 주장. Vela 코어와 스크립트 엔진은 오픈소스로 공개(주 3만 6천 다운로드, 회사 발표).
- **Quant 2.0 + Backtest Loop(11/16):** “BTC 4시간봉, 수익 팩터 1.5 이상, 승률 40% 이상, 낙폭 30% 미만, 거래 100회 이상”처럼 조건을 주면, 에이전트가 **최대 4시간** 동안 전략 수백 개를 시험하고 **처음 보는 데이터에서도 버틴 것만** 남긴다고 설명.
- **알림을 말로:** “이런 셋업이 나오면 알려 줘”라고 쓰면 Quant가 차트를 지켜보다 알려 주고 무엇을 봤는지 설명.
- **실거래(11/25):** 차트에서 바로 주문. Pepperstone·IC Markets·FP Markets·FxPro·Fusion Markets 등 **cTrader 브로커**, tastytrade, Hyperliquid, 일부 거래소 연결. 11/24 iOS·Android 앱 출시.

## 왜 중요한가
- 지난번 저장하신 **TradingView MCP·MT5 MCP 기사와 이어지는 소식**이다. 개인 지표(예: 직접 만든 오실레이터·클라우드)와 유료 지표를 TradingView에 두고 자동화를 붙이는 구조라면, **원본 Pine 코드를 로컬·Git에 따로 보관**하고, 핵심 신호는 웹훅/MT5 쪽에서도 재현 가능하게 해 두는 것이 이번 사건의 실전 교훈이다.
- ‘몇 시간씩 혼자 백테스트하는 에이전트’는 과최적화 위험이 크다. “처음 보는 데이터에서 버틴 것만”이라는 설명이 있어도 **검증 구간·수수료·슬리피지 가정을 직접 확인**해야 한다.
- 주의: 노출 제외 사유는 확인되지 않았고, 사용자 이동 규모(“며칠 새 수만 명”)·PineTS 1:1 호환은 LuxAlgo 주장이다. 경쟁 플랫폼을 홍보하는 당사자의 발언이라는 점도 감안해야 한다.

출처: [LuxAlgo X 계정 게시물(11/24~25)](https://x.com/LuxAlgo) · [TradingView 스크립트 게시 규정](https://www.tradingview.com/support/solutions/43000590599-script-publishing-rules/) · [Vela](https://vela.luxalgo.com/chart)
