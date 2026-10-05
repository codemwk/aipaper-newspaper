---
title: "AI 모델: Reflection Beam — 501B/활성 23B 오픈웨이트, ‘중국 오픈모델급을 추론 연산 3~4배 적게’"
date: 2026-10-06T07:03:00+09:00
category: "AI 모델"
slug: "reflection-beam-open-weight"
summary: "10/5 Reflection AI 첫 오픈웨이트 Beam: 텍스트 전용 MoE 501B(활성 23B), 사전학습 23.8T 토큰, 컨텍스트 1M. GB300 10.5K장·4주·1억+ 롤아웃 RL. GLM-5.2급 추론을 3~4배 적은 연산으로(자사 주장). 가중치는 이달 중 Apache 2.0 공개 예정, 지금은 대기자 프리뷰."
---

## 한줄 요약
설립 2년 차 미국 스타트업 Reflection AI가 10월 5일 첫 오픈웨이트 모델 **Beam**을 공개했다([Reflection Blog](https://reflection.ai/blog/introducing-beam)). 총 **501B 파라미터, 토큰당 활성 23B**의 텍스트 전용 MoE로, 코딩·추론·에이전트 작업에 맞췄다. 메시지는 하나다 — **“DeepSeek·Qwen·Z.ai에 대한 서구의 오픈 답안”**([TechCrunch](https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/)).

## 핵심 숫자
- **사전학습** 23.8조 토큰(웹+라이선스 데이터), GB300 NVL72 6,144장으로 4주 이내. 컨텍스트 **1M 토큰**.
- **강화학습**: GB300 **10,500장 × 4주**, 롤아웃 1억 건 이상, 샌드박스 약 13억 개, 학습 환경 약 100만 개. “오픈 랩 중 최대급 RL”이라고 주장, 연산을 더 넣을수록 성능이 계속 올라 **포화 징후가 없었다**고 했다.
- **자사 벤치마크**: SWE-Bench Verified 80.9, Terminal-Bench 2.1 80.1, GPQA Diamond 90.5, MCP Atlas 78.7. GLM-5.2와 비슷하고 Qwen 3.8-Max에 근접, **Kimi K3는 여전히 앞선다**고 스스로 인정. 독립 검증은 아직 없다.
- **효율**: 추론 벤치에서 GLM-5.2급 점수를 **3~4배 적은 추론 연산**으로. 사용자는 ‘reasoning effort’로 길이·성능을 조절한다.

## 회사와 사업
- 전 DeepMind 연구자 2명이 2024년 창업, 누적 조달 약 **$47억**(Nvidia·Sequoia·Lightspeed), 직전 라운드 프리머니 $250억. 올여름 SpaceX·Nebius와 **$70억+ 규모 GB300 확보 계약**(2029년까지).
- 목표는 기업·국가용 **‘AI 팩토리’** — 고객이 자기 데이터로 Reflection 모델을 학습시켜 자체 AI를 갖는 구조. 한국 **신세계그룹**과 소버린 AI 팩토리 파트너십을 시험 중이고, Axios에 따르면 헤지펀드·트레이딩 회사의 관심이 크다.

## 왜 중요한가
최근 오픈웨이트 상위권은 거의 중국 모델(Kimi·GLM·Qwen·DeepSeek)이었다. Beam은 **“더 큰 모델”이 아니라 “같은 성능을 더 싸게 돌리는 모델”**로 승부를 건다. 에이전트는 토큰을 많이 쓰니, 활성 23B·짧은 추론이 곧 운영비다. 다만 지금은 **대기자 프리뷰**이고 가중치·기술 보고서·모델 카드는 “이달 중” 공개 예정 — 숫자는 공개 후 다시 확인해야 한다.

## 기억할 것
- 라이선스: Apache 2.0(공개 시). 텍스트 전용(멀티모달 아님).
- [Reflection Blog 10/5](https://reflection.ai/blog/introducing-beam) · [TechCrunch 10/5](https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/)
