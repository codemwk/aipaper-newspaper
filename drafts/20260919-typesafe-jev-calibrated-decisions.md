---
title: "TypeSafe Jev — LLM이 아닌 ‘보정된 결정’ 모델, 에이전트 감시·라우팅용"
date: 2026-09-19T07:10:00+09:00
category: "AI Models"
slug: "typesafe-jev-calibrated-decisions"
summary: "2026-09-18 TechCrunch. 전 OpenAI RLHF 연구자 Diogo Almeida의 TypeSafe AI가 Jev 공개. 텍스트 대신 확률·캘리브레이션 출력. Vercel 등에서 안전 분류기가 Luna 대비 5~18배 빨라졌다는 현장 반응."
---

## 한줄 요약
[TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)(2026-09-18)에 따르면, ChatGPT·RLHF에 관여했던 **Diogo Almeida**가 설립한 **TypeSafe AI**가 **Jev**를 공개했다. LLM이 아니라 **미리 정의한 결정 공간에 대한 확률(캘리브레이션된 결정)**을 내놓는 트랜스포머다.

## 무엇이 바뀌었나
- 출력에 자연어가 없다 → **환각 토큰이 원칙적으로 없다**. 사용자는 “이 클래스일 확률”을 받고, 임계값으로 자동화 여부를 정한다.
- 가격·속도 포지션: 출력 토큰 무료, 입력은 **십억 단위** 미터링이라고 회사는 설명한다. API 수요로 일시 서빙 장애가 났을 정도로 개발자 관심이 컸다.
- 현장 예: Vercel 엔지니어가 ChatGPT **Luna 5.6** 안전 분류기를 Jev로 바꿨더니 **5~18배 빠르고** 정확도도 올랐다고 TechCrunch에 말했다. Bryo AI는 Gemini 대비 정확도는 비슷·비용은 10~20배 낮고 **신뢰 확률이 손에 잡힌다**고 평가.
- 쓰임: LLM **대체**(분류·게이트)뿐 아니라 **에이전트 트레이스 감시·jailbreak 차단·모델 라우팅** 보조. Armin Ronacher(Earendil/Pi)는 “50%면 동전, 95%면 진행” 식으로 사용자에게 결정을 넘긴다고 요약했다.
- 학습: 합성 데이터 + 회사가 부르는 **RL from calibrated decisions**. 아키텍처는 비공개(오픈웨이트 LLM 위라는 외부 추정만).

## 왜 중요한가
frontier 채팅 모델 경쟁과 다른 축이다. “말 잘하는 지능”이 아니라 **소프트웨어 자동화에 넣을 싸구려·빠른 판단기**. 에이전트 스택에서 MCP·툴콜 앞단에 붙이면, 비싼 LLM을 매번 돌리지 않아도 된다.

## 기억할 것
- [TechCrunch 기사](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/) · TypeSafe AI / Jev
