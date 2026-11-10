---
title: "같은 주에 나온 두 최상위 모델: Claude Fable 5.2 vs Gemini 4 Carbon — 무엇을 어디에 쓰나"
date: 2026-11-11T07:00:00+09:00
category: "AI 모델"
slug: "fable-5-2-gemini-4-carbon"
summary: "Anthropic이 11/9 Claude Fable 5.2·Mythos 5.2를, Google이 11/10 Gemini 4 Carbon을 공개했다. Fable은 코딩·과학·컴퓨터 사용에서, Carbon은 업무 자동화·가격에서 앞선다고 각자 주장한다. 순위보다 ‘어떤 일에 어느 모델을 올릴지’ 정리했다."
---

## 무슨 일이 있었나
- **11/9 Anthropic — Claude Fable 5.2 / Mythos 5.2.** 둘은 같은 모델이고, Fable은 사이버·생물학 안전장치를 켠 일반 공개판, Mythos는 검증된 보안·생명과학 기관용이다. 가격은 입력 100만 토큰당 **8달러 / 출력 40달러**(이전보다 인하), 출력 속도는 5.1보다 최대 30% 빠르고, 2.5배 빠른 fast mode는 16/80달러([Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-2)).
- **11/10 Google — Gemini 4 Carbon.** Google의 최상위 모델로, 장기 에이전트 작업·코딩·과학 추론·사이버보안을 겨냥한다. 11/30까지 도입가 **2/10달러**(Argon과 동일), 이후 **4/20달러**. Antigravity에 한 프롬프트를 여러 에이전트 팀으로 쪼개는 **/swarm** 프리뷰도 함께 나왔다([Google 블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)).

## 숫자로 본 차이 (모두 각사 발표치)
Anthropic 표 기준:
- 에이전트 코딩 FrontierCode 2.0: Fable 5.2 **49.1%**(Xhigh) / Opus 5.5 45.5% / GPT-6 Astra 42.8% / Carbon 41.1%(Medium).
- 업무 자동화 AutomationBench: **Carbon 53.9%** > Fable 5.2 51.4%. Anthropic 표에서도 Carbon이 이긴 항목이다.
- 컴퓨터 사용 OSWorld 2.1(부분셋): Fable 5.2 89.3% / Carbon 81.5%.

Google은 Carbon이 CursorBench 4.0·Perplexity WANDR·Zapier AutomationBench에서 1위이고, “다음 외부 모델보다 작업당 비용이 2배 이상 낮다”고 주장한다. 양쪽 표는 측정 조건(effort 단계, 하네스)이 달라 **직접 비교는 참고용**이다.

## 그래서 실무에선
- **Anthropic의 권고 자체가 흥미롭다**: “대부분의 코딩·지식 작업은 Opus 5.5로 시작하고, 필요할 때만 Fable로 올려라.” Fable은 작은 모델이 막힐 때 조언하는 **Advisor**, 일을 쪼개 하위 모델에 넘기는 **Orchestrator** 역할로도 쓰라고 한다.
- Google도 같은 그림이다. “대부분은 Argon, 한계를 시험하는 일만 Carbon”. /swarm에서 Carbon을 설계·조율·감사 역할에 두고 가벼운 모델과 짝지으라고 권한다.
- 즉 두 회사 모두 **“최상위 모델 = 팀장, 나머지 = 실무자”** 구성으로 가고 있다. 단일 모델 순위보다 라우팅 설계가 비용을 좌우한다.

## 눈에 띈 사례
- Fable 5.2 에이전트 1,000개가 **페르마의 마지막 정리 Lean 형식화를 30시간**에 완료(이전 연구판은 11일).
- Fable 5.2가 회로기판·외장·소프트웨어까지 설계한 기기 3종이 전기적 수정 없이 동작(Diode 협업).
- Carbon /swarm이 시의회 공개 PDF 7개(도면 206장)로 Google 사무실 3D 재구성.

## 주의
벤치마크는 모두 자사 측정이다. Fable은 사이버 관련 작업 상당수를 차단(대신 하위 모델이 응답)하므로, 보안 업무라면 Mythos 접근 프로그램 여부부터 확인해야 한다. Carbon의 2/10달러는 11/30까지의 도입가다.
