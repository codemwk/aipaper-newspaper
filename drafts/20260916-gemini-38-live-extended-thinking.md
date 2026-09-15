---
title: "제미니 3.8 Live · Live Extended Thinking — 말하면서 백그라운드 추론"
date: 2026-09-16T07:10:00+09:00
category: "AI Models"
slug: "gemini-38-live-extended-thinking"
summary: "공식 2026-09-15. Gemini 3.8 Live(스케일·비용)와 Live Extended Thinking(고복잡도·비동기 툴). Docs/Gmail/Keep Live·Search Live·Live API. 오디오 SynthID."
---

## 한줄 요약
[Google(2026-09-15)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)가 **Gemini 3.8 Live**와 **3.8 Live Extended Thinking**을 공개했다. 음성으로 대화하면서 툴·추론을 **백그라운드**에서 돌리고, 진행을 말로 나레이션하는 라이브 모델이다.

## 핵심
- **Live**: 저지연·비용 효율, 시각 그라운딩, 97개 언어 중도 전환, 대화 유지하며 툴/API 실행.
- **Live Extended Thinking**: 고복잡도용. `thinking_level` low/medium/high, 비동기(`NON_BLOCKING`) 툴. “Let me check…” 식 필러로 턴을 끊지 않음([API 문서](https://ai.google.dev/gemini-api/docs/live-api/thinking)).
- 벤치 주장: Artificial Analysis Speech-to-Speech Quality Index 1위(82.6), τ-Voice 68.6% 등 — 벤더는 자사 발표이므로 교차검증 권장.
- 롤아웃: Gemini API·AI Studio / Enterprise 프리뷰 / Search Live·Gemini Live / Workspace Docs(Pro·Ultra)·Gmail·Keep.
- 개발자 가격(동시 발표 오디오 글): 오디오 입력 $0.005/분, 출력 $0.018/분. 파트너: LiveKit·Pipecat·LangChain·Vercel 등.
- 생성 오디오는 **SynthID** 워터마크.

## 왜 중요한가
어제 다룬 ‘에이전틱 비디오’와 축이 다르다. 오늘은 **보이스 에이전트가 추론·툴을 병렬로** 가져가는 제품화다. OpenAI GPT-Live-1 API와 같은 주(9/10)에 맞붙어, “풀듀플렉스 + 백엔드 위임”이 표준 패턴이 됐다.

## 기억할 것
- 모델 ID 예: `gemini-3.8-live-extended-thinking`
- 공식: [블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) · [Live Thinking 가이드](https://ai.google.dev/gemini-api/docs/live-api/thinking)
