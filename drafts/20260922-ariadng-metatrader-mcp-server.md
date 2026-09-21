---
title: "ariadng/metatrader-mcp-server — Claude·ChatGPT를 MT5에 자연어로 붙이는 커뮤니티 MCP"
date: 2026-09-22T07:04:00+09:00
category: "AI Trading"
slug: "ariadng-metatrader-mcp-server"
summary: "ariadng/metatrader-mcp-server(MIT, GitHub ★~806). Claude/ChatGPT↔MT5 자연어 브리지. 시세·주문, 자격증명은 로컬, MCP/REST/WebSocket·PyPI. 어제 vincentwongso consent/audit 패턴과 보완 관계. 실주문은 되돌릴 수 없음 — 데모 먼저."
---

## 한줄 요약
오픈소스 [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)(MIT, ★약 806)는 MetaTrader 5를 **MCP로 감싸** Claude·ChatGPT 등 LLM이 **자연어로 시세·주문을 다루게** 한다. 자격증명은 로컬에 두고, MCP·REST·WebSocket·PyPI로 배포된다.

## 지금 뭐가 뜨나
- **역할**: “브로커 공식 MCP”가 아니라 **셀프호스트 자연어 브리지**. 차트·호가 읽기부터 주문 실행까지 에이전트 툴로 노출.
- **보안 모델**: 계정·비밀번호가 클라우드에 안 나가게 **로컬 프로세스**에 두는 설계가 README의 핵심 메시지.
- **보완 패턴**: 어제 다룬 [vincentwongso/mt5-trading-mcp](https://github.com/vincentwongso/mt5-trading-mcp)의 **동의·감사(JSONL)** 레이어와 겹치지 않는다 — 연결 UX vs 승인·감사. 실무에선 둘을 같이 보는 편이 안전하다.
- **경고**: 실거래는 **되돌릴 수 없다**. 데모 계좌·읽기 전용부터. MCP는 보안 경계가 아니다.

## 왜 중요한가
Build 6060 네이티브 MCP가 “플랫폼 공식 문”이라면, ariadng은 **이미 돌고 있는 커뮤니티 표준 포트**다. 툴 체인을 고를 때 발견 신호(스타·이슈)와 안전층(consent)을 분리해 읽자.

## 기억할 것
- [GitHub](https://github.com/ariadng/metatrader-mcp-server) · MIT · 데모 먼저 · consent/audit과 병행 검토
