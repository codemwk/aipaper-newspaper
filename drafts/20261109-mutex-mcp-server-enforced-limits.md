---
title: "AI 트레이딩: MUTEX MCP — ‘프롬프트가 아니라 서버가 한도를 강제한다’, 그래도 에이전트 키의 구멍은 인정"
date: 2026-11-09T07:15:00+09:00
category: "AI 트레이딩"
slug: "mutex-mcp-server-enforced-limits"
summary: "크립토 거래소 MUTEX가 11/2 계정 전체를 AI 에이전트에 맡길 수 있는 MCP 서버를 공개했다. 출금은 사전 연결된 지갑만, 에이전트는 자기 권한을 못 올림, 봇 키의 최악은 봇 잔고. 같은 주 브로커 MCP들(PrimeXBT·TradeStation·B2BROKER)과 안전 모델을 비교한다."
---

## 한줄 요약
MUTEX는 11/2 “Claude 등 MCP 에이전트가 계정을 운영하되, **한도는 프롬프트가 아니라 서버가 강제한다**”는 MCP 서버를 냈다. 핵심 문장은 “프롬프트는 설득당할 수 있지만 서버는 안 그렇다”([MUTEX 공지](https://mutex.trade/news/ai-agents-on-mutex)).

## 안전 설계 (공식 설명)
- 출금은 **본인이 미리 연결한 지갑**으로만. API와 서명기가 각각 다른 주소를 거부한다.
- 에이전트는 지갑 변경, 에이전트 접근 on/off, API 키 생성·폐기, 서명키 승인을 **할 수 없다**(자기 권한 상승 불가).
- 에이전트 접근은 **기본 꺼짐**. 꺼져 있으면 읽기도 거부된다.
- **봇 키**는 격리된 봇 계정 하나만 다루며, 최악의 손실은 ‘그 봇 잔고’. 출금하려면 별도 서명키를 30일 또는 90일 단위로 승인해야 한다.
- 주문 전 `preview_order`로 예상 체결·수수료·증거금을 보고 `place_order`를 부르게 하며, 재시도는 고유 참조로 **중복 체결/중복 출금을 막는다**.

## 스스로 밝힌 한계
“에이전트 키는 내 세션과 같아서, 에이전트가 탈취되면 **메인 퍼프 계정을 거래하고 연결 지갑으로 출금**할 수 있고 서버는 서명 전에 묻지 않는다.” 그래서 **작게 채운 봇 키로 시작**하라고 권한다. 이 솔직함이 이 공지의 가장 쓸모 있는 부분이다.

## 이번 주 다른 MCP들과 비교
- **PrimeXBT**(11/4): 모든 주문에 명시적 확인, 읽기전용/읽기+거래 권한, AI로 출금·이체 불가([GlobeNewswire](https://www.globenewswire.com/news-release/2026/11/04/3395052/0/en/primexbt-launches-ai-assisted-trading-with-mcp-integration-connecting-chatgpt-and-claude-to-trading-accounts.html)).
- **TradeStation 기관용 MCP**: OAuth 2.0 PKCE, 기존 권한·위험 한도 상속, 도구별 범위 지정, 주문 승인 필수, 감사 로그([TradeStation](https://institutional.tradestation.com/technology/institutional-ai-trading/)).
- **B2BROKER B2TRADER**: 터미널 내 채팅은 거래마다 확인하지만 **풀 액세스 MCP는 건별 확인이 없고** 주문은 되돌릴 수 없다고 문서가 직접 경고, 프롬프트 인젝션 위험도 명시([B2BROKER 문서](https://docs.b2broker.com/b2trader/terminal/connect-your-ai-agent/full-access-safety)).

## 왜 중요한가
브로커 MCP가 늘수록 비교축은 기능이 아니라 **‘확인 vs 서버 한도 vs 키 범위’**다. MT5 네이티브 MCP를 쓰는 분도 같은 질문을 던져 볼 만하다: 에이전트가 자기 권한을 올릴 수 있나, 최악 손실은 얼마로 제한되나, 데모 계정부터 시작할 수 있나.

## 주의
위 내용은 각사 공식 설명이다. 실거래 보안 검증이나 사고 사례 데이터는 없다. 레버리지 상품은 손실 위험이 크다. 투자 권유가 아니다.
