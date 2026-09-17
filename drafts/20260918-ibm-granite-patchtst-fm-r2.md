---
title: "IBM Granite PatchTST-FM-r2 — 상업용 허가 제로샷 시계열 예보의 상위권"
date: 2026-09-18T07:20:00+09:00
category: "AI Models"
slug: "ibm-granite-patchtst-fm-r2"
summary: "2026-09-09 HF 블로그. Granite Time Series PatchTST-FM-r2(~385M). GIFT-Eval 재현 가능 제로샷에서 전체 2위·상업용 친화 라이선스(Apache 2.0/OpenMDW) 중 1위(2026-09-08 기준). 확률 예보·결측 보간."
---

## 한줄 요약
[Hugging Face 블로그](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series)(2026-09-09)에서 IBM은 **Granite Time Series PatchTST-FM-r2**를 공개했다. 약 **385M** 파라미터 제로샷 예보 모델이다.

## 무엇이 바뀌었나
- 전작 r1 대비 **conformer 블록**(어텐션+시간 컨볼루션), 패치 오버랩·Hamming 가중, 블록 수 확대 등으로 장·단기 패턴을 같이 잡는다.
- 컨텍스트 최대 **8,192**, 유연한 예보 길이, **99 분위** 확률 헤드, 결측값 **imputation** 지원.
- **2026-09-08** 기준 GIFT-Eval에서 재현 가능·제로샷·테스트 누수 없는 그룹 **전체 2위**(CRPS·MASE), 그중 **허가형 상업용 라이선스** 모델로는 1위라고 IBM은 밝혔다. TimesFM-3 바로 뒤.
- 이중 라이선스 **Apache 2.0 / OpenMDW 1.0**(선택). 가중치·아키텍처·추론·벤치 재현 코드 공개. `ibm-granite/granite-timeseries-patchtst-fm-r2`.
- Confluent Cloud Early Access에서 Granite TSFM 스트리밍 추론과도 연결된다고 언급(초기 포트폴리오에 r1 등 포함, r2는 블로그에서 노트북·허브 중심).

## 왜 중요한가
트레이딩·수요·전력·텔레메트리처럼 **표 형태 시계열**을 LLM 에이전트와 붙일 때, “또 하나의 챗 모델”보다 **전용 제로샷 예보**가 필요한 구간이 있다. 허가 조건이 명확한 SOTA급 오픈 가중치는 사내 거버넌스 통과에 유리하다. 자동매매 파이프라인에서는 신호 생성·리스크 시나리오의 **불확실성 구간(분위수)** 을 같이 가져갈 수 있다.

## 기억할 것
- [IBM/HF 블로그](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series) · Hub: `ibm-granite/granite-timeseries-patchtst-fm-r2` · `granite-tsfm>=0.3.9`
