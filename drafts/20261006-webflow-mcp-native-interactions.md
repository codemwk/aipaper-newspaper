---
title: "디자인/UI·UX: Webflow MCP, 애니메이션을 ‘네이티브 Interactions’로 — 에이전트가 만든 모션을 디자이너가 타임라인에서 다시 만진다"
date: 2026-10-06T07:11:00+09:00
category: "디자인/UI·UX"
slug: "webflow-mcp-native-interactions"
summary: "10/2 Webflow MCP 업데이트: 연결된 에이전트가 GSAP 기반 네이티브 Interactions(스크롤·호버·커서·텍스트 분할)를 생성. 결과가 커스텀 코드가 아니라 Interactions 패널의 트리거·타임라인으로 남아 수동 편집 가능. 커서 틸트·단어별 스크롤 등장(3분 30초)·고정 섹션+진행 내비(액션 10개+) 데모. Cloud 앱 배포·로그 읽기·재배포도."
---

## 한줄 요약
Webflow가 10월 2일 MCP 서버 업데이트를 소개하며 **“이제 에이전트가 사이트를 움직이게 한다”**고 밝혔다([Webflow Blog](https://webflow.com/blog/interactions-gsap-mcp)). 지금까지 에이전트는 레이아웃은 만들어도 Webflow 고유 애니메이션은 못 건드렸다. 이번부터 GSAP 기반 **네이티브 Interactions**를 직접 만든다. (같은 업데이트의 ‘사이트 가이드라인 자동 초안’은 10/2자 AiPaper에서 다뤘다.)

## 핵심: 결과물이 ‘편집 가능한 모션’이다
- 에이전트가 만든 애니메이션이 붙여 넣은 커스텀 코드가 아니라 **Interactions 패널의 트리거·타임라인·속성**으로 남는다. 디자이너가 열어서 이징·스태거·속성을 손으로 바꿀 수 있다.
- 데모 3개(Codex + GPT-6 Astra): ① 커서를 따라 기울어지는 버튼(마우스 무브 트리거) ② 스크롤하면 줄마다·단어마다 등장하는 문단 — **3분 30초** ③ 섹션이 고정된 채 왼쪽 내비가 진행률을 따라가고 오른쪽 이미지가 바뀌는 패턴 — Interactions에 **액션 10개 이상**.
- 한계도 명시: 모든 GSAP 기능이 Interactions 속성에 1:1로 대응하진 않는다. 더 필요하면 여전히 커스텀 코드. 더 저렴한 모델은 결과가 달라질 수 있다.

## 따라 할 만한 ‘프롬프트 3단’
1. **맥락**: 어떤 사이트에, 어떤 레퍼런스(GSAP 데모 URL)를.
2. **제약**: “네이티브·편집 가능한 Webflow Interactions로” — 에이전트가 커스텀 코드로 도망가지 않게.
3. **보류**: “끝나면 알려 줘, 내가 확인할게.” 모델은 스스로 검증하려고 토끼굴에 빠지는데, **애니메이션이 ‘느낌이 맞는지’는 사람이 판단할 일**이다([Art Direction Daily 10/2](https://artdirectiondaily.com/issues/2026-10-02-codex-rebuilt-gsap-demos-webflow.html)).

## 함께 들어온 것
Webflow Cloud(풀스택 앱) 쪽에선 에이전트가 코드를 고쳐 푸시한 뒤 **배포 완료를 기다리고, 실패하면 빌드·런타임 로그를 읽고 고쳐 재배포**한다. 브랜치→환경 매핑, 이전 배포로 롤백도 가능. 별도 설정 없이 이미 MCP를 연결한 사용자에게 라이브.

## 왜 중요한가
AI 생성 UI의 고질병은 “**한 번 뽑으면 디자이너가 손댈 수 없는 결과물**”이다. Framer·Figma가 ‘레이어는 캔버스에 남긴다’로 답했다면, Webflow는 **모션까지 같은 원칙**을 적용했다. 에이전트는 초안을 빠르게, 사람은 타이밍과 감각을 — 모션 디자인에서 분업선이 처음으로 명확해졌다.

## 기억할 것
- [Webflow Blog 10/2](https://webflow.com/blog/interactions-gsap-mcp) · [Art Direction Daily 10/2](https://artdirectiondaily.com/issues/2026-10-02-codex-rebuilt-gsap-demos-webflow.html)
