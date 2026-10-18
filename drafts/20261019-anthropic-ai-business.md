---
title: "AI 비즈니스: Anthropic — 3분기 매출 168억 달러·조정 흑자, Pro 월 $20·Max $100부터·API 토큰 과금으로 번다, 그런데 성장률은 142%→45%로 꺾이고 Replit은 기본 모델을 바꿨다"
date: 2026-10-19T07:00:00+09:00
category: "AI 비즈니스"
slug: "anthropic-ai-business"
summary: "Anthropic(Claude): 투자자 설명회(10/14, FT·Reuters)에서 3분기 매출 $168억(2분기 $116억, 1분기 $47억), 조정 기준 흑자라고 밝힘. 상장은 11월 미국 중간선거 이후 유력, 목표 기업가치 $2조+. 다만 분기 성장률 142%→45% 둔화, SemiAnalysis는 연환산 추정치를 약 $740억으로 낮춤(서울경제 인용). 10/16 Replit이 기본 모델을 OpenAI로 전환(전 ‘상위 5위 고객’). 10/18 주식 5%로 ‘공익 펀드’ 신설. 요금: Free $0, Pro 월 $20(연 결제 $17), Max 월 $100부터, Enterprise 좌석당 $20+API 사용량. API: Opus 5.5 입력 $4/출력 $20, Sonnet 5.5 $2/$10, Fable 5.1 $10/$50(100만 토큰당)."
---

## 한줄 요약
이번 주 AI 업계에서 가장 큰 숫자는 모델 점수가 아니라 매출이었다. **Anthropic**은 상장 전 투자자 설명회(2026-10-14)에서 3분기 매출이 **168억 달러**로 2분기(116억)보다 45% 늘었고, **조정 기준으로 흑자**였다고 밝혔다([Reuters, 10/14](https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208)). 그런데 같은 주에 “성장이 느려졌다”는 논쟁과 큰 고객 이탈 소식, 그리고 주식 5%를 내놓는 ‘공익 펀드’ 발표가 잇따랐다.

## 누구에게 무엇을 파나
- **개인·전문가**: 채팅 앱 Claude와 코딩 에이전트 **Claude Code**. Pro 이상에는 Claude Code, Claude Science, Chrome·Microsoft 365 연동, 대시보드(베타)가 들어간다.
- **팀·기업**: Team(2~150명), Enterprise. SSO·감사 로그·데이터 보존 설정 같은 관리 기능이 핵심 상품이다.
- **개발자·플랫폼**: API(Claude Platform). Replit 같은 코딩 플랫폼, 사내 에이전트를 만드는 회사들이 **토큰 단위**로 산다.

