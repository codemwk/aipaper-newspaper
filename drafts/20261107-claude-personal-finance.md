---
title: "AI 트레이딩: Claude Personal Finance — Plaid로 계좌 연결, 읽기 전용 소비·청구 분석 미국 베타"
date: 2026-11-07T07:10:00+09:00
category: "AI 트레이딩"
slug: "claude-personal-finance"
summary: "Anthropic이 11/5 전후 Claude Personal Finance 베타를 열었다. 미국 Pro·Max·Ultra가 Plaid로 은행·카드를 연결해 잔액·최대 2년 거래를 묻고, Claude는 이체·투자를 할 수 없다. 허브 대화는 모델 학습에 쓰이지 않는다고 밝혔다."
---

## 한줄 요약
MT5 에이전트가 “주문”을 만진다면, Claude **Personal Finance**는 **가계부를 읽기만** 한다. 미국 Pro/Max/Ultra 대상으로 롤아웃 중이며, Plaid로 직접 로그인해 읽기 전용 동의를 준다([Anthropic](https://claude.com/resources/articles/introducing-personal-finance-in-claude), [TechCrunch 11/5](https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/)).

## 할 수 있는 것
- “이번 달 돈이 어디로 갔나”, 전월 대비, 급여 전 잔여, 이중 청구·수수료·슬며시 오른 구독.
- 주간 차트·청구 캘린더·대시보드를 대화로 조정.
- 보는 데이터(연결한 계좌만): 은행명, 계좌명/유형/끝 4자리, 잔액·한도, **최대 2년 거래**.
- **못 하는 것**: 이체, 자산 운용, 카드·대출·예금 상품 판매. 광고·스폰서 추천 없음(회사 주장).

## 프라이버시
Personal Finance **허브 안** 대화는 모델 학습에 사용하지 않는다고 명시. 허브 밖은 기존 프라이버시 설정. 연결 해지 시 해당 데이터 접근 종료. 은행 비밀번호는 Claude가 받지 않는다(Plaid 경유).

## 왜 중요한가
트레이딩 MCP 스택과 다른 축 — **개인 재무 읽기 에이전트** — 가 빅모델 제품에 들어왔다. “다음엔 라이선스 금융사와 함께 큰 결정”이라고 Anthropic도 적어, 규제 샌드박스형 확장을 예고한다.

## 주의
투자 자문 아님. 숫자 오류 가능 — 거래 원문을 물어보고 은행 앱과 대조. 현재 **미국 플랜 한정** 베타.
