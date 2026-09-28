---
title: "AI 콘텐츠: Google Research ‘AI Video Co-Director’ — 분 단위 롱폼의 정체성 드리프트 잡기"
date: 2026-09-29T07:05:00+09:00
category: "AI 콘텐츠"
slug: "google-video-codirector"
summary: "Google Research(9/24). Co-Director·CANVAS·A²RD·VQQA 멀티에이전트 프레임워크. Gemini+Veo 오케스트레이션, 월드스테이트·시각 메모리로 캐릭터/배경 일관성. COLM·EMNLP 2026. SynthID 상속."
---

## 한줄 요약
[Google Research 블로그(2026-09-24)](https://research.google/blog/coherent-long-form-video-generation/)는 **수 분짜리 내러티브 비디오**에서 캐릭터·소품·배경이 샷마다 바뀌는 “드리프트”를 줄이는 **멀티에이전트 코디렉터** 연구를 공개했다. Gemini·Veo 위 오케스트레이션 레이어로, 생성물에는 **SynthID** 등 기반 모델 안전장치가 그대로 실린다.

## 네 기둥 (쉽게)
- **Co-Director**: 창작 전략·서사 모드·미학을 multi-armed bandit으로 고르고, 프리프로덕션→키프레임·비디오·오디오→MLLM 판사 루프.
- **CANVAS**: 캐릭터·장소·오브젝트 **월드스테이트**를 유지하는 스토리보드 에이전트. HardContinuityBench에서 복귀 장면 일관성 강조.
- **A²RD**: 세그먼트별 retrieve–synthesize–refine–update. 10분급 데모에서 extrapolation(이야기 전진)과 interpolation(정체성 고정) 전환.
- **VQQA**: 시각 질문으로 결함을 찾아 **프롬프트를 고쳐 재샘플**하는 폐쇄 루프(픽셀 페인트가 아님).

## 왜 중요한가
Vids의 “무료 클립”과 맞물리면, **짧은 생성 → 긴 일관성**이 다음 전쟁터가 된다. 크리에이터 툴은 모델 API보다 **에이전트 연출 레이어**를 사게 될 가능성이 크다.

## 기억할 것
- [Google Research](https://research.google/blog/coherent-long-form-video-generation/) · Co-Director(COLM 2026)·CANVAS(EMNLP 2026)
