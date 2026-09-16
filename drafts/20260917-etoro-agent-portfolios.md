---
title: "eToro Agent Portfolios — 하위 계좌·스코프 토큰으로 에이전트 자율매매"
date: 2026-09-17T07:15:00+09:00
category: "AI Trading"
slug: "etoro-agent-portfolios"
summary: "eToro Builders. 전략별 Agent Portfolio 생성, 위임 토큰 mint·갱신·폐기. 승인된 한도 안에서 AI가 포지션 운용. REST·MCP 에디터 워크플로. 격리·감사 로그가 제품의 핵심."
---

## 한줄 요약
[eToro Builders — Agent Portfolios](https://builders.etoro.com/products/agent-portfolios)는 사용자가 **격리된 에이전트 포트폴리오**를 만들고, **범위가 한정된·폐기 가능한** 위임 토큰으로 AI가 대신 거래하게 하는 API 표면이다.

## 무엇이 제공되나
- 포트폴리오 생성·목록·삭제 — 전략·유스케이스별로 분리.
- 위임 유저 토큰 **mint / update / revoke**, 스코프·수명·사용 이력 추적.
- 빌더 시나리오: 리스크 경계 안 코파일럿, 멀티전략(포트폴리오별 격리), 리밸런싱 자동화, 엔터프라이즈 감사.
- 도구: REST Playground, 인증 가이드, **MCP + AI 에디터**(Cursor·Claude Code 등).
- Finance Magnates 등 업계 보도는 MT5와 대비해 eToro를 “한도 안 **자율 체결**” 축으로 분류한다.

## 왜 중요한가
“에이전트가 거래한다”는 말이 MCP 툴 나열만으로 끝나지 않는다. eToro는 **계좌 격리 + 토큰 스코프 + 철회**를 제품 기본값으로 둔다. 자동매매·프롭·개인 에이전트 빌더는 “어느 권한이 기본인가”를 MT5(연구·수동 컨펌)·cTrader(MCP 실행)·eToro(위임 포트폴리오) 삼각으로 비교해야 한다.

## 기억할 것
- 제품: [Agent Portfolios](https://builders.etoro.com/products/agent-portfolios)
- 이용자 안내: [eToro Agent Portfolios 업데이트](https://www.etoro.com/news-and-analysis/etoro-updates/agent-portfolios-let-your-ai-agent-trade-for-you/)
