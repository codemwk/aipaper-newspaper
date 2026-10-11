---
title: "AI 모델: OpenAI, 내부 프론티어 모델의 수학 원고 700+편을 GitHub에 — Lean 형식화·인용 규약과 함께"
date: 2026-10-12T07:04:00+09:00
category: "AI 모델"
slug: "openai-math-manuscripts"
summary: "10/6 OpenAI가 github.com/openai/math에 AI 생성 수학 결과물을 공개. 카탈로그 ~719–722편, 다수 Lean 형식화, 평균 계산량은 ChatGPT Pro 사고 ~3시간 상당이라고 회사 공표. IAS 자문그룹 권고를 반영한 공개 방식. 스타 ~14.0K."
---

## 한줄 요약
OpenAI는 **2026-10-06** [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)에서 내부 프론티어 모델이 만든 수학 결과를 **GitHub 저장소**로 공개했다. [openai/math](https://github.com/openai/math)는 원고 PDF·소스·인용 지침·(다수) **Lean** 증명 형식화를 담고, 스타는 **~14,041**(10/12).

## 어떻게 공개하나
- **자문**: Institute for Advanced Study의 *Advisory Group on Mathematics and Artificial Intelligence* 권고를 반영했다고 명시. 개정·인용 프로토콜을 저장소에 둠.
- **규모**: 초기 보도·탐색기는 **722** 원고/372 패밀리, README·카탈로그는 철회·수정 반영 **~719** 전후 — **유동**.
- **투명성 부가물**: 모델 추론 요약 **10건**, ChatGPT **Pro 사용량으로 환산한 컴퓨트**, 시도 문제 수 통계. “평균 결과는 Pro thinking **약 3시간** 상당”이라고 회사 문장.
- **앞으로**: 워크숍·학회 지원 예고, 모델 자체 책임 공개는 “작업 중” 수준으로만 언급.

## 왜 중요한가 (그리고 논쟁)
Fields 메달리스트 Hugo Duminil-Copin이 자기 분야 관련 AI 원고 홍수에 공개적으로 고뇌를 표했다는 X·언론 요약이 돌았다 — **감정·규범 논쟁**이지, 개별 정리의 진위를 여기서 검증하진 않았다. 제품 관점에선 “블로그 포스트”가 아니라 **버전 관리되는 증명 아티팩트 + 기계검증(Lean)** 으로 과학 소통 채널을 옮기려는 실험이다. 세컨드 브레인/LLM Wiki와 맞닿는 점: **raw 결과 → 위키식 정리 → 형식 검증** 파이프라인.

## 기억할 것
- “수백 개 미해결 문제를 풀었다”는 **회사·저장소 주장**을 그대로 정답으로 수용하지 말 것. 수학 커뮤니티 피어 리뷰가 본게임이다.
- 모델 이름·가중치는 이 글에서 **공개되지 않음**.

출처: [OpenAI — Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/) · [github.com/openai/math](https://github.com/openai/math)
