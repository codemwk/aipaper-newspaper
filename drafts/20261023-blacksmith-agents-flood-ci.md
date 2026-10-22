---
title: "AI 도구: 코딩 에이전트가 ‘테스트 서버’를 터뜨리고 있다 — CI 작업 주 500만→9,000만 건, Blacksmith가 창업 2년 만에 유니콘($6,600만 시리즈 C)"
date: 2026-10-23T07:10:00+09:00
category: "AI 도구"
slug: "blacksmith-agents-flood-ci"
summary: "Sequoia가 10/21 CI(코드 자동 빌드·테스트) 인프라 스타트업 Blacksmith의 $6,600만 시리즈 C를 주도, 기업가치 $10억(8월 공개된 시리즈 B $5억 5,000만의 약 2배). 누적 $1억 2,500만. CI 작업량 2026년 1월 주 500만 건 → 10월 9,000만 건 이상, ARR 17배. 이유: 사람은 하루 PR 3~4개지만 에이전트는 ‘제출→CI 확인→실패 진단→수정→재제출’ 루프로 작업당 10~20회 CI를 돌린다(TechTimes 분석). GitHub Actions 대비 2배 빠르고 최대 60% 저렴하다는 주장(LangChain 실사용 약 40% 절감), 워크플로 파일 한 줄 변경으로 이전, 고객 1만 곳 이상(Mercury·Granola·Supabase 등). 실패한 검사를 고치는 에이전트 Codesmith도 운영."
---

## 한줄 요약
AI 코딩 에이전트가 코드를 빨리 쓰는 건 다 안다. 덜 알려진 부작용은 **그 코드를 검사하는 서버**가 감당을 못 한다는 것이다. 이 병목을 파는 회사 **Blacksmith**가 10/21 Sequoia 주도 **$6,600만 시리즈 C, 기업가치 $10억**을 발표했다([TechTimes](https://www.techtimes.com/articles/329367/20261022/sequoia-backed-blacksmith-raises-66m-1b-fix-ci-broken-ai-coding-agents.htm), [TechStartups 10/22 펀딩 정리](https://techstartups.com/2026/10/22/startup-funding-news-today-october-22-2026-flapping-airplanes-legora-mach9-peak-energy-whop-more/)).

## CI가 뭐고, 왜 터지나 (쉽게)
- **CI(지속적 통합)**: 코드를 합칠 때마다 서버가 자동으로 빌드하고 테스트를 돌려 “깨진 게 없나” 확인하는 절차.
- 사람 개발자는 하루 PR(변경 요청) 3~4개 정도라 부하가 예측 가능했다.
- 에이전트는 **“코드 제출 → CI 결과 읽기 → 실패 원인 분석 → 수정 → 재제출”** 을 반복한다. 작업 하나에 CI가 **10~20번** 돌 수 있다. 에이전트가 더 오래 혼자 일할수록 CI 비용은 더 커진다.

## 숫자
- Blacksmith의 CI 작업량: 2026년 1월 **주 500만 건 → 10월 9,000만 건 이상**(18배), 같은 기간 ARR 17배.
- 회사가 인용한 수치: Anthropic 내부 CI는 Claude Code가 뜬 뒤 6개월 동안 25배 증가.
- 기사 인용 GitHub 데이터: 에이전트가 연 PR이 약 400만(2025년 9월) → 1,700만 이상(2026년 3월).
- 고객 1만 곳 이상(2025년 9월 약 800곳): Mercury, Granola, Handshake, LangChain, Supabase 등.

## 무엇으로 빨라지나
- 서버용 대신 **고클럭 데스크톱 CPU**(AMD Ryzen 7950X) — 빌드·테스트는 대부분 단일 코어 속도가 좌우.
- 캐시를 **같은 기계의 NVMe SSD**에 — CI 시간의 30~50%가 의존성·도커 이미지 캐시 읽고 쓰기.
- 작업마다 새 **Firecracker 마이크로VM**(약 5ms 부팅)으로 격리 — CI 서버엔 토큰·비밀 키가 많아 보안이 중요.
- 주장: GitHub 기본 러너보다 **2배 빠르고 최대 60% 저렴**. LangChain 엔지니어는 실사용 **약 40% 절감**이라고 했다(작업 유형에 따라 차이). 이전은 GitHub Actions 워크플로 파일 **한 줄 변경**.
- 실패한 검사를 자동으로 고치는 에이전트 **Codesmith**도 운영 — 에이전트가 만든 코드를 에이전트가 고치는 닫힌 루프.

## 왜 중요한가
AI 개발 비용 하면 다들 모델 API 요금을 떠올리지만, 앞으로는 **검증(테스트) 인프라**가 더 큰 항목이 될 수 있다는 신호다. 혼자 에이전트로 앱을 만드는 사람에게도 교훈은 같다: 에이전트에게 “CI 통과할 때까지 반복해”라고 맡길 땐 **반복 횟수·시간 상한**을 함께 주자. 10/21에 다룬 Daytona(에이전트용 샌드박스)와 함께 ‘에이전트용 인프라’ 붐의 한 축이다.

출처: [TechTimes (10/22)](https://www.techtimes.com/articles/329367/20261022/sequoia-backed-blacksmith-raises-66m-1b-fix-ci-broken-ai-coding-agents.htm) · [TechStartups — 10/22 펀딩 뉴스](https://techstartups.com/2026/10/22/startup-funding-news-today-october-22-2026-flapping-airplanes-legora-mach9-peak-energy-whop-more/)
