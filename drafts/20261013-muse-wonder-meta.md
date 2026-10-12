---
title: "AI 모델: Meta Muse Wonder·Wonder Full — 에이전트용 프론티어, Model API는 입력 $4/출력 $20(1M 토큰), Muse Code Power $50·Maximum $200"
date: 2026-10-13T07:01:00+09:00
category: "AI 모델"
slug: "muse-wonder-meta"
summary: "Meta가 10/12 Muse Wonder·Wonder Full을 발표. Active Memory·Active Focus를 내세운 에이전트 모델. Model API `muse-wonder-1.0`(1M 컨텍스트, 표준 $4/$0.20/$20 per 1M). Wonder Full은 Muse Code 구독(Power $50·Maximum $200 등). Spark 표준은 $1.25/$0.15/$4.25."
---

## 한줄 요약
Meta는 **2026-10-12** [Muse Wonder와 Muse Wonder Full](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)을 “개인·업무 에이전트 작업용 최전선 모델”로 내놓았다. 개발자는 **Meta Model API**와 **Muse Code**로 Wonder에 접근하고, Wonder Full은 **Muse Code 구독자** 쪽에 열려 있다고 밝혔다. 보험 클레임·임대차·앱 제작 같은 **장기 에이전트 과제**와 **Active Memory / Active Focus**를 전면에 걸었다.

## 어떻게 동작하나 (공개 스펙·가격)
- **제품 주장**(뉴스룸): Active Memory(대화 간 중요 맥락 유지), Active Focus(난관에서 재시도·오류 복구·중요 조치 전 확인). 법률·금융·헬스 도메인과 코딩을 함께 강조.
- **Model API**: 모델 id **`muse-wonder-1.0`**, 컨텍스트 **1,048,576** 토큰, Base `https://api.meta.ai/v1`. 미리보기(preview)로 표기([docs](https://dev.meta.ai/docs/overview)).
- **토큰 가격**(표준 모드, [Pricing](https://dev.meta.ai/docs/pricing-rate-limits) 2026-10-13 확인): Wonder **캐시 입력 $0.20 / 입력 $4.00 / 출력 $20.00**(1M 토큰). Contributor 모드는 Wonder에 **없음**. Muse Spark 표준 **$1.25 / $0.15 / $4.25**, Contributor **$0.10 / $0.002 / $0.20**.
- **Muse Code 구독**(공식 제품·구독 문서): Everyday → High(**Everyday 대비 5×**) → **Power $50/월**(가장 강한 Muse 모델·**Wonder Full** 포함, Everyday 대비 **20×**) → **Maximum $200/월**(Everyday 대비 **80×**). Everyday·High 달러가는 제품 페이지에서 Power·Maximum만큼 명확히 확인되지 않아 **적지 않음**.
- **같은 스택**: Muse Image($0.01/장), Voice Transcribe($0.18/시간), SAM 3.1, 오픈웨이트 **Muse Glimmer**(Apache 2.0)가 나란히 있다.

## 왜 중요한가
Anthropic·OpenAI가 “에이전트가 실수하면 어떻게 막나”를 공개하는 주와 같은 타이밍에, Meta는 **에이전트 제품 라인(Muse)**의 최상단 모델을 정식 브랜드로 올렸다. 가격 구조는 명확하다 — **API는 토큰**, **터미널 에이전트는 월정액 상한**. Wonder Full을 구독에만 두는 분리는 “최강 모델 = 코딩 에이전트 락인” 신호로 읽힌다.

## 기억할 것
- Wonder는 **preview**. 벤치 숫자·안전성 풀 리포트는 “곧”이라고만 적혀 있다.
- 웹 검색 그라운딩은 토큰과 별도 **$2.50 / 검색 1,000회**.

출처: [Meta — Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) · [Pricing](https://dev.meta.ai/docs/pricing-rate-limits) · [Muse Code](https://dev.meta.ai/products/muse-code) · [Subscriptions](https://dev.meta.ai/docs/muse-code/subscriptions)
