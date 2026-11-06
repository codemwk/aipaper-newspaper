---
title: "AI 비즈니스: Traversal — AI가 쓴 코드를 지키는 AI SRE, 시리즈 B 1.2억·기업가치 10억 달러·ARR 올해 9배"
date: 2026-11-07T07:00:00+09:00
category: "AI 비즈니스"
slug: "traversal-ai-business"
summary: "Traversal은 프로덕션 장애의 원인을 찾아 고치는 AI SRE다. 11/3 Kleiner Perkins·Redpoint·Khosla 공동 주도 시리즈 B 1.2억 달러로 기업가치 10억 달러. ARR은 연초 대비 9배(절대액 비공개), 지난 분기 조사 15만 건. Datadog Bits AI와 경쟁하며 멀티 텔레메트리 레이어를 판다."
---

## 한줄 요약
코딩 에이전트가 배포 속도를 올리자, **누가 깨진 프로덕션을 고칠지**가 다음 예산이 됐다. Traversal은 로그·메트릭·코드·배포 이력을 읽어 원인을 찾는 **AI SRE**다. 11/3 Kleiner Perkins·Redpoint Ventures·Khosla Ventures가 공동 주도한 **시리즈 B 1.2억 달러**로 기업가치 **10억 달러**, 누적 약 1.73억 달러([BusinessWire 11/3](https://www.businesswire.com/news/home/20261103122345/en/Traversal-Raises-%24120M-with-a-%241-Billion-Valuation-to-Keep-Code-Running-With-a-Superintelligent-AI-Site-Reliability-Engineer)).

## 누구에게 무엇을 파나
- **고객**: Nubank, Harvey, DigitalOcean, PepsiCo, American Express 등. Forbes는 Blackstone도 고객으로 전했다([TNW](https://thenextweb.com/news/traversal-120m-series-b-1b-valuation-ai-sre)).
- **상품**: Traversal Workers. Splunk·Dynatrace·CloudWatch·Elasticsearch·GitHub/GitLab·Jira/ServiceNow 등을 **기본 읽기 전용**으로 연결하고, **Production World Model**(서비스·컨테이너·의존성 지도)과 **Causal Search Engine**(가설 수천 개 병렬 검증)으로 근본 원인을 좁힌다. Slack/Teams에 근거와 권장 수정(가끔 PR 초안)을 올린다([Sacra](https://sacra.com/c/traversal/)).
- **벤치마크**: Cornell Tech·Columbia와 만든 ORCA-bench(1,079개 RCA 과제)에서 프론티어 에이전트 최고 성적이 중간 난이도 **25.3%**, 모호한 보고서는 **10%**, 환각은 **최대 40%** — “범용 에이전트만으론 온콜이 안 된다”는 회사 주장의 근거다.

## 돈 버는 구조
엔터프라이즈 세일즈. 공개 가격표 없음. 장애·알림 볼륨, 텔레메트리 규모, 온콜 구조, 롤아웃 범위로 **Worker 수와 배포 형태**를 잡는다([Get Pricing](https://www.traversal.com/get-pricing)). 회사 발표: ARR **연초 대비 9배**, 제품 사용량 약 100배, MAU 약 20배; 지난 분기 조사 **15만+**, 엔지니어 **4,000+**, 주요 장애 1,000+/경미 5만+/중요 변경 5,000+. 절대 ARR은 Agarwal CEO가 Forbes에도 밝히지 않았다.

## 왜 중요한가
어제 판 **Upwind**(런타임 보안)가 ‘에이전트가 클라우드에 뿌려진 뒤 방어’였다면, Traversal은 **에이전트가 쓴 코드가 프로덕션에서 깨질 때 조사·복구**다. Datadog Bits AI SRE(플랫폼 묶음) vs 멀티 툴 독립 레이어 경쟁의 유니콘 숫자다.

## 주의
- ARR 절대액·ROI “수천만 달러”는 회사·사례 인용. 감사 실적 아님.
- 자율 수정 권한을 키울수록 오진단 리스크가 커진다. 기본은 읽기 전용.
