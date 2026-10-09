---
title: "AI 모델: GPT-6.1 Sol Ultrafast — Standard 대비 최대 8배 빠르다 주장, API 가격은 6배($12/$60), Codex·Work는 Pro $500부터"
date: 2026-10-10T07:04:00+09:00
category: "AI 모델"
slug: "gpt-61-sol-ultrafast"
summary: "OpenAI가 10/8 GPT-6.1 Sol에 Ultrafast 모드를 API·Codex·ChatGPT Work에 롤아웃. Responses API에서 service_tier=ultrafast. Standard 입력 $2·출력 $10의 6배. Codex/Work는 Pro 500·적격 Enterprise/Edu. AWS Bedrock에도 同日 지원."
---

## 한줄 요약
**GPT-6.1 Sol**에 **Ultrafast** 티어가 붙었다. OpenAI는 Standard 대비 **최대 8배** 빠르다고 하고, API 요금은 Standard의 **6배**다([Developer Community 10/8](https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475/1), [모델 문서](https://developers.openai.com/api/docs/models/gpt-6.1-sol)).

## 무엇이 바뀌나
- **켜는 법**: Responses API에서 `model: "gpt-6.1-sol"` + `service_tier: "ultrafast"`.
- **가격(짧은 컨텍스트 Standard 기준)**: 입력 **$2** · 캐시 읽기 **$0.10** · 캐시 쓰기 **$2.50** · 출력 **$10**(1M 토큰). Ultrafast는 각각 **6배** → 입력 **$12** · 출력 **$60**. Fast는 2배, Batch/Flex는 50% 할인. 272K 초과 프롬프트는 입력·캐시 2배·출력 1.5배.
- **누가 쓰나**: API는 지원 지역 전체. Codex·ChatGPT Work는 출시 시 **Pro $500**, 사용량 기반 Enterprise, 크레딧 Edu — 관리자가 켜야 함. Community 공지는 Ultrafast가 Astra 대비 **약 1.2배 비용**이라고도 적어, “최고속 티어를 Astra급에 가깝게” 포지셔닝한다.
- **클라우드**: 같은 날 AWS가 **Amazon Bedrock**에서 GPT-6.1 Sol Ultrafast를 발표했다([AWS](https://aws.amazon.com/about-aws/whats-new/2026/10/openai-gpt-sol-ultrafast-amazon/)).

## 왜 중요한가
10/3에 Pro $500 Ultrafast 이야기가 나왔다면, 이번은 **Sol 본체를 API·Work·Bedrock까지 같은 속도 티어로 묶는** 확장이다. 장애 디버깅·앱을 탐색하는 에이전트·실시간 UX처럼 **대기 시간이 곧 비용**인 구간에, “똑똑한데 느린 모델” 대신 **비싸지만 즉시 반응하는 Sol**을 고르는 선택지가 생긴다. 8배 수치는 회사 주장이고 독립 벤치마크는 아직 없다.

출처: [OpenAI Community — Ultrafast rollout](https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475/1) · [GPT-6.1 Sol docs](https://developers.openai.com/api/docs/models/gpt-6.1-sol) · [AWS Bedrock Ultrafast](https://aws.amazon.com/about-aws/whats-new/2026/10/openai-gpt-sol-ultrafast-amazon/)
