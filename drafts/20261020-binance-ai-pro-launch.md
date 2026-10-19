---
title: "AI 트레이딩: Binance AI Pro 정식 출시 — 말로 전략을 짜면 ‘전략 캔버스’로 그려 주고 모의매매부터, 실거래는 별도 승인·격리 계좌, 무료 월 25만 크레딧·Premium 19.99 USDC… 백테스트는 아직 없다"
date: 2026-10-20T07:05:00+09:00
category: "AI 트레이딩"
slug: "binance-ai-pro-launch"
summary: "Binance가 10/19 금융 특화 AI 에이전트 Binance AI Pro를 웹·앱에 정식 출시(별도 가입 불필요): 자산·조건·리스크 한도를 평범한 말로 설명하면 빈 곳을 채워 시각 워크플로 ‘Strategy Canvas’로 보여 주고 코드는 자동 생성. 모든 전략은 가상 자금 모의매매로 시험 가능, 실거래는 별도 검토·승인 후 메인 계좌와 분리된 ‘AI Strategy Account’에서만, 자금은 사용자 수동 이체, 외부 출금 불가, 언제든 중지·회수. 현물·USDS-M 선물, 사용자당 전략 10개, 첫 버전엔 백테스트 없음(자동 코드 테스트+모의매매로 대체). 무료 Standard 월 25만 크레딧, Premium 월 19.99 USDC(1,000만 크레딧, ChatGPT Sol·Astra·Claude Opus 등 상위 모델). 지역 제한 적용."
---

## 한줄 요약
10/6·10/14 기사에서 “10월 하순 출시 예정”으로 소개했던 **Binance AI Pro**가 2026-10-19 실제로 나왔다. 말로 설명한 매매 아이디어를 **눈으로 확인할 수 있는 순서도**로 바꾸고, **모의매매 → 사람 승인 → 격리 계좌 실거래** 순서를 강제하는 구조다([Binance 보도자료](https://www.prnewswire.com/news-releases/binance-launches-binance-ai-pro-bringing-conversational-ai-strategy-building-to-users-302912575.html)).

## 어떻게 쓰나
1. 친구에게 설명하듯 말한다: 어떤 코인을, 어떤 조건에서, 어느 정도 손실까지 감수할지.
2. AI Pro가 **빠진 조건을 되묻고** 전략을 다듬은 뒤, 데스크톱에선 채팅 옆에 **Strategy Canvas**(시각 워크플로)로 보여 준다. 각 단계를 눌러 수치를 바꾸거나 블록을 빼고 넣을 수 있다. 모바일은 채팅으로 조정.
3. **모의매매(가상 자금)**로 먼저 돌린다.
4. 실거래는 **별도 검토·승인** 단계를 거쳐야 하고, 메인 계좌와 분리된 **AI Strategy Account**에서만 돈다.
매매 말고도 일일 리포트, 시장 감시, 알림, 시그널 생성 같은 워크플로도 만들 수 있다.

## 안전장치
- 격리 계좌에 돈을 넣을 수 있는 건 **사용자 본인의 수동 이체뿐** — 에이전트가 스스로 자금을 옮길 수 없다.
- 전략 계좌는 **외부 주소로 출금 불가**, 본인 계좌 사이 이체만.
- 전략은 언제든 **중지·수정·회수**.
- 설계 원칙은 Binance 정책팀이 이달 낸 보고서 ‘Know Your Agent’의 **“제한된 자율성”**: 에이전트는 분석·추천하고, 결과가 큰 행동은 반드시 사람의 명시적 승인.

## 요금과 한도
| 항목 | Standard(무료) | Premium |
|---|---|---|
| 가격 | 0 | **월 19.99 USDC**(Binance Pay) |
| 월 크레딧 | 25만 | **1,000만** + 추가 충전 가능 |
| 모델 | 기본 | ChatGPT Sol·ChatGPT Astra·Claude Opus 등(가능 지역) |
- 사용자당 전략 **10개**(모의·실거래·시그널 합산), 대상은 **현물과 USDS-M 선물**. 지역 규제에 따라 이용 범위가 다르다.
- 추가 충전 크레딧은 월 한도를 다 쓴 뒤에 쓰이고 12개월 뒤 소멸.

## 짚어 둘 점: 백테스트가 없다
첫 버전엔 **과거 데이터로 전략을 검증하는 백테스트가 빠졌다**. 대신 자동 코드 테스트와 모의매매를 제공한다. 어제 기사(TradingAgents 0.7.0)에서 본 것처럼 백테스트는 ‘미래 정보 엿보기’ 같은 함정이 많아 제대로 만들기 어렵다. 반대로 말하면, 지금 AI Pro로 만든 전략은 **실제 성과 기록 없이** 모의매매 몇 주의 감각으로 판단해야 한다는 뜻이다.

## 왜 중요한가
이번 주 업계의 기본값이 선명해졌다. IBKR은 승인 없는 자율매매를 초대제로 열었고(10/17), Alpaca·Schwab은 ‘보기만 허용’ 쪽(10/18), Binance는 **‘만드는 건 자유, 돈이 걸린 단계는 사람이’**다. 공통점은 **격리 계좌**다. AI에게 매매를 맡긴다면 ① 잃어도 되는 금액만 격리 계좌에 ② 손실 한도를 전략 안에 명시 ③ 모의매매 기간을 충분히 — 이 세 가지를 먼저 정하자.

출처: [Binance — AI Pro 출시 (PR Newswire, 10/19)](https://www.prnewswire.com/news-releases/binance-launches-binance-ai-pro-bringing-conversational-ai-strategy-building-to-users-302912575.html) · [TradingAgentStack 변경 피드](https://tradingagentstack.com/changes/)
