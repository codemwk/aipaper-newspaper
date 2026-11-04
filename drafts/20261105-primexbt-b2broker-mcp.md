---
title: "AI 트레이딩: 하루에 브로커 두 곳 MCP 개방 — PrimeXBT는 ‘주문마다 확인’, B2BROKER는 ‘전권 위임 시 확인 없이 체결’"
date: 2026-11-05T07:02:30+09:00
category: "AI 트레이딩"
slug: "primexbt-b2broker-mcp"
summary: "11/4 PrimeXBT가 ChatGPT·Claude를 계좌에 붙이는 MCP를 열었다. 주문 미리보기(가격·수수료·증거금·청산가)까지 해 주지만 모든 주문은 트레이더 확인 필요, 출금·이체 불가, 데모·실계좌 모두 지원. 같은 날 B2BROKER는 B2TRADER에 MCP와 터미널 내 AI 채팅을 넣었는데, ‘전체 권한’을 받은 외부 에이전트는 주문별 확인 없이 체결할 수 있다. 권한 설계는 브로커가 정한다."
---

## 한줄 요약
어제 정리한 **브로커 권한 사다리**에 같은 날 두 칸이 더 생겼다. 둘 다 MCP로 AI를 계좌에 붙이지만, **누가 마지막 버튼을 누르느냐**가 다르다.

## PrimeXBT — 준비는 AI, 체결은 사람
- 링크 하나와 PrimeXBT 로그인으로 연결, 코드·API 키 불필요.
- 계좌 조회, 시세·차트, 거래 내역, 비용·레버리지·증거금 규칙 질문.
- 시장가·지정가·스탑 주문을 **준비**하고 예상 가격·수수료·증거금·레버리지·**청산가**를 거래 엔진이 계산해 보여 준다.
- **모든 주문은 명시적 확인 후 체결**. 권한은 읽기 전용 / 읽기+거래 두 단계. **출금·이체 불가**.
- PXTrader 2.0의 CFD·크립토 선물, **데모와 실계좌 모두** 지원([GlobeNewswire 11/4](https://www.globenewswire.com/news-release/2026/11/04/3395052/0/en/primexbt-launches-ai-assisted-trading-with-mcp-integration-connecting-chatgpt-and-claude-to-trading-accounts.html)).

## B2BROKER — 브로커가 권한 수준을 고른다
- B2TRADER 플랫폼에 MCP와 **터미널 안 AI 채팅** 추가. “수익 난 포지션 전부 청산”, “열린 포지션마다 손절 설정” 같은 자연어 지시.
- 브로커가 MCP 끄기 / 읽기 전용 / 전체 권한 중에서 선택. 에이전트는 승인한 트레이더 본인 계좌에만 접근.
- 터미널 채팅이 제안한 거래는 확인이 필요하지만, **전체 권한을 받은 외부 에이전트는 주문별 확인 없이 허용된 거래를 실행**할 수 있다([GlobeNewswire 11/4](https://www.globenewswire.com/news-release/2026/11/04/3395078/0/en/b2broker-expands-b2trader-ai-strategy-with-mcp-trading-agents-and-in-terminal-chat.html)).

## 왜 중요한가 (MT5 관점)
지난번 저장하신 **MT5 + MCP 안전 레이어** 소식과 이어진다. B2BROKER는 브로커들에게 플랫폼을 파는 회사라, 이 기본값이 여러 브로커로 퍼질 수 있다. 내 에이전트를 붙일 때 체크할 것: ① **데모 계좌에서 먼저**(PrimeXBT는 데모 지원), ② 전권 위임이라면 **청산가·손실 한도를 별도로** 걸 수 있는지, ③ 출금 차단 여부.

## 주의
“수익 난 포지션 전부 청산” 같은 지시는 해석이 틀리면 되돌릴 수 없다. 레버리지 CFD·선물은 손실이 원금을 넘을 수 있다.
