---
title: "TradingView Desktop MCP — 차트 조작·Pine·시그널을 MT5로 잇는 커뮤니티 스택"
date: 2026-09-23T07:09:00+09:00
category: "AI Trading"
slug: "tradingview-desktop-mt5-bridge"
summary: "Unjoselo/tradingview-desktop-mcp. CDP로 TradingView Desktop 제어(심볼·지표·Pine·Strategy Tester). 별도 mt5_server + signal_bridge(종가 봉만·데모 기본). Windows. 네이티브 MT5 MCP(6060)·브로커 MCP와 다른 ‘차트앱 원격조종’ 각도. 소형 레포·실험용."
---

## 한줄 요약
[tradingview-desktop-mcp](https://github.com/Unjoselo/tradingview-desktop-mcp)는 **이미 켜 둔 TradingView Desktop**을 Chrome DevTools Protocol로 붙잡아, Claude·Codex·Cursor가 차트·지표·Pine·Strategy Tester를 조작하게 한다. 옵션으로 **MT5 MCP**와 **인디케이터 시그널→MT5 주문 브리지**가 있다.

## 구조(개념)
- **TV 서버**: `tv_set_symbol`·`tv_add_study`·`tv_pine_*`·`tv_strategy_report`·스크린샷 등. 계정 API/스크래핑이 아니라 **로컬 Electron 앱 세션**.
- **MT5 서버**: 잔고·캔들·포지션·시장가. **데모만 기본**, 실계좌는 `MT5_ALLOW_REAL=1`을 사용자가 켠다.
- **signal_bridge**: 채팅 밖 데몬. 차트 BUY/SELL 셰이프를 읽어 **종가 봉만** 스톱앤리버스. `--once`/`--test` 후 가동. `bridge_trades.csv` 로그.
- **한계**: Windows 전용. CDP 포트=앱 세션 전체 권한(localhost 바인딩). 비공식 내부 API라 앱 업데이트에 깨질 수 있음. 금융 조언 아님.

## 어제·최근 기사와 결
- 9/22 **MT5 Build 6060 네이티브 MCP**, **ariadng 커뮤니티 MCP**, 9/21 **consent/audit** — “터미널 안 에이전트”.
- 오늘은 **차트 워크벤치(TradingView) ↔ 체결(MT5)** 를 에이전트·브리지로 잇는 **데스크톱 원격조종** 각도. 스타는 작아도 구조가 선명하다.

## 왜 중요한가
자동매매 관심이 “한 MCP로 주문”에서 **리서치 UI와 실행 UI를 누가 붙이느냐**로 넘어간다. 가드레일(데모 기본·종가 봉·매직넘버)을 README에 박아 둔 점이 실무 체크리스트다.

## 기억할 것
- [github.com/Unjoselo/tradingview-desktop-mcp](https://github.com/Unjoselo/tradingview-desktop-mcp) · MT5 네이티브 MCP 릴리즈노트와 병행 비교
