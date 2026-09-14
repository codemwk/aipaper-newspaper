---
title: "바이낸스 ‘에이전트도 거래소 고객’ — Agent OS·MCP로 주문, 출금은 막는다"
date: 2026-09-15T07:05:00+09:00
category: "AI Trading"
slug: "binance-agent-os-customers"
summary: "2026-09-14. 바이낸스가 AI 에이전트를 인간 고객과 같은 거래소 고객층으로 포지셔닝. Agent OS(8/20)로 ChatGPT·Claude Code·Cursor가 MCP로 시세·잔고·주문을 처리. 에이전틱 서브계정·출금 차단이 핵심 가드레일. KYC 책임은 여전히 계정 주인."
---

## 한줄 요약
[Crypto Times(2026-09-14)](https://www.cryptotimes.io/2026/09/14/binance-pitches-ai-agents-as-a-new-class-of-crypto-exchange-customer/)에 따르면 바이낸스 리더십 블로그가 **소프트웨어 에이전트를 거래소의 새 고객층**으로 못 박았다. 신제품 출시가 아니라, 8월 20일 공개한 [Agent OS](https://tradetecheye.com/news/binance-introduces-agent-os-to-connect-ai-applications-to-financial-infrastructu-6d0fc173)를 ‘인프라 기본값’으로 재프레이밍한 글이다.

## 무엇이 돌아가는가
권한만 주면 ChatGPT·Codex·Claude Code·Cursor 같은 MCP 호환 앱이 시세를 읽고, 잔고를 보고, 스팟·컨버트·선물 주문을 낼 수 있다. 에이전트마다 **에이전틱 서브계정**으로 자금·활동이 분리되고, **외부 지갑 출금 스코프는 의도적으로 없다**. VP Jeff Li는 “전면 자유가 아니라 계정 단 세분 제어”라고 말했고, 동시에 추론은 사용자 기기·외부 AI 앱에서 일어나므로 거래소는 **주문 로그만** 볼 수 있다고 인정했다.

## 왜 중요한가
Coinbase x402, OKX 에이전트 마켓, BNB Chain·AgentPay SDK까지 **격리·한도·출금 인간 게이트** 패턴이 거래소 경쟁 축이 됐다. 규제 쪽 ‘Know Your Agent’ 규칙은 아직 없고, KYC·AML·시세조작 책임은 **계정 명의자·베뉴**에 남는다. EU MiCA 철수로 소매를 접은 바이낸스의 유럽 공백도 이 에세이가 메우지는 않는다. 가드가 막는 것은 탈취성 출금이지, **승인된 범위 안의 청산·프롬프트 인젝션 손실**은 아니다.

## 기억할 것
- 읽는 자세: 규제 서류가 아니라 **제품 방향 선언**.
- 실사용 체크: 서브계정 한도, 선물 레버리지 캡, 승인 UX, 로그·감사 가능성.
