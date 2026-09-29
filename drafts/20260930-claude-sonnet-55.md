---
title: "AI 모델: Claude Sonnet 5.5 — Sonnet 5 대비 30%+ 빠르고 작업당 비용 최대 30%↓, 디자인 감각 강조"
date: 2026-09-30T07:04:00+09:00
category: "AI 모델"
slug: "claude-sonnet-55"
summary: "Anthropic 공식 2026-09-28. Sonnet 5.5=Claude 5.5 패밀리 두 번째. 입출력 단가 $2/$10로 Sonnet 5와 동일하나 토큰 효율로 작업당 최대 ~30% 저렴, 생성 30%+ 빠름. Terminal-Bench 4.0 70.6%(Sonnet 5 10.3%). 사이버 세이프가드 포함."
---

## 한줄 요약
[Anthropic — Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)(2026-09-28)는 Sonnet 5 대비 **명확한 업그레이드**로, **30%+ 빠른 생성**과(회사 측정) **작업당 비용 최대 약 30% 절감**을 내세운다. 표기 단가는 Sonnet 5와 같은 **$2 / $10 per 1M in/out**, 캐시 리드 **$0.20**. Opus 5.5의 저가·고속 보완재로, 일상 코딩·문서·슬라이드·스프레드시트·**디자인 폴리시**에 강하다고 한다.

## 숫자로 보면 (공식 표)
- **Terminal-Bench 4.0**: Sonnet 5.5 **70.6%** vs Sonnet 5 **10.3%**(에이전틱 코딩).
- **CursorBench 4.0**: **55.5%**(Opus 5.5 57.8%에 근접).
- **GDPval-AA v2.1**: 1844(Sonnet 5 1449, Opus 5.5 1846에 거의 동률).
- **세이프가드**: 사이버 역량 상승으로 Opus급 사이버 폴백 적용. 고위험 사이버 요청은 Sonnet 5로 떨어짐. Haiku 5.5는 수주 내 예고.

## 왜 중요한가
“같은 단가표, 더 적은 토큰·더 빠른 루프”는 Cursor·Lovable·Slackbot 같은 **고빈도 에이전트 워크로드**의 기본 모델을 갈아끼우게 만든다. 랭킹 표보다 **작업당 달러·반복 횟수**가 편집실 기준이다.

## 기억할 것
- [anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)
