---
title: "디자인/UI·UX: Google DESIGN.md(~28K★) — 코딩 에이전트용 ‘시각 정체성’ 포맷, 토큰 YAML + 린트/내보내기 CLI"
date: 2026-10-13T07:07:00+09:00
category: "디자인/UI·UX"
slug: "design-md-agent-format"
summary: "google-labs-code/design.md ~28,351★(2026-10-13). 에이전트가 디자인 시스템을 지속 이해하도록 색·타이포·간격·라디우스·컴포넌트 토큰을 YAML 프론트매터+마크다운으로 적는 스펙. `npx @google/design.md lint|export`(DTCG·Tailwind). Stitch 이야기의 ‘포맷 레이어’가 따로 크는 중."
---

## 한줄 요약
Figma 파일이 사람에게 디자인 시스템이라면, 에이전트에게는 **읽을 수 있는 계약서**가 필요하다. Google Labs의 [DESIGN.md](https://github.com/google-labs-code/design.md)는 그 계약서 스펙이다. 2026-10-13 `gh` 기준 **~28,351★**.

## 어떻게 동작하나
- **구성**: YAML 프론트매터에 색·타이포·스페이싱·라디우스·컴포넌트 토큰(규범), 마크다운 본문에 사용법·근거. 토큰 참조는 `{colors.primary}` 형태.
- **툴링**: `npx @google/design.md lint DESIGN.md`, `export --format dtcg` 및 Tailwind v3 JSON / v4 CSS 내보내기(공식 README·스펙).
- **위치**: 9월 Stitch·브랜드 키트 기사에서 스치듯 나왔지만, 지금은 **에이전트 핸드오프 포맷 자체**가 독립 저장소로 **2.8만★**대다. Linear 등도 에이전트용 design.md 실험을 이어 온 흐름과 맞물린다.

## 왜 중요한가
캔버스 에이전트(Figma)·사이트 에이전트(Framer)·슬라이드 에이전트(PPT Master)가 늘수록, **“우리 브랜드 규칙”을 어디에 두느냐**가 병목이 된다. DESIGN.md는 그 답을 **레포 안의 텍스트 파일**로 옮긴다 — PR로 리뷰 가능, CI로 린트 가능. 한계는 포맷이 **알파·스펙**이고, 실제 픽셀 품질은 여전히 렌더러·에이전트 구현에 달렸다는 점이다.

## 기억할 것
- 스타 ≠ 채택. 팀 토큰 소스 오브 트루스(Figma Variables 등)와의 **동기화 파이프**가 없으면 문서만 쌓인다.
- DTCG보내기는 디자인·엔지니어 공통언어로 가는 다리로 읽으면 된다.

출처: [GitHub google-labs-code/design.md](https://github.com/google-labs-code/design.md) · [스펙(raw)](https://raw.githubusercontent.com/google-labs-code/design.md/main/docs/spec.md)
