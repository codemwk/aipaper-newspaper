---
title: "AI Trading: MT5↔MCP 브리지 실전 — 14개 툴·동의 힌트·데모 먼저"
date: 2026-09-24T07:09:00+09:00
category: "AI Trading"
slug: "mql5-mt5-mcp-howto"
summary: "MQL5 아티클(2026-04-30). Python FastMCP+MetaTrader5, 14툴, constants/client/handlers/server 4층. readOnlyHint vs destructiveHint. 주문 전 get_account·get_symbol_info 지시. Windows 전용. 데모 필수."
---

## 한줄 요약
[MQL5 아티클](https://www.mql5.com/en/articles/21905)은 네이티브 Build 6060/6180과는 별도로, **Python FastMCP로 MT5를 에이전트에 붙이는 실전 레시피**를 정리한다. 읽기 툴과 체결 툴을 나누고, 파괴적 동작에는 확인 힌트를 건다.

## 구조
- **14개 툴**, 약 676줄 Python. 의존성: `MetaTrader5` + `fastmcp`.
- 레이어: constants(문자열↔상수) → mt5client(연결·타임아웃) → handlers(계좌·시세·포지션·주문·히스토리) → server(등록).
- **stdio** 로컬 전송. Claude Desktop 설정 JSON, OpenClaw+Telegram 스킬 예시.
- 안전: 전역 instructions로 주문 전 `get_account`·`get_symbol_info`, `destructiveHint` on close/order.
- 한계: MT5 Python **Windows 전용**, 싱글스레드. **데모 계정 먼저** — 저자 면책.

## 왜 중요한가
최근 판이 네이티브 MCP·브로커 MCP를 다뤘다면, 오늘은 **직접 브리지를 짤 때 무엇을 가드해야 하는지**다. 라이브 주문 전에 상태 동기화·동의 UI가 제품의 핵심이라는 점을 코드 구조로 보여 준다.

## 기억할 것
- [How to connect AI agents to MetaTrader 5 via MCP](https://www.mql5.com/en/articles/21905)
