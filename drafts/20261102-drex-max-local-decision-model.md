---
title: "AI 모델: Nace Drex Max v1 공개 가중치 — 글을 쓰지 않고 ‘고르기만’ 하는 27B 결정 모델, 24GB 맥에서 돈다"
date: 2026-11-02T07:02:00+09:00
category: "AI 모델"
slug: "drex-max-local-decision-model"
summary: "Nace AI가 결정 모델 Drex Max v1(27B dense, 262K 컨텍스트)을 Open RAIL-M 가중치로 공개했다(11/1). 텍스트·JSON·이미지를 넣고 질문을 주면 생성 없이 한 번의 순전파로 최대 255개 선택지 확률을 돌려준다. 4비트 빌드는 24GB+ 애플 실리콘. 자체 Decision Index 0.4 67.52(Drex v2.0 61.25). 수치는 자체 발표, 소개 기사는 후원 콘텐츠."
---

## 한줄 요약
에이전트의 ‘이 티켓은 어느 팀?’, ‘이 요청은 정책 위반?’ 같은 판단을 **로컬에서, 생성 없이** 처리하는 모델이 공개 가중치로 나왔다([MarkTechPost](https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/)).

## 어떻게 다르나
- 입력: 상태(텍스트·JSON·이미지) + 이름 붙은 질문들. 질문 유형은 **선택지 / 예·아니오 / 순위 점수** 3가지.
- 출력: 문장이 아니라 **선택지별 확률**. 한 번의 순전파, 질문당 최대 255개 선택지.
- 구조: 64층 중 48층은 Gated DeltaNet 선형 어텐션, 16층은 전체 어텐션(비인과). 마지막에 255-way 판독 헤드.

## 어디서 돌리나
| 런타임 | 하드웨어 | 체크포인트 |
|---|---|---|
| Python | NVIDIA(H100 bf16 / L40S 8비트) | bf16 약 49GB, 8비트 약 26GB |
| llama.cpp·Ollama 포크 | 애플 Metal·CPU | Q8_0 GGUF 27.25GB(48GB 맥) |
| MLX·Kapitsa | 애플 실리콘 | affine Q4 14.45GB(**24GB+ 맥**) |

로컬 맥·CPU 경로는 **아직 텍스트만**(이미지는 GPU 파이썬 경로). Nace 측정상 M5 Pro의 Q8_0이 H100 bf16과 확률 차 0.02 이내.

## 숫자 (모두 자체 발표)
- Decision Index 0.4: **67.52** (Drex v2.0 61.25, 폐쇄형 Jev 1.13.0 57.96).
- 영역별: Tools 81.9, Language 72.2, Retrieval 68.8.
- 호스팅 가격(출시가) 1,000회 결정당 **0.03달러**.

## 왜 중요한가
- 라우팅·분류·가드레일은 에이전트 비용의 숨은 덩어리다. 이걸 **생성 LLM 대신 작은 ‘판단 전용’ 모델로 떼어 내 로컬에 두는** 패턴이 굳어지고 있다(10/31 Baseten joey-1, 11/1 RightNow System Zero에 이어).
- 단, 벤치마크는 전부 Nace 자체 수치이고, 소개 기사도 Nace 후원 콘텐츠라고 명시돼 있다. 직접 내 데이터로 확률 보정부터 확인할 것.
