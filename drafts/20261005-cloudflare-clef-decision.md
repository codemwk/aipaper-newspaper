---
title: "AI 모델: Cloudflare Clef·Clef-flash — 글을 쓰지 않고 ‘확률 붙은 결정’만 내는 오픈소스 결정 모델, Apache 2.0"
date: 2026-10-05T07:03:00+09:00
category: "AI 모델"
slug: "cloudflare-clef-decision"
summary: "10/1 Cloudflare 첫 자체 학습 모델. Jev API 호환, 비전 입력·64K 컨텍스트(Jev 32K). Qwen3.8-27B/3.5-9B 동결+라우팅 헤드·LoRA. 중앙값 지연 Clef 209ms·flash 39ms vs Jev 524ms(회사 측정). Workers AI 호스팅+HF 공개, FDE 동반 RL 파인튜닝."
---

## 한줄 요약
[Cloudflare](https://blog.cloudflare.com/clef-decision-models/)가 10월 1일 **Clef**와 **Clef-flash**를 냈다. Workers AI 팀이 직접 학습한 첫 모델이며, 문장을 생성하는 LLM이 아니라 **‘결정 모델(decision model)’**이다. 입력(예: 고객 문의 한 줄)과 질문 스키마(긴급한가? 어느 팀? 심각도?)를 주면 **타입이 정해진 답 + 확률**만 돌려준다. 9월에 화제가 된 Typesafe의 **Jev System One**과 **API가 완전 호환**되고, 가중치는 [Hugging Face에 Apache 2.0](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/)으로 공개됐다.

## 무엇이 다른가
- **입력**: 비전 인코더가 있어 이미지도 분류(Jev는 텍스트만). 컨텍스트 **64K**(Jev 32K).
- **구조**: Qwen 백본으로 **프리필 한 번만** 돌리고, 가능한 스키마 선택지를 **병렬 채점** — 토큰을 하나씩 생성하지 않아 빠르다. Clef는 Qwen3.8-27B, Clef-flash는 Qwen3.5-9B를 동결하고 라우팅 헤드와 LoRA(rank 256)를 학습. 확률 보정을 위해 Brier loss와 자체 RL 기법(RLCD)을 썼다.
- **속도(회사 측정, 43개 벤치)**: 중앙값 지연 Clef **209ms**, Clef-flash **38.8ms**, Jev **524ms**.
- **실사용 예**: 위협 인텔리전스 팀이 도메인을 렌더링·분류(“패션 95%, 이커머스 85%, 피싱 <1%”)하는 데 **2.2초** — 범용 LLM gpt-oss-120b는 같은 흐름에서 4.7초에 분류 2개만 반환.
- **약점도 공개**: When2Call·BRIGHT 등 일부 항목은 Jev가 앞선다. 회사 자체 평가이므로 독립 검증 전까진 ‘주장’으로 읽자.

## 돈 버는 방식
모델은 무료 공개, 수익은 **Workers AI 호스팅 + 파인튜닝 서비스**다. 먼저 전담 엔지니어(FDE)가 붙는 맞춤 RL 튜닝을 팔고, 이후 AI Gateway로 쌓인 요청 로그 → Containers 샌드박스 → 새 Trainer → 재배포로 이어지는 **셀프서브 플랫폼**을 만들겠다고 했다.

## 왜 중요한가
에이전트 파이프라인에서 “이 주문 위험한가?”, “이 메일 누구 담당?” 같은 **분기 판단**을 비싼 LLM에 맡기던 걸, 40ms짜리 결정 모델로 떼어 내는 흐름이 생겼다. 트레이딩 봇의 ‘진입/보류’ 게이트, 뉴스 큐레이션의 ‘실을까/버릴까’ 분류에도 그대로 들어맞는 부품이다.

## 기억할 것
- [Cloudflare Blog 10/1](https://blog.cloudflare.com/clef-decision-models/) · [Changelog](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/)
