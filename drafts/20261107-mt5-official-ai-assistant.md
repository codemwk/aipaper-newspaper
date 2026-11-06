---
title: "AI 트레이딩: MetaTrader 5 — 공식 AI Assistant + MCP로 시세·테스터·주문까지, 권한은 사용자가 잠근다"
date: 2026-11-07T07:05:00+09:00
category: "AI 트레이딩"
slug: "mt5-official-ai-assistant"
summary: "MetaQuotes가 MT5에 MCP 기반 공식 AI Assistant를 설명했다. MQL5 계정만으로 시세·포지션·차트·Strategy Tester·주문에 에이전트가 접근한다. 브로커별 MCP(Axi 등)와 달리 터미널 레이어다. 민감 작업 권한은 사용자가 제어하고, 결과는 조언이 아니다."
---

## 한줄 요약
지난 [11/6] Axi가 Claude↔MT5 **브로커 MCP**를 열었다면, MetaQuotes는 **터미널 자체**에 AI를 심었다. 최신 MT5 + MQL5.community 로그인만으로 무료 **AI Assistant**가 MCP로 플랫폼 데이터·기능에 붙는다([MetaTrader 뉴스 10/20](https://www.metatrader.com/en/news/metaquotes/4506407-ai-in-metatrader-5-from-market-analysis-to-trading)).

## 할 수 있는 일 (문서 기준)
- **포지션·히스토리**: 심볼·방향·요일·보유시간별 손익 분해, 달러 1% 강세 시나리오 같은 노출 질문.
- **시장·차트**: 틱/바/볼륨, Market Watch 스캔, 템플릿 적용·워치리스트 정리.
- **매매**: 조건에 맞는 심볼 선별 후 주문·SL/TP(변동성·R:R 기준) — **권한 켠 경우만**.
- **Strategy Tester**: 다수 심볼·기간 테스트·최적화 기준(예: 드로다운 우선)을 에이전트가 조율.

## 브로커 MCP와 다른 점
Axi·PrimeXBT 등은 **계좌·주문 경로가 브로커 클라우드**다. MT5 공식 Assistant는 **로컬/터미널 MCP**로 분석·테스터·UI까지 넓다. 둘을 같이 쓰면 권한이 겹치니, 읽기 전용·주문 허용을 **한곳만** 켜는 편이 안전하다. 지난번 저장하신 MT5 MCP 안전 레이어 관심과 바로 이어진다.

## 주의
공식 문구: AI 결과는 오류·불완전할 수 있고 **금융·투자 조언이 아니다**. 실행 전 반드시 사람이 검증. 웹 접근을 켜면 뉴스·매크로를 붙이지만 환각 위험이 커진다.
