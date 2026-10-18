---
title: "AI 트레이딩: TradingAgents 0.7.0(~11.2만★) — ‘AI 투자위원회’를 ChatGPT 구독으로 돌린다, 그리고 ‘미래 뉴스를 보고 채점하던’ 백테스트 버그를 고쳤다"
date: 2026-10-19T07:10:00+09:00
category: "AI 트레이딩"
slug: "tradingagents-070-chatgpt-plan"
summary: "Tauric Research TradingAgents v0.7.0(10/16, Apache-2.0, ~11.2만★): 애널리스트·리서처·트레이더·리스크·포트폴리오 매니저 역할의 LLM 에이전트가 토론해 매매 결정을 내는 오픈소스 프레임워크(연구·모의 매매용). ① chatgpt 제공자 추가 — API 키 대신 ChatGPT Plus/Pro 구독으로 실행(OpenAI의 오픈소스 앱용 로그인, tradingagents login chatgpt). ② 룩어헤드 수정 — d일 실행은 d일 장 마감 후 뉴스를 읽으므로, 결정은 d일 종가가 아닌 ‘다음 첫 종가’로 채점. 기존 기록과 섞이니 새 run으로 비교 권장. ③ 하루 1회 새 버전 안내(끌 수 있음), 릴리스마다 wheel 첨부. 0.6.0(10/3)은 HTML 보고서·티어별 제공자·암호화폐 Reddit 감성 추가."
---

## 한줄 요약
여러 AI 에이전트가 **투자위원회처럼 토론해** 매수·매도를 정하는 오픈소스 **TradingAgents**가 2026-10-16 **v0.7.0**을 냈다. 9월에 이 프레임워크를 소개했는데, 이번 업데이트에는 개인 사용자에게 바로 와닿는 변화 두 가지가 있다 — **비용**과 **백테스트의 정직성**([릴리스 노트](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.7.0)).

## TradingAgents 복습 (코드 없이)
펀더멘털·감성·뉴스·기술적 분석을 맡은 **애널리스트 에이전트**들이 보고서를 쓰면, 강세·약세 **리서처**가 토론하고, **트레이더**가 안을 내고, **리스크 관리**와 **포트폴리오 매니저**가 최종 결정을 내린다. GitHub 별 약 11.2만 개, Apache-2.0. TradingAgentStack은 이를 **연구·모의 매매 전용**으로 분류한다([TradingAgentStack](https://tradingagentstack.com/changes/)).

## 바뀐 점 ① — API 키 대신 ChatGPT 구독으로
새 **chatgpt 제공자**를 고르면 API 키 없이 **ChatGPT Plus 또는 Pro 플랜**으로 돌아간다. OpenAI가 오픈소스 앱용으로 제공하는 로그인을 쓰며, CLI 메뉴에서 ‘Subscription’을 고르거나 `tradingagents login chatgpt`로 한 번 로그인하면 Docker·예약 실행에서도 된다. 로그아웃하면 권한이 회수된다. 토큰 단위로 과금되는 API에 비해 **매일 돌리는 분석 루틴의 비용 예측**이 쉬워진다(구독 사용 한도는 적용).

## 바뀐 점 ② — ‘미래를 보고 채점’하던 버그 수정
가장 중요한 수정이다. 예전에는 **d일**에 실행한 결정이 **d일 장 마감 후에 나온 뉴스**까지 읽고도, 성과는 **d일 종가**로 채점됐다. 즉 시장이 이미 닫힌 뒤의 정보로 그날 종가에 산 것처럼 계산된 것 — 백테스트 수익률을 부풀리는 전형적인 **룩어헤드(look-ahead) 편향**이다. 0.7.0부터는 결정이 **d일 이후 첫 종가**에 진입한 것으로 채점된다(#1518). 이 프로젝트는 0.4.0(8월)·0.5.2(9월)에도 데이터 시점 관련 수정을 냈는데, 이번엔 ‘채점 시점’까지 맞춘 셈이다.
- 주의: 이미 메모리 로그에 정산된 예전 결정은 옛 방식 그대로 남는다. 같은 run을 이어 돌리면 두 방식이 섞이므로 **새 run을 시작해 비교**하라고 릴리스 노트가 권한다.

## 그 밖에
- 대화형 CLI가 **하루 한 번** 새 버전을 알려 준다(백그라운드라 실행을 늦추지 않음, `TRADINGAGENTS_NO_UPDATE_CHECK=1`로 끔). 터미널 없는 예약 실행은 확인하지 않는다.
- 릴리스마다 wheel 파일이 붙어 `pip install`로 바로 설치.
- 직전 0.6.0(10/3)은 한 페이지 **HTML 보고서**, 빠른/깊은 모델 티어별로 다른 제공자(예: 매니저는 Claude, 애널리스트는 OpenAI), 암호화폐 종목은 r/CryptoCurrency 등 전용 서브레딧 감성 분석을 더했다.

## 왜 중요한가
AI 트레이딩 실험에서 가장 흔한 착각은 **“백테스트가 좋았다”**다. 이번 수정은 유명 프로젝트조차 정보 시점을 잘못 맞출 수 있음을 보여 준다. 직접 전략을 시험한다면 세 가지를 확인하자: ① 결정 시점에 **실제로 알 수 있던 정보만** 썼나 ② 진입 가격이 **결정 이후의 가격**인가 ③ 비교할 때 **같은 규칙으로 처음부터** 다시 돌렸나. 그리고 이 도구는 어디까지나 연구용 — 실계좌 연결은 별개의 문제다.

출처: [GitHub — TradingAgents v0.7.0 릴리스 (10/16)](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.7.0) · [GitHub TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) · [TradingAgentStack 변경 피드 (10/18)](https://tradingagentstack.com/changes/)
