---
title: "AI 모델: 텐센트 Hy4 — 첫 ‘눈 달린’ 오픈 가중치 플래그십, 입력 100만 토큰당 0.9달러. 같은 날 SenseNova 6.8 Flash는 블렌더를 직접 조작"
date: 2026-11-05T07:00:30+09:00
category: "AI 모델"
slug: "tencent-hy4-open-weights"
summary: "텐센트가 11/4 Hy4를 공개했다. 시리즈 최초로 이미지 이해(차트 분석·시각 수학)를 넣었고, 블렌더·CAD 같은 전문 소프트웨어 조작을 따로 학습했다. 가중치와 시스템 카드는 며칠 내 공개 예정. 가격은 Preview와 같은 입력 0.9달러/출력 2.7달러(100만 토큰), 12/31까지 TokenHub 50% 할인. 스스로도 최상위 폐쇄형 모델보다는 뒤진다고 인정했다."
---

## 한줄 요약
텐센트가 11/4 차세대 LLM **Hy4**를 내놨다. 이번 시리즈에서 처음으로 **이미지 이해**가 들어갔고, 회사는 “가장 강한 오픈 가중치 모델 중 하나”라고 했다([Tencent 11/4](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/)).

## 무엇이 새로운가
- **시각 + 도구 호출**: 세밀한 이미지 처리, 복잡한 차트 분석, 그림이 섞인 수학 추론. 긴 컨텍스트·장기 에이전트 작업도 개선.
- **전문 소프트웨어 학습**: Blender·CAD 같은 프로그램을 다루는 작업을 따로 학습했다고 밝혔다.
- **가격**: Hy4 Preview와 동일하게 100만 토큰당 입력 **약 0.90달러**, 출력 **2.70달러**, 캐시 입력 0.045달러. TokenHub에서는 12/31까지 50% 할인, WorkBuddy·CodeBuddy는 11/4~15 무료. 더 싼 **Hy4 Flash**도 곧 나온다.
- **어디서 쓰나**: 텐센트 클라우드 TokenHub, WorkBuddy, CodeBuddy, Yuanbao 등. OpenRouter·Hermes·OpenCode로도 API 제공.
- **가중치**: “며칠 안에” 가중치와 시스템 카드를 공개하겠다고 했다. 아직은 예고 단계다.

## 같은 날 중국 쪽 흐름
SenseTime도 **SenseNova 6.8 Flash**를 정식 출시하며 장기 메모리, 먼저 도움을 제안하는 오피스 비서, 움직이는 슬라이드·포스터 생성, 그리고 **에이전트가 Blender를 직접 조작하는 3D 디자인 기능**을 내세웠다(Raccoon에서 12/1까지 무료)([AI Trend Research 11/4](https://ai-trend.me/en/briefs/2026-11-04/)). 두 회사 모두 벤치마크보다 “어떤 업무 도구 안에서 쓰이나”를 앞세웠다.

## 왜 중요한가
오픈 가중치 모델이 **화면·도면·3D 툴까지 읽고 조작하는** 방향으로 가고 있다. 디자인·3D 작업 자동화를 생각한다면 폐쇄형 API 말고도 선택지가 생긴다는 뜻이다.

## 주의
SCMP에 따르면 텐센트는 연구 수준 수학, 장기 코딩, 고난도 시각 질의응답 등에서 **여전히 최상위 폐쇄형 모델보다 뒤진다**고 인정했다([SCMP](https://www.scmp.com/tech/big-tech/article/3373227/tencent-unveils-hy4-open-weight-ai-race-deepseek-zai-alibaba-heats)). 성능 주장은 회사 자체 평가다.
