---
title: "AI 트레이딩: 메리츠증권 ‘OPEN API’ 정식 출시 — Claude·ChatGPT 같은 AI에 말하면 시세 조회부터 실제 주식 주문까지. 기본은 ‘조회 전용’, 주문은 직접 켜고 매번 확인"
date: 2026-10-27T07:04:00+09:00
category: "AI 트레이딩"
slug: "meritz-open-api-mcp"
summary: "메리츠증권이 10/26 MCP를 붙인 ‘OPEN API’를 정식 출시(10/12~25 시범 운영). ‘Trading MCP’는 국내외 시세·잔고 조회와 주문 실행, ‘Coding Assistant MCP’는 원하는 기능을 설명하면 API를 찾아 자동매매 코드 작성을 돕는다. 대상은 Super365·종합매매 계좌 개인 고객. 기본 설정은 조회 전용이고, 주문은 이용자가 기능을 활성화해야 하며 주문 전 종목·수량·가격을 확인한다. API 이용료 무료, 거래 수수료는 기존 계좌 조건."
---

> 지난번 저장하신 MT5 + MCP 안전장치 기사들(MT5 Build 6060 매매 권한 설정, RiskGate)과 이어지는 소식입니다 — 같은 구조가 국내 증권 계좌에 들어왔습니다.

## 한줄 요약
해외 브로커·MT5 이야기였던 **“AI 에이전트가 내 계좌로 주문”**이 국내 증권사 정식 서비스가 됐다. 메리츠증권이 OPEN API에 AI 연결 규격 MCP를 결합해 **10/26 정식 출시**했다([디지털데일리](https://www.ddaily.co.kr/page/view/2026102609080546806)).

## 무엇을 할 수 있나
- **Trading MCP**: 국내외 주식 시세 조회, 계좌 보유 수량·평가금액 정리, **매수·매도 주문 실행**.
  - 예: “삼성전자와 엔비디아 주가 흐름 비교해 줘”, “내 보유 종목 정리해 줘”.
- **Coding Assistant MCP**: “이런 기능이 필요해”라고 설명하면 관련 API를 찾아 **프로그램 코드 작성**을 돕는다.
  - 예: 설정 가격 도달 시 알림, 거래량 급증 종목 찾기, 매수·매도 조건을 넣어 **내가 안 보는 시간에도 주문**.

## 쓰는 방법
1. 메리츠증권 **Super365 또는 종합매매 계좌**(개인) 필요. 금융상품 전용 종합매매 계좌는 제외.
2. OPEN API 포털에서 신청 → 개인 인증정보 **APP KEY / APP SECRET** 발급.
3. MCP를 지원하는 AI 프로그램에 기능을 설치하고 인증정보 등록.
- 비용: **OPEN API 무료**, 거래 수수료는 기존 계좌 조건. Super365의 국내주식 온라인 수수료 무료 혜택은 올해 말까지 OPEN API 거래에도 적용.

## 안전장치는 어디에
| 장치 | 내용 |
|---|---|
| 기본값 | **조회 전용** 설정 사용 가능 |
| 주문 | 이용자가 **직접 기능을 활성화**해야 함 |
| 주문 직전 | 종목·수량·가격 **확인 절차** |
| 자동매매 | 별도 실행 환경·거래 설정 필요, AI가 만든 코드는 사용 전 검증 필요(회사 안내) |
- 비교: 유럽 Freedom24도 8월 MCP를 열면서 **모든 주문에 고객 확인**, 이체·출금은 MCP로 불가, API 키는 고객이 보관하는 방식을 택했다([FinTech Futures](https://www.fintechfutures.com/ai-in-fintech/freedom24s-ceo-on-ai-trust-and-owning-the-stack)). MT5도 AI 매매를 허용/확인 요청/금지 중 고르게 돼 있다([MT5 도움말](https://www.metatrader5.com/en/terminal/help/mcp_and_ai)).

## 써 보기 전 체크리스트
- **APP SECRET은 비밀번호급.** 에이전트 설정 파일·공유 저장소·노트(Obsidian 볼트 포함)에 평문으로 두지 말 것.
- **‘확인 절차’가 어디서 뜨는지 먼저 확인.** 사람이 보는 대화창에서 확인하는 것과, 내가 만든 자동매매 코드가 혼자 도는 것은 위험이 전혀 다르다. 무인 자동매매는 금액·종목·횟수 상한을 코드에 직접 걸어 둘 것.
- **처음엔 조회 전용으로.** 시세·잔고 정리만으로도 쓸모가 크다. 주문 기능은 소액으로 충분히 시험한 뒤에.
- 행사: 11/2~12/31 OPEN API로 1회 이상 거래한 고객 선착순 2,000명에게 네이버페이 5,000포인트.

출처: [디지털데일리 — 메리츠증권 OPEN API 출시 (10/26)](https://www.ddaily.co.kr/page/view/2026102609080546806) · [FinTech Futures — Freedom24 (10/20)](https://www.fintechfutures.com/ai-in-fintech/freedom24s-ceo-on-ai-trust-and-owning-the-stack) · [MetaTrader 5 도움말 — MCP and AI](https://www.metatrader5.com/en/terminal/help/mcp_and_ai)
