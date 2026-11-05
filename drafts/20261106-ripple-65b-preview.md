---
title: "AI 모델: Ripple-65B Preview — 전직 구글러 칩 회사의 Apache-2.0 오픈 가중치, 학습비 3,200만 달러 주장"
date: 2026-11-06T07:07:00+09:00
category: "AI 모델"
slug: "ripple-65b-preview"
summary: "Ricursive Intelligence가 11/4 Ripple-65B Preview를 공개했다. 65B 덴스, 12T 토큰 학습, Apache 2.0. 회사 집계 Terminal-Bench 2.1 80.5·SWE-bench Pro v2 Hard 79.1. 학습 총비용 약 3,200만 달러 주장. OpenRouter(GMICloud) 입력 0.20/출력 0.60달러 per MTok. 벤치 비교는 벤더 간 불일치가 있어 자체 검증이 필요하다."
---

## 한줄 요약
반도체 설계 AI 스타트업 Ricursive가 **Ripple-65B Preview**를 일반용 오픈 가중치로 풀었다. “미국 오픈 코딩 1위” 헤드라인보다, **Apache 2.0 + 비교적 싼 API + 작은 총 파라미터**가 실무 포인트다([VentureBeat 11/4](https://venturebeat.com/ai/ex-googlers-new-apache-2-0-model-ripple-65b-preview-claims-the-u-s-open-coding-lead-on-two-major-benchmarks)).

## 지금 뭐가 뜨나
- **스펙**: 65B 덴스, 80층, 12T 토큰 프리트레인. BF16·NVFP4 인스트럭션 가중치 + 베이스. Hugging Face·Together·GMI·OpenRouter(Fireworks 예정).
- **벤치(회사 표)**: Terminal-Bench 2.1 **80.5**, SWE-bench Pro v2.0 Hard **79.1**. 같은 표에서 DeepSWE 등은 Meta Muse Spark Open에 뒤진다.
- **비용 주장**: 예비 실험부터 최종 런까지 **약 3,200만 달러**. Lightspeed 주도 시리즈 A **3억 달러 / 기업가치 40억**(1월)의 칩 설계 회사 부산물.
- **API 가격(확인된 경로)**: OpenRouter GMICloud **입력 $0.20 / 출력 $0.60 per MTok**, 캐시 입력 $0.05. 다만 엔드포인트 컨텍스트는 확인 시점 **16,384** — 광고의 1M 컨텍스트와 다르다.
- **창업**: Anna Goldie·Azalia Mirhoseini(구글 AlphaChip 관련).

## 왜 중요한가
‘더 큰 MoE’가 아닌 **덴스 65B로 에이전트 코딩 벤치를 노린다**는 실험이다. 로컬·셀프호스트 팀에는 Apache 2.0이 Cursor/사내 에이전트에 넣기 쉬운 라이선스다. 다만 Reflection Beam 등과의 수치 차이는 0.4%p 수준이고, 표·모델카드 간 숫자도 어긋나 VentureBeat가 **재현성 주의**를 걸었다.

## 주의
벤치 1위 주장은 선택한 미국 오픈 모델·테스트에 한정. 중국 오픈 모델·다른 하네스 결과는 더 높을 수 있다. 칩 설계 본업 성능과는 별개 공개본이다.
