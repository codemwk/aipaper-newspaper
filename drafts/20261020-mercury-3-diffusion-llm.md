---
title: "AI 모델: Inception Mercury 3 — 글자를 ‘한 번에 여러 개’ 쓰는 확산형 언어모델, 초당 1,000토큰 이상·100만 토큰 컨텍스트, 출시가 입력 $0.10·출력 $0.35"
date: 2026-10-20T07:02:00+09:00
category: "AI 모델"
slug: "mercury-3-diffusion-llm"
summary: "Inception이 10/19 확산형 LLM(dLLM) Mercury 3 공개: Mercury 1(2025년 6월)보다 40배 이상 크지만 엔비디아 GPU에서 초당 1,000토큰 이상 유지, 컨텍스트 26만→100만 토큰. 회사는 GPT-6 Luna·Claude Haiku 5.5와 같거나 낫고 4~8배 빠르다고 주장. 정가 100만 토큰당 입력 $0.20·출력 $0.70, 출시 기념 50% 할인($0.10/$0.35), 캐시 토큰은 입력가의 90% 할인. Inception API·Baseten·OpenRouter·Vercel 제공, OpenAI API 호환. 브라우저 에이전트·교육·실시간 검색·고객지원에서 초기 사용."
---

## 한줄 요약
지금 쓰는 거의 모든 챗봇은 글자를 **앞에서부터 한 토큰씩** 쓴다. **Inception**의 Mercury는 이미지 생성 AI처럼 **흐릿한 초안 전체를 여러 번 다듬어** 한꺼번에 완성하는 ‘확산(diffusion)’ 방식 언어모델이다. 2026-10-19 나온 **Mercury 3**는 이 방식이 **커져도 빠르다**는 걸 보여 주겠다는 모델이다([Business Wire via Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/inception-launches-mercury-3-setting-164800350.html)).

## 확산형 언어모델, 쉽게 말하면
- 일반 모델(자기회귀형): “오늘 → 날씨가 → 맑다”처럼 **순서대로 한 단어씩**. 앞 단어가 나와야 다음 단어를 쓴다.
- 확산형: 답변 자리 전체를 놓고 **여러 토큰을 병렬로** 채운 뒤 몇 번에 걸쳐 고친다. 그래서 같은 GPU에서 **훨씬 빨리** 끝난다.
- 그동안의 의문은 “모델을 키워도 이 속도가 유지되나”였다. 공동창업자 스테파노 에르몬은 “한계는 계산량과 데이터이지 알고리즘의 벽이 아니다”라고 말했다.

## Mercury 3 한눈에
| 항목 | 내용 |
|---|---|
| 크기 | Mercury 1(2025년 6월)보다 **40배 이상** |
| 속도 | 널리 쓰이는 엔비디아 GPU에서 **초당 1,000토큰 이상** |
| 컨텍스트 | **100만 토큰**(Mercury 2.5는 26만) |
| 정가 | 100만 토큰당 입력 **$0.20** / 출력 **$0.70** |
| 출시 할인 | 50% 할인 **$0.10 / $0.35**, 캐시 토큰은 입력가의 90% 할인 |
| 제공처 | Inception API, Baseten, OpenRouter, Vercel — **OpenAI API 호환** |

성능은 회사 주장 기준으로 GPT-6 Luna·Claude Haiku 5.5 같은 ‘빠른 모델’급이거나 그 이상이며 **4~8배 빠르다**. 독립 검증은 아직이다.

## 누가 쓰나
학습 앱 RevisionDojo는 힌트·채점·용어 설명이 **약 1초** 안에 돌아오게 됐다며 “기존 스택에 그대로 끼웠다”고 말했다. 그 밖에 브라우저를 대신 조작하는 에이전트, 실시간 검색 에이전트, 고객지원에서 시험 중이다.

## 왜 중요한가
에이전트는 한 작업에 모델을 여러 번 부르기 때문에 **한 번의 지연이 곱셈으로 쌓인다**. 확산형 모델이 이 정도 지능에서 초당 1,000토큰을 낸다면 “똑똑하지만 느린 모델”과 “빠르지만 단순한 모델” 사이의 선택이 사라진다. 실사용 관점에선 음성 비서, 실시간 번역, 글쓰기 도구처럼 **사람이 기다리는 화면**에서 먼저 체감될 것이다. 할인가 기준으로는 오늘 같은 날 나온 MiniMax M3.1 Flash보다도 싸다.

출처: [Inception — Mercury 3 발표 (Business Wire, 10/19)](https://finance.yahoo.com/technology/ai/articles/inception-launches-mercury-3-setting-164800350.html) · [Price Per Token — 신규 모델 목록](https://pricepertoken.com/news/model-releases)
