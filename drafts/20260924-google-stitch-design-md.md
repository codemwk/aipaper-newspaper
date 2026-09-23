---
title: "Design: Google Stitch DESIGN.md — 디자인 시스템을 AI가 읽는 개방 포맷으로"
date: 2026-09-24T07:03:00+09:00
category: "Design / UI·UX"
slug: "google-stitch-design-md"
summary: "Google Labs Stitch. DESIGN.md 초안 스펙 오픈소스(2026-04-21). I/O 업데이트(2026-05-19): 실시간 스트림·음성/텍스트 에이전트, AI Studio 공유, Antigravity·Netlify 내보내기. 색의 의도·WCAG 검증을 AI가 공유 언어로."
---

## 한줄 요약
[Google Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)의 **DESIGN.md**가 오픈소스 초안이 됐다. 색이 “예쁜 값”이 아니라 **용도·접근성 규칙**을 담은 공유 언어가 되어, 도구를 바꿔도 AI가 같은 디자인 시스템을 읽게 하려는 시도다.

## 핵심
- **DESIGN.md 오픈소스**(2026-04-21): Stitch 프로젝트 간에 디자인 규칙을 import/export. 에이전트가 색의 목적과 WCAG 검증을 이해하도록 설계([발표](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/)).
- **실시간 바이브 디자인**(2026-05-19 I/O): Stitch Agent가 캔버스에 작업을 스트리밍. 텍스트·음성으로 조향. Google AI Studio로 공유 링크, **Antigravity**로 백엔드 연결 또는 **Netlify** 퍼블리시([업데이트](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/)).

## 왜 중요한가
Figma가 “캔버스 안의 에이전트”라면, Stitch/DESIGN.md는 **디자인 시스템을 파일로 들고 다니는 쪽**이다. 에이전트 UI 생성물이 브랜드·접근성을 깨지 않으려면, 프롬프트보다 **기계가 읽을 규칙 파일**이 필요하다.

## 기억할 것
- [DESIGN.md 오픈소스](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/) · [실시간 Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/)
