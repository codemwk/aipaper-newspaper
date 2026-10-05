---
title: "AI 비즈니스: Replit — 구독 위에 ‘에이전트 사용량’을 얹어 ARR $525M, 코딩 툴에서 ‘누구나 앱 만드는 공장’으로"
date: 2026-10-06T07:00:00+09:00
category: "AI 비즈니스"
slug: "replit-agent-usage-arr"
summary: "Sacra 추정 2026년 4월 연환산 매출 $525M(2025년 말 $300M). 3월 Series D $400M@$9B. Core $20·Pro $100/월 + 작업 난이도별 에이전트 과금(단순 실행 $0.06~). 사용자 5,000만+. 9/25 Atta 인수로 ‘채팅 속 인터랙티브 차트’, 10/2 GPT-6.1 Sol·Sonnet 5.5 모드 추가."
---

## 한줄 요약
[Replit](https://replit.com)은 원래 **브라우저 안의 코딩 환경**(설치 없이 열면 바로 코딩·배포)이었다. 2024년 9월 **Replit Agent**가 나오며 정체가 바뀌었다 — 말로 설명하면 앱을 만들고, 테스트하고, 배포까지 해 준다. 돈 버는 방식도 함께 바뀌었다: **월 구독 + 에이전트가 일한 만큼 내는 사용량 과금**. Sacra는 Replit의 연환산 매출이 **2026년 4월 $5.25억**(2025년 말 $3억)에 이르렀다고 추정한다([Sacra](https://sacra.com/c/replit/)).

## 돈이 흐르는 구조
- **구독(바닥)**: 무료 → **Core $20/월**(컴퓨트 한도 상향, 비공개 저장소, 협업자 5명, 월 크레딧 포함) → **Pro $100/월**(파워 유저·전문가용). 기존 $25 Core를 내리고 Pro를 신설, Teams 플랜은 폐지했다.
- **사용량(천장)**: 에이전트 작업은 **‘노력(effort) 기반’** 과금. 예전엔 체크포인트당 $0.25 정액이었지만 지금은 **단순 실행 $0.06부터, 복잡한 다단계 작업은 몇 달러**. 여기에 배포 오토스케일링·대역폭·DB 사용량이 클라우드처럼 붙는다.
- **마켓플레이스**: 사용자가 코딩 일을 걸고 Replit 화폐(Cycles)로 지불하는 Bounties에서 수수료.
- **자본**: 2025-09 $2.5억(@$30억) → **2026-03 Series D $4억(@$90억, Georgian 리드)**. 6개월 만에 기업가치 3배([Sacra](https://sacra.com/c/replit/)). 2025년 10월엔 ‘2026년 말 연환산 $10억’을 목표로 제시했다([Business Insider](https://www.businessinsider.com/replit-projects-1-billion-revenue-by-2027-ai-coding-boom-2025-10)).

## 누구에게 파나
- 사용자 **5,000만+**(2026-03), Fortune 500의 85%에서 사용자가 있다. 핵심 타깃은 개발자보다 **‘코드를 모르는 업무 담당자’** — 마케터·영업·PM이 사내 툴과 대시보드를 직접 만든다.
- 엔터프라이즈 쪽은 Snowflake·Databricks·BigQuery 커넥터, 160+ 외부 서비스 연동(OpenInt 인수), Google Cloud·Azure 마켓플레이스 판매로 ‘구매 절차’까지 들어간다.

## 최근 움직임 (지난 2주)
- **9/25 Atta 인수**(10/4 업데이트): 비즈니스 분석·차트 스타트업. 첫 기능은 **Replit 채팅 안의 인터랙티브 차트** — “이거 시각화해 줘”라고 하면 SQL 없이 워터폴·히트맵을 만든다. 목표로 ‘자율주행 회사(self-driving companies)’를 내걸었다([Replit Blog](https://replit.com/blog/replit-acquires-atta)).
- **10/2 릴리스**: Max Mode에 **GPT-6.1 Sol**, Power Mode에 **Claude Sonnet 5.5**, 분류·라우팅 같은 구조화 결정용 Jev 통합, 엔터프라이즈 워크스페이스 정책 화면([AI News Pro 정리](https://ainewspro.com/article/replit-jev-ai-integrations-model-update-2026)).

## 리스크: 매출보다 ‘마진’
Sacra에 따르면 2025년 Replit의 매출총이익률은 **36%에서 -14%까지** 출렁였다. 에이전트가 일할수록 LLM 비용이 나가기 때문이다. 정액 체크포인트에서 노력 기반 과금으로 바꾼 것도, 저렴한 모델 모드를 나눠 둔 것도 결국 **“토큰 원가를 고객 가격에 얼마나 정확히 연동하나”**의 문제다. Agent 4 iPhone 출시가 애플 심사로 4개월 막혔던 일도 플랫폼 의존 리스크를 보여 줬다.

## 왜 중요한가 (AiPaper·퍼스널 OS 관점)
Lovable·Gamma가 ‘좌석 구독’ 중심이었다면 Replit은 **“구독은 입장권, 실제 매출은 에이전트가 한 일의 양”**인 하이브리드의 대표 사례다. 퍼스널 OS 구독을 설계할 때도 ‘월 기본료 + 무거운 작업(리서치·영상·자동화)은 크레딧’ 구조가 가장 현실적인 레퍼런스이고, 동시에 **원가가 고객 사용량에 그대로 연동되는 위험**도 함께 들고 와야 한다는 교훈이다.

## 기억할 것
- 숫자는 대부분 **Sacra 추정치**(회사 공식 공시 아님). 2026년 말 $10억 목표의 달성 여부는 아직 미확인.
- [Sacra: Replit](https://sacra.com/c/replit/) · [Replit, Atta 인수](https://replit.com/blog/replit-acquires-atta) · [Business Insider 2025-10](https://www.businessinsider.com/replit-projects-1-billion-revenue-by-2027-ai-coding-boom-2025-10) · [10/2 업데이트 정리](https://ainewspro.com/article/replit-jev-ai-integrations-model-update-2026)
