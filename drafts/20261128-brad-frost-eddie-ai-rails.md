---
title: "디자인: 아토믹 디자인 창시자 브래드 프로스트의 18개월 실험 — 사업용 웹사이트 20여 개를 전부 ‘내 디자인 시스템 Eddie’로만 AI에게 짓게 했다. 비결은 프롬프트가 아니라 ‘강철 장막’ 검사"
date: 2026-11-28T07:25:00+09:00
category: "디자인"
slug: "brad-frost-eddie-ai-rails"
summary: "‘아토믹 디자인’으로 유명한 브래드 프로스트가 11/20 브라질 Detach! 컨퍼런스 발표 직후, AI가 자기 디자인 시스템 Eddie를 일관되게 쓰도록 만드는 데 약 18개월이 걸렸고 지금은 사업에 쓰는 웹사이트 20여 개가 전부 Eddie로만 만들어진다고 밝혔다. AI가 쓴 코드는 검사·테스트·평가를 통과해야 배포되는 ‘Steel Curtain’을 거치고, 바이브 코딩 페이지를 디자인 시스템 부품으로 바꾸는 ‘vibe-killer’ 같은 에이전트 스킬도 공개했다."
---

## 한줄 요약
“AI가 우리 디자인 시스템을 안 따른다”는 불평에 대한 실전 답. **디자인 시스템 → 제품 → 다시 디자인 시스템**으로 이어지는 순환을 AI로 실제 굴리고 있다([Brad Frost 블로그, 11/20](https://bradfrost.com/blog/post/making-better-products-with-design-systems/)).

## 무엇을 했나
- 발표 슬라이드조차 자체 프레임워크 **eddie-slides**로 만들었고, 글은 자체 편집 앱 content-brain으로 쓴다. 강의 사이트·블로그·블랙프라이데이 페이지까지 **20여 개 사이트가 Eddie 하나로** 돈다.
- 핵심 문장: Eddie를 바꾸면 20여 개 제품으로 흘러가고, 각 제품 작업이 다시 Eddie를 강하게 만든다 — 아토믹 디자인이 말해 온 “연결된 디자인 시스템”을 AI 덕에 **처음으로 실제로 산다**는 것.

## 공개한 방법 (무료 강의 영상 3편)
- **디자인 시스템 있이 vs 없이:** 같은 UI를 AI가 바이브 코딩할 때와 Eddie로 지을 때 비교.
- **Steel Curtain(강철 장막):** AI가 쓴 코드는 **검사·테스트·평가(evals)의 관문**을 통과해야만 배포된다. “AI 슬롭을 프로덕션에 못 들어오게.”
- **Subatomic:** 디자인 토큰을 디자인 시스템 밖 **제품 층**에서도 쓰면서 연결을 유지하는 법.

## 에이전트 스킬 5종 (개발 중, 이슈·PR 환영)

| 스킬 | 하는 일 |
| --- | --- |
| product-inspection | 10단계 점검으로 제품 품질 진단 |
| vibe-killer | 바이브 코딩한 페이지를 **디자인 시스템 부품으로만** 다시 짓기 |
| ds-ai-rails | AI를 디자인 시스템 궤도에 묶어 두는 프로세스 평가 |
| product-to-storybook | 제품 화면을 Storybook으로 빨아들여 프로토타이핑 |
| storybook-to-product | Storybook에서 만든 UI를 실제 제품으로 옮기기 |

## 왜 중요한가
- 지난번 저장하신 **DESIGN.md·impeccable(‘AI 티 안 나게’ 스킬) 기사와 이어지는 소식**이다. 그 흐름이 “규칙 문서를 AI에게 읽힌다”였다면, 프로스트는 한 걸음 더 나가 **규칙을 어기면 배포가 막히는 관문**을 강조한다. 11/26 소개한 AI Canvas의 done-gate와 같은 결론이다.
- 대시보드·앱을 여러 봇으로 동시에 만드는 환경이라면, **공통 디자인 시스템 하나 + 통과 검사**가 화면 간 일관성을 지키는 가장 싼 방법이라는 실례.
- 주의: 블로그는 강의 판매 페이지를 겸한다. “20여 개 사이트”는 본인 사업 규모의 사례이고, 팀·대기업 규모에서 같은 효과가 나는지는 별개다.

출처: [Brad Frost — Putting AI & Design Systems to work](https://bradfrost.com/blog/post/making-better-products-with-design-systems/) · [Detach! 26](https://www.detach.com.br/)
