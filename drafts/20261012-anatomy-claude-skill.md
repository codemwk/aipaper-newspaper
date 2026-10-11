---
title: "디자인/UI·UX: Anatomy — ‘상자-화살표’ 대신 움직이는 기계로 설명하는 Claude Code 스킬, 사흘 만에 수천★"
date: 2026-10-12T07:02:00+09:00
category: "디자인/UI·UX"
slug: "anatomy-claude-skill"
summary: "wheresryan22/anatomy(10/8 생성, ~3.1K★)은 한 줄 아이디어를 등각(isometric) 인터랙티브 기계 그림으로 만든다. 규칙: ‘오브젝트가 설명이다’. SVG·WebGL·3D(베타), React 패키지 anatomy-figures, MIT. npx skills add로 설치."
---

## 한줄 요약
[Anatomy](https://skills.wheresryan.sh/anatomy)는 Claude Code용 **스킬**이다. “LRU 캐시가 어떻게 쫓아내는지 설명해”라고 쓰면 **상자 다이어그램이 아니라**, 책장·과일 슬롯머신·수조 같은 **실제 기계**를 수십~수백 파트로 조립하고, 드래그·키보드로 움직이게 한다. 저장소는 **2026-10-08** 생성, 스타 **~3,064**(10/12 `gh`).

## 어떻게 동작하나
- **한 줄 규칙**(SKILL.md): *The object is the explanation.* 박스·화살표·떠다니는 라벨 금지. 움직임이 개념과 1:1이어야 한다.
- **키워드**: `interactive`(포인터/키보드), `WebGL`(불·물·플라즈마), `3D`(진정 회전, 베타·느림).
- **크기 예산**: Figure 40–80파트·30–90분 / Hero 80–150·2–4시간 / Epic은 추정만 하고 **승인 없이 시작 안 함**.
- **검증**: 스크린샷·4× 크롭·겹침 감사(예: Trent 터보팬 541 solids·6,320 overlapping pairs). 제작자 Ryan은 시계 무브먼트 **1h54m**, Raptor **10h33m** 등 실측 시간을 공개.
- **배포**: `npx skills add wheresryan22/anatomy` 또는 `npm install anatomy-figures`. 테마 dark/light/paper/blueprint/sepia.

## 왜 중요한가
diagram-design·Framer Skills가 **브랜드 도판·디자인 시스템**을 다룬다면, Anatomy는 **설명 디자인(explainer design)** 을 에이전트 스킬로 제품화한다. 문서·랜딩·교육에서 “에이전트가 그린 그림”이 **장난감이 아니라 모델과 동일한 숫자**를 읽게 만드는 것이 핵심(스프링 모델 ↔ 게이지 눈금). 한계: 느리고, Claude가 “동작은 맞는데 보기엔 틀린” 파트를 자주 놓친다고 제작자도 인정 — **두 번째 눈으로 고치는 루프**가 필수.

출처: [Anatomy 사이트](https://skills.wheresryan.sh/anatomy) · [GitHub wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) · [explainx 요약](https://explainx.ai/blog/anatomy-claude-code-skill-isometric-interactive-figures-wheresryan22-2026)
