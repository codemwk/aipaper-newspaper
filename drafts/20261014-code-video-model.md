---
title: "AI 콘텐츠: Code Video Model — 영상을 먼저 ‘코드(Three.js)로 프리비즈’하고 MiniMax-H3가 실사로 입힌다, 추가 학습 없이 VACE 대비 우위"
date: 2026-10-14T07:05:00+09:00
category: "AI 콘텐츠"
slug: "code-video-model"
summary: "Code Video Model(10/12 공개, 보도상 Microsoft Research 연구진): 프롬프트→에이전트가 Three.js 장면 코드 작성→1분 내 저폴리 프록시 영상 렌더→고정된 MiniMax-H3가 프록시+레퍼런스 이미지로 최종 클립. 초반 샘플링 단계에만 프록시를 보는 early-step conditioning. CodeVideoBench 85.2/82.1/85.8 vs VACE 74.3/73.1/80.6. 코드 Apache-2.0."
---

## 한줄 요약
영상 생성 모델은 물체 위치·움직임·카메라를 **블랙박스 안에서 ‘상상’**한다. **Code Video Model**은 영화의 프리비즈(previs)처럼, 먼저 **코드로 장면을 짜서 거친 미리보기 영상을 렌더**하고, 그 구조를 따라 실사 클립을 만든다([프로젝트 페이지](https://code-video-model.github.io/), [GitHub](https://github.com/code-video-model/CodeVideoModel)).

## 어떻게 동작하나
1. **코드로 연출**: 프롬프트를 받으면 에이전트(저장소 기준 GPT-6)가 **Three.js 프로그램**을 작성 — 장면 배치, 오브젝트 애니메이션, 카메라 경로, **방정식으로 계산한 물리**.
2. **프록시 렌더**: 저폴리 미리보기가 **1분 미만**. 코드라서 요소 하나하나를 정확히 고칠 수 있다.
3. **실사화**: 레퍼런스 이미지(GPT-Image-2 생성 또는 사용자 제공)와 프록시를 조건으로 **고정된 MiniMax-H3**가 최종 클립 생성.
4. **핵심 트릭 — early-step conditioning**: 구조가 잡히는 **초반 샘플링 단계에서만** 프록시를 참고하고 이후엔 놓는다. 그래야 저폴리의 ‘납작한 질감’이 최종 영상에 복사되지 않는다. **추가 학습 없음**.

## 숫자
- 자체 벤치 **CodeVideoBench**(게임·장면 편집·월드모델 데이터·물리·불릿타임·3D/4D) 종합: **85.2 / 82.1 / 85.8**(심사 모델 QwenVL-3.8-27B / GPT-5.6 / GPT-6) vs 최강 학습형 베이스라인 **VACE 74.3 / 73.1 / 80.6**.
- 코드 Apache-2.0, 예제 CC BY 4.0, 저장소 ~411★(10/14). 공식 페이지는 ‘Code Video Model Team’으로만 표기하며, Microsoft Research 소속은 [SlopTV News](https://sloptvnews.com/microsoft-code-video-model-previs/) 보도 기준.

## 왜 중요한가
제품 촬영·건축 시네마틱·불릿타임처럼 **“카메라가 정확히 이렇게 움직여야 하는”** 샷에서 프롬프트 운에 기대지 않아도 된다. 크리에이티브 스튜디오 관점에선 **코딩 에이전트 = 촬영감독**, 영상 모델 = 렌더러라는 분업이 보인다. 한계는 자체 벤치·LLM 심사라는 점과, MiniMax-H3 구동에 CUDA GPU 환경이 필요하다는 점.

출처: [Code Video Model 프로젝트](https://code-video-model.github.io/) · [GitHub code-video-model/CodeVideoModel](https://github.com/code-video-model/CodeVideoModel) · [SlopTV News](https://sloptvnews.com/microsoft-code-video-model-previs/)
