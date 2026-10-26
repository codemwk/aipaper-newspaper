---
title: "GitHub 트렌드: 구글發 ‘코끼리와 금붕어’(~1.7천★, 주간 +1.7천) — 다 기억하는 AI가 설계서를 쓰고, 아무것도 모르는 AI 여러 마리가 그걸 두들겨 본 뒤에야 코드를 짠다"
date: 2026-10-27T07:09:00+09:00
category: "GitHub 트렌드"
slug: "elephant-goldfish-spec"
summary: "google/elephant-goldfish-model(EGM)이 10/20–26 Upstar ‘AI 에이전트’ 주간 순위 1위(+1.7천 별, 총 ~1.7천). 구글에서 만든 ‘명세 주도 개발’ 방법론·스킬 묶음(Apache-2.0, 구글 공식 지원 제품은 아님). 프로젝트 맥락을 다 아는 ‘코끼리’ 세션이 설계 문서를 쓰고, 대화 맥락 없이 문서와 코드만 읽는 ‘금붕어’ 서브에이전트 무리가 디자인 비평가·순진한 독자·테크 리드 등 역할로 검토한다. Claude Code·Codex·Antigravity 플러그인. 같은 주 JetBrains의 ThinkRail(~2.8천★)도 ‘살아 있는 명세’를 내세움."
---

## 한줄 요약
AI 코딩이 빨라지면서 문제는 **“빨리 잘못 만드는 것”**이 됐다. 이번 주 AI 에이전트 저장소 순위 1위인 구글의 EGM은 해법을 동물 비유로 푼다. **다 기억하는 코끼리가 쓰고, 아무것도 기억 못 하는 금붕어가 검사한다**([GitHub](https://github.com/google/elephant-goldfish-model), [Upstar 주간 순위](https://upstar.dev/t/ai-agents)).

## 어떻게 일하나
- 🐘 **코끼리(다 기억)**: 시스템 역사·아키텍처·컴포넌트 경계·사용자 여정을 다 불러온 깊은 맥락의 에이전트. 브레인스토밍을 하고 한계를 따져 **설계 명세를 쓴다**.
- 🐠 **금붕어(맥락 0)**: 대화 기록 없이 **초안 명세와 실제 코드만** 읽는 독립 서브에이전트들. 대화 중 생긴 편견이 없다. 역할별로 서로 다른 관점에서 공격한다:
  - 디자인 비평가 · 순진한 독자 · 테크 리드 · 코드베이스 감사자 · 구조 검증자 · 문체 편집자 · 큰 그림 아키텍트
- 🧑‍💻 **사람(결과 책임)**: AI는 탐색 파트너이자 자동 감사관. 설계 결정·트레이드오프·최종 결과는 사람이 진다.

## 단계
1. **아이디어 → 집중 포화**: 금붕어 무리가 초기 개념을 ‘격추’ 시험
2. **초안**: 개념 요약을 `docs/designs/기능명.md` 설계 문서로 한 섹션씩 작성
3. **검토·해결**: 큰 그림 → 이해도 → 비평 → 준비도 순서의 다단계 검토, 지적 사항을 분류해 패치
4. **제출·구현**: 검증된 설계 문서를 PR로 올리고, 승인된 명세대로 코드 작성
- 덤: 명세와 실제 코드가 어긋난 곳을 찾는 **drift report**, 기존 코드베이스 문서를 아래에서부터 만들어 주는 **bootstrap**.

## 이번 주 같은 흐름
- **JetBrains ThinkRail**(~2.8천★, 주간 +1.8천): pi 코딩 에이전트를 감싼 가벼운 IDE. 작업 공간을 분리하고, **‘살아 있는 명세(living specs)’와 재사용 스킬**로 프로젝트 지식을 쌓는다([GitHub](https://github.com/JetBrains/thinkrail)).
- 공통점: **코드보다 명세가 먼저, 그리고 명세가 계속 갱신된다.**

## 왜 뜨나
- **‘같은 AI가 쓰고 같은 AI가 검토’의 맹점.** 긴 대화를 함께한 에이전트는 자기 설계의 구멍을 못 본다. 맥락을 일부러 지운 검토자는 사람 팀의 ‘처음 보는 동료 리뷰’를 흉내 낸다.
- **코드 리뷰 병목을 앞으로 당긴다.** 최근 연구들이 지적했듯 AI가 코드를 더 많이 쓰면 리뷰가 밀린다. 코드 전에 문서 단계에서 걸러 내면 리뷰할 양이 준다.
- **비개발자에게도 쓸모.** 브랜드 전략서·제안서도 같은 방식이 된다: 맥락을 다 아는 AI가 초안을, 아무것도 모르는 ‘처음 보는 클라이언트’ 역할 AI들이 비평을.
- 참고: README에 “구글의 공식 지원 제품이 아니다”라고 명시. 배경 글은 Dave Rensin의 에세이 ‘Elephants, Goldfish, and the New Golden Age of Software Engineering’.

출처: [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · [Upstar — AI agents 주간 순위 (10/20–26)](https://upstar.dev/t/ai-agents) · [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)
