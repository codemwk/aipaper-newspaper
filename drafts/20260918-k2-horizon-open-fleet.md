---
title: "K2 Horizon — 0.9B~375B 여섯 모델을 가중치·코드·학습데이터까지 한꺼번에"
date: 2026-09-18T07:30:00+09:00
category: "AI Models"
slug: "k2-horizon-open-fleet"
summary: "2026-09-03. MBZUAI IFM이 K2 Horizon 6종 공개. 0.9B~375B-A23B. Apache 2.0. 가중치·코드·학습 데이터·방법론 동봉 주장. HF·vLLM·SGLang·파트너 API."
---

## 한줄 요약
[PR Newswire](https://www.prnewswire.com/news-releases/institute-of-foundation-models-launches-the-industrys-largest-fully-open-source-fleet-of-ai-models-complete-with-weights-code-training-data-and-methodologies-302868628.html)(**2026-09-03**)에 따르면, MBZUAI의 **Institute of Foundation Models(IFM)**는 **K2 Horizon** 함대 여섯 종을 한꺼번에 냈다. 파라미터 **0.9B ~ 375B**.

## 무엇이 바뀌었나
- 라인업: **0.9B**(웨어러블급), **3.7B**·**7B**(온디바이스), **32B** dense, **36B-A4B**(MoVA, 활성 4B), **375B-A23B**(활성 23B 플래그십).
- IFM 주장의 핵심은 “오픈 웨이트”를 넘어 **학습 데이터·레시피·평가**까지 같이 공개해 재현·감사를 가능하게 한다는 점. 라이선스 **Apache 2.0**.
- 기술 키워드로 **diffusion distillation**(토큰 블록 병렬로 약 3× 속도)과 **mixture of value attention(MoVA)** 을 들었다.
- 배포: Hugging Face, vLLM, SGLang. API는 Compass·Cerebras·AWS·Nebius 등 파트너. 동적 라우팅으로 작은 모델→큰 모델 스케일 경로를 제시.

## 왜 중요한가
한 주 안의 Fable/Astra/Gemini 클로즈드 레이스와 결이 다르다. **엣지부터 엔터프라이즈까지 같은 패밀리**로 프로토타입→프로덕션을 옮기려는 연구·스타트업에 선택지가 생긴다. “완전 오픈” 주장의 세부(대형 모델 데이터·중간 체크포인트 완비 여부)는 커뮤니티 감사가 따라붙는 중이라, 도입 전 **해당 사이즈 아티팩트를 직접 확인**하는 편이 안전하다.

## 기억할 것
- [IFM 보도자료](https://www.prnewswire.com/news-releases/institute-of-foundation-models-launches-the-industrys-largest-fully-open-source-fleet-of-ai-models-complete-with-weights-code-training-data-and-methodologies-302868628.html) · [ifm.ai](https://ifm.ai/) · Hugging Face K2 Horizon
