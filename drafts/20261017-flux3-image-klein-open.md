---
title: "AI 콘텐츠: FLUX 3 Image Klein 오픈웨이트 — 5.6B로 4K·편집·레퍼런스 10장·바운딩박스, 8GB 그래픽카드에서 돌고 연 매출 $500만 미만은 상업 무료"
date: 2026-10-17T07:04:00+09:00
category: "AI 콘텐츠"
slug: "flux3-image-klein-open"
summary: "Black Forest Labs(10/15): FLUX 3 Image Klein 공개. 5.6B 파라미터 오픈웨이트, 텍스트→이미지·편집·최대 10장 멀티 레퍼런스, 네이티브 4K, 바운딩박스 배치·편집 영역 제한. 16스텝 증류 모델 + 50스텝 베이스(파인튜닝용), FP8·INT8·NVFP4. BF16 11.2GB·FP8 5.6GB, INT8은 VRAM 8GB. RTX 5090 1MP 약 4초. API flux-3-image-klein 1K 이미지당 $0.009부터. FLUX Kommunity License."
---

## 한줄 요약
10/4 본지가 “오픈웨이트는 수주 내”라고 전했던 **FLUX 3** 계열에서 **작은 오픈 모델**이 먼저 나왔다. Black Forest Labs(BFL)는 2026-10-15 **FLUX 3 Image Klein**을 공개했다 — 5.6B 파라미터로 큰 FLUX 3 Image의 핵심 기능(네이티브 4K, 정밀 편집, 바운딩박스)을 그대로 가져왔다([BFL 블로그](https://bfl.ai/blog/flux-3-image-klein)).

## 무엇을 할 수 있나
- **세 가지 일을 한 모델로**: 텍스트→이미지, 이미지 편집, **최대 10장**의 레퍼런스를 섞는 멀티 레퍼런스 생성.
- **바운딩박스**: 프롬프트에 박스를 넣어 요소가 놓일 **자리를 지정**하거나, 편집을 **정해진 영역 안으로 제한**한다. 레이아웃이 중요한 광고·썸네일 작업에 직접 쓰이는 기능.
- **두 체크포인트**: 빠른 생성용 **증류 모델(16스텝)**과 LoRA·파인튜닝용 **베이스(50스텝)**. Diffusers·Ostris AI Toolkit·NVIDIA NeMo가 첫날부터 학습을 지원.
- **API 옵션**: 모델명 `flux-3-image-klein`, 프롬프트 자동 보강과 **편집하지 않은 영역을 픽셀 그대로 보존**하는 기능 포함. 가격은 1K 이미지당 **$0.009부터**.

## 얼마나 가벼운가 (BFL·NVIDIA 측정)
- 생성기 가중치 **BF16 11.2GB, FP8 5.6GB**. **INT8 빌드는 VRAM 8GB** GeForce RTX에서도 ComfyUI·Diffusers로 동작.
- 증류 모델+INT8로 1MP 이미지 1장: **RTX 5090 약 4초, RTX 4070 9초 미만**. 데이터센터 GB300(NVFP4)에선 0.6초 미만.
- 자체 평가에서 이전 FLUX.2 [klein] 9B보다 파라미터는 38% 적은데 Elo가 텍스트→이미지 +91, 편집 +70. (비교·순위는 회사 내부 평가다.)

## 라이선스가 핵심
**FLUX Kommunity License**: 개인과 **연 매출 $500만 미만 기업은 상업 이용 무료**, 연구·비상업도 허용. 그 이상은 자체 호스팅 라이선스나 API를 사야 한다. 1인 스튜디오나 소규모 에이전시는 내 PC에서 돌려 클라이언트 작업에 써도 된다는 뜻이다. 이것은 FLUX 3 Action에 이은 FLUX 3 계열의 **두 번째 오픈웨이트**이고, BFL은 “더 나온다”고 했다.

## 왜 중요한가
이미지 생성의 실무 병목은 “예쁜 한 장”이 아니라 **“로고는 여기, 제품은 저기, 나머지는 건드리지 마”**를 지키는 것이다. 바운딩박스와 미편집 영역 보존이 5.6B짜리 로컬 모델에 들어오면서, 브랜드 에셋을 클라우드에 올리지 않고 **내 그래픽카드에서 반복 수정**하는 워크플로가 현실이 됐다. 브랜드 일관성을 위해 자사 스타일 LoRA를 학습시키기에도 베이스 모델 크기가 적당하다.

출처: [BFL — FLUX 3 Image Klein](https://bfl.ai/blog/flux-3-image-klein) · [Hugging Face — FLUX.3 in Diffusers](https://huggingface.co/blog/flux-3) · [BFL Docs](https://docs.bfl.ml/flux_3/flux3_image_klein)
