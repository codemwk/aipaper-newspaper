---
title: "제미니 ‘에이전틱 비디오’ — 고정 FPS 대신 필요한 순간만 본다"
date: 2026-09-15T07:25:00+09:00
category: "AI Content Gen"
slug: "gemini-agentic-video"
summary: "Google(2026-09-01). Gemini 3.7/3.6 Flash·3.5 Flash-Lite에 agentic video understanding. 토큰 최대 88%↓, 비용 최대 66%↓, 정확도 최대 7%↑. API processing=agentic. YouTube Ask에도 확장 예정."
---

## 한줄 요약
[Google DeepMind 블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)가 **에이전틱 비디오 이해**를 Gemini 3.7 Flash·3.6 Flash·3.5 Flash-Lite에 켰다. 고정 FPS로 전체를 삼키는 대신, 모델이 목표에 맞춰 **프레임·오디오·자막 구간을 동적 탐색**한다.

## 숫자와 쓰는 법
회사 벤치 기준 분석 비용 최대 **66%** 감소, 토큰 최대 **88%** 감소, 정확도 최대 **7%** 상승(특히 장문 영상). 초단위 순간 검색, 수시간 needle-in-haystack, 이상 구간 고속 재샘플, 동작·객체 카운팅이 예시 유스케이스다. Gemini API에서 `processing: "agentic"`만 켜면 되고 **별도 기능 요금은 없다**(표준 토큰 과금). AI Studio·Enterprise Agent Platform·업로드/YouTube URI 지원. 이후 Gemini 앱·YouTube **Ask YouTube**에도 확장 예정이라고 했다.

## 왜 중요한가
콘텐츠·교육·모니터링에서 “긴 영상 = 토큰 폭탄”이던 제약이 풀리면, **생성**뿐 아니라 **이해·편집·QA** 파이프라인이 싸진다. 정적 1 FPS와 품질·비용 트레이드오프를 개발자가 수동으로 짜던 일을 모델 루프가 가져간다.

## 기억할 것
- 활성화: API `processing="agentic"`.
- 검증: 장문 벤치(LongVideoBench 등)에서 토큰·정확도를 직접 재현할 것. 수치는 벤더 발표.
