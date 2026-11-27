---
title: "AI 모델: 엔비디아 ‘Pixel as Code’ — 그림은 이미지 모델이, 웹페이지·슬라이드·차트는 ‘고칠 수 있는 코드’로. 30B(활성 3B) 이미지 모델 Nemotron-Labs-Image 가중치 공개"
date: 2026-11-28T07:15:00+09:00
category: "AI 모델"
slug: "nemotron-labs-pixel-as-code"
summary: "엔비디아가 Nemotron-Labs-VisualCreation 프레임워크의 이미지 생성 부품 Nemotron-Labs-Image-30B-A3B 가중치를 Hugging Face에 올렸다. 총 30B, 토큰당 3B만 쓰는 자기회귀 이미지 모델로, 글자 많은 이미지 벤치마크 LongTextBench 97.98(GPT Image 2 96.00)을 회사가 보고했다. 프레임워크의 핵심은 웹페이지·발표 자료·차트를 픽셀이 아니라 HTML/SVG 같은 ‘편집 가능한 구조’로 만들고, 렌더링해 눈으로 검사한 뒤 고치는 것. 라이선스는 비상업 연구용이며 하네스·코드 모델은 아직 미공개."
---

## 한줄 요약
AI가 만든 슬라이드의 **오타 하나를 고치려고 이미지를 통째로 다시 뽑는** 문제를 정면으로 다룬다. 사진 같은 부분은 이미지로, 글자·레이아웃은 **코드로** 만든다([Hugging Face 모델 카드](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B), [Dataconomy, 11/26](https://dataconomy.com/2026/11/26/nvidia-releases-open-image-model-with-3b-active-parameters/)).

## 구조 — 결과물에 따라 길을 나눈다

| 경로 | 하는 일 | 결과물 |
| --- | --- | --- |
| 이미지 직행 | Image 모델이 후보 생성 → Super-VL이 골라냄 | 래스터 이미지 |
| 브라우저 기반(웹·하이브리드) | Ultra가 레이아웃 계약을 정하고, 두 모델이 코드 작성 → 렌더링 검사·시각 감사 → 부분 수리 | **편집 가능한 HTML** + 미리보기 |
| 네이티브(발표 자료·문서·SVG) | 형식별 생성기·렌더러가 검사 | 원본 파일 |

- 수리는 기본 **8번 시도 중 최대 3번 승인**까지만 하고, 가장 나은 중간본을 남긴다. 감사에서 문제를 “계획·에셋·레이아웃·코드·내용” 중 누구 책임인지 배정한다.

## 공개된 것
- **Nemotron-Labs-Image-30B-A3B:** Nemotron 3 Nano에서 출발한 Mamba-2+어텐션 하이브리드 MoE. 약 6.4억 파라미터 토크나이저 동봉. 단독 텍스트→이미지 생성 가능.
- 회사 보고 점수: LongTextBench **97.98**(GPT Image 2 96.00, Nano Banana Pro 97.60), 비즈니스 그래픽 BizGenEval **86.0**(GPT Image 2 83.2). 반면 GenEval2·Qwen-Image-Bench는 GPT Image 2가 앞선다.
- **미공개:** 전체 하네스와 구조화 코드 모델 VisionCode(30B·120B)는 “법무 검토 후 공개”.
- 라이선스: **비상업 연구·평가용**.

## 왜 중요한가
- 디자인·콘텐츠 도구의 흐름(Figma식 구조 프롬프트, 레이어 분리 모델)과 같은 방향이다. 결과물이 **고칠 수 있는 원본**이어야 실무에 들어간다는 것. 11/27 소개한 Ming-Image-Design이 “이미지 안의 레이어”로 접근했다면, 엔비디아는 **처음부터 코드로** 간다.
- “만들고 → 렌더링해 보고 → 고친다”는 루프는 AI 화면 생성의 품질 관문(done-gate) 논의와도 맞닿는다.
- 주의: 점수는 모두 **엔비디아 기술 보고서 기준**이며 독립 검증 전이다. 상업적 사용 불가, 핵심 하네스가 빠져 있어 지금 당장은 연구용 이미지 모델로 보는 게 맞다.

출처: [모델 카드](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B) · [arXiv 2611.31358](https://arxiv.org/abs/2611.31358) · [Dataconomy](https://dataconomy.com/2026/11/26/nvidia-releases-open-image-model-with-3b-active-parameters/)
