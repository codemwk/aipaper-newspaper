---
title: "ProreX × MT5 — MCP로 스크리너·Smart Score까지, 주문은 기본 수동 확인"
date: 2026-09-16T07:05:00+09:00
category: "AI Trading"
slug: "prorex-mt5-mcp-agentic"
summary: "2026-09-11. MetaTrader 5 Build 6060 네이티브 MCP·AI 위에 ProreX 자체 MCP 서버. 스크리너·Smart Score·아이디어·캘린더를 에이전트에 연결. 기본은 수동 컨펌, 자동체결은 옵트인."
---

## 한줄 요약
[ProreX / ACCESS Newswire(2026-09-11)](https://investor.wedbush.com/wedbush/article/accwirecq-2026-9-11-prorex-limited-brings-agentic-trading-and-its-own-mcp-tools-to-metatrader-5)에 따르면, MT5 **Build 6060**의 네이티브 MCP·에이전틱 AI에 더해 브로커 **ProreX**가 자체 MCP 서버를 붙였다. 한 에이전트가 ProreX 리서치 + MT5 시세·체결을 한 흐름으로 쓴다.

## 무엇이 돌아가는가
- MT5 쪽: 내장 AI Assistant, MQL5.community 기본 프로바이더, OpenAI·Anthropic·Gemini·DeepSeek·Ollama 키, Codex·Claude Code 등 외부 MCP 에이전트 연결([MT5 릴리즈 노트](https://www.metatrader5.com/en/releasenotes/terminal/2447)).
- ProreX MCP: 스크리너·**Smart Score**·트레이드 아이디어·시그널·뉴스·경제 캘린더를 에이전트 툴로 노출. 터미널 MCP 설정에서 “Add new MCP server”.
- 실행 가드: **수동 확인이 기본**. 분석 전용(거래 끔) / 수동 컨펌 / 명시적 자동체결 옵트인. 네트워크는 기본 GET, 위험 셸 비활성, 외부 에이전트는 재생성 API 키.

## 왜 중요한가
암호화폐 거래소 Agent OS와 달리, 여기는 **FX·멀티에셋 MT5 데스크톱**에 MCP가 들어온다. “시세만 보는 범용 AI”와 “브로커 리서치까지 한 세션”의 격차를 제품으로 메운다. 다만 PR이므로 **실주문 로그·슬리피지·프롬프트 인젝션** 검증은 사용자 몫이다.

## 기억할 것
- 플랫폼: [MT5 Build 6060](https://www.metatrader5.com/en/releasenotes/terminal/2447)
- 브로커 발표: [Wedbush/ACCESS](https://investor.wedbush.com/wedbush/article/accwirecq-2026-9-11-prorex-limited-brings-agentic-trading-and-its-own-mcp-tools-to-metatrader-5) · [TradeTechEye](https://tradetecheye.com/news/prorex-limited-brings-agentic-trading-and-its-own-mcp-tools-to-metatrader-5-0b4fa035)
