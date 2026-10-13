---
title: "AI 모델: Anthropic ‘증류 방어’ 성적표 — 추출된 추론 토큰 10~100배 감소, 오탐 0.1% 미만, 차단 요청도 과금"
date: 2026-10-14T07:02:00+09:00
category: "AI 모델"
slug: "anthropic-distillation-defenses"
summary: "Anthropic(10/12): 무단 증류 대응 3중 방어 — preserved thinking(2026-08-31 이후 API 계정은 이전 컨텍스트 편집 불가), 2단계 추출 탐지 분류기(오탐 <0.1%, Sonnet 5.5·Opus 5/5.5·Fable 5/5.1), 반복 시도 계정 차단(수만 개, 종종 2시간 내). 추출 추론 토큰 10~100배↓. 대가: 일부 통합 수정, 차단 요청 과금(9/24~)."
---

## 한줄 요약
경쟁사가 프론티어 모델의 출력을 대량 수집해 싼 모방 모델을 학습시키는 **무단 증류(distillation)**. Anthropic은 2026-10-12 연구 글에서 새 방어책으로 **증류자가 가져간 Claude 추론 토큰이 10~100배 줄었다**고 밝혔다([Anthropic](https://www.anthropic.com/research/distillation-defenses)).

## 3중 방어
- **① 이동 차단 — preserved thinking**: Fable 5.1·Opus 5.5와 함께 도입. **2026-08-31 이후 생성된 API 계정**은 Claude의 이전 컨텍스트를 편집할 수 없다. 보호된 추론 블록을 대화·모델·계정 사이로 옮겨 “토해내게” 만드는 수법을 막는다.
- **② 탐지 — 2단계 분류기**: 헌법 분류기 계열로, 수동·자동 레드팀을 거쳤다. 회사 표현으로 “생물무기 지원 차단과 대략 같은 수준의 견고함”, **오탐률 0.1% 미만**. 현재 **Sonnet 5.5, Opus 5·5.5, Fable 5·5.1**에 적용.
- **③ 비용 부과 — 제재**: 반복 시도 계정은 사용량 제한·차단. **수만 개 계정**을 차단했고 다수는 캠페인 시작 **2시간 이내**. 또한 **9/24부터** 해당 분류기가 응답 전에 막은 요청도 **과금**한다(오탐 <0.1% 영역 한정).

## 대가와 한계
Anthropic 스스로 “정상 사용자 경험에 영향 없이”라는 2월 목표를 **완전히 달성하진 못했다**고 인정했다: 일부 개발자는 preserved thinking 때문에 통합을 고쳐야 했고, 0.1% 미만이라도 정상 요청이 막히며, 그 요청도 돈을 낸다. 또 “고도로 정교하고 끈질긴 우회 시도는 아직 보지 못했다”며 **고양이와 쥐 게임**이 계속될 것이라 했다. 보도(TAO Media)에 따르면 글은 Zhipu의 GLM-5.3, Moonshot Kimi 관련 의혹 사례도 거론했다.

## 왜 중요한가
요약된 추론이 아니라 **‘추론 과정 원문’**이 가장 비싼 학습 데이터라는 점을 공식화한 글이다. 사용자에게 보이는 효과는 두 가지 — (1) **원문 추론은 점점 더 안 보이게** 되고, (2) 에이전트 하네스가 이전 턴 컨텍스트를 **임의로 고쳐 쓰는 패턴**은 막힐 수 있다. 직접 하네스를 만든다면 Claude 추론 블록을 **수정·이식하지 않는 설계**가 안전하다.

출처: [Anthropic — Strengthening our defenses against distillation attacks](https://www.anthropic.com/research/distillation-defenses) · [TAO Media 정리](https://www.tao.media/anthropic-says-anti-distillation-defenses-cut-claude-reasoning-extraction-by-90-99/)
