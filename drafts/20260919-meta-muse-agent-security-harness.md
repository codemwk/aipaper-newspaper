---
title: "Meta Muse — 메일·결제까지 하는 개인 에이전트, Sentinel·자격증명 분리 하네스"
date: 2026-09-19T07:40:00+09:00
category: "AI Models"
slug: "meta-muse-agent-security-harness"
summary: "2026-09-18 DeepLearning.AI The Batch. Muse(Spark 1.3)가 앱/WhatsApp으로 메일·폼·구매·백그라운드 작업. VM 셀 분리, 모델은 자격증명 미보유, Sentinel 승인. 미국 18+, Free/$20/$100."
---

## 한줄 요약
[DeepLearning.AI The Batch](https://www.deeplearning.ai/the-batch/how-to-secure-agents-for-the-masses)(2026-09-18)는 Meta **Muse** 개인 에이전트(모델 **Muse Spark 1.3**)를 **보안 하네스** 관점에서 해부했다. 앱·WhatsApp으로 메일 송수신, 브라우징, 폼, **Stripe Link 구매**, 앱을 꺼도 백그라운드 작업을 한다.

## 무엇이 바뀌었나
- 연결: 브라우저·메일·캘린더·Instagram/Facebook·차량·스마트홈 등, 서비스별 읽기/쓰기. 메모리 열람·편집·삭제, 활동 로그.
- 가격(보도): Free(~1억 토큰/주), **$20**(~5억), **$100**(~30억). 미국·18+·iOS/Android/muse.ai/WhatsApp.
- 보안 설계 요지: 에이전트는 **격리 VM/컨테이너** 안. **자격증명은 셀 밖** — 모델은 스탠드인만 보고, **Sentinel**이 요청을 허용·거부·사용자 확인 후 실토큰을 붙인다. 승인 UI는 대화 메시지가 아니라 **시스템 다이얼로그**(인젝션으로 가짜 승인 방지). 메일·구매는 항상 사용자 검증, 낯선 상점 구매는 **일회용 카드**.
- 추가 방어: 비신뢰 라벨, 셀 밖 분류기 앙상블, 브라우저는 접근성 트리 요약(JS 실행 없음). 버그바운티(유효 리포트 최대 $300k, 성공 인젝션 최대 $130k)로 검증을 외주에 맡긴 상태. 분류기 정확도 수치는 미공개.

## 왜 중요한가
Simon Willison의 “lethal trifecta”(사적 데이터+비신뢰 콘텐츠+외부 송신)를 **모델이 속아도 OS 게이트가 막는다**는 가정으로 설계한 대중 제품 사례다. 가중치 공개 약속보다 **하네스 오픈**이 더 중요하다는 Batch의 결론이 실무적으로 와닿는다.

## 기억할 것
- [The Batch](https://www.deeplearning.ai/the-batch/how-to-secure-agents-for-the-masses) · Muse / Muse Spark 1.3
