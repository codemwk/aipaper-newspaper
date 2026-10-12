---
title: "AI 콘텐츠: Helix World — 실시간 시청각 월드모델, H800에서 RTF 0.77·WBench 79.9, 공간 음향 점수 41.8(EchoWM 12.7)"
date: 2026-10-13T07:04:00+09:00
category: "AI 콘텐츠"
slug: "helix-world-av"
summary: "Noiz AI×HKUST가 10/12 Helix World를 공개. 한 장 이미지에서 WASD·화살표로 탐색하면 비디오+스테레오 사운드를 동시에 생성(24fps, 768×512). H800 RTF 0.77, WBench navigation 79.9. HelixBench 공간일관성 41.8 vs EchoWM 12.7. 코드·프리뷰 가중치·helixworld.org 데모. GitHub ~627★."
---

## 한줄 요약
대부분의 인터랙티브 월드모델은 **무음**이다. Noiz AI와 HKUST는 **2026-10-12** [Helix World](https://noiz.ai/lp/blog/meet-helix-world)로, 카메라가 돌면 **스테레오 음장도 같이 도는** 실시간 시청각 월드모델을 냈다. 단일 **NVIDIA H800**에서 **RTF 0.77**(1초 영상에 0.77초 연산, 디코딩 포함), WBench navigation **79.9**.

## 어떻게 동작하나
- **입력**: 시작 이미지(768×512) + 선택적 텍스트. **WASD·화살표**로 이동·시야. 약 **1.3초** 청크 단위로 생성되어 다음 청크부터 입력 반영.
- **벤치**(논문 Table 3·4를 블로그가 인용): 실시간(RTF<1) 모델 중 WBench 최고 **79.9**(무음 SANA-WM 76.0, Matrix-Game 3 71.3). 더 높은 점수대(82.0 등)는 RTF 1.98–4.29로 실시간 밖.
- **소리**: 자체 HelixBench(1,015 케이스)에서 공간-음향 일관성 **41.8** vs EchoWM **12.7**(블로그 한곳 12.6). 비디오→오디오 후처리 파이프라인은 공간 점수가 음수까지 떨어지기도 함.
- **데이터**: 원본 4,100시간 → 필터 후 **3,000시간·210만 클립**(수율 73.1%), 진짜 스테레오+메트릭 카메라 포즈.
- **구조**: LTX-2.3 기반 양방향 teacher → causal student(self-forcing + trajectory distillation). 공개물: [arXiv:2609.38123](https://arxiv.org/abs/2609.38123), GitHub [NoizAI/HelixWorld](https://github.com/NoizAI/HelixWorld)(**~627★**, 2026-10-13 `gh`), HF 프리뷰, 데모 helixworld.org.

## 왜 중요한가
영상 생성에서 “예쁜 클립” 다음 전쟁은 **조작 가능한 세계**다. Helix는 **소리까지 같은 루프**에 넣어, 후처리 더빙이 깨는 공간 일관성을 정면으로 잰다. 한계도 분명하다 — 해상도 768×512, 속도는 **데이터센터 H800** 기준, 시각만 보면 최강 무음 모델에 살짝 못 미치고, 공개 체크포인트는 **프리뷰**.

## 기억할 것
- “실시간”은 소비자 GPU 수치가 아니다.
- 사용자 연구에서 오디오 포함 시 EchoWM 대비 선호 67.9% vs 20.8% — **이점이 주로 소리에서** 온다고 블로그가 요약한다.

출처: [Noiz — Helix World](https://noiz.ai/lp/blog/meet-helix-world) · [GitHub NoizAI/HelixWorld](https://github.com/NoizAI/HelixWorld) · [arXiv:2609.38123](https://arxiv.org/abs/2609.38123)
