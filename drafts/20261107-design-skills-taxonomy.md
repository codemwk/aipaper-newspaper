---
title: "신선 각도: 디자인 스킬은 하나가 아니다 — 13개 레포를 5개 일로 나누는 분류법"
date: 2026-11-07T07:03:00+09:00
category: "디자인"
slug: "design-skills-taxonomy"
summary: "Setproduct가 11/3, Claude Code·Cursor·Codex용 디자인 스킬 13개를 스타가 아니라 ‘일’로 분류했다. A 처음부터 만들기 / B 기존 UI 다듬기 / C 방향 탐색 / D 다이어그램·쇼케이스 / E 가짜 제품 UI. 같은 레인은 경쟁, 다른 레인은 조합 — Marble taxonomy처럼 도구 목록이 아니라 운영 프레임이다."
---

## 한줄 요약
에이전트에게 랜딩을 시키면 Inter·보라 그라데이션·카드 안의 카드가 나온다. 그걸 막겠다고 쏟아진 “design skill” 레포는 11/3 기준 1.3k~145k★인데, **스타로는 고를 수 없다**. Setproduct는 13개를 **다섯 가지 일(lane)**으로 다시 잘랐다([Setproduct](https://www.setproduct.com/blog/design-skills-for-ai-agents-compared)).

## 다섯 레인
| 레인 | 하는 일 | 대표 |
|---|---|---|
| A 처음부터 | 페이지 생성 + 검사 | hallmark (101k★), hallmark, UI UX Pro Max (145k★) |
| B 다듬기 | 이미 있는 코드에 규칙 | emilkowalski/skills, jakubkrehel/skills, transitions.dev |
| C 탐색 | 변형을 나란히 | oil-ui |
| D 인접 산출물 | 다이어그램·맵 | diagram-design, archify |
| E 가짜 UI | 히어로용 미니 화면 | Stageshow |

규칙: **같은 레인 둘은 싸운다**(hallmark vs impeccable 둘 다 `DESIGN.md` 파이프라인). **다른 레인은 겹친다**(Krehel + Emil + impeccable detect CI).

## 숫자보다 검사기
표에서 중요한 열은 stars가 아니라 **How output is checked**. hallmark는 브라우저 8폭 렌더, impeccable은 **62개 결정적 디텍터·CI exit code**, Stageshow는 `film.mjs --gate` 콘택트 시트. 검사기 없는 스킬은 스타일 가이드일 뿐이다. elayadesign 13.9k★/커밋 16, Stageshow 1.3k★/커밋 1 — 런치 주간 스타의 함정.

## 왜 중요한가
지난번 저장하신 **impeccable / UI UX Pro Max**와 이어지는 소식이다. Marble taxonomy처럼 **제품 런칭이 아니라 분류 프레임**을 한 편에 담았다. “다 설치”가 아니라 **이번 주 일 → 왼쪽 도구 하나 → 출고될 때까지 멈춤**이 실무 규칙이다.

## 주의
스타·커밋은 2026-11-03 스냅샷. Premium/Pro(Oil UI $9.99, transitions.dev, uupm.cc)와 impeccable 텔레메트리 기본 On을 확인한 뒤 쓸 것.
