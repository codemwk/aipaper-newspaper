---
title: "AI 모델: MiniMax M3.1 Flash — 입력 $0.15·출력 $0.60, 에이전트 작업 비용 70%↓·속도 약 3배, 익명 ‘Space Bunny’로 200조 토큰을 처리했던 그 모델… 단, 모르면 지어내는 경향"
date: 2026-10-20T07:01:00+09:00
category: "AI 모델"
slug: "minimax-m31-flash"
summary: "중국 MiniMax가 10/19 M3.1 Flash 정식 출시: 업무 자동화(여러 SaaS를 오가는 영업·마케팅·재무·HR 작업), 코딩, 컴퓨터 조작, 보안에 초점. 100만 토큰당 입력 $0.15·출력 $0.60·캐시 입력 $0.015(전작 M3는 $0.30/$1.20), 에이전트 작업 전체 비용 70%↓, 출력 초당 200토큰+(중앙값 170+), 컨텍스트 100만 토큰. 익명 모델 ‘Space Bunny’가 초기 버전으로 200조 토큰 이상 처리. MiniMax API·M Plan·MiniMax Code에서 사용, 가중치는 10/23 공개 예정(라이선스 미정). 독립 평가에서 사실 질문에 ‘모른다’ 대신 틀린 답을 내는 경향이 매우 높게 나옴."
---

## 한줄 요약
에이전트는 한 작업에 모델을 수십~수백 번 부른다. 그래서 요즘 모델 경쟁의 핵심은 ‘가장 똑똑한가’보다 **“이 일을 얼마에, 얼마나 빨리 끝내나”**다. 중국 **MiniMax**가 2026-10-19 내놓은 **M3.1 Flash**는 그 질문에 맞춘 모델이다([MiniMax 블로그](https://www.minimax.io/blog/minimax-m31f)).

## 무엇이 달라졌나
- **가격**: 100만 토큰당 **입력 $0.15 / 출력 $0.60 / 캐시 입력 $0.015**. 전작 M3($0.30/$1.20)의 절반이고, MiniMax는 에이전트 작업 기준 **전체 비용이 70% 줄었다**고 밝혔다.
- **속도**: 더 공격적인 희소화(sparsity)로 온라인 추론이 **약 3배** 빨라졌다. 출력 초당 **200토큰 이상**, 중앙값 170토큰 이상.
- **용도**: 영업·마케팅·고객지원·재무·HR처럼 **여러 업무 앱을 오가며 끝까지 처리**하는 작업, 코딩, 화면을 보고 마우스·키보드를 쓰는 컴퓨터 조작, 취약점 찾기 같은 보안 작업.
- **입출력**: 텍스트·이미지 입력, 텍스트 출력, 컨텍스트 **100만 토큰**(VentureBeat가 Artificial Analysis 자료 인용).

## ‘Space Bunny’의 정체
최근 익명으로 돌던 모델 **Space Bunny**가 M3.1 Flash의 초기 버전이었다. 정체를 밝히기 전까지 **200조 토큰 이상**을 처리했다고 MiniMax는 말한다. 실제 사용자 트래픽으로 먼저 다듬고 나중에 이름을 붙이는 방식이 업계의 새 출시 공식이 되는 중이다.

## 어디서 쓰나
MiniMax API(platform.minimax.io), 구독형 **M Plan**, 데스크톱 코딩 앱 **MiniMax Code**. 가중치는 **10/23 공개 예정**이지만 라이선스 조건은 아직 없다(VentureBeat). 더 큰 **Pro** 모델도 예고됐다(날짜 미정).

## 조심할 점: ‘모르면 지어낸다’
VentureBeat가 인용한 Artificial Analysis의 사실 지식 테스트에서 M3.1 Flash는 정답률 56%로 경쟁 저가 모델보다 높았지만, **틀린 경우의 93%가 ‘모르겠다’ 대신 그럴듯한 오답**이었다. 정답을 많이 맞히는 것과 **자기 한계를 아는 것**은 다른 능력이라는 뜻이다. 고객 기록을 고치거나 재무 문서를 분석하는 에이전트라면 검색 근거 붙이기, 검증 단계, 사람 확인을 꼭 함께 설계해야 한다.

## 왜 중요한가
같은 주에 DeepSeek V4.1-Flash-1017(10/18 기사)이 비슷한 가격대로 나왔다. 저가 중국 모델들이 **입력 $0.15·출력 $0.60 선**에서 맞붙으며 ‘매일 수백 번 도는 자동화’의 원가를 끌어내리고 있다. 개인 루틴(뉴스 정리, 메일 분류)처럼 **반복량이 많은 일**은 이런 모델로, 사실 정확도가 중요한 마지막 확인은 더 신중한 모델이나 사람에게 — 이렇게 **역할을 나누는 것**이 비용과 품질을 함께 지키는 방법이다.

출처: [MiniMax — M3.1 Flash 발표 (10/19)](https://www.minimax.io/blog/minimax-m31f) · [VentureBeat — M3.1 Flash 분석 (10/19)](https://venturebeat.com/technology/minimaxs-new-m3-1-flash-beats-deepseek-and-opus-5-on-a-key-business-benchmark-at-lower-cost-but-with-a-high-hallucination-rate) · [Reuters (Investing.com 게재, 10/19)](https://www.investing.com/news/stock-market-news/chinas-minimax-launches-updated-ai-model-m31-flash-claims-major-improvements-4957342)
