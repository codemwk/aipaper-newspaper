---
title: "AI 트레이딩: Lightspeed Connect API — 숏 로케이트·페이퍼 트레이딩·‘AI가 읽기 쉬운’ 문서를 열었다. 자율매매 권한은 아니다"
date: 2026-11-01T07:01:00+09:00
category: "AI 트레이딩"
slug: "lightspeed-connect-api"
summary: "미국 주식·옵션용 Lightspeed Connect API가 10/30 숏 로케이트, 페이퍼 트레이딩, 통합 테스트 리소스, AI 친화 문서를 추가했다(FinanceFeeds). 코딩 어시스턴트가 엔드포인트를 찾기 쉽게 만든 것이지, 에이전트에 주문 권한을 준 발표가 아니다. 11/4 웨비나."
---

## 한줄 요약
지난번 저장하신 MT5·브로커 MCP 안전 레이어 이야기와 이어지는 소식이다. Lightspeed는 **에이전트에게 열쇠를 넘기지 않고**, 개발자가 커스텀 앱을 붙이기 쉽게 **API·문서·시뮬**을 키웠다([FinanceFeeds](https://financefeeds.com/lightspeed-adds-short-locate-and-paper-trading-to-connect-api/)).

## 무엇이 추가됐나
| 항목 | 의미 |
|---|---|
| Short locate | 공매도 전에 대주 가능 여부를 API로 조회·워크플로에 넣는 기능. **가능 종목·수수료·유효기간 목록은 발표에 없음** |
| Paper trading | 실주문 없이 지원 기능을 테스트 |
| Integration testing | 메시지·계정 갱신 흐름을 프로덕션 전에 검증 |
| AI-ready docs | LLM·코딩 어시스턴트가 읽기 좋은 구조의 기술 문서 |

Connect는 미국 주식·옵션용 **WebSocket** 인터페이스로 소개된다.

## 중요한 구분
- 문서가 AI에 친화적이라고 해서 **계정 접근·주문 권한이 생기는 것은 아니다.** FinanceFeeds도 “개발 지원이지 에이전트 실행·추천이 아니다”라고 선을 그었다.
- 페이퍼 환경은 메시지 형식 검증용이다. **실시간 유동성·부분체결·대주 가능 여부를 그대로 재현한다고 보장하지 않는다.**

## 왜 중요한가
- IBKR 자율매매·B2Trader MCP·Tria 거래 전용 키처럼 ‘에이전트가 주문한다’ 쪽과 달리, Lightspeed는 **사람이 만든 앱의 DX**에 베팅한다.
- 브로커 API 경쟁이 주문 종류만이 아니라 **문서·샌드박스·예제**로 옮겨 가는 신호. 11/4 웨비나에서 locate 응답 스키마·프로덕션 온보딩을 확인해야 한다.
