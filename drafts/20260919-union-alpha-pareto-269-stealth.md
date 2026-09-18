---
title: "Union Alpha = Pareto 26.9 — 스텔스 1일 무료 뒤 유료 전환, Astra급 벤치 주장"
date: 2026-09-19T07:15:00+09:00
category: "AI Models"
slug: "union-alpha-pareto-269-stealth"
summary: "2026-09-16~18. OpenRouter 스텔스 Union Alpha가 unbiased.ai Pareto 26.9로 신원 공개. 262K 컨텍스트, GPT-6 Astra·Claude Fable 5.1급 벤치 주장. 무료 주간 예정이 수요 폭주로 1일 만에 종료."
---

## 한줄 요약
[GIGAZINE](https://gigazine.net/gsc_news/en/20260918-union-alpha/)(2026-09-18) 정리에 따르면, OpenRouter에 **2026-09-16** 올라온 스텔스 모델 **Union Alpha**는 하루 만에 **unbiased.ai의 Pareto 26.9**로 밝혀졌다. 연구·코딩·에이전트 워크플로용 멀티모달, **262,144** 토큰 컨텍스트.

## 무엇이 바뀌었나
- 벤치: GPT-6 **Astra**·Claude **Fable 5.1**과 비슷한 수준이라고 소개됐다(보드·자체 주장은 교차검증이 필요).
- 트래픽: 무료 체험을 **1주일** 예정이었으나, “분당 수십억 토큰”급 수요로 속도가 붕괴 → AWS로 용량을 늘려도 부족해 **조기 유료화**. 계정은 “실제 반응·스케일 이슈를 보고 **10/10 공식 출시**에 반영하려 익명 공개했다”고 밝혔다.
- 유료 요금(보도 수치): 입력 **$2.50** / 캐시 **$0.25** / 출력 **$7.50** per million tokens — “Astra 정가의 1/4 미만”이라고 Union Alpha 측. Cloudflare AI에도 stealth 경로로 노출.

## 왜 중요한가
스텔스 드롭 → 신원 공개 → 용량 한계 → 가격 공개는 2026년 오픈라우터 생태계의 반복 패턴이다. 에이전트 워크로드를 돌리는 사람은 **벤치 숫자보다 분당 토큰·대기열·캐시 가격**을 먼저 본다. 10/10 공식판이 안정성 테스트판이다.

## 기억할 것
- [GIGAZINE](https://gigazine.net/gsc_news/en/20260918-union-alpha/) · [OpenRouter Union Alpha](https://openrouter.ai/stealth/union-alpha) · [Cloudflare stealth 문서](https://developers.cloudflare.com/ai/models/stealth/union-alpha/)
