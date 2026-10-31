---
title: "새로운 각도: Project Suncatcher — 궤도 TPU가 첫 프롬프트에 하이쿠로 답했다. 우주 데이터센터의 ‘Hello World’"
date: 2026-11-01T07:05:00+09:00
category: "새로운 각도"
slug: "suncatcher-orbit-tpu-haiku"
summary: "Google이 10/1 발사한 Suncatcher 프로토타입 위성이 시운전 후, 지상 프롬프트에 탑재 Gemma 4로 하이쿠를 다운링크했다(10/30 발표). TPU 4기 탑재·동시 1기·약 20분 가동. 다음 마일스톤은 2027년 쌍위성 광링크. 방사선·열 스트레스 시험이 과제."
---

## 한줄 요약
지상 데이터센터가 아니라 **위성 위 TPU**가 모델 응답을 돌려보낸 첫 공개 사례다([Google Research 블로그](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-satellite-response/), [TechCrunch](https://techcrunch.com/2026/10/30/googles-first-data-center-satellite-is-online-and-writing-poetry/)).

## 무슨 일이
- 10/1 SpaceX Falcon 9로 프로토타입 발사. 약 3주 시운전 후 호스트·TPU 트레이 전원·초기 ML 테스트.
- 스발바르 지상국 패스에서 Gemma 4에 “우주에 있는 느낌의 하이쿠”를 올림. 다운링크:
  > Blue marble below / Data streams in silent grace / Starlight feeds my core.
- 이어서 우주 테마 라임릭·텔레메트리 프롬프트도 시험. 대변인: “nominal”.

## 하드웨어 현실
| 항목 | 내용 |
|---|---|
| 탑재 | **TPU 4기**(동시 가동은 1기 — TechCrunch 정정) |
| 전력 | 최대 약 **1 kW**. TPU 부하 때문에 **약 20분**만 켤 수 있음 |
| 다음 | 방사선·열 스트레스. 2027년 **쌍위성** + 위성 간 광링크 |
| 맥락 | 학습보다 추론이 방사선에 덜 민감하다는 지상 가속기 시험 → 궤도에서 검증 |

## 왜 이 각도인가
- 벤치마크·펀딩 뉴스와 다른 축: **전력·냉각·발사 단가가 AI 인프라의 물리적 한계**를 드러낸다. Google은 2030년대 경제성을 보는 문샷이라고 했고, Starship 재사용 횟수 가정이 논문에 등장한다.
- Alphabet이 SpaceX에 지분이 있고, 분산 추론용 근접 편대는 SpaceX·Starcloud 비전과 겹치면서도 다르다.
