---
title: "AI 모델: 구글이 이틀 새 내놓은 두 모델 — 빠른 일꾼 ‘Gemini 4 Hydrogen’, 글은 안 쓰고 ‘확률만 답하는’ Gemini Decision 1"
date: 2026-11-13T07:01:00+09:00
category: "AI 모델"
slug: "gemini-4-hydrogen-decision-1"
summary: "구글이 11/12 코딩·에이전트 작업용 고속 모델 Gemini 4 Hydrogen(100만 토큰, 입력 1.50달러/출력 7.50달러, 컨텍스트 전 구간 동일 가격)을 무료 사용자까지 풀었다. 하루 전 11/11에는 텍스트를 생성하지 않고 예/아니오·객관식·루브릭 점수에 확률만 돌려주는 Decisions API(Gemini Decision 1, 입력 100만 토큰당 0.10달러, 출력 무료)를 냈다."
---

## 한줄 요약
구글이 “깊게 생각하는 최상위 모델” 바깥의 두 자리를 채웠다. **많이, 빨리 일하는 모델**(Hydrogen)과 **결정만 내리는 모델**(Decision 1)이다.

## Gemini 4 Hydrogen (11/12)
- 구글 설명으로 Gemini 4 **Carbon·Argon**이 길고 어려운 추론을 맡고, **Hydrogen은 일상적인 코딩·에이전트 작업을 빠르게 처리**하는 역할이다([Google 블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)).
- 가격: **100만 토큰 컨텍스트 전 구간에서 동일하게** 입력 100만 토큰당 1.50달러, 출력 7.50달러. 긴 프롬프트를 넣어도 할증이 없다(지난번 Muse Ember 기사에서 짚은 ‘긴 프롬프트 요금 함정’과 반대).
- 제공 범위: Gemini API·AI Studio, 기업용 Gemini, Gemini 앱, 구글 검색, Sheets 속 Gemini, 유료 구독자용 Antigravity. 무료 사용자는 자동 모델 선택으로 상황에 맞을 때 쓰게 된다.

## Gemini Decision 1 / Decisions API (11/11)
- 답을 한 글자씩 생성하지 않는다. 미리 정한 선택지에 **확률과 신뢰도(0~1)**를 매겨 돌려준다. 질문 형식은 세 가지다: 예/아니오(구글 표기 `noul`), 2~255개 중 객관식, 순서형 루브릭 점수([Google 블로그](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)).
- 한 번의 입력(텍스트·이미지·오디오·영상·PDF, 최대 256K 토큰)에 **질문 최대 1,000개**를 함께 던질 수 있다. 응답은 150~250ms. **입력 100만 토큰당 0.10달러, 출력은 무료**다.
- 구글 내부 활용 예: Gemini Notebook의 모델 라우팅(일상 질의 지연 최대 40% 감소), Stitch의 빠른 와이어프레임 실험, 검색의 MCP 도구 안전 검사.
- Simon Willison이 직접 테스트해 보니, 예/아니오 질문에 다른 회사 결정 모델(Jev, OpenAI)은 1.0/0.0으로 딱 잘라 답한 반면 Gemini는 0.92처럼 **조금 덜 확신하는 값**을 돌려줬다([simonwillison.net](https://simonwillison.net/2026/Nov/11/gemini-decisions-api/)). ‘결정 모델’ 카테고리에 Jev·OpenAI·구글 세 회사가 모두 들어온 셈이다.

## 왜 중요한가
에이전트 비용의 상당 부분은 “이 요청은 어느 모델로 보낼까”, “이 도구 호출은 안전한가” 같은 **작은 판단의 반복**에서 나온다. 이런 판단은 결정 모델에, 실제 작업은 Hydrogen 같은 고속 모델에, 어려운 문제만 최상위 모델에 맡기는 **3단 분업**이 이제 한 회사 안에서 다 가능해졌다. 신뢰도가 낮게 나온 건만 사람에게 넘기는 설계도 쉬워진다.

## 확인할 점
성능 비교 수치는 모두 구글 자체 발표다. Decision 1은 아직 AI Studio의 Gemini API(v1beta)에서만 제공되고, Google Cloud 지원은 “곧”이라고만 했다.
