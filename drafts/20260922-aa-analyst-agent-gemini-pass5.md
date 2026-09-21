---
title: "AA-AnalystAgent — pass^5에서 Gemini 3.7 Flash(high) 60%로 선두"
date: 2026-09-22T07:08:00+09:00
category: "AI 모델"
slug: "aa-analyst-agent-gemini-pass5"
summary: "Artificial Analysis AA-AnalystAgent: 스프레드시트·문서 기반 분석 80과제. 지표는 pass^5(5회 전부 정답). Gemini 3.7 Flash(high) 60.0% 1위, Claude Fable 5.1 Max ~57.5%, Opus 5 Max ~53.8%. ‘한 번 맞힘’이 아니라 재현 신뢰도가 상품."
---

## 한줄 요약
[AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent)는 비즈니스·데이터 분석가가 만나는 **스프레드시트·문서 정량 질문 80개**를 에이전트에게 돌린다. 헤드라인 지표는 **pass^5** — 같은 문제를 **5번 모두** 맞힌 비율이다.

## 지금 상단(공식 보드)
- **Gemini 3.7 Flash (high)** — **60.0%** (pass^5 1위)
- **Claude Fable 5.1** (Adaptive Reasoning, Max Effort 등) — **약 57.5%**
- **Claude Opus 5** (Adaptive Reasoning, Max Effort) — **약 53.8%**
- 과제는 14개 비즈니스·과학 도메인. 문제·정답은 오염 방지를 위해 비공개(예시만 공개).

## 왜 pass^5인가
pass@1(한 번 성공)이나 pass@5(한 번이라도 성공)와 달리, pass^5는 **재실행해도 같은 답이 나오는지**를 본다. Artificial Analysis 표현을 빌리면, 분석 에이전트는 “운 좋은 한 방”이 아니라 **재확인 없이 믿어도 되는 비율**이 쓸모다.

## 왜 중요한가
에이전트 모델 고를 때 Arena·Agentic Index만 보면 “대화·툴 오케스트레이션”에 치우친다. AA-AnalystAgent는 **표·문서 작업의 신뢰도**라는 다른 축이다. 퍼스널 OS·대시보드·리서치 파이프에 LLM을 넣을 때 필수 체크리스트에 넣을 만하다.

## 기억할 것
- [AA-AnalystAgent](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 지표: pass^5 · 80 tasks × 5 runs
