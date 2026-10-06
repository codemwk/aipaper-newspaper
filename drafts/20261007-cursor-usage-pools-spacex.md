---
title: "AI 비즈니스: Cursor — Sacra 추정 연환산 매출 $40억, ‘두 개의 사용량 통’으로 자사 모델에 마진을 싣는 코딩 에이전트"
date: 2026-10-07T07:11:00+09:00
category: "AI 비즈니스"
slug: "cursor-usage-pools-spacex"
summary: "Sacra 추정 2026년 5월 연환산 매출 $4B(2025년 말 $1.2B), 매출의 약 60%가 대기업. SpaceX가 6/16 발표·8/14 종결한 $600억 전액 주식 인수. 요금은 Pro $20·Pro Plus $60·Ultra $200, Teams $40/$120. 자사 모델(Grok 4.x·Composer 2.5) 통은 넉넉히, 타사 모델은 API 원가+팀 플랜엔 $0.25/M ‘Cursor Token Rate’."
---

## 한줄 요약
[Cursor](https://cursor.com)는 VS Code를 바탕으로 만든 **AI 코딩 에디터**에서 출발해, 지금은 여러 에이전트를 동시에 돌리고 클라우드·모바일·Slack에서 일을 맡기는 **“코딩 에이전트 지휘소”**가 됐다. Sacra는 Cursor의 연환산 매출이 **2026년 5월 $40억**(2025년 말 $12억)에 이르렀다고 **추정**한다([Sacra](https://sacra.com/c/cursor/)). 그리고 8월, 이 회사는 **SpaceX의 자회사**가 됐다.

## 돈이 흐르는 구조
**1) 구독 = 입장권 + 포함 사용량** ([요금 문서](https://cursor.com/docs/models-and-pricing))
- 개인: **Pro $20 / Pro Plus $60 / Ultra $200**(월). 인도 전용 **Start ₹649**.
- 팀: **Teams Standard $40 / Premium $120**(1인당 월, Premium은 에이전트 한도 5배), 그 위에 맞춤형 Enterprise.
- 공식 가이드의 ‘현실 비용’: 매일 에이전트를 쓰면 **월 $60~100**, 여러 에이전트·자동화를 돌리는 파워 유저는 **$200+**.

**2) 사용량 = 두 개의 통** — 이게 이 회사 비즈니스 모델의 핵심이다.
- **Cursor Models 통**: Cursor와 SpaceXAI가 함께 학습한 **Grok 4.7/4.6/4.5**와 자체 **Composer 2.5**. “훨씬 많은 포함 사용량”을 준다. Composer 2.5는 입력 $0.50·출력 $2.50/M.
- **Other Models 통**: Claude·GPT·Gemini 등 타사 모델은 **해당 모델 API 가격 그대로** 차감, 넘치면 같은 단가로 종량 과금.
- **Cursor Token Rate**: Teams·Enterprise에서 타사 모델을 쓰면(자동 라우팅 포함, BYOK도) **100만 토큰당 $0.25**를 얹는다. **자사 모델은 면제**.

즉, 사용자는 모델을 자유롭게 고를 수 있지만 **가격 설계가 자사 모델 쪽으로 기울어 있다**. 남의 모델은 원가 전달 + 통행료, 내 모델은 넉넉한 포함량 — 마진이 남는 곳으로 트래픽을 유도하는 구조다.

## 왜 이렇게 바꿨나: 마진
Sacra에 따르면 Cursor는 2026년 4월에야 **매출총이익이 간신히 흑자**로 돌아섰다. 동력은 **자체 Composer 모델 사용 증가와 저렴한 모델 라우팅**. 대기업 계정은 흑자지만 **개인 개발자 계정은 여전히 적자**다. 매출의 약 **60%가 대기업**, 엔지니어링 팀 5만 곳 이상, Fortune 1000의 약 70%가 고객 명단에 있다. 회사는 2026년 말 **연환산 $60억+**를 전망했다(Sacra).

## SpaceX 인수 — 모델 공급망을 산 것
- 6월 16일 발표, **8월 14일 종결된 $600억 전액 주식 거래**. Anysphere 주식은 SpaceX 클래스 A 약 **3억 8,930만 주**로 바뀌었다. 4월에 SpaceX가 “$600억 인수 또는 $100억 협력” 중 고를 수 있는 옵션을 확보해 뒀다가 **인수를 택한** 것([The Index Today](https://theindextoday.com/spacex-closes-60-billion-purchase-of-cursor-maker-anysphere-its-biggest-bet-yet-on-ai/)).
- 의미: Cursor 최대의 리스크는 “모델을 남(OpenAI·Anthropic·Google)에게서 사 온다”는 점이었다. 이제 xAI의 Colossus 인프라에서 학습한 **공동 모델(Grok 4.x)**이 생겼고, 그게 바로 위의 ‘Cursor Models 통’이다.

## 왜 중요한가 (AiPaper·퍼스널 OS 관점)
Replit이 “구독 + 노력 기반 과금”이었다면, Cursor는 한 단계 더 나가 **“어떤 엔진을 쓰느냐에 따라 가격표가 달라지는”** 구조다. 퍼스널 OS 구독을 설계한다면 교훈은 분명하다 — **기본 엔진(싸고 내 마진이 남는 모델)은 넉넉히 포함, 프리미엄 엔진은 원가 전달**. 다만 위험도 함께 온다: 사용자가 “내 도구가 특정 모델 쪽으로 기운다”고 느끼는 순간 신뢰가 깎인다. 인수 후 Cursor 경쟁사들이 인재·기업 고객을 노리고 있다는 보도도 같은 맥락이다.

## 기억할 것
- 매출·마진·고객 수치는 **Sacra 추정**(회사 공시 아님). 인수 조건은 언론 보도 기준.
- [Sacra: Cursor](https://sacra.com/c/cursor/) · [Cursor 모델·요금 문서](https://cursor.com/docs/models-and-pricing) · [SpaceX 인수 종결 보도](https://theindextoday.com/spacex-closes-60-billion-purchase-of-cursor-maker-anysphere-its-biggest-bet-yet-on-ai/)
