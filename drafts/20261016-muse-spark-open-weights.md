---
title: "AI 모델: Meta ‘Muse Spark Open’ 가중치 공개 — 816B(활성 42B) MoE·100만 토큰, 맥 스튜디오 두 대로 집에서 돌리는 코딩 에이전트"
date: 2026-10-16T07:01:00+09:00
category: "AI 모델"
slug: "muse-spark-open-weights"
summary: "Meta(10/15)가 Muse Spark의 오픈 가중치판을 공개. 총 816B·토큰당 활성 약 42B(256 전문가 중 8개), 텍스트·이미지·오디오·영상 입력 → 텍스트 출력, 컨텍스트 100만 토큰. BF16(약 1.5TB)·NVFP4 체크포인트, M5 Ultra 맥 스튜디오 2대로 구동(회사). HF 테스트: M3 Ultra 512GB에서 2비트 18 tok/s, oQ3e 21 tok/s. 추론 끄기 불가. 라이선스는 ‘제한적 상업 조건’의 Muse Model License."
---

## 한줄 요약
9월에 다뤘던 Meta의 **Muse Spark**가 2026-10-15 **오픈 가중치**로 풀렸다. Meta는 이를 “미국산 오픈 가중치 중 가장 강력한 모델”이라고 부른다(회사 주장). 코딩·에이전트 작업에 맞춰 학습했고, 스크린샷을 보고, 음성 메모를 듣고, 화면 녹화를 보면서 코드를 고치는 **멀티모달 에이전트 모델**이다([Meta AI Research](https://research.meta.ai/blog/muse-spark-open)).

## 숫자로 보는 모델 (Hugging Face 해설 기준)
- **구조**: 총 약 **816B**, 토큰당 활성 약 **42B**. 층마다 전문가 **256개 중 8개**를 고르는 MoE, 62층. 파라미터의 약 97%가 전문가에 있다.
- **입출력**: 텍스트·이미지·오디오·영상 입력 → 텍스트 출력. 오디오는 80ms마다 토큰 1개(10초 = 125토큰), 영상은 기본 2FPS·최대 96프레임.
- **컨텍스트**: 최대 **100만 토큰**(이미지·영상·오디오 토큰 포함). 꽉 채우면 KV 캐시만 약 266GB(BF16).
- **체크포인트**: BF16(약 1.5TB)과 NVIDIA Blackwell용 **NVFP4**. BF16은 H200 32장(4노드), NVFP4는 B200 1노드.
- **추론 레버**: low/medium/high/xhigh(기본 xhigh). **추론을 완전히 끌 수는 없다** — 쉬운 일엔 low로 두라는 안내.

## “집에서 돌린다”의 실제 의미
Meta는 **M5 Ultra 맥 스튜디오 2대**(대당 최대 512GB 통합 메모리)를 묶어 모델 전체를 올렸다고 밝혔다. 데모로 오픈소스 마스토돈 앱 Ice Cubes에 실제 iOS 수정을 넣고, DaVinci Resolve를 끝까지 조작해 영상을 프레임 단위로 검토·세로 크롭했다고 한다(회사 테스트). Hugging Face 측 실측은 더 현실적이다: **M3 Ultra 512GB 한 대**에서 2비트 양자화가 **18 tok/s**(모델 304GB), oMLX oQ3e가 생성 **21 tok/s**(344GB)([HF 블로그](https://huggingface.co/blog/meta-muse-spark-open)). 즉 “개인용”이라도 **최소 256GB 이상 메모리**가 필요한 급이다.

## 어디서 쓰나
- API: Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, Together AI.
- 가중치: Hugging Face, Amazon SageMaker, Google Cloud Model Garden, Microsoft Foundry. llama.cpp·vLLM·SGLang·MLX·Unsloth 지원, 미세조정은 TorchTitan/TRL.
- **라이선스**: Muse Model License, “제한적 상업 조건” — Apache/MIT식 완전 개방은 아니다. 상용 서비스 전 조건 확인 필수.

## 왜 중요한가
오픈 가중치 최상위권은 그동안 중국 모델이 주도해 왔다. 미국 대형 연구소가 **100만 토큰·멀티모달·에이전트 특화**급을 풀었다는 건, 사내 데이터를 밖으로 내보내기 어려운 팀(금융·의료·보안)에 선택지가 생겼다는 뜻이다. 다만 벤치마크 수치는 Meta 자체 평가이고, 안전성 전체 보고서는 “곧 공개” 상태다.

출처: [Meta AI Research — Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) · [Hugging Face — Welcome Muse Spark Open](https://huggingface.co/blog/meta-muse-spark-open) · [HF 컬렉션](https://huggingface.co/collections/meta-models/muse-spark-open)
