---
title: "AI 콘텐츠: Sber Kandinsky Avatar 1.0 — 사진 한 장 + 음성 + 한 줄 설명이면 최대 1분 ‘말하는 아바타’. MIT 라이선스, Lite는 집 GPU에서"
date: 2026-11-04T07:04:00+09:00
category: "AI 콘텐츠"
slug: "kandinsky-avatar-open"
summary: "Sber가 말하는 아바타 영상 모델 Kandinsky Avatar 1.0(Kandinsky S2V 1.0)을 코드·가중치까지 MIT로 공개했다. 참조 이미지·오디오·장면 설명을 넣으면 입 모양, 표정, 고개, 제스처까지 맞춘 영상을 최대 1분 생성. Pro(21B, HD)와 Lite(2B, SD, 가정용 GPU) 두 종류와 증류(빠른) 버전. 95개 언어 인터뷰·강연·팟캐스트 100만+ 클립으로 학습. ComfyUI·Diffusers 지원."
---

## 한줄 요약
HeyGen·Synthesia가 구독으로 팔던 ‘말하는 아바타’를 **상업적 사용까지 되는 오픈 모델**로 풀었다. Sber는 Pro가 “HeyGen과 같은 수준”이라고 주장한다([vc.ru](https://vc.ru/ai/3233090-kandinsky-avatar-1-0-ot-sbera), [프로젝트 페이지](https://kandinskyavatar.github.io/)).

## 무엇을 하나
- **입력 3개**: 인물 이미지 1장, 음성 파일, 장면 텍스트. 감정·동작을 글로 지시할 수 있다.
- **출력**: 립싱크, 표정, 고개 돌림, 손짓이 들어간 영상. 길이 **최대 1분**. 아바타는 넣은 음성의 언어로 말한다.
- **두 크기**: **Pro 21B**(HD, 품질 우선) · **Lite 2B**(SD, 가정용 그래픽카드). 각각 단계를 줄인 증류 버전도 있다([Hugging Face 예](https://huggingface.co/kandinskylab/Kandinsky-S2V-1.0-Pro-distill-Diffusers)).
- **학습**: 95개 언어(러시아어·영어·카자흐어·스페인어·프랑스어 등)의 인터뷰·강연·팟캐스트 클립 100만 개+. 기반은 Kandinsky 5.0 Video.
- **배포**: GitHub·GitVerse·Hugging Face, **MIT**. ComfyUI·Diffusers에서 쓸 수 있다.

## 왜 중요한가
- 아바타 영상 시장의 가격 기준이 흔들린다. 최근 일주일 오픈 진영엔 Pika H3 Flex 가중치, Hy-SimulMT(목소리 복제 통역)가 있었다. **사진 + 목소리 + 통역**을 로컬에서 엮는 1인 다국어 채널 파이프라인이 오픈 모델만으로 가능해지는 중이다.
- 브랜드 스튜디오 관점: 설명 영상·제품 소개를 여러 언어로 찍어 내는 비용이 ‘구독료’에서 ‘GPU 시간’으로 바뀐다.

## 주의
- “HeyGen급”은 회사 주장. 프레임레이트는 보도마다 24fps(vc.ru)·25fps(프로젝트 설명)로 다르게 나온다.
- MIT라도 **실존 인물의 얼굴·목소리** 사용은 초상권·동의 문제가 별개로 남는다.
