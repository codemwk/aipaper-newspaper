---
title: "AI 모델: JetBrains Mellum2.1 Instruct — ‘생각을 빼고’ 바로 답하는 오픈 코딩 모델, 서브에이전트용 일꾼"
date: 2026-11-26T07:30:00+09:00
category: "AI 모델"
slug: "mellum-2-1-instruct"
summary: "JetBrains가 11/25 Mellum2.1 Instruct를 공개했다. 10월에 낸 Mellum2.1 Thinking과 같은 구조(12B MoE, 활성 2.5B)·같은 학습이지만 사고 과정을 출력하지 않는다. 에이전트 코딩 작업에서 Thinking의 절반 정도 토큰으로 SWE-bench Verified 점수는 거의 비슷하다고 밝혔다. Apache 2.0, GGUF와 최대 1.8배 빠른 MTP 헤드도 함께 나왔다."
---

## 한줄 요약
코딩 에이전트의 일 대부분은 **작은 수정, 명령어 하나, 코드에 대한 질문**이다. 이런 일에 긴 ‘생각’은 시간만 잡아먹는다. JetBrains는 그 자리를 노린 **빠른 일꾼 모델**을 따로 냈다([JetBrains 블로그](https://blog.jetbrains.com/ai/2026/11/mellum2-1-instruct-is-out-bringing-faster-answers-for-coding-agents/)).

## 무엇이 나왔나
- **Mellum2.1 Instruct**: 총 **12B, 토큰당 활성 2.5B**인 MoE(전문가 혼합) 모델. 10월의 Mellum2.1 Thinking과 구조·학습이 같고, **사고 과정(chain of thought) 없이 바로 답한다.**
- 차이를 만든 건 사후 학습. **실제 저장소 단위 과제에서 대규모 강화학습**을 했다(NVIDIA NeMo RL·Megatron-Bridge 사용).
- 회사 수치:
  - 에이전트 코딩 작업에서 Thinking 대비 **토큰 약 절반**, SWE-bench Verified는 **거의 비슷.**
  - 이전 Mellum2 Instruct 대비 SWE-bench Verified **두 배.**
  - 비교 대상(Qwen3.5 9B, Gemma 4 E4B, 둘 다 사고 끔) 중 코드 생성은 1위, 다단계 도구 사용은 Qwen3.5 9B와 비슷. SWE-bench Verified는 Qwen3.5 9B가 더 높다.
  - 대신 활성 파라미터가 작아 단일 요청 **약 1.4배**, 부하 시 **약 1.8배** 빠르다(10월 글 기준).
- 배포: Hugging Face **Apache 2.0**, 내 컴퓨터용 **GGUF**, 생성 속도를 최대 **1.8배** 올리는 **MTP(다중 토큰 예측) 헤드.**

## 언제 무엇을 쓰나
- **Instruct**: 작은 수정, 도구 호출 루프, 채팅, 강한 모델 옆의 **서브에이전트.**
- **Thinking**: 실패한 테스트의 원인 찾기, LiveCodeBench·AIME 같은 어려운 알고리즘·수학 문제.

## 왜 중요한가
- **‘큰 모델 하나’보다 ‘지휘자 + 싼 일꾼’ 구성**이 기본이 되고 있다. 지휘는 강한 모델이, 반복 작업은 로컬에서 도는 작은 모델이 맡으면 비용과 대기 시간이 크게 준다.
- 로컬 추론에선 **생각 토큰 하나하나가 기다리는 시간**이다. 같은 계열에서 “생각 있는 버전/없는 버전”을 나눠 주는 방식은 다른 오픈 모델에도 번질 가능성이 높다.
- 주의: 벤치마크는 모두 JetBrains 자체 측정이다.
