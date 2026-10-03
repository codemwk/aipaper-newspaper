---
title: "AI 모델: Aleph Alpha Kolibri — 독·영 MoE 78B/활성 3B·컨텍스트 최대 1M, Apache 2.0 오픈웨이트"
date: 2026-10-04T07:06:00+09:00
category: "AI 모델"
slug: "aleph-alpha-kolibri"
summary: "Aleph Alpha(2026-10-03): Kolibri 공개. 78.1B total / ~3.5B active, 추론 none~high, 프리트레인 20T. 독일·핀란드 인프라, EU AI Act·GDPR 지향. HF Apache 2.0. Origin(30B) → 3개월 만 스케일."
---

## 한줄 요약
[Aleph Alpha 공식](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/)(2026-10-03, 독일 통일기념일): **Kolibri** — 영어·독일어 MoE 트랜스포머, **총 78.1B / 토큰당 활성 ~3.46B**, 컨텍스트 **최대 1M**, 추론 노력 **none/low/medium/high**. Hugging Face **Apache 2.0** 풀웨이트. 규제 산업·공공·항공우주 등 **주권(sovereign)** 배포용으로 특화. Origin(30.6B, 65k 맥락, 비공개) 프리트레인 종료(6/11) 후 **3개월**(9/11 프리트레인 종료) 만에 스케일·공개.

## 실무로 보면
- **효율**: 활성 파라미터를 작게 유지해 온프레미스·서빙 비용 절충. 풀어텐션은 50층 중 일부, 나머지는 512 윈도.
- **독일어**: 프리트레인 토큰의 **~21.3%**가 독일 — 번역 의존이 아닌 유기·재구문 중심 큐레이션을 강조.
- **그라운딩**: Merlin-Arthur 프로토콜로 “모른다” 학습. 환각보다 **기권**이 규제 고객 KPI.
- **서빙**: `aleph-alpha-inference` + vLLM 플러그인. 예: `vllm serve Aleph-Alpha/Kolibri-1 ...`

## 왜 중요한가
“벤치 1등 레이스”가 아니라 **EU 규제·온프레미스·이중언어** 제품 포지션. 오픈웨이트라도 **공급망·데이터 투명성**을 파는 B2G/B2B 스토리다.

## 기억할 것
- [Kolibri Has Landed](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) · Hugging Face Aleph-Alpha/Kolibri
