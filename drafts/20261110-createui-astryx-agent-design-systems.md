---
title: "디자인: ‘에이전트가 지어내지 못하게’ — CreateUI는 Figma↔React 토큰 97% 일치+MCP, Meta Astryx는 코어 0.7.4에 주간 13.5만 다운로드"
date: 2026-11-10T07:25:00+09:00
category: "디자인"
slug: "createui-astryx-agent-design-systems"
summary: "디자인 시스템이 ‘에이전트용 어휘집’으로 팔리기 시작했다. CreateUI는 컴포넌트 80+·변형 18,500+·변수 950+의 Figma 파일과 Tailwind+Radix 기반 React 라이브러리를 97% 토큰 일치로 묶고 MCP·스킬 파일을 붙였다. 10월 다룬 Meta Astryx는 코어 0.7.4가 이번 주 배포됐고 npm 주간 다운로드 약 13.5만을 기록 중이다."
---

## 한줄 요약
코딩 에이전트가 UI를 만들 때 가장 흔한 실패는 **없는 스타일·없는 컴포넌트를 지어내는 것**이다. 이번 주 두 소식은 같은 처방을 낸다: 사람과 에이전트가 **같은 사전**을 보게 하라.

## CreateUI — Figma 파일과 React 코드를 한 몸으로
- **규모**: 핵심 컴포넌트 80개 이상, 크기·상태·인터랙션 변형 **18,500개 이상**, 시맨틱 색·4px 그리드 간격·타입 위계를 담은 변수·스타일 **950개 이상**.
- **코드**: Tailwind CSS + Radix UI 기반 설치형 React 라이브러리. Figma와 코드의 토큰 일치도 **97%**(회사 주장).
- **반응형·테마**: 데스크톱(1280px+)·태블릿(768–1279px)·모바일(320–767px) 3단 브레이크포인트, 라이트/다크 테마 20종 이상, Remix 아이콘 3,200개 이상.
- **에이전트용**: MCP 지원과 ‘스킬’ 파일로 에이전트가 이 시스템의 컴포넌트·토큰을 직접 쓰게 한다. 개인·팀 단위 유료 티어로 판매([TheNextGenTechInsider, 11/6](https://thenextgentechinsider.com/pulse/createui-syncs-figma-and-react-with-new-ai-native-design-system-and-component-library)).

## Meta Astryx — 오픈소스 한 달 뒤
10/10에 다룬 Meta의 사내 디자인 시스템 Astryx(8년, 13,000개 이상 앱, 접근성 컴포넌트 150개 이상, MIT)는 이번 주 코어 패키지 **0.7.4**(1.0 이전)가 나왔고 npm 주간 다운로드가 **약 13.5만**이라고 Babelwire가 전했다. 핵심 설계는 그대로다: `astryx init`이 **AGENTS.md나 CLAUDE.md에 컴포넌트 색인을 써 넣어** 에이전트가 컴포넌트·템플릿·토큰을 ‘발견’하게 하고, CLI가 문서 제공·템플릿 생성·버전 간 코드모드를 맡는다. 제약도 여전하다: React 19 필수, 차트 컴포넌트는 카나리 전용, Node 22+·pnpm 11([Babelwire, 11/9](https://babelwire.ai/en/story/meta-astryx-open-source-design-system-2026-11-09)).

## 왜 중요한가
지난번 저장하신 Meta Astryx·DESIGN.md 계열과 이어지는 소식이다. 흐름은 분명하다. 디자인 시스템의 고객이 디자이너·개발자에서 **에이전트까지** 넓어지고, 상품의 핵심이 Storybook과 Figma 키트에서 **기계가 읽는 API·문서·컨텍스트 파일**로 옮겨 간다. “더 좋은 프롬프트”보다 **작고 의견이 분명한 어휘집**이 AI UI의 일관성을 지킨다는 베팅이다.

## 주의
CreateUI 수치(97% 일치 등)는 회사 자료 기반이고 독립 검증은 없다. Astryx 다운로드 수는 보도 기준이며 직접 확인하지 않았다.
