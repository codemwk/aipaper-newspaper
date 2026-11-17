---
title: "AI 모델: Microsoft, 자체 모델 7종 한꺼번에 — ‘MAI Code 2’는 GitHub Copilot에, 이미지 2.7·실시간 음성 1·라이선스 가중치까지"
date: 2026-11-18T07:10:00+09:00
category: "AI 모델"
slug: "microsoft-mai-seven-models"
summary: "Microsoft AI가 11/17 Ignite에서 자체 모델 7종을 냈다. 일상 코딩용 MAI Code 2·Code 2 Flash는 GitHub Copilot에서 바로 쓸 수 있고, MAI Image 2.7(이미지 편집), MAI Realtime 1(음성 대화, 분당 $0.01부터), 보안용 MAI Cyber 2 Flash, 의료 받아쓰기, 모델 라우팅용 Decision 1.1이 함께 나왔다. 기업이 자기 데이터로 고쳐 자기 Azure에서 돌리는 ‘MAI Licensed Weights’도 발표했다. 성능·가격 비교는 모두 Microsoft 측정이다."
---

## 한줄 요약
Microsoft AI(MAI)가 11/17 Ignite에서 **자체 모델 7종**을 한 번에 냈다. 메시지는 하나다. “에이전트를 24시간 돌려도 감당할 수 있는 **가격 대비 성능**.” OpenAI 의존을 줄이고 자기 모델 라인업을 갖추려는 흐름이 분명해졌다([Microsoft AI 발표](https://microsoft.ai/news/microsoft-ignite-2026/), [MAI Code 2 소개](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)).

## 라인업 한눈에
- **MAI Code 2**: 일상적인 기업 코딩용. 여러 파일 수정, 디버깅, 저장소 전체 이해, UI에 맞췄다. Microsoft 측정으로 GPT-6.1 Sol 품질의 98%를 약 40% 가격에 낸다. **대시보드·시각화 생성**에 따로 튜닝했고, 프런트엔드 블라인드 비교에서 개발자 64%가 GPT-6 Sol보다 선호했다. **GitHub Copilot에서 바로** 쓸 수 있다. 단, 과학 연구나 아주 긴 에이전트 작업에는 “아직 맞추지 않았다”고 스스로 밝혔다.
- **MAI Code 2 Flash**: 코드 설명, 작은 수정 같은 대량 작업용. Copilot과 Foundry(제한 프리뷰). OpenRouter, Vercel 등에도 곧 올라간다.
- **MAI Image 2.7 / 2.7 Flash**: 이미지 편집용. Flash는 대량 생성에 **1,000장당 약 10달러**. Microsoft Foundry에서 쓴다.
- **MAI Realtime 1**: 첫 실시간 음성 대화(speech-to-speech) 모델. **오디오 분당 0.01달러부터**. 지금은 MAI Labs에서 체험·대기 등록 단계다.
- **MAI Cyber 2 Flash**: 보안 방어용. 이전 MAI Cyber 1.1 Flash보다 출력 토큰 가격 86% 인하.
- **Dragon Copilot Transcribe**(MAI Transcribe 2 기반): 의사-환자 대화 받아쓰기. 월 1,000만 건 진료에 쓰인다.
- **Decision 1.1**: 앱 안에서 **쉬운 일은 싼 모델, 어려운 일만 비싼 모델로 보내는 라우팅 모델**. 고객 4,000곳.
- 여기에 2세대 AI 칩 **Maia 200**이 실제 운영에 들어갔다(와트당 토큰 1.7배).

## ‘내 가중치’ 옵션
**MAI Licensed Weights**는 MAI 모델을 받아 **자기 데이터로 고치고, 자기 Azure 환경에서 돌리는** 방식이다. 접근 권한도, 데이터도, 수정본도 고객 소유라는 설명이다. AT&T가 5G 네트워크 분석용 맞춤 모델을 먼저 썼다고 소개했다.

## 왜 중요한가
- 개인 사용자에게 당장 와닿는 건 **GitHub Copilot 모델 선택지**다. 대시보드나 관리 화면처럼 반복적인 프런트엔드 작업이라면 싼 모델로 충분한지 시험해 볼 만하다.
- 오늘 AI 비즈니스의 Model ML처럼, 업계 흐름은 “최고 모델 하나”가 아니라 **작업별로 싼 모델과 비싼 모델을 섞는 것**이다. Microsoft가 라우팅 모델(Decision)을 따로 파는 이유다.
- 주의: 발표 속 비교 수치와 순위는 모두 Microsoft가 고른 벤치마크 기준이다. 실제 품질은 내 작업으로 확인해야 한다.
