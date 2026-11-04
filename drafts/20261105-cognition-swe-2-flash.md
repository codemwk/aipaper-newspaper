---
title: "AI 모델: Cognition ‘SWE-2 Flash’ — 형님 모델의 5분의 1 가격·3배 속도. 비결은 강화학습 전에 끼운 ‘중간 학습’"
date: 2026-11-05T07:01:00+09:00
category: "AI 모델"
slug: "cognition-swe-2-flash"
summary: "Devin을 만드는 Cognition이 11/4 저가·고속 코딩 모델 SWE-2 Flash를 Devin Desktop과 CLI에 넣었다. Thinking Machines의 Inkling-Small을 바탕으로, 처음으로 강화학습 전에 mid-training 단계를 추가해 Terminal-Bench 4.0을 0.9%→20.0%로 끌어올렸다고 밝혔다. 가중치는 사이버 위험 때문에 파트너·연구자 대상 프로그램으로만 공유할 계획."
---

## 한줄 요약
코딩 에이전트 Devin의 Cognition이 **SWE-2 Flash**를 공개했다. 더 큰 형 모델 SWE-2 대비 **가격 5분의 1, 속도 3배**이고, 오늘부터 Devin Desktop과 CLI에서 쓸 수 있다([Cognition 11/4](https://cognition.com/blog/swe-2-flash)).

## 어떻게 만들었나
- **바탕 모델**: Thinking Machines의 Inkling-Small.
- **새 단계 — 중간 학습(mid-training)**: 보통은 바탕 모델에 바로 강화학습을 하는데, 그 사이에 코딩 데이터로 한 번 더 길들이는 단계를 처음 넣었다. 회사 수치로 Terminal-Bench 4.0이 **0.9% → 20.0%**, FrontierCode 2.0이 **3.2% → 24.0%**로 올랐다.
- **주장**: 미국산 오픈 가중치 모델 중 최고, 3배 큰 모델도 앞선다(회사 자체 평가).

## 가중치는?
공개 다운로드가 아니다. **사이버 위험**을 이유로 업계 파트너·연구자에게 안전하게 나눠 주는 프로그램을 만들고 있다고 했다.

## 왜 중요한가
코딩 에이전트를 여러 개 돌리면 비용이 곧 병목이다. ‘작고 빠른 모델로 대부분 처리, 어려운 건 큰 모델’이라는 분업이 에이전트 도구의 기본값이 되고 있고, Cognition은 그 작은 쪽을 직접 만들기 시작했다. 어제 소개한 ‘내 모델을 갖는’ 흐름(Endeavor·Cohere)과도 같은 방향이다.
