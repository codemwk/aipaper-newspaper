---
title: "AI 도구: OpenAI ‘Decisions API’ 정식 출시 — 글을 쓰지 않고 ‘고르기만’ 하는 AI, 출력 요금 0원·입력 100만 토큰 $0.10, Datadog은 ‘이 명령 위험한가’ 판정을 40배 빠르게"
date: 2026-10-25T07:06:00+09:00
category: "AI 도구"
slug: "openai-decisions-api"
summary: "OpenAI가 10/22 Decisions API를 정식 출시. GPT-6 Luna 기반으로 ‘답이 정해진 질문’(이 문의는 고객지원? 영업? / 이 사진에 파손이 있을 확률은? / 심각도 1~5?)에만 답해, 같은 Luna를 Responses API로 쓸 때보다 최대 10배 빠르다. 답 형식은 확률(predicate)·선택(choice)·점수(score) 3가지. 요청당 질문 400개, 입력 100만 토큰당 $0.10(캐시 $0.01), 출력 요금 없음. 음성 GPT-Live와 직결. Datadog·Sierra·Box·Speak·Ramp 사례 공개."
---

## 한줄 요약
에이전트가 하는 일의 대부분은 긴 글쓰기가 아니라 **작은 판단**이다 — 어디로 보낼까, 다시 시도할까, 사람에게 넘길까. OpenAI가 이 ‘작은 판단’만 따로 빠르고 싸게 처리하는 **Decisions API**를 10/22 정식 출시했다([OpenAI](https://openai.com/index/decisions-api)).

## 어떻게 쓰나
질문과 **허용되는 답**을 정하고, 맥락(텍스트·이미지·JSON)을 넣으면 세 가지 중 하나로 답한다.

| 형식 | 예시 | 돌려주는 값 |
|---|---|---|
| predicate | “이 상품 사진에 파손이 보이나?” | 0~1 확률 |
| choice | “계속 / 재시도 / 사용자에게 확인” 중 무엇? | 고른 값 + 각 확률·신뢰도 |
| score | 루브릭 기준 심각도 | 확률 가중 평균 점수 |

- 요청 하나에 **질문 최대 400개**(베타 때의 2배), 프롬프트 캐시, 미국·EU 처리 지역 선택.
- **가격**: 입력 100만 토큰당 $0.10, 캐시 입력 $0.01, **출력 요금 없음**([개발 문서](https://developers.openai.com/api/docs/guides/decisions)).
- **GPT-Live 연동**: 음성 대화 중에 “명확히 되묻기 / 다른 부서로 / 상급자 연결”을 실시간으로 고르거나, 아바타가 사용자 말에 맞춰 **표정(웃음·윙크)**을 바꾸게 할 수 있다.

## 고객사가 밝힌 수치 (각사 자체 측정)
- **Datadog**: 에이전트가 만든 셸 명령의 **실행 전 위험도 채점** — 최신 모델 대비 p95 지연 **40배 빠르게**, 정확도 비슷
- **Sierra**: 실시간 고객 상담에서 다음 행동 선택 p95 **280ms 미만**, 이전 방식보다 3배 빠르고 호출당 비용 90%↓
- **Box**: 보험 증명서 30건 분류·라우팅 약 5배 빠르게, 정확도 동일
- **Speak**(언어 학습): 다음 행동까지 1.4초 → 0.13초
- **Ramp**: AI 비용을 실제 업무에 귀속 — 4배 빠르고 30% 저렴

## 왜 중요한가
- **에이전트 비용 구조가 바뀐다**: 판단마다 큰 모델에 긴 답을 생성시키던 걸, “고르기 전용” 호출로 바꾸면 지연·비용이 확 준다. 특히 Datadog 사례처럼 **‘실행 전 안전 검문’**을 매 단계에 넣을 수 있게 된다는 점이 크다.
- 개인 자동화에 대입하면: 뉴스 분류(이 기사는 디자인? 트레이딩?), 메모 태그 달기, 매매 신호를 **“진입 / 대기 / 사람 확인”**으로 거르는 1차 필터 같은 곳에 딱 맞는 형태다.
- 단 확률은 **모델의 추정치**다. 돈이 걸린 판단은 임계값 아래를 사람에게 넘기는 설계가 기본.

출처: [OpenAI — Build more responsive apps with the Decisions API (10/22)](https://openai.com/index/decisions-api) · [Decisions 개발 가이드](https://developers.openai.com/api/docs/guides/decisions) · [Unite.AI](https://www.unite.ai/openai-makes-decisions-api-generally-available-with-gpt-6-luna/)
