---
title: "AI 트레이딩: 증권 계좌가 챗봇 안으로 — LS증권 ‘LS Connector’(MCP) 시범 서비스, MT5 브로커 NordFX는 ChatGPT·Claude 연결을 ‘읽기 전용부터’"
date: 2026-11-25T07:05:00+09:00
category: "AI 트레이딩"
slug: "broker-mcp-ls-nordfx"
summary: "같은 날(11/23) 두 증권사가 ‘내 계좌를 AI 비서에 직접 연결’하는 서비스를 내놨다. LS증권은 MCP 기반 ‘LS Connector’ 시범 서비스로 Claude·ChatGPT·Cursor·Copilot·Grok에서 잔고 조회, 주식 주문, 포트폴리오 분석을 대화로 하게 했다. MT4·MT5 브로커 NordFX는 ‘NordFX AI Trading’으로 잔고·이체·실계좌 성과 분석·포지션 관리를 열었고, 권한을 골라 읽기 전용으로 시작하거나 AI 거래만 따로 끌 수 있게 했다."
---

## 한줄 요약
에이전트 트레이딩이 **‘개발자가 직접 API를 붙이는 일’에서 ‘증권사가 공식 연결을 내주는 일’**로 넘어가고 있다. 11/23 하루에 한국 LS증권과 해외 MT5 브로커 NordFX가 각각 그 방향의 서비스를 발표했다([서울경제 영문판](https://en.sedaily.com/market/2026/11/23/ls-securities-pilots-ls-connector-linking-generative-ai-to), [NordFX 보도자료](https://www.accessnewswire.com/newsroom/en/oil-gas-and-energy/nordfx-launches-ai-integration-for-client-services-and-trading-1254257)).

## LS증권 ‘LS Connector’ (시범 서비스)
- 생성형 AI를 LS증권 **오픈 API**에 직접 잇는 프로그램이다. 연결 규격은 **MCP**(AI가 외부 시스템의 데이터·기능을 쓰는 표준).
- 사용자가 요청하면 LS Connector가 의도를 파악해 오픈 API를 부르고, 결과를 AI 채팅창에 돌려준다. **HTS·MTS를 열지 않고** 대화만으로:
  - 보유 종목 실적 발표 일정, 예수금 확인
  - **매수·매도 주문 실행**
  - 국내외 시황 브리핑, 관심 기업 분석, 종목별 손익·비중 변화 리포트
- 지원 도구: **Claude, ChatGPT, Cursor, Copilot, Grok.** LS증권 ‘API투자전략센터’ 웹사이트에서 내려받아 연결한다.
- 시범 기간 피드백으로 안정성·편의성을 다듬은 뒤 정식 출시한다고 밝혔다.

## NordFX ‘NordFX AI Trading’
- 2008년 설립, **MT4·MT5**로 외환·금속·지수·주식·코인 CFD를 파는 브로커다. ChatGPT·Claude 등 호환 AI 앱에 계좌를 연결했다.
- 할 수 있는 일: 지갑·계좌 잔고, **내 계좌 간 이체 요청**, 본인인증 상태, 고객지원 요청 / 시세, **실계좌 성과 분석**(수수료·스왑 뺀 결과, 종목별 비교), **포지션 관리.**
- 예시: “지난달 비용이 결과에 얼마나 영향을 줬나?”를 묻고, 이어서 지갑 잔액을 보고 특정 거래 계좌로 이체를 요청하는 걸 한 대화에서.
- **안전장치:** 코딩·API 키 불필요. **권한을 골라 부여**하고, **읽기 전용으로 시작**하거나 **AI 거래만 따로 끌** 수 있으며, 개인 영역에서 연결을 철회할 수 있다. 추가 연동 비용은 없다.

## 왜 중요한가
지난번 저장하신 **MT5 MCP·에이전트 거래 안전장치(MT5 태그)** 흐름과 이어지는 소식이다. 어제 다룬 MT5 내장 MCP는 ‘거래 허용’이 기본값이었다. 이번 두 서비스는 **브로커가 직접 권한 단계를 설계**했다는 점이 다르다. 특히 NordFX처럼 **“읽기 전용 → AI 거래 별도 스위치”** 구조가 실전 계좌에선 출발점으로 적당하다.
- LS Connector도 처음엔 **성과 리포트·실적 일정 확인 같은 조회 업무**부터 써 보는 게 안전하다.
- 주의: LS Connector 보도에는 주문 한도·확인 단계 같은 세부 안전장치가 나오지 않았다. 주문 기능을 켜기 전에 확인할 것. 에이전트가 낸 주문도 평소 주문과 똑같이 손익·리스크에 잡힌다.
