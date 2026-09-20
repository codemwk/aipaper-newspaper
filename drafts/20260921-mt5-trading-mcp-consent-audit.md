---
title: "mt5-trading-mcp — 에이전트 MT5 주문에 동의·감사(JSONL) 안전층"
date: 2026-09-21T07:03:00+09:00
category: "AI Trading"
slug: "mt5-trading-mcp-consent-audit"
summary: "vincentwongso/mt5-trading-mcp(PyPI 최신 1.6.x). 읽기 12도구+주문 4도구. preflight·idempotency·append-only JSONL 감사. auto_approve_notional 기본 0(자동 실행)이라 게이트를 켜야 사람이 승인. Windows 네이티브·Linux Docker."
---

## 한줄 요약
오픈소스 [mt5-trading-mcp](https://github.com/vincentwongso/mt5-trading-mcp)는 MetaTrader 5 Python API를 MCP로 감싸 **시세·포지션 읽기**와 **실주문**을 에이전트에 붙인다. 차별점은 브로커 MCP “연결”이 아니라 **동의(consent)·멱등·감사 로그**를 코드에 박아 둔 점이다.

## 지금 뭐가 뜨나
- 읽기: 계좌·호가·포지션·주문·히스토리·OHLC·마진 추정·(Windows) 차트 스크린샷 등 **동의 없이** 가능.
- 쓰기: `place_order` / `modify_order` / `cancel_order` / `close_position` — preflight → (옵션) 사람 승인 → idempotency → **JSONL 감사**.
- 기본값 주의: `auto_approve_notional` **기본 0**이면 변이 호출이 **자동 실행**된다. 문서도 “게이트는 opt-in”이라고 명시. 사람 확인을 원하면 임계값을 올려 ApprovalPreview를 켠다.
- 배포: `pip install mt5-trading-mcp` · Windows 네이티브 또는 Linux **올인원 Docker**. OpenClaw 등록 예시가 README에 있음.
- 한계: MCP는 **보안 경계가 아님**. 하드 한도는 브로커 MT5 서버. 라이브 전에 데모·`doctor` 필수.

## 왜 중요한가
9/16 ProreX·9/20 IBKR가 “브로커가 연 공식 MCP”라면, 오늘은 **셀프호스트 안전층**이다. 에이전트 트레이딩에서 승부는 “더 많은 툴”이 아니라 **누가 언제 주문을 막느냐·기록이 남느냐**다.

## 기억할 것
- [GitHub](https://github.com/vincentwongso/mt5-trading-mcp) · [PyPI](https://pypi.org/project/mt5-trading-mcp/) · docs/SECURITY·DISCLAIMER 먼저
