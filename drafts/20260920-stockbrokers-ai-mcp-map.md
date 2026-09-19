---
title: "미 브로커 MCP 지도 2026 — IBKR 1위, Webull·tastytrade·Robinhood 가드레일 비교"
date: 2026-09-20T07:14:00+09:00
category: "AI Trading"
slug: "stockbrokers-ai-mcp-map"
summary: "2026-09-16 StockBrokers.com. 1선 MCP 7곳 실계좌 테스트. IBKR=지시서만(체결 분리) 종합 1위. Webull=한도·화이트리스트, tastytrade=드라이런 토큰(9월 공식 서버), Robinhood=에이전트 전용 계좌. 커뮤니티 MCP만 있는 Schwab 등은 제외."
---

## 한줄 요약
[StockBrokers.com](https://www.stockbrokers.com/guides/ai-agent-brokers)(2026-09-16, Jessica Inskip)이 **1선(official) MCP**를 돌리는 미 브로커 7곳을 실계좌로 비교했다. 모델 점수보다 **브로커가 무엇을 허용·강제하느냐**로 순위를 매겼다.

## 지금 뭐가 뜨나
| 브로커 | 에이전트 체결 | 핵심 가드 |
|---|---|---|
| **Interactive Brokers** | 불가(지시서→사람 제출) | 종합 1위·추가비 없음·임의 MCP |
| **Webull** | 가능 | 금액/수량 캡·심볼 WL·읽기전용·샌드박스 기본 |
| **tastytrade** | 가능(드라이런 토큰) | 9월 공식 로컬 서버·60초 해시 토큰·기본 $50k BP 캡. 토큰≠사람 승인 |
| **Moomoo** | 가능 | 호스팅 MCP·가입 가장 쉬움·페이퍼 기본 |
| **Robinhood** | 가능(전용 계좌) | 거래는 분리 계좌, **조회는 전 계좌** |
| Public / TradeStation | 가능 | Public=승인 후 무인 실행 가능·캡 약함 / TS=$10k+유료 AI 구독 |

Schwab·E*TRADE는 공식 API+커뮤니티 MCP만, Fidelity 등은 소매 공개 API 없음 → 가이드 제외. eToro Agent Portfolios는 미국 미제공.

## 왜 중요한가
“어떤 LLM이 매매에 좋나”보다 **어느 브로커가 잘못된 주문을 스스로 거절하나**가 2026년 질문이다. 자동화 트레이딩을 붙일 때 체크리스트: (1) 1선 MCP인가 (2) 사람/토큰/캡 중 무엇이 강제인가 (3) 샌드박스 기본값.

## 기억할 것
- [Best Brokers for AI Trading Agents](https://www.stockbrokers.com/guides/ai-agent-brokers) · 검증일 2026-09-16
