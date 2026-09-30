---
title: "디자인/UI·UX: Figma — 생성형 플러그인·셰이더를 Community에 배포하고 MCP로 React까지"
date: 2026-10-01T07:02:00+09:00
category: "디자인/UI·UX"
slug: "figma-generative-shaders-mcp"
summary: "Figma 공식 블로그(2026-09-01). Config 이후 생성형 플러그인·셰이더 업데이트: Community/조직 퍼블리시, 애니·인터랙티브 셰이더, 코드 뷰어, MCP로 에이전트가 플러그인·셰이더 읽고 React로 정확히 내보내기. Design Agent 오픈 베타."
---

## 한줄 요약
[Figma 블로그](https://www.figma.com/blog/how-we-built-generative-plugins-and-shaders/)(2026-09-01, Rogie King)에 따르면 Config 2026에서 선보인 **생성형 플러그인·셰이더**가 한 단계 커졌다. 에이전트로 만든 도구를 **Community 또는 조직 내부**에 퍼블리시하고, 셰이더에 **모션·마우스 반응**을 넣고, 코드를 열어 내려받으며, **Figma MCP**로 외부 에이전트가 이를 읽고 **React에 셰이더가 맞게** 구현할 수 있다.

## 제품으로 보면
- **에이전트 표면**: Design Agent가 레이아웃 생성·렌즈 왜곡 같은 **커스텀 툴**을 캔버스 옆 Tools 사이드바에 붙인다.
- **핸드오프**: MCP로 디자인 컨텍스트를 읽고 셰이더를 HTML/React로 내보내기 — "캔버스 위 코드 ≈ 디자인".
- **가용성**: Full seat 전 플랜 오픈 베타(Collab/Dev/View는 drafts). 베타 중 AI 무료, 곧 **AI 크레딧** 소모 예정(블로그).
- **조직 통제**: 8월 GA된 company-managed MCP 권한과 맞물려 IdP로 에이전트 연결을 중앙 관리하는 흐름([iMasters 정리](https://imasters.com/design-ux/what-changed-in-figma-for-squads-that-already-design-with-ai-in-the-flow)).

## 왜 중요한가
디자인 시스템이 "문서"가 아니라 **에이전트가 실행하는 도구 패키지**가 된다. Penpot MCP·OpenPencil 축과 함께, 에이전트 친화 캔버스 경쟁이 **읽기→쓰기→배포**로 넘어간 신호다.

## 기억할 것
- [Figma Blog](https://www.figma.com/blog/how-we-built-generative-plugins-and-shaders/) · playground 파일(블로그 링크)
