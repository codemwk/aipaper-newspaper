---
title: "AI 트레이딩: Ludus — 주문은 안 하고, MCP로 ‘논지·저널·레이팅’만 공개판에 올리는 에이전트 보드"
date: 2026-10-11T07:09:00+09:00
category: "AI 트레이딩"
slug: "ludus-trading-mcp"
summary: "Ludus(ludus.trading)가 10/8 MCP 접속 가이드 공개. free desk 키 발급→MCP URL→이메일 인증으로 Seat. 테시스(주장·근거·무효화 조건) 공개, 피어 반박, 자기보고 저널. 주문·키 보관 없음. Seat 리스트 $27, 런치 중 인증 시 무료(카드 없음)라고 명시."
---

## 한줄 요약
**Ludus**는 트레이딩 에이전트를 위한 **공개 보드+비공개 저널+레이팅 사다리**다. **주문을 대행하지 않고**, 브로커·거래소 키도 보관하지 않는다. 에이전트는 **MCP**로 붙여 논지(thesis)를 올리고 다른 에이전트 반박을 읽는다([가이드 2026-10-08](https://ludus.trading/blog/join-ludus-via-mcp/)).

## 접속 흐름 (공식 포스트)
1. `POST https://api.ludus.trading/api/desks/free`로 **desk 키** 발급(`opt_in_agent_platform` 필수). 키는 **한 번만** 표시.
2. Cursor 등 MCP 클라이언트에 `https://mcp.ludus.trading/d/{desk_id}/mcp` + `Authorization: Bearer …`. 다중 에이전트면 **데스크별 URL** 권장.
3. 이메일을 인증하면 **Spectator→Seat**. Seat 리스트 가격 **$27**, 런치 기간에는 인증만으로 **complimentary·카드 불필요**라고 적음(플랜 페이지로 재확인).
4. `whoami` → 거래 경로 선언 → `thesis_rubric` → `recommended_jobs`(프리오픈·애프터클로즈 루틴).

## 돈이 아니라 ‘평판’이 흐르는 구조
- **Gloria** 사다리: 참여·기록된 트레이드에 반응(계좌 크기 아님).
- **Denarii**: 인앱 읽기 크레딧(현금 아님).
- 챌린지 시드(~$50 언급)는 **참가자 본인 브로커에 남음** — Ludus가 수탁하지 않음.
- 저널은 **자기보고**. 피어 리뷰≠감사. Kalshi/Polymarket 등 벤더 예시는 **제휴 아님**.

## 왜 중요한가
eToro MCP·Catalyst가 “실행·승인” 쪽이었다면, Ludus는 **실행 전 논지를 공개 기록**하게 강제한 **소셜·연구 레이어**다. 자동화 트레이딩 OS에 “왜 들어갔는지” 모듈이 빠졌을 때 붙일 수 있는 부품이다. 투자 자문 아님·손실 가능 — 공식 디스클로저를 그대로 따른다.

출처: [Join Ludus via MCP](https://ludus.trading/blog/join-ludus-via-mcp/) · [ludus.trading](https://ludus.trading)
