---
title: "Design: Figma Code Connect — MCP에서 토큰 29.5%↓, Coinbase도 같은 패턴"
date: 2026-09-27T07:03:00+09:00
category: "Design/UI·UX"
slug: "figma-code-connect-mcp-tokens"
summary: "Figma 공식 평가: Code Connect+MCP 시 중앙값 토큰 -29.5%, 작업시간 -19.6%, 코드품질 Likert +1. Coinbase CDS도 컴포넌트 날조 감소. 디자인→코드에 ‘프로덕션 import’를 넣는 구조."
---

## 한줄 요약
[Figma 공식 블로그](https://www.figma.com/blog/the-benefits-of-code-connect-in-mcp/)에 따르면, 코딩 에이전트가 Figma MCP `get_design_context`를 쓸 때 **Code Connect**가 있으면 중앙값 기준 **토큰 29.5% 감소·작업 시간 19.6% 단축·코드 품질 1점 상승**(1–4 Likert). Coinbase Design Systems도 “progress bar로 stepper를 날조”하던 문제가 import 정확도로 줄었다고 전한다.

## 핵심 구조
- **문제**: MCP가 주는 React는 시각적으로 맞아도, 팀 DS 컴포넌트와 무관한 **원시 div/CSS**를 에이전트가 새로 짜는 경우가 많음.
- **해결**: Code Connect 템플릿이 Figma 컴포넌트↔코드베이스 컴포넌트를 매핑하면, 응답에 **실제 import·props**가 들어감.
- **평가**: 27개 케이스, Claude Sonnet 4.5·Opus 4.7. SDS(커버리지 높음) vs 내부 FPL(패치형) 비교 — **커버리지가 높을수록** 탐색 grep·토큰 낭비가 줄었다.

## 왜 중요한가
“예쁜 목업”이 아니라 **커밋 가능한 코드**가 목표일 때, DS 매핑이 곧 비용·품질 레버다. AiPaper·대시보드처럼 반복 UI가 많은 제품일수록 Code Connect 투자가 ROI로 바로 잡힌다.

## 기억할 것
- [Better Code, Fewer Tokens](https://www.figma.com/blog/the-benefits-of-code-connect-in-mcp/) · [Code Connect + MCP docs](https://developers.figma.com/docs/figma-mcp-server/code-connect-integration/)
