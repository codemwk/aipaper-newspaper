---
title: "AI 모델: Meta, 최상위 모델 Muse Wonder로 ‘대중용 모델’을 훈련해 배포 — Active Memory·Active Focus"
date: 2026-11-09T07:25:00+09:00
category: "AI 모델"
slug: "meta-specialized-models-active-memory"
summary: "Meta가 11/6 Muse Wonder로 훈련한 특화 모델을 Muse와 Meta AI 사용자에게 배포한다고 밝혔다. 중요한 정보와 낡은 정보를 구분하는 Active Memory(자사 평가 76%→90%), 문제가 생겨도 목표를 이어가는 Active Focus(일상 작업 완료 +67%). 전부 Meta 자체 평가다."
---

## 한줄 요약
Meta는 11/6 “몇 주 전 공개한 **Muse Wonder** 계열로 기존 모델을 다시 훈련한 **특화 버전**을 Muse와 Meta AI 사용자에게 배포한다”고 밝혔다. 가장 강한 모델을 직접 풀기보다 **가장 강한 모델이 더 작은 모델을 가르치는** 구조다([Meta AI Research](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai)).

## 무엇이 달라졌나 (Meta 발표)
- **Active Memory**: 임시 정보와 영구 정보를 구분하고, 시간이 지나 낡아진 정보를 가려내며, 예전 대화가 다시 관련될 때를 알아차리도록 훈련. 자사 평가에서 핵심 맥락을 제대로 쓴 작업 비율 **76% → 90%**, 중요한 정보를 잊는 일이 **2.4배 감소**.
- **Active Focus**: 예상 밖 문제(병목)를 만나도 다시 시도하거나 대안을 찾아 목표를 이어가는 능력. 일상 작업 완료율 **67% 개선**.
- 중간에 지시가 바뀌어도 헷갈리지 않고, 혼자 밀어붙일 때와 같이 협업할 때를 구분한다고 설명. Meta AI에서는 문제를 단계로 쪼개고 더 날카로운 후속 질문을 한다.
- 자사 ‘Personal Superintelligence Index’ 점수 38% → 47%.

## 왜 중요한가
세컨드 브레인 쪽에서 계속 나오는 질문이 **“기억이 낡았는지 어떻게 아는가”**(freshness)다. 모델 레벨에서 ‘낡은 정보 판별’을 훈련 목표로 삼았다는 점이 눈에 띈다. 또 ‘최상위 모델 → 대중용 모델 증류’는 비용 구조에서 오픈·폐쇄 가릴 것 없이 표준 레시피가 되고 있다.

## 주의
수치는 전부 Meta 자체 지표·평가이고 비교 대상은 ‘이전 Muse 모델’뿐이다. 외부 모델과의 비교, 평가 설계, 파라미터 규모는 공개되지 않았다. 순위 기사가 아니라 방향성 소식으로 읽을 것.
