---
title: "AI 모델: Microsoft Mage-VL-Cowork — 4B가 GUI 클릭과 터미널을 한 정책으로. OSWorld-Verified 66%"
date: 2026-11-01T07:03:00+09:00
category: "AI 모델"
slug: "mage-vl-cowork-4b"
summary: "Microsoft가 10/30 Hugging Face에 Mage-VL-Cowork(4B)를 올렸다. 스크린샷 기반 computer_use와 bash를 외부 오케스트레이터 없이 한 모델이 고른다. OSWorld-Verified 50스텝 기준 66.0%(4B대 최고 주장). Apache-2.0, Docker·SGLang 서빙."
---

## 한줄 요약
픽셀만 클릭하면 토큰이 낭비되고, 터미널만 주면 GUI 앱을 못 다룬다. Mage-VL-Cowork는 **언제 마우스를 쓰고 언제 셸을 쓸지**를 4B 한 모델 안에 넣었다([Hugging Face](https://huggingface.co/microsoft/Mage-VL-Cowork)).

## 핵심 숫자
| 항목 | 값 |
|---|---|
| 파라미터 | **4B** (bf16 약 9.5GB) |
| 벤치 | **OSWorld-Verified 66.0%** (361태스크, 50스텝, 2런 평균 65.33·66.75) |
| 비교 | 동급 4B 중 최고라고 팀 주장. ScaleCUA-Qwen3.5-9B 68.7 등은 더 큰 모델 |
| 데이터 | Mage-CUA-Forge로 **293,806** 태스크 합성, 태스크당 비용 $0.906→$0.158(−82.6%) |
| RL 효과 | Hybrid SFT 대비 +10.16pp, 평균 호출 −13%, 출력 토큰 −25.4% |

## 동작 방식(쉽게)
- 채널 둘: `computer_use`(클릭·타이핑·스크롤) + `bash`(파일·검증).
- 스프레드시트 병합처럼 **구조화된 편집**은 GUI 39스텝 대신 Python 6스텝으로 끝내는 식의 데모를 공개.
- 학습은 “먼저 GUI·코딩을 따로 세게 → 나중에 합치기” 5단계. 교사 하네스에서 중복 도구를 쳐내니 학생 4B가 +12.5pp 이득을 봤다고 한다.

## 왜 중요한가
- **온디바이스·소형 에이전트**가 ‘하이브리드 컴퓨터 사용’에 들어왔다는 신호. 다만 샌드박스·사람 확인 없이 셸을 열면 위험하고, 팀도 격리 환경을 권한다.
- 라이선스 Apache-2.0. `trust_remote_code` 커스텀 아키텍처(`llava_onevision2`).
