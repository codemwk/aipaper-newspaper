---
title: "AI 트레이딩: Webull 캐나다, ChatGPT·Claude·Perplexity·Grok에서 말로 주문 준비 — 실행은 ‘Webull 앱에서 직접 확인’. 그리고 MT5 MCP 실험이 찾은 ‘매매 스위치를 돌아가는 두 갈래 길’"
date: 2026-10-28T07:05:00+09:00
category: "AI 트레이딩"
slug: "webull-canada-mcp-mt5-routes"
summary: "Webull 캐나다 법인이 10/27 고객 계좌를 MCP로 ChatGPT·Perplexity·Claude·Grok에 연결하는 서비스를 발표(11월 초까지 전 계좌 순차 적용). AI는 실시간 시세·잔고·포트폴리오 분석과 ‘주문 준비’까지만 하고, 실제 실행은 투자자가 Webull에서 검토·확인해야 한다. 같은 주제로, MT5 내장 MCP를 직접 시험한 RoboXpert 가이드는 ‘AI 매매 허용’ 스위치가 알고 트레이딩 버튼과 따로 움직이며, 전문가 자문(EA)을 차트에 붙이는 도구와 외부 웹 요청 도구가 매매 스위치를 우회할 수 있는 길이라고 지적했다."
---

> 지난번 저장하신 MT5 + MCP 안전장치 기사들(MT5 Build 6060 매매 권한, RiskGate)과 이어지는 소식입니다(어제 다룬 메리츠증권 OPEN API의 연장선) — 이번엔 ‘확인 버튼이 어디에 있느냐’가 핵심입니다.

## 한줄 요약
“AI에게 말하면 주문이 준비된다”는 서비스가 또 하나 늘었다. 차이는 **최종 확인을 어디서 하느냐**다. Webull 캐나다는 그 확인을 **대화창이 아니라 Webull 앱 안**에 두었다([Investing.com](https://www.investing.com/news/stock-market-news/exclusive-webull-brings-aiassistant-trading-to-canada-via-chatgpt-claude-4975280)).

## Webull 캐나다 — 무엇이 되나
- 연결 대상: **ChatGPT, Perplexity, Claude, Grok**. 연결 규격은 MCP, 코딩 지식 불필요.
- 가능한 일: 실시간 시세, 잔고·보유 종목 확인, 포트폴리오 분석, **주문 준비**.
- 실행: “투자자가 Webull에서 검토하고 확인하기 전에는 **아무것도 체결되지 않는다**”(회사).
- 일정: 11월 초까지 대상 계좌 전체에 순차 적용. 미국에서는 이미 비슷한 서비스를 확대한 바 있다.
- 배경: 전 세계 등록 이용자 2,900만 명+. 최근 미국 하원 위원회 보고서가 중국과의 연관성을 비판했고 회사는 반박 중이다.

## MT5 내장 MCP — 실험으로 드러난 것
MT5는 7월 Build 6060부터 MCP를 내장했고, 설정에서 AI 매매를 **허용 / 확인 요청 / 금지** 중 고를 수 있다([MT5 도움말](https://www.metatrader5.com/en/terminal/help/mcp_and_ai)). RoboXpert가 Claude Code를 실제로 붙여 본 결과([가이드](https://roboxpert.ai/en/guides/mt5-mcp-server/)):

| 관찰 | 의미 |
|---|---|
| 계좌 정보에 `experts_trade_allowed: false`(알고 트레이딩 꺼짐)와 `mcp_trade_allowed: true`가 **따로** 나옴 | 알고 트레이딩 버튼을 껐다고 AI 주문까지 꺼진 게 아니다. **AI 매매 스위치는 별도로 확인** |
| 주문 도구 설명에 “사용자가 종목·방향·수량을 명시했을 때만 사용” 문구 | 이건 모델에게 주는 **부탁**일 뿐. 믿을 수 있는 건 도구 옵션의 스위치 |
| 파일 접근은 MQL5·Tester·Logs·Common 폴더로 제한, 계정 설정 폴더·윈도 시스템 파일 요청은 거부 | 파일 쪽 울타리는 작동 |
| `chart_add_expert`(차트에 EA 붙이기) | EA는 **자기 코드대로 매매**한다. 알고 트레이딩이 켜져 있으면 AI 매매 스위치와 무관하게 주문이 나갈 수 있는 길 |
| `send_web_request`(외부 웹 요청) | 에이전트가 읽은 내용(잔고·포지션 등)을 **아무 주소로나 보낼 수 있는** 길 |

- 두 우회로는 RoboXpert도 **직접 시험하지는 않았다**고 밝혔다. 권고는 “도구를 하나씩 허용할 수 있다면 **주문·차트·웹 요청 도구는 필요할 때까지 빼 두라**”.

## 왜 중요한가 — ‘확인’의 위치 3가지
1. **대화창 안 확인**(AI가 “주문할까요?” 묻고 내가 “네”): 가장 편하지만, 대화 내용이 조작되면(프롬프트 인젝션) 확인 자체가 흐려질 수 있다.
2. **증권사 앱에서 확인**(Webull 캐나다 방식): AI가 만든 주문서를 **AI 밖의 화면**에서 사람이 승인. 가장 안전한 축.
3. **확인 없음**(스위치 ‘허용’, 또는 EA 자동매매): 금액·종목·횟수 상한을 **코드나 브로커 쪽에** 걸어 두지 않았다면 쓰지 말 것.
- MT5를 쓴다면 오늘 할 일: 도구 → 옵션 → AI Assistant에서 매매를 **‘확인 요청’ 이상**으로 두고, 알고 트레이딩 버튼과 별개로 점검. 데모 계좌에서 먼저.

출처: [Investing.com — Webull Canada AI-assistant trading (10/27)](https://www.investing.com/news/stock-market-news/exclusive-webull-brings-aiassistant-trading-to-canada-via-chatgpt-claude-4975280) · [RoboXpert — MT5 MCP Server 가이드 (10/12)](https://roboxpert.ai/en/guides/mt5-mcp-server/) · [MetaTrader 5 도움말 — MCP and AI](https://www.metatrader5.com/en/terminal/help/mcp_and_ai) · [MT5 Build 6060 릴리스 노트](https://www.metatrader5.com/en/releasenotes/terminal/2447)
