---
title: "디자인/UI·UX: impeccable(~76K★) — ‘Inter·보라 그라디언트·카드 속 카드’ AI 티를 잡는 디자인 스킬, 탐지 규칙 61개"
date: 2026-10-05T07:08:00+09:00
category: "디자인/UI·UX"
slug: "impeccable-design-skill"
summary: "pbakaus/impeccable. 코딩 에이전트용 디자인 언어: 스킬 1개·명령 24개·결정론 탐지 규칙 61개(LLM·API 키 없이 CLI/브라우저 확장으로 실행). init→PRODUCT.md(제품 사실)·DESIGN.md(시각 시스템) 분리. Anthropic frontend-design 스킬에서 출발. 주간 트렌딩 2일."
---

## 한줄 요약
[impeccable](https://github.com/pbakaus/impeccable)은 AI 코딩 에이전트가 만든 화면의 **‘AI 티’**를 걷어내는 디자인 가이드 스킬이다. 10월 5일 조회 기준 별 **약 7.6만 개**, [9/28–10/3 주간 트렌딩](https://www.tommyz.blog/blog/github-trending-weekly-2026-09-28-to-2026-10-03)에 이틀 올랐다. 출발점은 Anthropic의 frontend-design 스킬이다.

## 문제 정의가 날카롭다
README의 진단: “모든 모델이 같은 SaaS 템플릿으로 학습했다. 가이드 없이 두면 매번 같은 흔적이 남는다 — **모든 곳에 Inter, 보라→파랑 그라디언트, 카드 안의 카드, 색 배경 위 회색 글씨, 모든 제목 위의 둥근 사각형 아이콘 타일**.” 금지 목록도 구체적이다: 남용 폰트(Arial·Inter·시스템 기본) 피하기, 순수 검정/회색 대신 **틴트**, 바운스·엘라스틱 이징 금지(낡아 보임).

## 구성
- **`/impeccable init`**: 프로젝트를 훑고 빠진 것만 물어 **PRODUCT.md**(대상·목적·맥락·제약·보이스·근거)를 쓴다. 시각 시스템은 따로 **DESIGN.md**에 — ‘제품의 사실’과 ‘표면의 스타일’을 섞지 않는 설계.
- **명령 24개**: craft, shape(코드 전 UX 설계), critique(위계·명료성 리뷰), audit(접근성·성능·반응형), polish, bolder/quieter, distill, harden(에러·i18n·텍스트 넘침), onboard(첫 실행·빈 상태), typeset, layout, clarify(UX 카피), live(브라우저에서 변형 반복) 등.
- **결정론 탐지 규칙 61개**: CLI와 브라우저 확장이 **LLM도 API 키도 없이** 돌린다. 편집 훅이 UI 파일 수정 때마다 탐지 결과를 에이전트 루프에 되먹인다.
- Cursor, Claude Code, Gemini CLI, Codex, Grok Build, Hermes 등 지원. `npx impeccable install` 한 번.

## 왜 중요한가
9/23에 반응이 좋았던 UI UX Pro Max가 ‘디자인 지능을 더하는’ 쪽이었다면, impeccable은 **‘하지 말아야 할 것’을 기계적으로 잡는** 쪽이다. 디자인 시스템 문서(DESIGN.md)가 사람용 가이드에서 **에이전트가 읽고 위반을 탐지당하는 계약**으로 바뀌는 흐름의 가장 대중적인 사례. 브랜드 스튜디오라면 자사 아이덴티티 규칙을 이런 탐지 규칙으로 옮기는 게 다음 서비스 아이디어가 될 수 있다.

## 기억할 것
- [GitHub impeccable](https://github.com/pbakaus/impeccable) · [impeccable.style](https://impeccable.style) · [주간 트렌딩 요약](https://www.tommyz.blog/blog/github-trending-weekly-2026-09-28-to-2026-10-03)
