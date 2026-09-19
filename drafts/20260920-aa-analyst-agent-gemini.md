---
title: "AA-AnalystAgent — 스프레드시트 에이전트 신뢰도 보드, Flash가 상단을 흔들다"
date: 2026-09-20T07:44:00+09:00
category: "AI Models"
slug: "aa-analyst-agent-gemini"
summary: "Artificial Analysis AA-AnalystAgent: 실무 스프레드시트·문서 80문항×5회, 헤드라인은 pass^5. 론칭 당시(8월) Opus 5~54%. 이후 보드 갱신으로 Gemini 3.7 Flash(high) ~60%·Fable 5.1 ~57.5%·Opus 5 ~53.8% 구간이 회자. ‘한 번 맞춤’이 아니라 ‘다섯 번 모두’."
---

## 한줄 요약
[Artificial Analysis](https://artificialanalysis.ai/evaluations/aa-analyst-agent)의 **AA-AnalystAgent**는 비즈니스 애널리스트가 겪는 **표·문서 정량 분석**을 에이전트에게 맡긴 뒤, **5번 모두 맞은 비율(pass^5)**만 헤드라인으로 쓰는 보드다. Intelligence Index와는 별도.

## 지금 뭐가 뜨나
- 설계(론칭 글 8/10): 80문항·14도메인, Stirrup 하네스(코드실행·웹페치 등), 오염 막으려 문항 비공개.
- 교훈: **pass@1이 높아도 pass^5가 낮으면** “가끔 맞으니 사람이 다시 검사” = 에이전트 가치가 반감. 조기 오해석 고착이 실패의 ~57%.
- 최근 공개 스냅샷(평가 페이지·집계 사이트 기준): **Gemini 3.7 Flash (high) ~60%**, **Claude Fable 5.1 ~57.5%**, **Claude Opus 5 ~53.8%** 전후. 숫자는 보드가 모델을 넣을 때마다 움직이니 **원 페이지를 최종본**으로.
- 실무 함의: “가벼운 Flash”가 분석 루프에서 상단에 오면, **비용·속도·신뢰도** 삼각을 다시 짜야 한다.

## 왜 중요한가
트레이딩·리서치·퍼스널 저널 에이전트 모두 “표 읽고 숫자 내기”가 핵심이다. 리더보드 마케팅 문구보다 **같은 답을 반복하느냐**가 채용 기준이 되고 있다.

## 기억할 것
- [AA-AnalystAgent 보드](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · [론칭 아티클](https://artificialanalysis.ai/articles/aa-analyst-agent)
