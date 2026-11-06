---
title: "AI 모델: Mistral Studio — Managed Agents·워크플로·앱을 퍼블릭 프리뷰로, 온프렘은 11월 말"
date: 2026-11-07T07:07:00+09:00
category: "AI 모델"
slug: "mistral-studio-agents"
summary: "Mistral이 Studio에 Managed Agents·Apps(퍼블릭 프리뷰)와 Cloud Workflows를 확장했다. Python SDK로 정의한 에이전트를 in-process·self-host·Mistral 관리형으로 배포하고, 실패 후 재개·사람 승인 대기를 지원한다. 프라이빗 클라우드·온프렘은 11월 말 예정."
---

## 한줄 요약
미국 빅테크 에이전트 런칭 사이에 유럽 진영도 **운영형 에이전트 콘솔**을  densify했다. Mistral **Studio**는 Managed Agents·Apps를 퍼블릭 프리뷰로 열고, Workflows는 Mistral Cloud에서 제공한다([Mistral 뉴스/문서 요약](https://mistral.ai/fr/news/build-with-studio/), [Managed Agents docs](https://docs.mistral.ai/studio/deployments/managed/agents)).

## 구조
- **정의**: `mistralai-agents` Python SDK.
- **실행 위치 3단**: 프로세스 안 / `agents serve` 셀프호스트 / **`agents deploy` 관리형**(백그라운드 내구성, 실패 후 재개, 민감 단계에서 human approval pause).
- **관측**: Studio가 에이전트·모델·툴 호출 트레이스를 남긴다.
- **배포 로드맵**: 프라이빗 클라우드·온프레미스 **11월 말** 목표(회사 발표).

## 왜 중요한가
“채팅창 에이전트”와 “기업이 밤에 돌려도 되는 에이전트”는 다르다. Mistral은 후자 — **내구성·승인·배포 위치** — 를 Studio 한곳에 묶었다. 데이터 거주·벤더 다변화가 필요한 EU·규제 업종 팀의 대안 후보로 보면 된다.

## 주의
퍼블릭 프리뷰 범위·쿼터·가격은 플랜별로 달라 문서의 access limits를 확인. 온프렘 일정도 “예정”이다.
