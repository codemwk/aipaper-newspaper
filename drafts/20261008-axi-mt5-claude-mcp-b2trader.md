---
title: "AI 트레이딩: Axi, MT5 계좌를 Claude에 MCP로 연결 — 주문·리스크 수정까지, B2TRADER는 ‘읽기 전용/전체 권한’ 두 단계"
date: 2026-10-08T07:00:00+09:00
category: "AI 트레이딩"
slug: "axi-mt5-claude-mcp-b2trader"
summary: "CFD·FX 브로커 Axi가 10/7 ‘Axi MCP’를 출시해 실계좌 MT5를 Claude 커넥터로 연결했다. 시세·포지션 조회는 물론 주문 실행·리스크 파라미터 수정까지 가능. 하루 앞서 B2Broker의 B2TRADER도 MCP 서버를 내며 ‘끔/읽기 전용/전체 권한’ 3단 모드와 민감 동작 확인 절차를 붙였다."
---

## 한줄 요약
MT5를 AI에 붙이는 일이 “개인이 만든 브리지”에서 **브로커가 공식 제공하는 커넥터**로 넘어가고 있다. 호주계 CFD·FX 브로커 **Axi**가 10월 7일 **Axi MCP**를 내놓았다 — 활성 MT5 계좌가 있는 고객은 **Claude 커넥터**에 Axi MCP URL을 추가하고 Axi 계정으로 로그인·승인하면 끝이다([Axi 발표](https://www.axi.com/int/blog/company-news/axi-launches-mcp-integration-mt5-claude)).

## 무엇이 되나
- **조회**: 실시간 시세, 계좌 데이터, 포지션 추적.
- **실행**: MT5 **주문 실행**과 **리스크 파라미터 수정**(손절·익절 등)까지 도구로 열려 있다.
- **연결 방식**: Claude.ai의 Connectors → URL 입력 → Axi 로그인으로 권한 위임. 별도 EA나 로컬 서버 설치가 필요 없다.
- 공식 발표문은 짧다. **주문 전 별도 확인 단계가 있는지**, 어떤 계좌 유형이 ‘적격’인지는 명시돼 있지 않다 — 쓰기 전에 꼭 확인할 부분이다.

## 같은 주, 플랫폼 쪽에서도: B2TRADER
화이트라벨 거래 플랫폼 **B2TRADER**(B2Broker)는 10월 6일 릴리스에서 **풀 MCP 서버 + 터미널 내장 AI Chat**을 추가했다([B2Broker](https://b2broker.com/news/b2trader-goes-ai-native-with-mcp-support-and-ai-chat/)).
- “수익 난 포지션 전부 청산해”, “열린 포지션 전부에 손절 걸어” 같은 말로 거래·시세·포트폴리오·잔고 작업.
- **권한 2단 표면**: 거래 도구를 구조적으로 뺀 **읽기 전용**(분석·모니터링, AI 마켓플레이스 등재용)과 자동매매용 **전체 권한**. 브로커는 배포 단위로 **끔/읽기 전용/전체** 중 고른다.
- 민감한 동작은 **명시적 확인 흐름**을 거친다. 에이전트는 **자기 트레이더의 계좌에만** 접근.

## 왜 중요한가
이번 주만 Match-Trader(10/5), B2TRADER(10/6), Axi(10/7)가 연달아 MCP를 냈다. 흐름은 분명하다 — **“AI가 내 계좌를 본다”는 이제 기본, 경쟁 포인트는 권한 설계**다. 개인 트레이더라면 처음엔 **읽기 전용으로 ‘리스크 점검 비서’**처럼 쓰고(노출·증거금·손절 누락 체크), 주문 권한은 소액 계좌에서 확인 절차를 검증한 뒤 여는 순서를 권한다. 레버리지 CFD는 원금 이상 손실 위험이 있다는 점도 그대로다.

출처: [Axi MCP 발표](https://www.axi.com/int/blog/company-news/axi-launches-mcp-integration-mt5-claude) · [B2TRADER MCP·AI Chat](https://b2broker.com/news/b2trader-goes-ai-native-with-mcp-support-and-ai-chat/)
