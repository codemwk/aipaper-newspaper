---
title: "디자인/UI·UX: Design Systems MCP — 에이전트가 ‘추측 UI’ 대신 토큰·컴포넌트를 조회"
date: 2026-09-29T07:10:00+09:00
category: "디자인/UI·UX"
slug: "design-systems-mcp"
summary: "southleft/design-systems-mcp 등. MCP로 컴포넌트·토큰·패턴·베스트프랙티스를 툴로 노출. Penpot·Figma MCP와 같은 ‘파일/시스템 진실 소스’ 흐름. 에이전트 UI의 환각을 거버넌스로 줄임."
---

## 한줄 요약
에이전트가 버튼을 “예뻐 보이게” 새로 그리는 대신, **실제 디자인 시스템의 props·토큰·패턴**을 조회하게 만드는 MCP 서버가 늘고 있다. 대표적으로 [southleft/design-systems-mcp](https://github.com/southleft/design-systems-mcp)(전용 디자인 시스템 어시스턴트)와 오픈 스타터 템플릿들이 “추측 UI”를 줄이는 쪽이다.

## 패턴
- **진실 소스**: Storybook·토큰 JSON·문서 사이트를 MCP 리소스로 연결 → Claude·Cursor가 `list/get`으로 조회.
- **플랫폼 MCP와 보완**: Figma·Penpot MCP가 **파일 레이어**를 읽고, Design Systems MCP는 **거버넌스된 컴포넌트 계약**을 읽는다.
- **제품 팀 도구와 연결**: Magic Patterns 등은 Figma/Storybook 임포트 후 `@Library/Button`처럼 **라이브러리 프리셋**을 프롬프트에 고정하는 상용 경로를 보여 줌([Magic Patterns 2.0](https://www.magicpatterns.com/blog/series-a-and-magic-patterns-2-0)).

## 왜 중요한가
어제 Linear DESIGN.md·pen.dev·Penpot Enterprise가 “에이전트가 읽을 명세”였다면, 오늘은 **그 명세를 MCP 툴로 표준화**하는 레이어다. UI 품질은 모델보다 **조회 가능한 시스템**에서 나온다.

## 기억할 것
- [southleft/design-systems-mcp](https://github.com/southleft/design-systems-mcp) · [Magic Patterns 2.0](https://www.magicpatterns.com/blog/series-a-and-magic-patterns-2-0)
