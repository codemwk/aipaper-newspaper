---
title: "AI 모델: Reflection ‘Beam’ 가중치 실제 공개 — 501B(활성 23B)·100만 토큰·Apache 2.0, NVFP4면 B300 4장, 전용 하네스 ‘Mirror’까지 오픈"
date: 2026-10-17T07:01:00+09:00
category: "AI 모델"
slug: "reflection-beam-weights-open"
summary: "10/6 대기자 프리뷰였던 Reflection Beam이 10/16 Hugging Face에 Apache 2.0으로 풀렸다. 텍스트 전용 MoE 501B/활성 23B, 52층·전문가 256개 중 8개, 1M 컨텍스트(KV 캐시 1M에 약 36GiB). BF16 ~1TB, NVFP4 ~280GB(B300 4장), FP8은 H200 8장. 추론 강도 5단계, 투기적 디코딩 드래프터, Rust 코어 하네스 Mirror CLI, 40+ 파트너. 자체 API는 무료로 시작."
---

## 한줄 요약
10/6 본지가 “가중치는 이달 중 공개 예정”이라고 전했던 **Reflection AI의 첫 모델 Beam**이 2026-10-16 약속대로 **Hugging Face에 Apache 2.0 라이선스로 공개**됐다([Reflection](https://reflection.ai/blog/beam-is-available)). 회사는 이를 “에이전트를 위한 오픈 운영체제 — 모델은 커널”이라고 부른다.

## 무엇이 공개됐나
- **구조**: 총 **501B, 토큰당 활성 23B**의 희소 MoE. 52층, 층마다 전문가 256개 중 8개 라우팅. **텍스트 입력·출력 전용**, 컨텍스트 **100만 토큰**([Hugging Face 블로그](https://huggingface.co/blog/reflection-beam)).
- **긴 문맥이 싼 이유**: 52층 중 43층은 직전 512토큰만 보는 슬라이딩 윈도, 9층만 전체를 본다. 그래서 KV 캐시가 1M 토큰에서 약 **36GiB**(전 층이 전체를 봤다면 208GiB).
- **체크포인트**: BF16(약 1TB), FP8, NVFP4(약 280GB) + 투기적 디코딩용 **드래프터 모델**. HF 안내 기준 NVFP4는 **B300 4장**(SGLang), FP8은 **H200 8장**. 집에서 돌릴 크기는 아니다.
- **추론 강도 5단계**(low~max), 턴을 넘어 사고를 유지하는 `preserve_thinking`, 전용 문법의 도구 호출.
- **하네스 Mirror CLI**: Python 프론트엔드 + Rust 에이전트 코어. 도구 호출 승인, 재개 가능한 대화, 워크트리별 병렬 에이전트, 스킬·MCP·확장 지원. Pi·OpenCode·Hermes에서도 테스트.
- **학습 규모(회사 공개)**: 최대 RL 실행에서 샌드박스 약 **13억 개**, 피크 시 vCPU 88만 3천 개(GCP·AWS 23개 클러스터).

## 어디서 쓰나
자체 API(platform.reflection.ai, 퍼블릭 베타, 무료로 시작) 외에 AWS·Google Cloud·Azure·Oracle, Baseten·Fireworks·Together·Modal·OpenRouter·Ollama·LM Studio 등 **40개 이상** 파트너. 사내망·에어갭 환경은 Dell·HPE가 맡는다. HF는 Beam으로 만든 프로젝트에 **$1만 Hub 크레딧**을 건다. 자기증류(self-distillation) 레시피는 “수일 내” 공개 예정.

## 왜 중요한가
어제(10/16) 다룬 Meta Muse Spark Open(816B/42B)에 이어 **미국 랩의 대형 오픈웨이트가 이틀 연속** 나왔다. 차이는 라이선스다 — Muse는 상업 이용이 제한된 자체 라이선스, Beam은 **Apache 2.0**이라 기업이 고쳐서 팔아도 된다. 다만 텍스트 전용이고, 성능 표는 전부 회사 제공 수치라는 점은 감안해야 한다. 실무 포인트는 모델보다 **하네스와 함께 학습시켰다**는 대목: 코딩 에이전트 시대엔 “어떤 모델이냐”만큼 “어떤 작업대에서 길들였냐”가 결과를 가른다.

출처: [Reflection — Beam is now available](https://reflection.ai/blog/beam-is-available) · [Hugging Face — Welcome Beam](https://huggingface.co/blog/reflection-beam)
