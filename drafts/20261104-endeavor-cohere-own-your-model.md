---
title: "AI 모델: ‘모델을 빌려 쓰지 말고 내 통제 아래’ — 같은 날 Flower Endeavor 1.1(사고 과정 공개·출력으로 내 모델 학습 허용)과 Cohere Model Vault(오픈 모델을 데이터 보관 0으로)"
date: 2026-11-04T07:02:00+09:00
category: "AI 모델"
slug: "endeavor-cohere-own-your-model"
summary: "11/3 Flower Labs가 Endeavor 1.1을 공개: 이미지 입력 추가, EU 내 GPU 추론, Flower 관리형·프라이빗 클라우드·온프레미스 배포, 읽을 수 있는 사고 과정(thinking trace) 제공, 그리고 출력·트레이스로 내 모델을 학습해도 된다는 조건. 같은 날 Cohere는 Model Vault에 DeepSeek·Gemma·GPT-OSS·Phi·GLM·Nemotron 등 오픈 모델을 올리고 프롬프트·출력 무보관을 기본값으로 했다."
---

## 한줄 요약
모델 경쟁의 축이 하나 더 생겼다. “얼마나 똑똑한가”가 아니라 **“누가 통제하나”** — 어디서 돌고, 생각 과정을 볼 수 있고, 결과물을 내 자산으로 쓸 수 있는가.

## Flower Endeavor 1.1 — ‘사용자의 기본권’을 상품으로
[Flower Labs 블로그(11/3)](https://flower.ai/blog/2026-11-03-introducing-endeavor-1.1)가 내건 조건:
- **배포 선택**: Flower 관리형, 프라이빗 클라우드, 온프레미스. 업그레이드 시점도 고객이 정한다.
- **EU 추론**: EU 안의 GPU에서만 돌리는 옵션 신설. 영국·중동·아시아·아프리카 지역 옵션도 예고.
- **사고 과정 공개**: 읽을 수 있는 thinking trace를 그대로 제공. Flower는 OpenAI가 요약만, Anthropic이 원본을 대체로 비공개한다고 대비시킨다.
- **출력으로 내 모델 학습 허용**: 대형 랩들이 경쟁 모델 학습에 출력 사용을 제한하는 것과 정반대. 예: 검증된 장애 해결 사례+트레이스를 모아 사내 ‘트러블슈팅 전용 소형 모델’을 만든다.
- 기능: 이미지 입력 추가, 1.0 대비 추론·코딩 강화(회사 수치 GPQA 92.0→94.4).

## Cohere Model Vault — 오픈 모델을 ‘관리형 금고’에
[Cohere(11/3)](https://cohere.com/blog/open-source-model-vault)는 자사 모델 전용이던 Model Vault에 DeepSeek V4.1 Flash, Gemma 4, GPT-OSS, Phi, GLM, MiMo, Nemotron, Tencent Hy3 등 **타사 오픈 모델**을 올렸다. 프롬프트·출력 **보관 0(zero data retention)이 기본값**, 미국·EU·캐나다 리전. 암호화 버전(Model Vault Encrypted)은 미국 먼저, 지원 모델은 Gemma·GPT-OSS·Phi 등 일부.

## 왜 중요한가
- 개인 사용자에겐 멀어 보여도, 내 노트·코드·거래 기록을 AI에 맡기는 순간 똑같은 질문이 생긴다. **“내 데이터가 어디로 가고, 결과물은 누구 것인가.”** 로컬 우선 PKM을 고민하는 사람에게 이 두 발표는 기업판 답안지다.
- ‘출력으로 학습해도 된다’는 조건은 작지만 크다. 큰 모델로 일하면서 쌓인 결과가 **나만의 작은 모델**로 이어지는 길이 계약상 열린다.

## 주의
- Endeavor의 “OpenAI·Anthropic과 동급 이상” 주장은 회사가 고른 4개 벤치마크(GPQA·AIME·HumanEval·IFEval) 합성 점수 기준이다. 독립 평가는 아직 없다. 가격도 공개되지 않았다.
- Cohere 표의 모델별 지원 여부는 리전·버전마다 다르다.
