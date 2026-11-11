---
title: "로봇의 ‘다음 장면’을 예측하는 모델이 공개됐다: Runway Praxis-1 오픈 웨이트, MBZUAI PAN 2"
date: 2026-11-12T07:00:00+09:00
category: "AI 모델"
slug: "praxis-1-open-world-action-model"
summary: "11/11 Runway가 영상과 로봇 행동을 함께 예측하는 ‘월드 액션 모델’ Praxis-1(27B MoE)을 Apache 2.0 오픈 웨이트로 풀었다. 같은 날 MBZUAI는 행동을 말로 주면 다음 장면을 영상으로 시뮬레이션하는 PAN 2를 학습 코드까지 공개했고, DeepMind는 Gemini Robotics 2.5를 냈다. 영상 생성 기술이 로봇 두뇌로 넘어가는 하루."
---

## 한줄 요약
영상 생성 회사로 알려진 **Runway**가 11/11 **Praxis-1**을 누구나 쓸 수 있는 **오픈 웨이트(Apache 2.0, 상업 이용 가능)**로 공개했다. 9월에 소개한 첫 ‘월드 액션 모델’로, **영상과 행동을 함께 예측하는 27B 파라미터 MoE 확산 트랜스포머**다([Runway 발표](https://runway.com/news/company-news/praxis-1-is-now-available)).

## 무엇이 새로운가
- **영상으로 배운 로봇 감각**: 대규모 영상 사전학습으로 “물체가 어떻게 움직이고 작업이 어떻게 진행되는지”를 먼저 배운다. Runway는 자체 연구에서 **웹 영상이 원격조종 로봇 영상만큼 사전학습 데이터로 유효**했다고 주장한다. 병목이 비싼 로봇 데이터에서 흔한 영상으로 옮겨 간다는 뜻이다.
- **수치(회사 발표)**: NVIDIA RoboLab-120에서 1,200 에피소드 성공률 **46.2%**(FLUX 3 Action 42.9%, Cosmos3 Nano 36.8%, π0.5 28.0%). 학습에 없던 Google RT-1 로봇에 미세조정하자 SimplerEnv **80.0%**(원래 RT-1 정책 52.4%).
- **어디서 돌아가나**: 가중치·추론·미세조정 코드(LoRA 포함)를 GitHub·Hugging Face(LeRobot 지원)·vLLM-Omni로 배포. H100부터 RTX 5090, 로봇 탑재용 Jetson Thor까지.

## 같은 날 나온 두 가지
- **PAN 2 (MBZUAI 산하 IFM)**: 시작 장면과 ‘행동을 말로’ 주면 다음에 벌어질 일을 물리·시간·공간에 맞는 영상으로 시뮬레이션. “행동하기 전에 결과를 본다”는 **시뮬레이션 추론**. 가중치에 더해 **학습 코드 전체**까지 Apache 2.0으로 공개한 드문 사례다([MBZUAI](https://mbzuai.ac.ae/news-events/news/the-institute-foundation-models-unveils-pan-2-open-world-model-physical)).
- **Gemini Robotics 2.5 (DeepMind)**: 메르세데스-벤츠 개념검증에서 자동차 부품 포장 성공률 96%, 작업 속도 20~30% 향상(회사 발표). Apptronik·Boston Dynamics 등 파트너를 통해 배포([SiliconANGLE](https://siliconangle.com/2026/11/11/google-deepmind-releases-new-advanced-robotics-ai-model-and-next-generation-gene-prediction-model/)).

## 왜 중요한가 (콘텐츠 만드는 사람에게도)
영상 생성 모델이 “예쁜 장면”을 넘어 **“그다음에 실제로 무슨 일이 일어나는가”**를 맞히는 쪽으로 가고 있다. 같은 능력이 영상 쪽에선 물리적으로 그럴듯한 연출로, 로봇 쪽에선 행동 계획으로 쓰인다. Runway가 영상 툴 회사에서 **물리 AI 회사**로 무게를 옮기는 신호이기도 하다.

## 주의
벤치마크는 모두 발표 주체가 고른 수치다. 로봇 성공률 46%는 ‘절반 이상 실패’라는 뜻이기도 하다. 실제 현장 투입은 여전히 하드웨어별 미세조정과 안전 검증이 필요하다.
