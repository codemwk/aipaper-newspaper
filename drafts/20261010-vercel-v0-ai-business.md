---
title: "AI 비즈니스: Vercel v0 — 좌석료+$30 크레딧으로 들어와, 생성은 토큰으로 과금하고, 배포는 Vercel 인프라 매출로 이어진다"
date: 2026-10-10T07:02:00+09:00
category: "AI 비즈니스"
slug: "vercel-v0-ai-business"
summary: "Vercel의 AI 앱 빌더 v0는 Free(일일 메시지 한도)·Plus(좌석당 월 $30 크레딧)·Business($100/유저)·Enterprise로 팔린다. Sacra 추정 Vercel ARR $3.4억(2026-02), Series F $9.3B. v0 사용자 400만+, Teams·Enterprise가 v0 매출 50% 초과. AI 수수료와 배포 인프라가 한 줄로 묶인 구조."
---

## 한줄 요약
**v0**는 프롬프트·스크린샷·Figma를 **배포 가능한 React/Next.js 앱**으로 바꾸는 Vercel의 AI 빌더다. 돈은 **① 좌석·포함 크레딧 구독**, **② 초과분의 토큰·크레딧 사용량**, **③ v0로 만든 앱이 Vercel에 올라가며 생기는 인프라 소비** — 이 세 갈래로 흐른다([v0 가격](https://v0.app/pricing), [Sacra](https://sacra.com/c/vercel/)).

## 숫자가 말하는 구조 (공개·추정 구분)
- **회사 전체**: Sacra는 2026년 2월 기준 Vercel **연환산 매출(ARR) 약 $3.4억**으로 추정. 2025년 9월 **Series F $3억, 기업가치 $93억**(Accel·GIC 공동 주도).
- **v0**: 출시 이후 사용자 **400만+**(Series F 시점 350만에서 증가). Sacra는 **Teams·Enterprise가 v0 매출의 절반 이상**이라고 본다 — 개인 체험 도구가 아니라 B2B 단가가 잡히기 시작했다는 신호.
- **배포 쪽 파급**: Sacra에 따르면 Vercel 주간 배포의 **30% 이상**이 코딩 에이전트가 시작하며, 에이전트가 올린 프로젝트는 사람이 올린 프로젝트보다 AI 추론 API를 부를 확률이 **20배** 높다. v0·에이전트가 “앱을 더 자주 올리는” 쪽이 인프라 매출을 밀어 올린다.

## 돈이 흐르는 구조
**1) 입장권 = 플랜** — 가격 페이지 기준 Free는 $0에 일일 메시지 한도·배포·Design Mode·GitHub 동기화. 유료는 좌석당 **월 포함 크레딧**(Plus/Business 모두 유저당 **$30** 크레딧 + 로그인 시 일 **$2** 크레딧)과 팀 공유 추가 구매. Business는 **$100/유저/월**, 기본 학습 옵트아웃. Enterprise는 SSO·RBAC·우선 큐·SLA.
**2) 실제 소모 = 토큰→크레딧** — v0 Mini·Pro·Max·Max Fast별로 입력·캐시·출력 단가가 다르다(예: Mini 입력 $0.20/1M·출력 $1.20/1M, Max Fast 입력 $10/1M·출력 $50/1M). 프롬프트뿐 아니라 채팅 기록·소스·Vercel 지식도 입력 토큰으로 잡힌다.
**3) 풀스루 = 배포 클라우드** — v0는 Vercel 구독을 대체하지 않는다. 생성한 앱이 Hobby/Pro/Enterprise 인프라(빌드·대역폭·함수)를 쓰면 **마진이 다른 두 번째 매출**이 붙는다. Sacra는 v0를 “상품 클라우드 리셀보다 마진이 높은 소프트웨어(추론)”로 본다.

## 왜 중요한가 (ANDRSN·퍼스널 OS 관점)
- **Lovable·Replit·Cursor**와 겹치지만 포지션이 다르다. Lovable은 비개발자 비주얼, Cursor는 에디터 속 에이전트, v0는 **“생성된 UI가 바로 Vercel에 붙는”** 프론트 클라우드 락인이다.
- 리스크: 토큰 과금은 세션 비용을 예측하기 어렵고, Next.js·Vercel 스택 밖에서는 가치가 줄어든다. Sacra 수치·ARR은 **추정치**이지 감사 공시가 아니다.

출처: [v0 Pricing](https://v0.app/pricing) · [Sacra — Vercel](https://sacra.com/c/vercel/) · [Updated v0 pricing (블로그, 토큰 계량 전환)](https://vercel.com/blog/updated-v0-pricing)
