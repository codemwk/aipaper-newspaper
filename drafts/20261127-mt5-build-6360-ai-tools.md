---
title: "AI 트레이딩: MT5 베타 빌드 6360 — AI 어시스턴트에 MCP 도구 40여 개 추가. 호가창 읽기, ‘보내지 않고’ 주문 미리 검사, 알림·뉴스·서비스 관리까지"
date: 2026-11-27T07:10:00+09:00
category: "AI 트레이딩"
slug: "mt5-build-6360-ai-tools"
summary: "MetaQuotes가 11/26(목) MetaTrader 5 베타 빌드 6360을 내놓으며 AI 어시스턴트가 쓰는 MCP 도구를 40개 넘게 늘렸다. MQL5 서비스 시작·중지, 차트·템플릿·그래픽 객체 조작, 호가창(시장 깊이) 구독, 실제 주문을 보내지 않는 증거금·손익 계산과 주문 사전 검사, 알림 생성·수정, 금융 뉴스 읽기 등이다. AI 기능은 MQL5.community 계정으로 로그인하면 무료 MQL5 Lite 요금제로 쓸 수 있다."
---

## 한줄 요약
11/24 기사에서 “MT5 안에 이미 AI용 문(MCP)이 있다”고 썼다. 이틀 뒤 MetaQuotes가 그 문으로 할 수 있는 일을 **40개 넘게 더 늘린 베타**를 공식화했다([FX News Group, 11/26](https://fxnewsgroup.com/forex-news/platforms/mt5-beta-build-6360-comes-equipped-with-over-40-new-ai-tools/)).

## 새로 생긴 것 (회사 릴리스 노트 기준)
- **MQL5 서비스 관리:** 등록된 서비스 목록·상태 확인, 시작·중지, 새 인스턴스 등록·삭제, 입력값 읽기.
- **차트·템플릿·프로필:** 심볼·타임프레임 변경, 화면 설정, 과거로 이동, 스냅샷, 템플릿 저장·삭제, 차트 프로필 생성·전환.
- **그래픽 객체:** 추세선·레벨 같은 객체를 만들고 속성을 바꾸고 지운다 — 분석선을 AI가 직접 그리는 일.
- **호가창(시장 깊이):** 구독해서 현재 매수·매도 호가와 물량을 읽는다.
- **주문 사전 검사·증거금 계산:** 필요 증거금, 예상 손익, 시장가·지정가 주문이 자금·한도에 맞는지 **실제 주문을 보내지 않고** 검사.
- **알림:** 가격·시간 알림 생성·조회·수정·켜기/끄기·삭제.
- **터미널 정보·금융 뉴스:** 서버 연결·리소스 상태, 뉴스 목록과 본문 읽기.
- **테스트 결과 창:** 열린 백테스트·최적화 결과 창 정보를 읽고 닫기 — 전략을 연달아 시험할 때 편해진다.
- AI 기능은 **MQL5.community 계정 로그인** 후 사용, 모든 사용자에게 **무료 MQL5 Lite 요금제**가 자동 제공된다.

## 왜 중요한가
- 방향이 분명하다. AI가 “차트를 열고 → 레벨을 그리고 → 주문 조건을 미리 검사하고 → 알림을 거는” **여러 단계 작업**을 터미널 안에서 끝내게 하려는 것. 수동 매매 보조로는 쓸모가 커진다.
- 동시에 **AI가 만질 수 있는 범위가 넓어졌다**는 뜻이기도 하다. 11/24 기사에서 본 것처럼 시험 터미널에선 ‘MCP 거래 허용’이 기본으로 켜져 있었다. 프롭 계정(FTMO 등)에서는 **AI 어시스턴트 설정의 Trading을 ‘확인 요청’ 또는 ‘거래 안 함’으로**, ‘위험한 셸 작업’은 꺼 두는 원칙을 그대로 유지하자([MT5 도움말: MCP 설정](https://www.metatrader5.com/en/terminal/help/mcp_and_ai/configuration)).
- 새 ‘서비스 시작·중지’ 도구는 상시 돌아가는 자동매매 서비스를 AI가 켜고 끌 수 있다는 의미다. 자동매매 시스템을 MT5 서비스로 돌리고 있다면 **권한 범위부터 점검**할 것.
- 주의: 베타 빌드이고, 기능 설명은 MetaQuotes 발표 기준이다.

출처: [FX News Group — MT5 beta build 6360](https://fxnewsgroup.com/forex-news/platforms/mt5-beta-build-6360-comes-equipped-with-over-40-new-ai-tools/) · [MetaTrader 5 도움말: MCP and AI 설정](https://www.metatrader5.com/en/terminal/help/mcp_and_ai/configuration) · [Kairotick MT5 MCP 실측(11/23)](https://kairotick.com/ai/mt5-mcp/)