## 돈 버는 구조: 구독 + 토큰
공식 요금표 기준([claude.com/pricing](https://claude.com/pricing), 10/19 확인):

| 상품 | 가격 |
|---|---|
| Free | $0 (Sonnet·Haiku, 프로젝트 5개까지) |
| Pro | 월 $20 (연 결제 시 월 $17, $200 선결제) |
| Max | 월 $100부터 (Pro의 5배 또는 20배 사용량, API 크레딧 월 $100~200 포함) |
| Enterprise | 좌석당 월 $20 + 사용량은 API 요금으로 별도 |
| API Opus 5.5 | 100만 토큰당 입력 $4 / 출력 $20 |
| API Sonnet 5.5 | 입력 $2 / 출력 $10 |
| API Fable 5.1 | 입력 $10 / 출력 $50 |

- 에이전트 실행 인프라도 따로 판다: **Managed Agents는 활성 세션 1시간당 $0.08**(토큰 별도), 코드 실행 컨테이너 시간당 $0.05.
- 핵심은 Enterprise 요금 구조다. 좌석료는 $20로 낮추고 **실제 쓴 만큼 API 요금을 받는다** — 에이전트가 많이 일할수록 매출이 커지는 설계.

## 숫자
- **분기 매출**: 1분기 $47억 → 2분기 $116억 → 3분기 $168억. 3분기 조정 흑자(설명회 참석자 인용, Reuters).
- **작년**: 2025년 매출 약 $46억(12배 성장), 영업손실 $80억 이상. 앞으로 10년간 클라우드·컴퓨팅에 최소 **$5,180억**을 약정했다(Reuters).
- **상장**: 11월 미국 중간선거 이후가 유력, 목표 기업가치 **$2조 이상**(Reuters). 분석가들은 연말 연환산 매출이 $1,100억에 이를 수 있다고 봤다.
- **둔화 논쟁**: 분기 증가액이 $68억 → $52억으로 줄며 성장률이 142% → 45%로 떨어졌다. 서울경제 AI PRISM은 FT 등을 인용해 Meta·Microsoft가 비용 때문에 자체·오픈 모델로 옮겼고, 증류 단속으로 매출의 5~7%를 차지하던 관련 수요가 줄었으며, SemiAnalysis가 연환산 매출 추정을 약 **$740억**으로 낮췄다고 전했다. 일부 투자자 사이에선 기업가치 $1.5조 이야기도 나온다([서울경제, 10/17](https://en.sedaily.com/society/2026/10/17/anthropic-posts-168-billion-in-q3-revenue-as-growth-slows)).
- **효율**: Anthropic 자체 보고서에 따르면 창업 5년 차 기준 **직원 1인당 매출이 같은 시기 Meta·Google의 2~4배**([Anthropic, 10/16](https://www.anthropic.com/research/employment-at-anthropic)).

## 이번 주의 두 사건
1. **Replit의 기본 모델 교체(10/16)**: CEO 암자드 마사드는 TechCrunch Disrupt 무대에서 “비용·파트너십·성능” 때문에 **OpenAI를 기본 모델로** 삼았다고 말했다. Replit은 최근까지 Anthropic의 **상위 5위 고객**이었다. Claude는 여전히 선택할 수 있지만 대부분 사용자는 기본값을 쓰므로 지출이 크게 줄 수 있다. Anthropic 쪽 관계자는 파트너십이 유지되고 있다고 반박했다([TechCrunch](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)).
2. **공익 펀드(10/18)**: 주식 **5%**를 회사 내 100% 자회사 형태의 펀드에 넣고, 기업가치가 50% 오를 때마다 2%를 더 넣을 수 있게 했다. 비영리 기부나 특정 계층 직접 지원 등에 쓸 수 있고, 운영 구조는 몇 달 안에 공개한다. AI가 일자리에 미치는 영향 연구에는 이미 2억 달러를 약정했다([TechCrunch](https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/)).

## 왜 중요한가
Anthropic의 공식은 **“모델 → 코딩 에이전트 → 토큰 사용량”**이다. 에이전트가 오래 일할수록 돈을 버는 구조라 성장이 빠르지만, 반대로 **큰 고객 몇 곳이 기본값을 바꾸면 매출이 바로 흔들린다**. Replit 사례가 보여 주듯 플랫폼 기업에게 모델은 ‘부품’이고, 부품은 가격과 성능으로 언제든 교체된다. ANDRSN 관점: AI를 내부 제작 시스템으로 쓰는 스튜디오라면 한 회사 모델에 작업 흐름을 묶지 말고 **모델을 갈아 끼울 수 있는 구조**로 짜는 게 비용 협상력이다. 모든 매출 수치는 설명회 참석자 전언과 언론 보도이며 회사 공식 공시는 아니다.

출처: [Reuters — Anthropic 3분기 매출 $168억 (10/14)](https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208) · [서울경제 AI PRISM — 성장 둔화 논쟁 (10/17)](https://en.sedaily.com/society/2026/10/17/anthropic-posts-168-billion-in-q3-revenue-as-growth-slows) · [TechCrunch — Replit, OpenAI를 기본값으로 (10/17)](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/) · [TechCrunch — 주식 5% 공익 펀드 (10/18)](https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/) · [Claude 요금표](https://claude.com/pricing)
