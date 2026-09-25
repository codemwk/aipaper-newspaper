---
title: "Design: Primitiv — 디자인 시스템 ‘계약’을 MCP로 에이전트에"
date: 2026-09-26T07:06:00+09:00
category: "Design / UI·UX"
slug: "primitiv-design-system-mcp"
summary: "AI-by-design/primitiv(GitHub). 코드·Figma·Storybook에 흩어진 토큰·컴포넌트·규칙을 기계가독 계약으로 묶고 읽기전용 MCP로 노출. init/build/serve. Design-workflow 스킬과 페어. ‘검색’이 아니라 ‘조정(reconciliation)’."
---

## 한줄 요약
[Primitiv](https://github.com/AI-by-design/primitiv)는 “에이전트가 디자인 시스템을 **추측**하지 않게” 만드는 **계약(contract) 레이어**다. Retrieval이 데이터를 주고, Reconciliation이 진실에 맞춘다는 슬로건.

## 무엇을 하나
- **문제**: 토큰·컴포넌트·근거가 코드·Figma·Storybook·문서에 흩어지면 사람은 경험으로 맞추지만, 코딩 에이전트는 **제네릭 UI 패턴**으로 미끄러진다.
- **해법**: `init` → `build`(계약 생성) → `serve`(MCP 호환 에이전트에 읽기전용 제공). 충돌·드리프트·하드코딩 토큰 남용을 드러냄.
- **짝**: [Design-workflow](https://github.com/AI-by-design/Design-workflow) Claude Code/Cursor 스킬이 프로세스(빌드·감사)를, Primitiv가 **단일 진실 소스**를 담당.
- **포지션**: Figma Make·Stitch가 “화면 생성”이라면, Primitiv는 **이미 있는 시스템을 에이전트가 지키게** 하는 인프라.

## 왜 중요한가
생성형 UI가 늘수록 “새 화면”보다 **기존 디자인 시스템과의 정렬**이 제품 품질을 가른다. MCP로 계약을 노출하는 방식은 UserTesting·Framer External과 같은 ‘에이전트 네이티브 디자인 스택’ 흐름과 맞닿는다.

## 기억할 것
- [GitHub: primitiv](https://github.com/AI-by-design/primitiv) · [Design-workflow](https://github.com/AI-by-design/Design-workflow) · [primitiv.design](https://primitiv.design)
