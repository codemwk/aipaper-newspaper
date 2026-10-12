---
title: "AI 도구: DigitalOcean Agent Data Services — 에이전트용 ‘컨텍스트+실행 추적’ 데이터 레이어, 프라이빗 프리뷰(가격·SLA 미확정)"
date: 2026-10-13T07:03:00+09:00
category: "AI 도구"
slug: "digitalocean-agent-data"
summary: "DigitalOcean이 10/12 Agent Data Services를 프라이빗 프리뷰로 공개. Data Flows로 멀티모달·구조화·에이전트 세션을 인덱싱하고, 하나의 카탈로그에서 SQL·벡터·API로 조회. 실행 트레이스를 Learning Services(평가·시뮬레이션)에 흘리는 ‘읽기+쓰기’ 루프가 핵심. 가격·GA 일정은 미약속."
---

## 한줄 요약
에이전트의 실력은 **모델보다 컨텍스트 파이프**에 묶인다. DigitalOcean은 **2026-10-12** [Agent Data Services](https://www.digitalocean.com/blog/introducing-agent-data-services)를 **프라이빗 프리뷰**로 내며, 문서·영상·오디오·운영 DB·**에이전트 실행 로그**를 한곳에서 읽고, 실행 결과를 다시 쓰는 **관리형 데이터 기반**을 제안했다.

## 어떻게 동작하나
- **Managed Data Flows**: 도착하는 데이터를 처리·벡터 인덱싱·풍부화. 파이프라인 인프라를 직접 안 돌린다는 포지션.
- **Data Catalog**: 구조화 레코드와 벡터를 **하나의 거버넌스 카탈로그**에. 소스 계보(lineage) 강조.
- **질의**: 사람·에이전트가 **SQL과 API**로 같은 최신 데이터를 봄.
- **피드백 루프**: 멀티스텝 실행 트레이스·세션 상태를 캡처해 RAG·**Learning Services**(Signals·Evaluations·Simulations)에 연결한다고 명시.
- **배치**: Managed Agents·Serverless Inference·Spaces와 같은 DO 클라우드 위. 외부 스토리지도 연결 가능하다고 적음.
- **한계(블로그 고지)**: 프리뷰는 as-is, **SLA·표준 컴플라이언스 미적용**, 가격·기능·일정은 변경·중단 가능 — **구매 결정 근거로 쓰지 말 것**.

## 왜 중요한가
어제·그제 모델 안전 이슈가 “에이전트가 바깥에서 실수한다”면, 이건 “에이전트가 **무엇을 기억·학습하는가**를 제품화”한다. 벡터 DB·ETL·트레이스 스토어를 각각 조립하던 팀을 **한 기판**으로 묶겠다는 주장이다. 다만 숫자는 없다 — ARR·단가·벤치 공개 없음.

## 기억할 것
- 지금 단계는 **초대 프리뷰**. GA·가격표를 기다릴 것.
- “에이전트 품질 = 데이터 재단”이라는 문장은 마케팅이지만, 트레이스를 1급 시민으로 올리는 방향은 Granola·LLM Wiki와 같은 **컨텍스트 인프라** 레이어와 맞닿는다.

출처: [DigitalOcean — Agent Data Services](https://www.digitalocean.com/blog/introducing-agent-data-services)
