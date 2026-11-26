---
title: "AI 모델: 러시아 Sber ‘GigaChat 4’ — 708B 오픈 모델을 MIT로 공개, 100만 토큰 문맥에 ‘생각 모드·즉답 모드’를 한 체크포인트에"
date: 2026-11-27T07:15:00+09:00
category: "AI 모델"
slug: "gigachat-4-open-708b"
summary: "러시아 최대 은행 Sber가 11/26 AI Journey 행사에서 GigaChat 4를 공개하고 가중치를 Hugging Face에 올렸다. 총 708B(토큰당 41B 활성) MoE에 기본 문맥 100만 토큰, Reasoning·Instant 두 모드를 한 모델에 담았다. 자체 측정 Terminal-Bench 2.0은 71.26%(전작 30.30%). 708B 지시 튜닝 모델은 MIT, GPU 1~2장용 37B 소형 모델은 개인 비상업 라이선스다."
---

## 한줄 요약
초대형 오픈 모델 진영에 **러시아 은행**이 들어왔다. 크기(708B), 문맥(100만 토큰), 라이선스(MIT) 세 가지가 모두 공격적이다([GigaChat 4 기술 보고서, 11/26](https://giga.chat/blog/en/posts/gigachat-4-tech-report), [Vedomosti](https://www.vedomosti.ru/technology/news/2026/11/26/1415693-novie-modeli)).

## 무엇이 나왔나
- **GigaChat4-708B-A41B:** 총 7,080억 파라미터, 토큰당 410억만 쓰는 MoE. 전문가 256개 중 8개 + 공유 전문가 1개.
- **GigaChat4-37B-A4B:** 총 37B·활성 4B. GPU 1~2장에서 돌릴 수 있는 소형판.
- **문맥 100만 토큰**을 기본 지원. 학습 중 32K→128K→1M으로 단계적으로 늘렸다.
- **두 모드를 한 모델에:** 전작 3.5는 즉답·추론 체크포인트가 따로였지만, 4는 요청마다 Reasoning/Instant를 고른다.
- **구조:** Gated DeltaNet(선형 어텐션) 층과 DeepSeek Sparse Attention 층을 3:1로 섞어 긴 문맥 비용을 낮췄다. 생성 가속용으로 MTP와 별도 확산형 초안 모델 DFlash2를 지원.
- **형식·라이선스:** FP8·BF16·**GGUF** 공개. 708B 지시 튜닝 모델은 **MIT**, 37B는 **개인 비상업 라이선스**. 호스팅 API 가격은 발표되지 않았다.

## 성능 (자체 측정)
- Terminal-Bench 2.0: **Reasoning 71.26% / Instant 60.47%** (GigaChat 3.5는 30.30% / 12.94%).
- 회사는 코딩·에이전트 과제에서 DeepSeek V4 Flash, Mistral 4 Large와 “비슷한 수준”이라고 적었다. 독립 검증은 아직 없다.

## 왜 중요한가
- 같은 날 Sber는 이미지·영상 모델 **Kandinsky 6.5**(10초 2K 영상, 여러 인물 장면)도 내놨다([RIA](https://ria.ru/20261126/sber-2134158900.html)). 미국·중국 밖에서도 **풀스택 오픈 모델 공급자**가 생기고 있다는 뜻이다.
- 실사용 관점에선 37B 소형판이 더 현실적이지만 **상업 이용 불가**다. 회사 업무에 쓰려면 708B(MIT)를 호스팅해야 하는데, 이는 개인에겐 무겁다.
- 주의: 성능은 회사 평가 프로토콜 기준이고, 러시아 기업 모델이라 조직에 따라 **공급망·제재 검토**가 필요할 수 있다.

출처: [GigaChat 4 Technical Report](https://giga.chat/blog/en/posts/gigachat-4-tech-report) · [Hugging Face ai-sage/GigaChat4-708B-A41B](https://huggingface.co/ai-sage/GigaChat4-708B-A41B) · [GPTOnline 정리](https://gptonline.ai/sber-gigachat-4-708b-open-model-1m-context/) · [Vedomosti](https://www.vedomosti.ru/technology/news/2026/11/26/1415693-novie-modeli)
