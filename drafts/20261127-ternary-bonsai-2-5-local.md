---
title: "AI 모델: 27B 모델을 5.9GB로 — PrismML ‘Ternary Bonsai 2.5’, 가중치를 -1·0·1 세 값으로 줄이고도 원본 SWE-bench의 94% 수준, RTX 4090에서 초당 204토큰"
date: 2026-11-27T07:20:00+09:00
category: "AI 모델"
slug: "ternary-bonsai-2-5-local"
summary: "칼텍 연구진 출신 PrismML이 11/24 Ternary Bonsai 2.5 27B를 Apache 2.0으로 공개했다. Qwen3.8 27B의 가중치를 세 가지 값(1.76비트)으로 압축해 54GB짜리를 5.9GB로 줄였고, 전작에서 무너졌던 에이전트 코딩 성능을 크게 되살렸다. SWE-bench Verified 75.6(원본 80.6), AppWorld 90.5(원본 93.2). Mac·iPhone(MLX), NVIDIA·Intel GPU(llama.cpp)에서 돈다."
---

## 한줄 요약
“내 파일을 밖으로 보내지 않는 로컬 에이전트”의 걸림돌은 메모리였다. Bonsai 2.5는 **27B급 두뇌를 6GB 안쪽**에 넣고, 이번엔 **여러 번 도구를 부르는 긴 작업**에서도 덜 무너지게 만들었다([PrismML 발표, 11/24](https://prismml.com/news/bonsai-2-5-27b)).

## 무엇이 달라졌나
- **크기:** 원본 약 54GB → **5.93GB**. 가중치 하나를 -1·0·1 세 값만 쓰는 ‘3진(ternary)’ 압축(약 1.76비트)([The Decoder 경유 보도](https://anishoai.com/en/news/ai-models/2026-11-26), [Hugging Face](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)).
- **문맥 262K 토큰, 이미지 입력** 지원.
- **전작(Bonsai 2) 대비 회복폭이 핵심:**

| 벤치마크 | 원본 Qwen3.8 27B | Bonsai 2 | **Bonsai 2.5** |
| --- | --- | --- | --- |
| SWE-bench Verified | 80.6 | 60.8 | **75.6** |
| DeepSWE v1.1 | 30.1 | 0 | **27** |
| Terminal-Bench 2.1 | 70.8 | 52.8 | **60.1** |
| AppWorld | 93.2 | 51.2 | **90.5** |
| τ³-Bench | 72.8 | 69.1 | **73.9** |

- 전작의 고질병이던 **과한 생각·반복 루프**를 줄여 더 적은 턴·토큰으로 끝낸다고 설명.
- **속도:** H100에서 초당 291토큰(MTP 사용), 소비자용 **RTX 4090에서 초당 204토큰**.
- **실행:** NVIDIA·Intel GPU는 llama.cpp(전용 포크 또는 표준 빌드 b11556+의 Q2_0), Apple 기기는 MLX. 라이선스 **Apache 2.0**.

## 왜 중요한가
- 개인 볼트·사내 저장소처럼 **밖으로 내보내기 싫은 자료**를 다루는 코딩·문서 에이전트를 노트북이나 Mac mini에서 돌릴 현실적 후보가 생겼다.
- 압축 모델의 약점은 늘 “한 번 답하기는 괜찮은데 도구를 열 번 부르면 무너진다”였다. AppWorld 51→90 회복은 그 약점을 정면으로 고쳤다는 주장이다.
- 주의: 모든 수치는 PrismML 자체 측정(백서 공개)이다. 최상위 성능은 여전히 원본보다 낮고, 일부 형식은 전용 llama.cpp 포크가 필요하다.

출처: [PrismML — Introducing Ternary Bonsai 2.5 27B](https://prismml.com/news/bonsai-2-5-27b) · [모델 문서](https://docs.prismml.com/models/bonsai-2-5-27b) · [Hugging Face GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)
