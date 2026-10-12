---
title: "AI 모델: Muse 스택의 SAM 3.1·Glimmer — 세그멘테이션 API(장당 과금)와 Apache 2.0 로컬 오픈웨이트가 Wonder와 같이 깔렸다"
date: 2026-10-13T07:11:00+09:00
category: "AI 모델"
slug: "muse-sam-glimmer"
summary: "Muse Wonder 발표와 같은 Meta Model API 문서 기준으로 SAM 3.1이 API에 올랐다(이미지 세그 $2.50/1천 장, 비디오 $0.20/1천 프레임). Muse Glimmer는 Spark에서 증류한 오픈웨이트로 vLLM 등 로컬 서빙, Apache 2.0. Wonder 토큰 모델과 ‘같은 계정·다른 과금 단위’ 포트폴리오."
---

## 한줄 요약
Meta의 Muse 발표는 텍스트 에이전트만이 아니다. 공식 [Model API 개요·가격](https://dev.meta.ai/docs/overview) 기준으로 **Segment Anything Model 3.1**이 API로 제공되고, **Muse Glimmer**는 **가중치를 받아 로컬에서** 돌리는 오픈웨이트로 분리된다. Wonder가 “월정액·토큰”이라면, 이 둘은 **장·프레임·자체 호스팅** 축이다.

## 어떻게 동작하나
- **SAM 3.1**: 짧은 텍스트로 이미지·비디오 속 객체를 찾아 **박스+마스크**. 엔드포인트는 Responses·Files. 가격은 토큰이 아니라 **이미지 1,000장당 $2.50**, **비디오 1,000프레임당 $0.20**(표준=스트리밍 동일 표기).
- **Muse Glimmer**: Muse Spark에서 증류한 **멀티모달 오픈웨이트**, **Apache 2.0**. Model API 호출이 아니라 vLLM·SGLang·llama.cpp·ExecuTorch 등으로 **직접 서빙**. “허가된 작은 모델” 포지션.
- **같은 계정**: Wonder/Spark/Image/Voice와 인증은 한 Meta Model API 체계. 과금 단위만 갈라진다(토큰 vs 장 vs 시간 vs 자체 GPU).

## 왜 중요한가
에이전트가 UI를 만지려면 **화면 위 객체 경계**가 필요하고, 온프레·엣지에는 **가중치 반출**이 필요하다. Meta는 Wonder(폐쇄·고가 토큰)와 Glimmer(개방·로컬)를 **한 브랜드 포트폴리오**에 넣었다. 경쟁사는 모델 하나만 내세우는 경우가 많은데, 여기는 **과금·배포 형태가 다른 도구 묶음**이다.

## 기억할 것
- SAM·Glimmer 상세 벤치는 개요 수준. 카드·레포를 추가로 확인할 것.
- Wonder Full ≠ Glimmer. 로컬 오픈웨이트가 구독 최강 모델을 대체한다고 적혀 있지 않다.

출처: [Meta Model API overview](https://dev.meta.ai/docs/overview) · [Pricing](https://dev.meta.ai/docs/pricing-rate-limits)
