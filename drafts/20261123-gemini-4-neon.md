---
title: "AI 모델: 구글 ‘Gemini 4 Neon’ — Carbon과 Hydrogen 사이의 ‘일 잘하는 중간 모델’, 입력 100만 토큰당 3달러·출력 15달러"
date: 2026-11-23T07:05:00+09:00
category: "AI 모델"
slug: "gemini-4-neon"
summary: "구글이 11/18 Gemini 4 Neon을 냈다. 가장 큰 Carbon(긴 프로젝트용)과 빠른 Hydrogen(일상 작업용) 사이에서 ‘깊이와 비용의 균형’을 맡는다. 가격은 100만 토큰당 입력 3달러(캐시 0.15달러), 출력 15달러, 컨텍스트 100만 토큰. 생각 수준은 low·medium·high(기본)·xhigh 네 단계다. Gemini API, AI Studio, Gemini for business, Antigravity, Gemini 앱(Pro·Ultra)에서 쓸 수 있다. 구글은 high 기준 Carbon보다 작업당 비용이 32% 낮다고 밝혔다."
---

## 한줄 요약
구글 Gemini 4 가족에 **중간 체급 Neon**이 들어왔다(11/18). 구글의 표현으로는 “Carbon은 가장 어렵고 긴 프로젝트, Hydrogen은 빠른 일상 실행, **Neon은 그 사이의 균형**”이다([구글 블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)).

## 무엇을, 얼마에
- **가격**: 100만 토큰당 입력 **3달러**, 캐시된 입력 **0.15달러**(95% 할인), 출력 **15달러**(생각 토큰 포함). 컨텍스트 **100만 토큰**.
- **생각 수준 4단계**: low, medium, **high(기본)**, xhigh. 일의 난이도에 맞춰 지능과 토큰 비용을 조절한다.
- **비용**: 구글은 기본 high 설정에서 작업당 비용이 **Carbon보다 32% 낮다**고 밝혔다.
- **쓸 수 있는 곳**: Gemini API 유료 등급(AI Studio·Android Studio), Gemini for business(API·모델 선택 메뉴), Google Antigravity(유료 AI Pro·Ultra), Gemini 앱(Pro·Ultra 구독자). 보안 방어용 *Neon for cyber*는 신뢰 기관 프로그램(Fairwind)으로 며칠 내 배포된다.

## 무엇이 달라졌나
- **긴 에이전트 작업**: 도구를 많이 쓰는 긴 작업을 끝까지 이어 가도록 만들었다. 같은 파일을 쓸데없이 다시 읽는 일을 줄이고, 진행 상황을 공유하고, 긴 세션에서 대화 압축(context compaction)을 안정적으로 처리한다고 한다.
- **지휘자 역할**: Antigravity에서 Neon이 **여러 Hydrogen 하위 에이전트를 병렬로 지휘**하는 구성을 내세웠다. 비싼 모델은 판단만, 실행은 싼 모델이 하는 구조다.
- **업무 문서**: 스프레드시트·PDF·차트·오디오·영상을 한 컨텍스트에 넣어 정리된 결과물로 바꾸는 일을 강조했다. 앱에서는 Gmail·Docs 내용을 끌어와 보고서를 쓴다.
- **정직성**: 구글 내부 평가에서 코딩 ‘지름길(꼼수)’ 비율 2.45%로 Gemini 4 중 가장 낮았고, 에이전트 정직성 평가 통과율은 99.2%였다고 밝혔다. 모두 구글 자체 수치다.

## 왜 중요한가
요즘 모델 경쟁의 승부처는 ‘가장 똑똑한 모델’보다 **‘대부분의 일을 싸게 끝내는 중간 모델’**이다. 11/18 전한 GPT-6.2 Sol(입력 2달러·출력 10달러), Microsoft MAI Code 2와 같은 자리다. 실무 팁은 단순하다. **기본은 중간 모델(high)로 돌리고, 정말 막힐 때만 xhigh나 최상위 모델을 부른다.** 그리고 같은 프롬프트가 반복되면 캐시 가격(0.15달러)이 비용을 크게 줄인다. 구글이 낸 벤치마크 순위는 대부분 자체 발표라, 내 작업으로 직접 비교해 보는 것이 가장 정확하다.
