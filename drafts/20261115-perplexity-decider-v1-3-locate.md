---
title: "AI 모델: Perplexity Decider v1.3 — 글을 쓰지 않고 ‘확률’만 답하는 결정 모델, 이번엔 문장 속 정확한 위치를 집어내는 Locate 추가"
date: 2026-11-15T07:02:00+09:00
category: "AI 모델"
slug: "perplexity-decider-v1-3-locate"
summary: "Perplexity가 11/13 결정 모델 Decider v1.3(27B)과 Flash v1.3(4B)을 Apache 2.0 오픈 웨이트로 냈다. 예/아니오·객관식·점수 질문에 문장 대신 선택지별 확률을 돌려준다. 새 기능 Locate는 이름·장소·개인정보 같은 텍스트 구간을 글자 위치까지 정확히 뽑는다. API 가격은 입력 100만 토큰당 0.02달러, 출력은 무료다."
---

## 한줄 요약
이틀 전(11/13) 소개한 구글 Gemini Decision 1에 이어, 이번엔 Perplexity가 **‘결정 모델’** 새 버전을 냈다. **Decider v1.3**(27B, Qwen3.8-27B 기반)과 **Decider Flash v1.3**(4B, Qwen3.5-4B 기반)이다. 가중치는 **Apache 2.0**으로 Hugging Face에 공개됐고 Perplexity Decisions API와 OpenRouter에서도 쓸 수 있다([MarkTechPost](https://www.marktechpost.com/2026/11/13/perplexity-decider-v1-3-open-weight-decision-models-locate/), [모델 카드](https://huggingface.co/perplexity-ai/pplx-decider-v1.3), [API 문서](https://docs.perplexity.ai/docs/decisions/quickstart)).

## 결정 모델이 뭐길래
- 일반 챗봇은 문장으로 답한다. 결정 모델은 **선택지마다 확률**을 돌려준다. “이 메일은 스팸인가? 예 0.93 / 아니오 0.07” 같은 식이다.
- 그래서 분류, 라우팅(이 질문을 어느 에이전트에 보낼지), 검색 결과 재정렬, 채점 같은 **‘시스템 안의 판단’**에 맞는다. 답을 파싱할 필요가 없고 출력 토큰 비용도 없다.
- 한 입력(state)에 질문 여러 개를 한 번에 묻는다. v1.3에서는 **질문끼리 서로를 보지 못하게** 바꿨다. v1.2에서는 다른 질문 때문에 답이 흔들릴 수 있었다.

## 새 기능 Locate
- 텍스트에서 **정확한 구간을 시작·끝 글자 위치와 함께** 뽑는다. “location”처럼 짧은 이름이나 “채용 공고에서 근무 도시를 뽑아라” 같은 지시로 지정한다.
- 용도는 개체명 인식, **개인정보(PII) 탐지**, 근거 문장 추출. 한 요청에 최대 128개 질문까지, 텍스트 전용이다.

## 가격과 돌리는 조건
- API: v1.3 **입력 100만 토큰당 0.02달러**, Flash 0.01달러, **출력 무료**. 입력은 256K 토큰 미만.
- 로컬: BF16 가중치 기준 v1.3 약 **49GiB**, Flash 약 **8.5GiB**의 GPU 메모리가 필요하다. 양자화 버전은 아직 없다.
- 성능 수치(질의 분류 91.6% 등)는 **모두 Perplexity 자체 발표**다. 독립 평가는 아직 거의 채워지지 않았다.

## 왜 중요한가
에이전트를 직접 엮는 사람에게 **“판단만 하는 싼 부품”**이 생기고 있다. 구글(Decision 1)과 Perplexity(Decider)가 같은 주에 내놓은 건 우연이 아니다. 예를 들어 매일 들어오는 기사 수백 개를 “내 관심사인가?”로 거르거나, 노트에서 사람 이름·날짜만 정확히 뽑는 일을 **대형 모델 대신 결정 모델에 맡기면** 비용과 흔들림이 크게 줄어든다. Flash는 8.5GiB라 좋은 그래픽카드 한 장이면 로컬에서도 돌릴 수 있다.
