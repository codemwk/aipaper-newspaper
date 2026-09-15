---
title: "DeepSeek V4.1 Flash — 552B MoE·비대칭 인코더-디코더, Pro까지 라우팅"
date: 2026-09-16T07:15:00+09:00
category: "AI Models"
slug: "deepseek-v41-flash"
summary: "공식 2026-09-10. deepseek-flash. Causal Encoder–Decoder(입력 8B·출력 16B 활성), 네이티브 비전. KV 캐시 HBM 1/4·SSD 1/8. 9/14부터 v4-pro 요청도 Flash로."
---

## 한줄 요약
[DeepSeek(2026-09-10)](https://api-docs.deepseek.com/news/news260910)가 **DeepSeek-V4.1-Flash**를 API에 올렸다. 모델명 `deepseek-flash`. 새 아키텍처 패밀리의 가장 작은 구성으로 **네이티브 멀티모달**을 열고, 자사 테스트 기준 V4-Pro를 성능·비용·속도에서 앞선다고 주장한다.

## 핵심 수치·정책
- **552B** MoE. Causal Encoder–Decoder: 입력측 활성 **8B**, 출력측 **16B**.
- KV 캐시: 이전 세대 대비 HBM **1/4**, SSD **1/8** — 에이전트 캐시 히트 비용 절감이 명시 목적.
- 구모델: `deepseek-v4-flash` / `deepseek-v4-flash-vision-exp`는 임시로 V4.1-Flash로 라우팅.
- **2026-09-14 04:00 UTC**부터 `deepseek-v4-pro` 요청도 V4.1-Flash로 라우팅·Flash 요금(향후 V4.1-Pro까지). 이후 문서에 Pro API를 수요로 유지한다는 정정도 있으니 **가격 페이지를 재확인**.
- 피크/오프피크 요금(오프피크=피크의 50%). HF 가중치·테크 리포트 공개.

## 왜 중요한가
에이전트·코딩 CLI가 Flash급을 백본으로 쓰는 흐름에서 “작은 활성 파라미터 + 큰 토탈 MoE + 비전”은 **단가·지연 민감한 트레이딩/자동화 루프**에 직결된다. 다만 로컬 풀추론은 토탈 파라미터가 커 비현실적이라는 커뮤니티 지적이 있다 — API·파트너(WorkBuddy/OpenCode) 경로가 현실적이다.

## 기억할 것
- 호출: `model="deepseek-flash"`, base `https://api.deepseek.com`
- [발표](https://api-docs.deepseek.com/news/news260910) · [요금](https://api-docs.deepseek.com/quick_start/pricing/) · [HF](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
