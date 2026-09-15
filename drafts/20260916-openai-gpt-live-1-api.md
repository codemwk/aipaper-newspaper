---
title: "OpenAI GPT-Live-1 API — 풀듀플렉스 음성 $0.05/분, 추론은 백엔드에 위임"
date: 2026-09-16T07:20:00+09:00
category: "AI Models"
slug: "openai-gpt-live-1-api"
summary: "공식 2026-09-10. ChatGPT 보이스의 풀듀플렉스를 API로. STT-LLM-TTS 캐스케이드 대신 단일 보이스 레이어. Astra 등 백엔드에 툴·추론 위임. WebRTC·WebSocket·전화."
---

## 한줄 요약
[OpenAI(2026-09-10)](https://openai.com/index/introducing-gpt-live-1-in-the-api/)가 **GPT-Live-1**을 API에 공개했다. 듣고 말하는 것을 동시에 하는 풀듀플렉스 보이스 레이어이며, 깊은 추론·툴은 **백엔드 모델·에이전트 하네스**에 위임한다.

## 핵심
- 전통 STT→LLM→TTS 파이프라인의 핸드오프 지연·끊김을 줄이려는 단일 모델 보이스 레이어.
- **위임**: Responses 위임(OpenAI 백엔드) 또는 클라이언트 위임(자체 Codex/에이전트). 예: 대량 업무는 Luna급, 복잡 이슈는 Astra.
- 기능: 인터럽트·톤/페이스/스타일 프롬프트, 배경소음·침묵 처리, ASR 트랜스크립트, 키워드 바이어싱, 턴 디텍션, **텔레포니**.
- 가격: 보이스 레이어 **$0.05/분**(초 단위 과금). 백엔드 토큰·툴은 별도.
- 고객 인용: Speak — 생각 중 끼어들기 **약 80% 감소**(전기 턴제 대비, 조기 평가). Yelp·Intercom Fin·Devin 등 인용.

## 왜 중요한가
제미니 3.8 Live와 같은 주간에 **“대화는 듀플렉스, 일은 백엔드”** 아키텍처가 양대 벤더에서 공식화됐다. 트레이딩·고객응대·튜터링처럼 **손·눈이 바쁜 루프**에 음성 에이전트를 붙일 때, 빌더는 보이스 SLA와 백엔드 권한·취소를 분리 설계해야 한다(말 끊기가 백엔드 작업을 자동 취소하지 않음).

## 기억할 것
- 공식: [launch post](https://openai.com/index/introducing-gpt-live-1-in-the-api/) · [changelog](https://developers.openai.com/api/docs/changelog) · [WebSockets](https://developers.openai.com/api/docs/guides/voice-websockets)
