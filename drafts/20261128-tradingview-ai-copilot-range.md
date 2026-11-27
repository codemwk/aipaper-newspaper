---
title: "AI 트레이딩: TradingView AI Copilot에 ‘차트 구간 드래그 질문’ — 고른 기간의 뉴스까지 찾아 주고, 모델은 DeepSeek·GPT·Claude 중 골라 쓴다. MCP는 Pine 컴파일·백테스트까지"
date: 2026-11-28T07:05:00+09:00
category: "AI 트레이딩"
slug: "tradingview-ai-copilot-range"
summary: "TradingView가 11/24 AI Copilot에 ‘AI range’를 넣었다. 차트에서 날짜 구간을 드래그하고 “이 움직임 설명해 줘”, “이 구간의 뉴스·이벤트 찾아 줘”라고 물으면, 그 시기의 헤드라인을 찾아 답하고 지지·저항선도 그려 준다. 응답 속도는 2배 이상 빨라졌다. 11/16에는 모델 선택(DeepSeek V4.1 Flash·GPT-6 Luna·Claude Sonnet 5.5)과, 외부 AI용 TradingView MCP의 Pine Script 컴파일·백테스트 도구 및 하루 호출 한도가 발표됐다."
---

## 한줄 요약
“3월 초에 떨어진 거”라고 말로 설명할 필요가 없어졌다. **차트에서 구간을 고르면 AI가 그 기간 기준으로** 설명·뉴스·기술적 분석을 한다([TradingView 블로그, 11/24](https://www.tradingview.com/blog/en/ai-range-in-ai-copilot-62954/)).

## AI range — 어떻게 쓰나
1. 차트 왼쪽 그리기 패널의 **AI range 아이콘**을 누른다.
2. 차트에서 날짜 구간을 드래그한다.
3. 제안 질문 3개 중 하나를 고르거나 직접 묻는다.
   - “이 가격 움직임을 설명해 줘”
   - “이 움직임 뒤의 이벤트를 찾아 줘” — **그 날짜의 뉴스**를 찾는다(예전엔 최신 뉴스만 나왔다).
   - “이 구간의 기술적 분석” — 가격 구조와 주요 레벨.
- “이 구간에 지지·저항선 표시해 줘”라고 하면 **차트에 직접 그린다**. 선택 구간은 임시이고 레이아웃에 저장되지 않는다. 대화 기록에서 구간을 누르면 그 종목·기간으로 돌아간다.
- 웹·데스크톱, **유료 플랜 + AI Copilot 애드온** 필요.

## 모델 고르기 (11/16)

| 모델 | 속도 | 요청당 사용량 | 품질 |
| --- | --- | --- | --- |
| DeepSeek V4.1 Flash(기본) | 1× | 1× | 0.9× |
| GPT-6 Luna | 2× | 0.4× | 0.6× |
| Claude Sonnet 5.5 | 2× | 7.5× | 1× |

- 대화마다 모델과 **추론 깊이**를 바꿀 수 있다. Claude는 사용량을 7.5배 쓴다. 한도가 떨어지면 애드온과 같은 금액으로 **리필**(남은 양에 더해지는 게 아니라 100%로 리셋)([TradingView 블로그](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/)).

## 외부 AI용 TradingView MCP — Pine 도구 8개 (11/16)
- Claude·ChatGPT 같은 외부 비서가 **실제 Pine 컴파일러**로 코드를 검사(`validate`)하고, 아무 종목에서 지표를 돌리고, **전략 백테스트 리포트**(순이익·PF·MDD·승률·샤프 등)를 읽고, 컴파일되는 코드만 계정에 저장한다. 보호·초대 전용 스크립트 소스는 열리지 않는다.
- **11/17부터 하루 호출 한도:** Essential 10회, Plus 20회, Premium 50회, Ultimate 500회. AI 구독이 있으면 하루 500회(분당 50회). Pine 작업은 검사·실행·백테스트가 모두 1회씩 차감된다([TradingView 블로그](https://www.tradingview.com/blog/en/tradingview-mcp-pine-script-and-daily-limits-62532/)).

## 왜 중요한가
- 지난번 저장하신 **TradingView MCP·MT5 MCP 기사와 이어지는 소식**이다. 헤이킨아시 1시간봉에서 “왜 여기서 꺾였나”를 볼 때, 구간 선택 한 번으로 **그 시점 뉴스**를 붙여 보는 흐름이 생겼다.
- 개인 지표(Pine) 개선에는 MCP 쪽이 더 실용적이다. 같은 전략을 **여러 종목·파라미터로 돌려 표로 비교**하고 “리페인트 하나?”를 묻는 스트레스 테스트가 대화 안에서 끝난다. 다만 Plus 플랜이면 하루 20회라 금방 찬다.
- 주의: TradingView 약관상 MCP는 **개인용**이며 **자동매매·봇 연결 금지**, 데이터로 AI 학습 금지다. MT5 실행 스택에 신호를 넘기는 용도로 쓰면 약관 위반이 될 수 있다. Copilot 답변은 투자 조언이 아니다.

출처: [AI range](https://www.tradingview.com/blog/en/ai-range-in-ai-copilot-62954/) · [모델 선택](https://www.tradingview.com/blog/en/ai-copilot-claude-chatgpt-deepseek-62292/) · [MCP Pine·한도](https://www.tradingview.com/blog/en/tradingview-mcp-pine-script-and-daily-limits-62532/)
