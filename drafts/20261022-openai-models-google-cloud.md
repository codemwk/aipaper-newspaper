---
title: "AI 도구: OpenAI 모델이 Google Cloud에 들어갔다 — GPT-6 Astra·6.1 Sol·6 Luna 비공개 프리뷰, Codex CLI도 Gemini 플랫폼에서 추론, ‘구글 청구서 한 장’으로"
date: 2026-10-22T07:10:00+09:00
category: "AI 도구"
slug: "openai-models-google-cloud"
summary: "OpenAI와 Google Cloud가 10/21 파트너십 발표: OpenAI의 GPT-6 Astra(고난도 코딩·컴퓨터 사용·연구), GPT-6.1 Sol(Astra급에 더 낮은 비용), GPT-6 Luna(빠르고 저렴한 일상용)가 Google Cloud Model Garden에 일부 기업 대상 비공개 프리뷰로 출시. 로컬 Codex CLI·데스크톱도 Gemini 플랫폼에서 추론 연결. Google Cloud Marketplace로 거래돼 구글 청구서 한 장에 합산, 기존 클라우드 약정 차감 가능. 데이터는 고객 경계 안, 학습 미사용(ZDR·Confidential Compute는 예정). 곧 Gemini for business·Antigravity에도. 정식 출시는 수주 내. Google Cloud는 ‘3대 폐쇄형 LLM을 모두 제공하는 유일한 하이퍼스케일러’라고 주장. OpenAI는 ‘Microsoft가 여전히 주 클라우드 파트너’라고 명시."
---

## 한줄 요약
경쟁사의 모델을 자기 매장에 들여놓는 일이 또 일어났다. 이번엔 **OpenAI가 Google Cloud에** 들어갔다([OpenAI](https://openai.com/index/openai-models-google-cloud), [Google Cloud 블로그](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)).

## 무엇이 들어왔나
| 모델 | Google 설명 |
|---|---|
| **GPT-6 Astra** | 코딩·컴퓨터 사용·전문 업무·과학 연구 같은 고난도 작업 |
| **GPT-6.1 Sol** | Astra에 가까운 지능을 더 낮은 비용으로(에이전트 코딩·컴퓨터 사용) |
| **GPT-6 Luna** | 대량 일상 업무용 빠르고 저렴한 모델 |

- 지금은 **일부 기업 고객 대상 비공개 프리뷰**(신청 양식). OpenAI는 **수주 내 정식 출시**를 예고했다.
- 오늘부터 로컬 **Codex CLI·데스크톱** 작업을 Google의 Gemini 플랫폼 추론에 직접 연결할 수 있다.
- 곧 **Gemini for business**(OpenAI 쪽 표현으론 ‘Gemini Agent’)와 Google의 에이전트 IDE **Antigravity**에서도 OpenAI 모델을 고를 수 있게 된다.

## 돈과 보안: 기업이 반길 부분
- **청구서 한 장**: Google Cloud Marketplace로 거래돼, 사용료가 구글 청구서에 합산되고 **기존 클라우드 약정(커밋)에서 차감**되며 여러 모델 공급자에 걸친 Flexible Savings Plans에도 포함된다. 별도 벤더 계약이 필요 없다.
- **데이터 경계**: 프롬프트·맥락·출력은 고객이 지정한 경계 안에 머물고 기반 모델 학습에 쓰이지 않는다. 전용 Google Cloud 인프라에서 돌며, **ZDR(무보존) 옵션과 Confidential Compute는 ‘곧’**.
- **감사·신원**: 모든 에이전트·모델 호출이 인증된 신원으로 기록되고 VPC Service Controls로 보호된다.

## 행간
- Google Cloud는 이로써 “**3대 폐쇄형 LLM을 모두** 제공하는 유일한 하이퍼스케일러”라고 주장한다(기존 Gemini·Claude에 OpenAI가 더해졌다는 뜻으로 읽힌다). 200개 넘는 모델을 한 플랫폼에서 바꿔 끼우는 **‘모델 선택권’** 이 클라우드 경쟁의 핵심 상품이 됐다.
- OpenAI는 같은 글에서 “**Microsoft가 여전히 주 클라우드 파트너**”라고 못 박았다. 독점보다 **유통 채널 확대**가 우선이라는 신호다.

## 왜 중요한가
기업 입장에선 “어떤 모델이 최고냐”보다 **“우리 계약·보안 체계 안에서 쓸 수 있느냐”** 가 도입을 가른다. 이제 GCP 고객은 별도 벤더 계약 없이 Gemini·Claude·GPT를 작업별로 바꿔 쓸 수 있다. 개인 개발자에겐 Codex를 쓰면서 추론 비용을 회사 GCP 약정으로 돌리는 길이 열린 셈이다(프리뷰 승인 필요).

출처: [OpenAI — OpenAI models are coming to Google Cloud (10/21)](https://openai.com/index/openai-models-google-cloud) · [Google Cloud 블로그 (10/21)](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)
