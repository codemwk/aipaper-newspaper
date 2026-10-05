---
title: "AI 콘텐츠: Creatify Boreal-H3 — MiniMax H3를 ‘광고용’으로 후학습, 768p 초당 $0.04"
date: 2026-10-06T07:06:00+09:00
category: "AI 콘텐츠"
slug: "creatify-boreal-h3-ads"
summary: "10/2 Creatify Labs: MiniMax와 협력해 H3를 광고 작업에 맞춰 후학습. 자체 Ads Quality Index 133.3(H3=100). 가격 768p $0.04/초·1088p $0.12·2K $0.26(H3 정가의 절반, Seedance 2.5 약 $0.47 대비 약 12배 저렴). 레퍼런스 이미지 속 제품 라벨·패키지 형태·크리에이터 동일성 유지가 목표."
---

## 한줄 요약
Creatify Labs가 10월 2일 광고 전용 영상 모델 **Boreal-H3**를 냈다([PRWeb](https://www.prweb.com/releases/creatify-labs-launches-boreal-h3-a-minimax-h3-video-model-post-trained-for-advertising-302897040.html)). 중국 MiniMax의 영상 모델 **H3를 MiniMax와 함께 후학습(post-training)**한 것. 9월 ‘초당 1센트 실시간’ Boreal에 이은 패밀리 두 번째 모델이다.

## 무엇을 학습시켰나
광고주가 가장 먼저 확인하는 세 가지에 맞췄다.
- **제품 보존**: 레퍼런스 이미지 속 **라벨이 읽히는가, 패키지 모양이 유지되는가**.
- **크리에이터 연기**: UGC 광고처럼 자연스러운 말투·제스처, 첫 프레임부터 끝까지 **같은 사람**.
- **브리프 이행**: 쓴 대로 찍어 주는가.
자체 지표 Ads Quality Index에서 H3를 100으로 볼 때 **133.3** — 비교한 프런티어 영상 모델 중 최고라고 주장한다(회사 평가).

## 가격
| 해상도 | 초당 가격 |
|---|---|
| 768p | $0.04 |
| 1088p | $0.12 |
| 2K | $0.26 |
텍스트→영상, 이미지→영상, 레퍼런스→영상 모두 동일 가격. 768p 기준 **MiniMax H3 정가($0.08)의 절반**, Seedance 2.5(약 $0.47)보다 **약 12배 저렴**하다고 밝혔다. Model Playground와 API로 바로 쓸 수 있다.

## 왜 중요한가
범용 영상 모델 경쟁이 ‘더 예쁜 장면’이라면, 돈이 도는 곳은 **“제품이 망가지지 않는 영상”**이다. Boreal-H3는 (1) 남의 파운데이션 모델을 **도메인 후학습으로 특화**하고 (2) 원가 이하 가격으로 대량 소재 테스트 시장을 노리는 전형적인 2026년형 전략이다. 브랜드·스튜디오 입장에선 “어떤 모델이 최고냐”보다 **“내 제품 사진 10장을 넣고 라벨이 살아남는가”**로 직접 테스트해 보는 게 맞다.

## 기억할 것
- 품질 지표는 Creatify 자체 지수(독립 평가 아님).
- [PRWeb 10/2](https://www.prweb.com/releases/creatify-labs-launches-boreal-h3-a-minimax-h3-video-model-post-trained-for-advertising-302897040.html) · [Creatify Labs](https://labs.creatify.ai/)
