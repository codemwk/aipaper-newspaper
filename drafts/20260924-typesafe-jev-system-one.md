---
title: "AI Models: TypeSafe Jev — 채팅이 아니라 ‘캘리브레이트된 결정’을 파는 System One"
date: 2026-09-24T07:10:00+09:00
category: "AI Models"
slug: "typesafe-jev-system-one"
summary: "TypeSafe Jev(2026-09-15). System One 모델. Choice/Score/null + 캘리브레이트 확률, 병렬 샘플링. 입력 $42/10억 토큰·출력 무료. 70–500ms. 문자열 생성 없음→타입 환각 없음. 얼리 액세스."
---

## 한줄 요약
[TypeSafe AI의 Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)는 LLM 대체 챗봇이 아니라 **소프트웨어가 바로 쓸 수 있는 결정 함수**다. 상태를 넣고 Choice / Score / null 같은 **타입 안전 출력 + 캘리브레이트된 확률**을 병렬로 돌려준다.

## 제품 포인트
- 창업자 Diogo Almeida(RLHF·ChatGPT 관련 이력 언급). 학습: **RLCD**(Reinforcement Learning for Calibrated Decisions).
- 속도·가격(회사 발표): 엔드투엔드 **70–500ms**, 입력 **$42 / 10억 토큰**, **출력 토큰 무료**.
- 문자열을 포기한 대가: 타입 에러·환각 문자열을 구조적으로 줄임(스키마 매칭 보장 주장).
- 용도: 스마트 if, 라우팅, 가드레일, 대량 map-reduce, 실시간 UX.
- 워크플로 평가에서 Astra·Fable 평균 대비 파레토를 주장 — **회사 측 수치**, 독립 검증은 별도.

## 왜 중요한가
랭킹 스탬프가 아니라 **자동화 인터페이스** 이야기다. 에이전트 루프 안의 “클릭할까/가드할까” 같은 System 1 결정을 LLM에 맡기면 느리고 비싸다. Jev는 그 층을 분리하자는 제안이다.

## 기억할 것
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · typesafe.ai
