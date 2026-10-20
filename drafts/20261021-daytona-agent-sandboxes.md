---
title: "AI 도구: Daytona, 6,000만 달러 유치로 기업가치 10억 달러 — OpenAI·Anthropic이 쓰는 ‘에이전트용 컴퓨터’, 1~9월 매출 런레이트 25배"
date: 2026-10-21T07:09:00+09:00
category: "AI 도구"
slug: "daytona-agent-sandboxes"
summary: "AI 에이전트가 코드를 실행·테스트하는 격리된 실행 환경(샌드박스)을 제공하는 Daytona가 10/20 시리즈 B $6,000만, 기업가치 $10억(누적 $9,100만). FirstMark 주도, Stripe 패트릭 콜리슨·Shopify 토비 뤼트케·Perplexity 아라빈드 스리니바스·Zoom 에릭 위안·Quora 애덤 디안젤로·Datadog 올리비에 포멜 등 개인 투자, Qualcomm Ventures·Samsung Next·Okta Ventures 참여. 고객으로 OpenAI·Anthropic·NVIDIA·Meta 거명. 매출 런레이트 1~9월 25배, 월평균 50.9% 성장(CEO, Fortune 인터뷰) — 절대 매출은 비공개."
---

## 한줄 요약
에이전트가 ‘말’에서 ‘일’로 넘어가면 **자기만의 컴퓨터**가 필요하다. 코드를 돌리고, 패키지를 설치하고, 실패하면 버리고 다시 시작할 격리된 방. 그 방을 빌려주는 **Daytona**가 2026-10-20 **$6,000만**(시리즈 B)을 유치해 **기업가치 $10억**이 됐다([Tech Startups](https://techstartups.com/2026/10/20/daytona-raises-60m-at-1b-valuation-to-provide-ai-agent-infrastructure-to-openai-anthropic-and-others/)).

## 숫자
- **투자**: $6,000만, 누적 **$9,100만**. **FirstMark** 주도.
- **개인 투자자 명단**: Stripe 패트릭 콜리슨, Shopify 토비 뤼트케, Perplexity 아라빈드 스리니바스, Zoom 에릭 위안, Quora 애덤 디안젤로, Mercor 브렌던 푸디, Datadog 올리비에 포멜. 기관으로 Qualcomm Ventures·Samsung Next·Okta Ventures.
- **고객**: OpenAI, Anthropic, NVIDIA, Meta 등 주요 AI 회사들이 쓴다고 밝혔다.
- **성장**: 매출 런레이트가 **1월→9월 25배**, CEO 이반 부라진은 Fortune에 **월평균 50.9%** 성장이라고 말했다. 다만 **절대 매출은 공개하지 않아** 실제 규모는 알 수 없다.

## 무엇을 파나
에이전트가 코드를 실행하는 **샌드박스**(격리 실행 환경)다. 사람 개발자의 노트북 대신, 에이전트 수백~수천 개가 각자 띄우고 지우는 **일회용 컴퓨터**를 클라우드에서 빠르게 공급하는 것이 핵심 사업이다. 회사는 이것이 ‘대화형 AI를 넘어선’ 새로운 클라우드 범주가 될 것이라고 본다.

## 왜 중요한가
이번 주만 봐도 같은 그림이 반복된다. 10/16 Modal은 샌드박스 런레이트만 $3억이라고 했고(AI 비즈니스 기사), 10/20 orca는 에이전트마다 작업 폴더를 따로 주는 관제실이었다. **에이전트를 여러 개 돌리는 시대의 병목은 모델이 아니라 ‘안전하게 실행할 공간’**이다. 
개인에게 주는 교훈은 단순하다: 에이전트에게 내 메인 컴퓨터 전체 권한을 주기 전에 **격리된 공간(컨테이너·worktree·클라우드 샌드박스)**부터 마련하자. 오늘 Claude Code 기사의 ‘작업 브랜치 삭제 버그’도 같은 이유로 격리가 중요하다는 사례다.

출처: [Tech Startups — Daytona raises $60M at $1B valuation (10/20)](https://techstartups.com/2026/10/20/daytona-raises-60m-at-1b-valuation-to-provide-ai-agent-infrastructure-to-openai-anthropic-and-others/)
