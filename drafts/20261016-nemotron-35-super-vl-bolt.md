---
title: "AI 모델: NVIDIA Nemotron 3.5 ‘Super VL’(120B)·‘Bolt’(74B-A9B, 24GB) — 문서를 ‘보는’ 기업 에이전트와 노트북용 2비트 로컬 에이전트"
date: 2026-10-16T07:02:00+09:00
category: "AI 모델"
slug: "nemotron-35-super-vl-bolt"
summary: "NVIDIA(10/15)가 오픈 모델 3종 공개. Super VL 120B: OCR·표·차트·PDF·웹페이지를 읽는 멀티모달 에이전트용, 약 26조 토큰 학습·380만 샘플 후학습, 오픈 가중치+데이터셋+레시피. Bolt 74B-A9B: 네이티브 2비트로 24GB에 들어가는 로컬 에이전트용(llama.cpp·Ollama·LM Studio 지원). Bolt E4B(4GB)는 10/23. Perplexity·Atlassian·CrowdStrike·Salesforce 등이 도입·커스터마이즈 중(회사)."
---

## 한줄 요약
같은 날 Meta가 초대형 오픈 모델을 냈다면, NVIDIA는 **“층마다 하나씩”** 전략을 냈다. 2026-10-15 공개된 **Nemotron 3.5 Super VL**(데이터센터), **Bolt 74B-A9B 24GB**(데스크톱·노트북), **Bolt E4B 4GB**(엣지·음성, 10/23 출시)다([NVIDIA 블로그](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)).

## Super VL — 에이전트가 실제로 마주치는 ‘화면’을 읽는다
- **120B 오픈 모델**. 강점은 OCR, 표, 차트, PDF·웹페이지 같은 **시각 문서 이해**와 도구 사용·다단계 업무 흐름. 텍스트와 시각을 한 모델에서 처리해 “문서→데이터→결정”을 시스템 전환 없이 잇는다는 설명.
- NVIDIA 주장: 자사 최대 추론 모델과 비슷한 정확도를 **약 5분의 1 크기**로, 같은 급 오픈 모델 대비 **최대 5배 빠른 처리량**.
- 학습: 사전·연속 사전학습 약 **26조 토큰**, 후학습 약 **380만 샘플** + 수십 개 환경 RL. **가중치·데이터셋·학습 레시피**를 함께 공개하고, RL 환경은 NeMo Gym에 올렸다.
- 도입 사례(회사 발표): Scale AI가 EY의 M&A 실사 에이전트용으로, AfterQuery가 Hebbia의 대출 약정 분석용으로 후학습. Ramp(금융 문서), Perplexity(검색·Computer), Atlassian(Jira·Confluence 검색), CrowdStrike(블루팀), Salesforce(정부 업무).
- 배포: Hugging Face, OpenRouter, ModelScope, NVIDIA NIM.

## Bolt — “24GB에 들어가는 에이전트”
- **74B 총·9B 활성(A9B)** MoE를 **네이티브 2비트 양자화**로 24GB에 맞췄다. 다른 앱과 같이 돌아가는 것이 목표.
- 웹 리서치·글쓰기·코드 디버깅을 클라우드로 보내지 않고 로컬 에이전트 하네스에 맡기는 용도. llama.cpp·Ollama·LM Studio·Unsloth·vLLM 지원.
- 10/16 출시되는 **RTX Spark 노트북**을 겨냥했고, GeForce RTX PC·DGX Spark에서도 돈다. NVIDIA는 PinchBench 같은 급 1위, BrowseComp 2위라고 밝혔다(회사 발표).
- **Bolt E4B 4GB**(10/23): 음성 비서·인터랙티브 캐릭터용 소형.

## 왜 중요한가
NVIDIA가 모델을 내는 이유는 결국 **자사 하드웨어 위에서 돌 오픈 모델의 기본값**을 쥐기 위해서다. 사용자 입장에선 “사내 PDF·대시보드를 읽는 에이전트를 우리 서버에서, 우리 데이터로 후학습”할 수 있는 현실적인 선택지가 하나 늘었다. Bolt는 어제 다룬 Liquid LFM2.5-24B와 함께 **로컬 에이전트 모델**이라는 흐름을 키운다. 속도·순위 수치는 모두 NVIDIA 자체 발표다.

출처: [NVIDIA Blog — Nemotron 3.5 Super VL & Bolt](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
