---
title: "깃허브 핫 — NVIDIA OSMO, YAML 하나로 로봇 학습·시뮬·실기 테스트"
date: 2026-09-15T07:10:00+09:00
category: "GitHub Hot"
slug: "nvidia-osmo-physical-ai"
summary: "2026-09-14 MarkTechPost. NVIDIA가 Project GR00T·Isaac Lab·Isaac Sim용 내부 오케스트레이터 OSMO를 Apache-2.0로 오픈소스. 단일 YAML로 학습·시뮬·HIL을 GB200~Jetson까지 라우팅. 최신 6.3.1."
---

## 한줄 요약
[MarkTechPost(2026-09-14)](https://www.marktechpost.com/?s=OSMO)에 따르면 NVIDIA가 내부 Physical AI 파이프라인용 **Kubernetes 네이티브 워크플로 오케스트레이터 OSMO**를 오픈소스했다. Project GR00T·Isaac Lab·Isaac Sim에서 쓰던 것을 Apache-2.0으로 풀었고, 최신 표기는 **6.3.1**이다.

## 무엇을 하는 도구인가
로봇·물리 AI 팀은 보통 학습 클러스터, 시뮬 팜, 보드 위 HIL을 따로 붙인다. OSMO는 **한 YAML**에 작업(학습·시뮬·하드웨어 루프)을 정의하고, GB200급 클러스터부터 Jetson AGX Thor 같은 엣지까지 **맞는 컴퓨트 티어로 라우팅**한다. 인프라 코드를 매번 새로 쓰지 않아도 되게 만든 ‘물리 AI용 CI/CD 스케줄러’에 가깝다.

## 왜 중요한가
에이전트·코딩 하네스가 소프트웨어 쪽을 흡수하는 동안, 하드웨어 쪽은 **시뮬→실기 왕복**이 병목이다. OSMO는 “모델이 똑똑해지면 끝”이 아니라 **같은 스펙으로 여러 컴퓨트에 실험을 돌리는 운영층**을 공개한 신호다. 트레이딩·퀀트 쪽에서도 ‘백테스트 팜 ↔ 페이퍼 ↔ 실계좌’를 한 선언으로 묶는 패턴과 통한다.

## 기억할 것
- 라이선스: Apache-2.0. 내부 스택(GR00T/Isaac) 전제라 로컬 재현 비용은 별도.
- 읽을 때: 벤치마크 숫자보다 **워크플로 선언 + 라우팅**이 핵심 가치.
