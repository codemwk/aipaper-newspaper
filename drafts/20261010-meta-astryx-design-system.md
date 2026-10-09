---
title: "디자인/UI·UX: Meta Astryx 오픈소스 베타 — 8년·1.3만+ 앱이 쓰던 디자인 시스템을 ‘사람과 에이전트가 같은 CLI’로"
date: 2026-10-10T07:10:00+09:00
category: "디자인/UI·UX"
slug: "meta-astryx-design-system"
summary: "facebook/astryx(~13.6K★) 퍼블릭 베타. Meta 내부 8년, 13,000+ 앱. React 19+·StyleX, 150+ 접근성 컴포넌트, 테마 7종, swizzle로 소스 이젝트. 사람·AI가 같은 docs/CLI로 빌드하도록 설계. MIT."
---

## 한줄 요약
Meta가 사내에서 가장 크고 많이 쓰인 디자인 시스템 **Astryx**를 오픈소스 베타로 공개했다. README는 **8년**, **13,000개 이상** 앱, **150+** 접근성 컴포넌트를 명시한다([facebook/astryx](https://github.com/facebook/astryx), 문서 [astryx.atmeta.com](https://astryx.atmeta.com)).

## 무엇이 ‘에이전트 레디’인가
- **같은 레퍼런스**: API·문서·CLI를 한세트에 맞춰 “사람과 AI 어시스턴트가 **같은 방법**으로 만든다”고 적었다.
- **구조화 조회**: `@astryxdesign/cli`로 컴포넌트 목록·문서·테마·스캐폴딩. 에이전트가 프롭을 추측하지 않고 **문서화된 계약을** 읽게 하려는 설계.
- **잠금 해제**: StyleX로 쓰였지만 소비자에겐 빌드 플러그인 없이 CSS import + typed React. `className`으로 Tailwind·CSS Modules와 공존. `swizzle`로 컴포넌트 **전체 소스를 프로젝트에 꺼낸다**.
- **테마**: CSS 커스텀 프로퍼티 오버라이드 — 포크 없이 브랜드 색·타이포. neutral·butter·matcha 등 **7개** 테마 패키지.

## 숫자·라이선스
공개 시점 기준 저장소 스타는 **약 1.36만**. MIT. peer는 **React 19+**.

## 왜 중요한가
Figma 에이전트·ProtoPie MCP가 “캔버스에서 팀 컴포넌트만 쓰게” 했다면, Astryx는 **코드 쪽 디자인 시스템**을 에이전트 API로 열어 준다. “토큰·프롭을 환각하지 말고 CLI/문서를 물어라”는 문법은 Graphical·Mate DESIGN.md와 같은 계열이다.

출처: [facebook/astryx](https://github.com/facebook/astryx) · [Astryx docs](https://astryx.atmeta.com)
