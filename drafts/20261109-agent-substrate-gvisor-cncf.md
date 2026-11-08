---
title: "새로운 시각: 에이전트는 95%의 시간을 ‘기다린다’ — Google이 Agent Substrate와 gVisor를 CNCF에 기부한 이유"
date: 2026-11-09T07:35:00+09:00
category: "새로운 시각"
slug: "agent-substrate-gvisor-cncf"
summary: "AI 에이전트는 모델 응답·사람 검토를 기다리며 세션 시간의 90~95%를 보낸다. 그렇다고 컨테이너를 끌 수도 없다(메모리·git 상태). Google이 KubeCon에서 Agent Substrate 1.0과 gVisor를 CNCF 샌드박스로 기부했다: 500ms 미만 재개, 신뢰할 수 없는 코드 격리."
---

## 한줄 요약
에이전트가 코딩하거나 장애를 분석하는 동안 **90~95%의 시간은 모델 토큰을 기다리거나 사람의 리뷰를 기다리는 시간**이다(Google 설명). 그 사이 CPU는 0인데 상태(언어 런타임, 로컬 git, 미커밋 편집, 도구 세션)는 지켜야 한다. Google Cloud는 KubeCon NA(11/9~12, 솔트레이크시티)를 앞두고 **Agent Substrate와 gVisor를 CNCF 샌드박스로 기부**한다고 밝혔다([Google Open Source Blog](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html)).

## 문제: 쿠버네티스는 ‘기다리는 프로그램’을 위해 만들어지지 않았다
- **항상 켜둔 Pod**: 빠르지만 사용자가 만 명이면 유휴 비용이 감당 안 된다.
- **0으로 스케일**: 싸지만 저장소 클론·패키지 설치부터 다시 하느라 재개가 20초 넘게 걸린다.
- **대량 평가·RL**: 수천 개 짧은 샌드박스를 Pod로 만들면 etcd·API 서버가 무너진다.

## 해법: Actor와 Worker 분리
**Actor**는 세션 상태(파일시스템·환경변수·메모리)를, **Worker**는 미리 데워둔 Pod 풀의 연산을 맡는다. 요청이 오면 라우터가 붙잡아두고, 상태를 복원해 **500ms 미만에 재개**하고, 턴이 끝나면 스냅샷을 저장하고 자리를 반납한다. 격리는 **gVisor**(사용자 공간에서 시스템 콜을 가로채는 애플리케이션 커널)가 맡고, 하드웨어 가상화가 필요하면 Cloud Hypervisor microVM을 같은 API로 쓴다.

## gVisor 기부의 배경(프로젝트 공식 글)
gVisor 팀은 10/2 글에서 채택자가 Google·Ant Group·OpenAI·Anthropic·Modal·Tines 같은 소수에 몰려 있고, ‘Google 단독 소유’라는 거버넌스 위험이 확산을 막았다고 설명했다([gVisor 블로그](https://gvisor.dev/blog/2026/10/02/gvisor-cncf/)). 유지보수자로 Ant Group·Modal·Tines가 합류를 약속했고 OpenAI·Tencent·NVIDIA는 계속 기여한다.

## 왜 중요한가
‘에이전트 시대의 인프라’가 모델이 아니라 **“멈춰 있는 에이전트를 싸게 보관하고 안전하게 깨우는 문제”**로 옮겨가고 있다. 개인용 상시 비서형 에이전트도 같은 구조적 문제가 있다 — 대부분의 시간은 대기다.

## 주의
‘500ms 미만’, ‘90~95%’는 Google의 설명이고 독립 벤치마크는 없다. Agent Substrate는 1.0 릴리스이긴 하나 CNCF 샌드박스 단계의 초기 프로젝트다. 일반 개인 사용자가 당장 쓸 물건은 아니다.
