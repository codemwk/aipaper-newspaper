---
title: "디자인/UI·UX: Figma ‘Build by design’ — 코드 레이어 오픈 베타, 마크다운을 캔버스로 끌어온 ‘Specs’, 디자인 시스템에 코드 소스·가이드라인까지"
date: 2026-10-16T07:05:00+09:00
category: "디자인/UI·UX"
slug: "figma-code-layers-specs"
summary: "Figma(10/15, Dylan Field): ① Code layers 오픈 베타(전 플랜) — 디자인→코드 변환, 로컬 폴더·GitHub·MCP·크롬 확장으로 코드 프로토타입을 캔버스에. ② Specs 오픈 베타(유료 플랜) — 마크다운 컨텍스트를 멀티플레이어로, 프레임·FigJam 임베드, MCP로 코딩 에이전트에 전달. ③ 디자인 시스템: 가이드라인(오픈 베타)·GitHub/npm 코드 소스(클로즈드 베타), system map·system check 프리뷰. ④ Figma Make에 Payload CMS. ⑤ MCP 업데이트 + 파트너 통합 20개."
---

## 한줄 요약
Figma CEO Dylan Field의 진단: AI 덕에 코딩이 싸지자 팀들은 **“생각하려고 만든다(building to think)”**. 그런데 바이브코딩 프로토타입은 혼자 만들고 링크만 공유하니 **과정이 안 보인다** — “빠르고, 빠르고, 빠르다가… 느려진다.” 2026-10-15 발표된 ‘Build by design’은 그 코드와 맥락을 **다시 캔버스 위로** 끌어오는 묶음이다([Figma 블로그](https://www.figma.com/blog/build-by-design/)).

## 발표 5가지
1. **Code layers — 오픈 베타, 모든 플랜**: 기존 디자인을 동작하는 코드로 변환, 로컬 폴더 업로드, MCP로 코딩된 프로토타입 가져오기, GitHub 임포트, 크롬 확장으로 **라이브 웹사이트 캡처**. 코드 기반 아이디어를 팀이 캔버스에서 같이 만진다.
2. **Specs — 오픈 베타, 유료 플랜(웹·데스크톱·모바일)**: 에이전트 시대의 공용어가 된 **마크다운**을 위한 “캔버스 위 컨텍스트 컨테이너”. FigJam 파일·프레임·노드를 스펙 안에 임베드해 글과 디자인을 나란히 둔다. 스펙을 복제해 각자 버전을 쓰고 합칠 수 있고, Figma MCP로 **코딩 에이전트에 넘기거나** 스펙에서 바로 코드 레이어를 만든다. GitHub 커넥터로 코드베이스 기반 기술 스펙 초안도 가능([Specs 소개](https://www.figma.com/blog/introducing-figma-specs/)).
3. **디자인 시스템 확장**: 라이브러리에 **가이드라인**(오픈 베타)을 붙이고, GitHub 저장소·npm 패키지에서 **코드 소스**(클로즈드 베타)를 가져와 에이전트가 컴포넌트를 더 정확히 만들게 한다. 라이브러리를 한곳에서 관리하는 공간을 프리뷰 — **system map**(변경·의존 추적), **system check**(설명·인터랙션 상태 누락 스캔).
4. **Payload in Figma Make**: 작년 합류한 오픈소스 헤드리스 CMS Payload를 Make에 통합. 마케터가 소스코드 없이 콘텐츠를 고치고, 데이터·관리자 패널·API가 Figma 호스팅에 함께 산다. 전 플랜, 수주에 걸쳐 배포.
5. **Figma MCP 업데이트**: 외부 AI 도구에서 코드 레이어 생성·Specs 작업·이미지 생성·Weave 워크플로 실행. 오류와 토큰 사용을 줄였다고 하며, OpenCode·Dia·JetBrains Junie·Meta Muse 등 **파트너 통합 20개** 추가.

## 왜 중요한가
10/6 GA된 Figma 에이전트가 “캔버스 안의 일꾼”이었다면, 이번엔 **에이전트가 읽는 재료(스펙·가이드라인·코드 소스)**를 Figma가 소유하려는 수다. 디자인 시스템이 이제 사람용 문서가 아니라 **에이전트용 규칙집**이 된다는 흐름(10/13 DESIGN.md, 오늘 TypeUI·Nova)과 정확히 맞물린다. 실무 체크포인트: Specs·코드 소스가 유료 플랜 전용이고, 에이전트 작업은 10/12에 다룬 AI 크레딧 체계 위에서 돈다는 점.

출처: [Figma — Build by design](https://www.figma.com/blog/build-by-design/) · [Figma — Introducing Specs](https://www.figma.com/blog/introducing-figma-specs/)
