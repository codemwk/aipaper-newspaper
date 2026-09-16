---
title: "MT5 Build 6180 — AI가 Strategy Tester 리포트·최적화를 직접 돌리는 QA 모드"
date: 2026-09-17T07:05:00+09:00
category: "AI Trading"
slug: "mt5-build-6180-strategy-tester-ai"
summary: "2026-09-03. MetaTrader 5 Build 6180. MCP 연결 AI가 테스터 리포트·로그 회수, 최적화 실행, 차트 인디케이터 추가까지. 라이브 판단 체결은 아직 없음. cTrader·eToro와 대비되는 ‘연구형’ 노선."
---

## 한줄 요약
[Finance Magnates](https://www.financemagnates.com/forex/metatrader-5-ai-assistant-becomes-a-qa-engineer-for-trading-bots/)·[공식 릴리즈](https://www.metatrader5.com/en/releasenotes/terminal/2464)에 따르면, MetaQuotes는 **2026-09-03** MT5 **Build 6180**에서 AI Assistant·외부 MCP 에이전트의 Strategy Tester 권한을 크게 넓혔다. 봇 QA·최적화 쪽이다.

## 무엇이 바뀌었나
- 에이전트가 **테스터 리포트·최적화 결과**를 직접 가져가 분석할 수 있다.
- **최적화 실행·기준 설정**, 현재 테스터 설정 확인, **테스터·터미널·EA 로그** 조회가 추가됐다.
- 차트에 이동평균 등 인디케이터를 프롬프트로 붙이는 식의 워크스페이스 조작도 확장.
- Build **6060**(2026-07-23)에서 연 MCP·에이전틱 기반 위의 “연구 루프” 강화. 기사 기준, **라이브 계좌에서 판단·주문**은 여전히 미제공.
- MetaQuotes가 밝힌 사용량(8월 공개): MCP 도입 직후 약 3주간 AI Assistant **1조+ 토큰** 처리.

## 왜 중요한가
어제 다룬 ProreX MCP는 “브로커 리서치+수동 컨펌”이었다. 오늘은 **플랫폼 본체**가 테스터를 AI QA 스테이션으로 여는 단계. cTrader·eToro가 에이전트 체결을 더 열어두는 것과 달리, MT5는 당분간 **백테스트·디버그·최적화**에 힘을 싣는 보수적 갈래다. 자동매매 빌더는 “체결 MCP” 전에 “리포트 MCP”부터 검증할 수 있다.

## 기억할 것
- 릴리즈: [MT5 Build 6180](https://www.metatrader5.com/en/releasenotes/terminal/2464) · [MetaQuotes 뉴스](https://www.metaquotes.net/en/metatrader5/news/5555)
- 해설: [Finance Magnates](https://www.financemagnates.com/forex/metatrader-5-ai-assistant-becomes-a-qa-engineer-for-trading-bots/)
