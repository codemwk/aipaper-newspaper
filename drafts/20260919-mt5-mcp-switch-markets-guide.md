---
title: "MT5 네이티브 MCP — Switch Markets 가이드가 정리한 ‘에이전트↔터미널’ 실무"
date: 2026-09-19T07:05:00+09:00
category: "AI Trading"
slug: "mt5-mcp-switch-markets-guide"
summary: "2026-09-03 갱신. Switch Markets가 MT5 Build 6060+ 네이티브 MCP·AI Assistant 연결 절차를 장문 가이드로 공개. Codex/Claude Code URL·토큰, 써드파티 Python MCP, 라이브 주의사항. Build 6180 테스터 QA와 한 축."
---

## 한줄 요약
[Switch Markets](https://www.switchmarkets.com/learn/mt5-mcp-server)(2026-09-03 갱신)는 MetaQuotes가 **2026-07-23 Build 6060**에서 넣은 **네이티브 MCP·에이전틱 AI**를, 브로커 고객 관점에서 **설정·연결·한계**까지 풀어 쓴 실무 가이드다. 본지가 9/17에 다룬 [Build 6180 테스터 QA](https://codemwk.github.io/aipaper-newspaper/)와 같은 제품 라인의 **연결 매뉴얼**에 가깝다.

## 무엇이 바뀌었나
- MT5는 이제 **시세·계좌·개발·(허용 시) 거래**를 MCP로 외부 에이전트(OpenAI Codex, Claude Code 등)에 노출한다. 예전 비공식 브리지만 쓰던 시절과 다르다.
- 가이드 요지: 터미널 **Tools → Options → MCP**에서 localhost URL·bearer 토큰을 복사해 클라이언트에 넣고, 데모·읽기 위주로 먼저 검증한다. MQL5.community 로그인 시 **MQL5 Lite**가 기본 AI 제공자로 붙는다고 MetaQuotes 릴리즈도 설명한다.
- 써드파티 **Python MT5 MCP**(예: vincentwongso/mt5-trading-mcp 계열)는 커스텀·도커·승인 프리뷰가 필요할 때 여전히 선택지. 라이브 `place_order`는 **사람 확정 없이는 금지**가 공통 하드 룰로 강조된다.
- Build **6180**(9/3 릴리즈)은 Strategy Tester 리포트·최적화·로그를 어시스턴트가 직접 다루는 쪽으로 확장됐다 — MCP “연결”과 “테스터 QA”가 한 제품 스택.

## 왜 중요한가
어제 Leverate·TradingView MCP·cTrader 물결과 나란히 두면, **터미널 벤더가 MCP를 1급 시민으로 만든** 쪽이 MT5다. 트레이딩 MCP를 고를 때 질문 순서는 (1) 시세만인가 체결까지인가 (2) 사람 승인 UX (3) 로그·서브계정 격리. Switch 가이드는 그 체크리스트를 브로커 언어로 적어 둔 문서다.

## 기억할 것
- [Switch Markets MT5 MCP 가이드](https://www.switchmarkets.com/learn/mt5-mcp-server) · [Build 6060 릴리즈](https://www.metatrader5.com/en/releasenotes/terminal/2447) · [Build 6180](https://www.metatrader5.com/en/releasenotes/terminal/2464)
