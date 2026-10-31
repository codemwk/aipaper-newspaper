---
title: "AI 모델: RightNow System Zero — 입력이 들어오는 동안 결정을 스트리밍. ‘생각 전 단계’를 파는 YC 스타트업"
date: 2026-11-01T07:04:00+09:00
category: "AI 모델"
slug: "rightnow-system-zero"
summary: "YC F26 RightNow가 10/31 System Zero를 공개했다. 텍스트·JSON·PDF·이미지·음성·비디오(프리뷰)·코드베이스·로봇 상태를 받아, 도착하는 대로 선택지별 확률을 갱신한다. 텍스트 결정 약 30ms, 호출당 최대 1,024문항. 종량제(텍스트 $0.19/M 토큰 등), 가입 $5 크레딧."
---

## 한줄 요약
지난번 저장하신 ‘결정 모델(Clef·joey-1)’ 흐름과 이어지는 소식이다. RightNow는 LLM의 System 1/2 앞에 **System Zero = 결정 자체**를 두겠다고 한다([rightnowai.co](https://rightnowai.co), [DailyCited](https://dailycited.com/d/2026-10-31/)).

## 제품
- **입력 8종**: 텍스트, JSON, robot state, codebase, PDF, images, voice, video(preview).
- **출력**: 옵션별 확률·confidence. 입력이 더 오면 확률이 바뀐다(예: 깨진 블렌더 → 환불 확률 상승).
- **한도**: 컨텍스트 설정으로 **최대 1M**, 표준 약 38k. 호출당 질문 최대 **1,024**.
- **API**: `POST …/v1/system-zero/decide`, 모델명 `system-zero`.

## 요금(사이트 계산기·카드 기준)
- 텍스트 **$0.19 / M** 토큰, 캐시 텍스트 **$0.019 / M**.
- 답변된 질문당 **$0.00013**, 호출당 **$0.000055**.
- 가입 **$5** 무료 크레딧, 종량제.

## 벤치 주의
사이트에 Artificial Analysis Decision Index 표가 있으나, RightNow 3.0.0 **63.20\*는 자사 측정**(공개 홀드아웃 절반, 10/28)이고 AA 공식 평가가 아니라고 고지한다. 순위는 참고용.

## 왜 중요한가
- 에이전트 파이프라인에서 ‘긴 추론’ 전에 **라우팅·환불·승인** 같은 짧은 결정을 싸게 빼는 계층이 상품화되고 있다. Baseten joey-1과 같은 ‘결정 전용’ 시장 조각.
