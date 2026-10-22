---
title: "디자인/UI·UX: shadcn/ui ‘Trace’ — 에이전트가 한 일(생각·도구 호출·출처·계획)을 모두 ‘한 줄’ 모양으로 통일하다, AI Elements 21개 패턴 공개"
date: 2026-10-23T07:02:00+09:00
category: "디자인/UI·UX"
slug: "shadcn-trace-ai-elements"
summary: "shadcn/ui 10월 변경 로그: 새 컴포넌트 Trace(에이전트 단계 목록)와 Code Block(코드·터미널 출력·로그·diff), 그리고 에이전트 화면 패턴 모음 ‘AI Elements’(21개: Chat, Prompt Input, Reasoning, Tool, Plan, Subagent 등). 수백 개 에이전트 UI를 분석해 ‘에이전트가 한 일 + 결과’라는 공통 모양을 한 줄(아이콘·제목·설명·상태)로 정리. running/error/pending 상태, 펼치기·링크·대화상자, 중첩 지원, 키보드·스크린리더 지원. 패키지 설치 없이 코드를 복사해 쓰는 방식이고 모든 패턴 페이지가 Markdown으로도 제공돼 코딩 에이전트에 그대로 넘길 수 있다. 기존 AI SDK Elements는 폐기 예정."
---

## 한줄 요약
AI 앱 화면에서 가장 지저분해지기 쉬운 곳이 “에이전트가 지금 뭘 하는지” 보여 주는 부분이다. 생각(reasoning), 도구 호출, 참고 출처, 계획, 하위 에이전트… 앱마다 모양이 제각각이다. 인기 UI 컴포넌트 모음 **shadcn/ui**가 이걸 **‘Trace’라는 하나의 목록 모양**으로 통일했다([shadcn/ui 10월 변경 로그](https://ui.shadcn.com/docs/changelog/2026-10-ai-elements)).

## Trace는 무엇인가
- 팀은 **수백 개의 에이전트 화면 컴포넌트**를 연구해 공통점을 뽑았다: 결국 전부 “**에이전트가 한 일, 그리고 그 결과**”다.
- 그래서 각 단계는 **한 줄**: 아이콘 + 제목 + (선택) 설명 + 상태. 예: “pnpm --version 실행” / “pnpm install 실패” / “출처 2개 사용”.
- 상태: **실행 중(반짝임 효과)·오류·대기**. 줄을 누르면 펼쳐지거나, 다른 페이지로 가거나, 대화상자·시트가 열린다.
- **중첩**: 요약 한 줄 → 펼치면 단계들 → 단계를 펼치면 출력.
- 키보드와 스크린리더 접근성 기본 지원.

함께 나온 **Code Block**은 코드·터미널 출력·로그·diff를 보여 주는 상자다. Trace 안에 넣는 작은 크기도 있다.

## AI Elements: 21개 ‘에이전트 화면 패턴’
6월에 나온 채팅용 부품(메시지 스크롤러, 말풍선, 첨부, 되묻기 질문지 등)에 Trace·Code Block이 더해지면서, 이를 조합한 패턴 21개가 공개됐다 — Chat, Prompt Input, Reasoning, Tool, Plan, Subagent 등.
- **설치할 패키지가 없다**: 코드를 복사해 내 프로젝트에 넣는 방식이라 코드는 내 것이다.
- **모든 페이지가 Markdown으로도 제공**: “이 페이지의 Reasoning 패턴을 내 채팅에 추가해” 하고 링크만 코딩 에이전트에 주면 된다.
- 기존 ‘AI SDK Elements’는 폐기 예정. 페이지마다 **마이그레이션 프롬프트**가 있어 에이전트가 이름·속성을 유지한 채 다시 만들어 준다.

## 왜 중요한가
에이전트 제품의 신뢰는 결국 **“무엇을 했는지 보이느냐”** 에서 나온다. 단계 표시가 앱마다 다르면 사용자는 매번 새로 읽는 법을 배워야 한다. Trace는 그 표시 방식을 업계 공용 부품으로 만들려는 시도다. 디자이너에게는 “에이전트 진행 표시”를 0부터 그리지 말고 **이 문법 위에서 브랜드만 입히라**는 신호이기도 하다.

출처: [shadcn/ui — October 2026: Trace, Code Block and AI Elements](https://ui.shadcn.com/docs/changelog/2026-10-ai-elements)
