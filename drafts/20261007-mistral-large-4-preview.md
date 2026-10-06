---
title: "AI 모델: Mistral Large 4 프리뷰 — 1조 파라미터 오픈웨이트, ‘거절하지 않는 사이버 보안’과 유럽 자체 GPU로 승부"
date: 2026-10-07T07:01:00+09:00
category: "AI 모델"
slug: "mistral-large-4-preview"
summary: "10/6 API 프리뷰 공개, 가중치는 이달 말(보도 기준 10/27). 블로그 기준 1T/활성 49B(문서는 1.05T/52B+비전 1.6B), 컨텍스트 1M. 프리뷰가 입력 $0.68·출력 $2.09/M(정가의 50%). 유럽 자체 데이터센터의 Grace Blackwell 3,800장으로 학습. 수치는 모두 회사 발표."
---

## 한줄 요약
Mistral이 10월 6일 **Mistral Large 4(별명 ‘le Chonk’)** 퍼블릭 프리뷰를 냈다. 지금은 **Mistral Studio API로만** 쓸 수 있고, **가중치는 이달 말** 공개한다([Mistral](https://mistral.ai/news/mistral-large-4/)). The Next Web은 공개일을 **10월 27일**로 전했다([TNW](https://thenextweb.com/news/mistral-releases-large-4-a-1-trillion-parameter-open-weight-ai-model)).

## 스펙과 가격
- **규모**: 블로그는 “1조 파라미터, 활성 490억”, 공식 문서는 “**총 1.05T, 활성 52B, 비전 인코더 1.6B**”로 표기 — 수치가 조금 다르니 가중치 공개 때 기술 문서로 확인이 필요하다([Docs](https://docs.mistral.ai/models/mistral-large-4-0)).
- **컨텍스트 1M 토큰**, 네이티브 멀티모달, 함수 호출·구조화 출력·배치·에이전트 API 지원.
- **프리뷰 가격**: 입력 **$0.68**, 캐시 입력 $0.07, 출력 **$2.09** /100만 토큰. 정가($1.36/$0.14/$4.18)의 **절반**.
- **학습**: 유럽에 있는 Mistral 자체 데이터센터의 **NVIDIA Grace Blackwell GPU 3,800장**에서 처음부터 학습. 학습 데이터는 EU 공식 언어 전부를 포함한 **160개+ 언어**.

## 회사가 내세운 숫자 (자체 발표)
- 코딩: DeepSWE v1.1 **61.7%**, Terminal-Bench 4 **28.3%**. Surge AI 블라인드 평가에서 5개 모델 중 2위(3.74), 1위는 Claude Opus 5(4.22).
- 업무 자동화: Gmail·Sheets·Slack·Salesforce 등 657개 워크플로의 AutomationBench **59.9%**.
- 사이버: Cybench **93%**. “실제 취약점을 재현하고 패치하는” 테스트에서 82%로 최고점이며, **Claude Opus 5.5·GPT-6 Astra는 거절 때문에 0점 근처**라고 주장.
- 프롬프트 인젝션: Lakera B3 공격 **93.3%** 방어.

## 왜 중요한가
이번 주 오픈웨이트 경쟁(Reflection Beam, Aleph Alpha Kolibri)은 “중국 밖 최강”이라는 같은 깃발을 들고 있다. Mistral의 차별점은 두 가지다. ① **보안팀이 ‘거절’ 없이 쓰는 모델** — 사고 대응 중에 공급자 정책이 막히는 것 자체가 리스크라는 논리. ② **유럽 자체 인프라·유럽 법 아래 운영**이라는 주권 패키지. 가중치 공개 전 3주간은 보안 업체·국가 기관이 **완화된 모더레이션** 버전으로 레드팀을 한다.

## 체크포인트
- 벤치마크는 전부 **Mistral 자체 측정**(일부는 vals.ai 등 제3자 평가). 독립 재현은 가중치 공개 후.
- 1T급 MoE는 셀프호스팅 비용이 크다. 개인은 당분간 **API 프리뷰가(50% 할인)** 현실적인 체험 경로.
