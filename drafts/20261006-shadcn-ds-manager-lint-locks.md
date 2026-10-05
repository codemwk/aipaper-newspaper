---
title: "디자인/UI·UX: shadcn DS Manager — 에이전트가 ‘바꿔도 되는 것’을 표로 잠근다, Lint·Locks와 205개 ProBlocks"
date: 2026-10-06T07:09:00+09:00
category: "디자인/UI·UX"
slug: "shadcn-ds-manager-lint-locks"
summary: "10/4 shadcndesign DS Manager 업데이트: Lint 규칙 6종(Off/Warn/Block)과 컴포넌트×7개 변경 유형 Locks 표를 design-system.lint.json으로 배포, ESLint/Oxlint로 Claude Code·Cursor에도 강제. 내 토큰으로 스타일된 페이지 블록 205개(24카테고리), Pro는 에이전트가 커스텀 컴포넌트 제작. 캔버스 반영 345→103ms. Pro $19/월."
---

## 한줄 요약
shadcn/ui 기반 디자인 시스템을 웹에서 관리하는 [DS Manager](https://www.shadcndesign.com/blog/shadcn-design-system-blocks-lint-custom-components)가 10월 4일 큰 업데이트를 냈다. 핵심은 **Lint** — 에이전트가 디자인 시스템에서 **무엇을 바꿔도 되고 무엇은 안 되는지**를 사람이 적어 두고, 에이전트가 그걸 지키게 만든다.

## Lint: 규칙과 잠금
- **Rules 6종**: 재스타일링, 원시 색상(raw colors), 임의 크기, 인라인 스타일, 오타, 동적 클래스. 각각 Off·Warn·Block, 또는 Relaxed·Balanced·Strict 프리셋. 예: `text-rose-500`은 잡고 `text-destructive`를 요구.
- **Locks 표**: 컴포넌트와 그 부품을 **레이아웃·색·타입·간격·모양·효과·모션** 7가지 변경 유형과 교차시킨 표. 셀을 눌러 잠근다.
- Block이면 에이전트가 거절하며 이유를 댄다(“Locked. Agents can't change Color on Button.”). Warn이면 수정하되 경고를 붙인다. ‘Try a change’로 에이전트가 받을 답을 미리 볼 수 있다.
- 규칙은 `design-system.lint.json`으로 함께 배포되고, **ESLint/Oxlint 설정**으로 프로젝트에 깔리면 Claude Code·Cursor 같은 외부 에이전트도 같은 규칙에 걸린다. Lint는 무료 계정 포함 전원.

## 그 밖의 변화
- **ProBlocks 205개(24카테고리)**: 히어로~푸터 랜딩 블록이 **내 색·폰트·radius·아이콘·로고**로 렌더된다. 1280·768·390px 미리보기, `npx shadcn@latest add @your-system/hero-section-1` 한 줄 설치. 무료는 카테고리당 1개(24개).
- **커스텀 컴포넌트(Pro)**: 컬러 피커처럼 shadcn에 없는 컴포넌트를 에이전트가 React+TS로 만들고 검사한다. 4번 실패하면 드래프트로 격리 — 통과 전엔 레지스트리에 안 들어간다.
- 캔버스 반영 속도 약 345ms → **103ms**. Pro $19/월·$180/년.

## 왜 중요한가
어제 소개한 Frappe UI(SKILL.md)·impeccable(안티패턴 탐지)이 “에이전트에게 디자인 원칙을 **알려 주는**” 쪽이었다면, DS Manager는 **“어기면 막는”** 쪽이다. 문서는 무시될 수 있지만 린터는 CI에서 빨간불을 켠다. 디자인 시스템의 다음 산출물은 피그마 파일이 아니라 **잠금 표 + 린트 설정**이 될 가능성이 크다.

## 기억할 것
- Lint는 현재 기본 컴포넌트 대상(커스텀·블록은 추후).
- [shadcndesign 블로그 10/4](https://www.shadcndesign.com/blog/shadcn-design-system-blocks-lint-custom-components)
