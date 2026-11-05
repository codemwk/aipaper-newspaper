---
title: "AI 트레이딩: Axi — Claude 무료 플랜으로 MT5 주문까지, 채팅 승인형 브로커 MCP"
date: 2026-11-06T07:04:00+09:00
category: "AI 트레이딩"
slug: "axi-mt5-claude-mcp"
summary: "Axi가 MT5 계좌를 Anthropic Claude에 MCP로 연결했다. 시세·포지션·주문·SL/TP 수정이 가능하고, 기본은 채팅에서 건별 승인. Claude 무료 플랜(커스텀 커넥터 1개)으로 동작하며 TradeStation의 Pro+$1만 잔고 조건과 대비된다. 알파 단계. 자금 이체는 불가."
---

## 한줄 요약
어제 다룬 **PrimeXBT·B2BROKER MCP**가 ‘브로커가 에이전트 권한 사다리를 어떻게 짜나’였다면, Axi는 **Claude 무료 플랜 + 채팅 승인**으로 그 사다리의 가장 낮은 진입 문턱을 보여 준다([Finance Magnates](https://www.financemagnates.com/forex/brokers/axi-clients-can-now-ask-claude-to-place-trades-in-their-metatrader-accounts/), [Axi MCP](https://www.axi.com/int/trading-platforms/mcp)).

## 지금 뭐가 뜨나
- **할 수 있는 것**: 잔고·증거금, 심볼 검색, 실시간 호가, 미결제 손익, 매수·매도, 대기 주문, SL/TP 수정, 체결 이력, 캔들 OHLC.
- **승인**: 주문·변경은 기본적으로 채팅에서 **명시적 승인**. Claude 권한에서 특정 동작을 “Always allow”로 풀 수는 있다.
- **못 하는 것**: 입출금·이체. Claude는 EA(자동매매)가 아니며, 요청이 있을 때만 움직인다고 안내.
- **자격**: 활성 MT5(데모·라이브). MT4·Axi 자체 플랫폼만 쓰는 계좌는 제외.
- **비용 비교**: Axi는 Claude **무료** 플랜의 커스텀 커넥터 1개로 연결. TradeStation MCP는 Claude Pro + **$10,000** 잔고. CMC Markets ChatGPT 연동은 **읽기 전용**.

## 왜 중요한가
지난번 저장하신 **MT5 MCP·RiskGate** 테마의 실전 브로커 사례다. MetaQuotes가 MT5에 네이티브 MCP·AI를 넣은 뒤, 브로커마다 ‘읽기만 / 승인 후 주문 / Always allow’ 축이 갈린다. 자동화 트레이딩을 붙이려면 **프로토콜보다 승인 UX와 책임 문구**가 제품의 핵심이다.

## 주의
알파 테스트. 투자 조언이 아니며 손실 책임은 고객에게 있다고 Axi가 명시한다. Always allow는 사실상 반자동이므로 권한 설정을 꼭 점검할 것.
