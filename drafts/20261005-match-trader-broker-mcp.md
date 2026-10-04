---
title: "AI 트레이딩: Match-Trader Broker Management MCP — 브로커·프롭펌 ‘딜링 데스크’가 Claude·ChatGPT로 라이브 리스크를 묻는다"
date: 2026-10-05T07:02:00+09:00
category: "AI 트레이딩"
slug: "match-trader-broker-mcp"
summary: "10/1 Match-Trade Technologies 발표(스폰서 보도자료). Manager·Admin 데이터에 20+ 정의된 액션(계좌·포지션·원장·그룹·종목설정·리스크 룰). Full Server License 보유사 한정. 고객용이 아니라 브로커 내부 팀용 MCP."
---

## 한줄 요약
FX·프롭 트레이딩 플랫폼 [Match-Trader](https://financefeeds.com/match-trader-broker-management-mcp/)가 **Broker Management MCP**를 냈다. 트레이더(고객)가 아니라 **브로커·프롭펌 내부 팀**이 Manager·Admin 콘솔 데이터를 Claude·ChatGPT 등 MCP 클라이언트로 자연어 질의하는 서버다. 예: “XAUUSD 그룹별 순노출을 보여 주고, 마진 레벨 150% 미만 계좌 중 평가손익 상위 10개를 뽑아 줘.” 원래라면 화면 여러 개 → CSV 내보내기 → 스프레드시트 병합 → 개발팀 쿼리 요청이던 일이 한 번의 질문이 된다.

## 무엇을 노출하나
- 1차 릴리스 **20개 이상 액션**: 계좌, 포지션·주문, 원장(입출금·크레딧), 그룹·종목 설정, 시장 데이터, 거래 세션, 리스크 룰.
- 각 액션은 **사전 정의된 단일 작업** — 어시스턴트는 브로커가 이미 설정한 권한 안에서만 움직인다. 어떤 AI 클라이언트를 쓸지는 브로커가 고른다.
- 팀별 예시: 딜링·리스크(노출, 헤징·라우팅 룰, 어뷰즈 룰 커버리지), 백오피스(계좌 30일 입출금 요약), 프롭(Phase 1 vs Funded 그룹 레버리지·수수료 비교), 컴플라이언스(EURUSD 설정 비교, 휴장 일정).
- 대상: **Match-Trader Full Server License** 보유 브로커·프롭펌만.

## 같은 날 나온 다올과 비교
다올 MCP Trading이 **개인 고객 + 주문 실행(승인형)**이라면, Match-Trader는 **사업자 내부 + 데이터 질의 중심**이다. 보도자료는 CMC Markets의 영국 CFD 고객용 ChatGPT 연결이 **잔고·포지션·가격 조회만 되고 주문·자금 이동은 불가**하다는 점, Trading Central MCP가 리서치만 공급한다는 점도 함께 짚는다. MCP가 트레이딩 업계에 들어오는 경로가 ‘조회 전용 → 승인형 주문 → 내부 운영’으로 층이 갈리고 있다.

## 왜 중요한가
MT5 AI Assistant가 **트레이더의 손**을 늘리는 쪽이라면, 이건 **브로커의 눈**을 늘린다. 프롭펌 리스크 데스크가 에이전트로 실시간 노출을 감시하게 되면, 개인 트레이더 입장에선 ‘상대편’의 대응 속도도 빨라진다는 뜻이다.

## 기억할 것
- FinanceFeeds 게재분은 **스폰서 보도자료**(매체 검증 없음) — 회사 주장으로 읽을 것.
- [FinanceFeeds 10/1](https://financefeeds.com/match-trader-broker-management-mcp/) · [Finance Magnates](https://www.financemagnates.com/forex/brokers-and-prop-firms-get-management-mcp-from-match-trader/)
