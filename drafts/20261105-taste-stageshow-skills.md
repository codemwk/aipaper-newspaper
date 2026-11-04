---
title: "디자인: ‘AI가 만든 티’ 지우는 스킬 2종 — taste-skill은 아트 디렉션·레퍼런스, X 디자이너의 Stageshow는 결과를 영상으로 찍어 자가 검토"
date: 2026-11-05T07:04:00+09:00
category: "디자인"
slug: "taste-stageshow-skills"
summary: "코딩 에이전트의 밋밋한 UI를 고치는 스킬이 연달아 나왔다. taste-skill은 아트 디렉션·레퍼런스 이미지·브라우저 확인을 붙여 이번 주 +5,798★(누적 약 11만). X의 수석 디자이너 Benji Taylor가 공개한 Stageshow는 React로 목업·Bento Grid·커서 데모·모션을 만들고, 결과를 영상으로 녹화해 에이전트가 스스로 점검한다. 설치는 npx skills add 한 줄."
---

## 한줄 요약
에이전트가 만든 화면이 다 비슷해 보이는 문제, 이른바 **‘AI 룩’**을 고치려는 스킬이 이번 주에도 두 개 눈에 띈다. 지난번 저장하신 **impeccable·UI UX Pro Max**와 같은 계열의 후속 소식이다.

## taste-skill — 취향을 절차로
- 설명 그대로 “코딩 에이전트에게 **취향**을 주는 스킬”: 일반적인 AI 페이지 대신 **아트 디렉션**, **레퍼런스 이미지**, **브라우저에서 직접 확인**을 거치게 한다.
- 이번 주(10/28~11/4) **+5,798★**, 누적 약 10.9만([AgentDataCo](https://agentdataco.com/changes/fastest-growing-ai-github-repos-this-week), [저장소](https://github.com/Leonxlnx/taste-skill)).

## Stageshow — 만들고, 찍고, 다시 본다
- X의 수석 디자이너 **Benji Taylor**가 공개.
- React로 정적 UI 목업, 기능 카드, **커서 움직임 데모**, **Bento Grid**, 인터페이스 애니메이션을 만든다. 모션·구도 지침 포함.
- 핵심은 **자가 검증 루프**: 결과물을 영상으로 녹화하고 에이전트가 그 영상을 보고 품질을 점검한다.
- 설치: `npx skills add benjitaylor/skills --skill stageshow`([Junho Lee 큐레이션 11/4](https://datanexus-kr.github.io/curations/2026-11/2026-11-04-stageshow-ai-agent-ui-design-skill/)).

## 왜 중요한가
두 스킬의 공통점은 **‘보고 고치는 단계’를 에이전트에게 강제**한다는 것이다. 좋은 프롬프트보다 좋은 검토 절차가 결과를 바꾼다. 제품 소개 영상·랜딩 페이지 시안처럼 **움직임이 중요한 결과물**이라면 Stageshow의 영상 검토 방식이 특히 쓸모 있다.
