---
title: "AI 비즈니스: Infisical — 에이전트에게 ‘진짜 열쇠’ 대신 ‘가짜 열쇠’를 쥐여 주는 회사. 오픈소스로 개발자 30만 명을 모으고, 돈은 ‘사람 수’와 ‘대신 열어 준 요청 수’로 받는다. 기업가치 6억 달러"
date: 2026-10-28T07:00:00+09:00
category: "AI 비즈니스"
slug: "infisical-ai-business"
summary: "비밀번호·API 키 관리 오픈소스로 출발한 Infisical이 10/27 시리즈 B 4,000만 달러(기업가치 6억 달러, Elad Gil 주도)를 유치. 고객사 1,300곳+, 개발자 30만 명, 하루 100억 건의 비밀값을 지킨다. 회사는 ‘오래전부터 흑자 현금흐름’이라 돈이 급하지 않았지만, AI 에이전트가 사내 시스템에 접근하는 시대를 겨냥해 ‘Agent Vault’에 집중하려고 투자를 받았다고 설명. 핵심 오픈소스는 MIT로 무료, 돈은 제품별로 받는다: 비밀 관리는 ID당 월 $20~40, Agent Vault는 매달 5,000건 무료 후 1,000건당 $2."
---

## 한줄 요약
AI 에이전트가 일을 하려면 GitHub·결제·클라우드에 들어갈 **열쇠(API 키·비밀번호)**가 필요하다. 그런데 에이전트는 이상한 지시문(프롬프트 인젝션)에 속아 열쇠를 밖으로 흘릴 수 있다. Infisical은 **에이전트에게는 가짜 열쇠만 주고, 진짜 열쇠는 중간 관문이 대신 끼워 주는** 방식을 판다([Infisical 발표](https://infisical.com/blog/series-b)).

## 누구에게 무엇을 파나
- **고객**: 개발팀과 보안팀. 1,300곳+ 조직, 개발자 30만 명. 공개 고객은 Airbus, Volkswagen, Hugging Face, OpenRouter, Wise, Clay, LG, First American Financial, 미국 정부 등([PR Newswire](https://www.prnewswire.com/news-releases/infisical-raises-40-million-at-600-million-valuation-to-secure-the-ai-agent-economy-302920994.html)).
- **제품 4종**: ① 비밀값 관리(키·비밀번호를 한곳에 보관·교체) ② 인증서 관리 ③ 특권 접근 관리(PAM: 서버 접속 승인·녹화) ④ **Agent Vault**(에이전트 전용).
- **Agent Vault 작동 방식**([문서](https://docs.agent-vault.dev/)):
  1. 에이전트에게는 `__github_pat__` 같은 **가짜 값**만 준다.
  2. 에이전트의 모든 인터넷 요청은 Agent Vault라는 **중간 관문(프록시)**을 지난다.
  3. 관문이 목적지(GitHub, Stripe, Anthropic API 등)를 확인하고, 규칙에 맞으면 **나가는 순간에만 진짜 키로 바꿔 끼운다.**
  - 그래서 에이전트가 속아서 “키를 알려 줘”라는 요청에 응해도, 손에 든 건 가짜다. Claude Code·Cursor·Codex·OpenClaw·Hermes Agent 연결 안내가 있다.
  - 참고: 처음 별도 오픈소스로 냈던 ‘단독판 Agent Vault’는 더 이상 관리하지 않고, Infisical 본체(역시 오픈소스·자체 설치 가능)로 합쳐졌다.

## 돈 버는 구조
핵심 코드는 **MIT 라이선스로 무료**, 직접 설치하면 공짜. 클라우드·고급 기능·기업 지원에서 돈을 번다. 제품마다 **과금 단위가 다르다**는 점이 흥미롭다([가격표](https://infisical.com/pricing)).

| 제품 | 과금 단위 | 가격 |
|---|---|---|
| 비밀값 관리 | ID(사람 + 기계 계정) | 무료 5개 / Pro $20 / Advanced $40 (연간, 월 결제는 $23·$46) / Enterprise 견적 |
| 특권 접근(PAM) | 사람 1명 | Pro 월 $20 / Enterprise 견적 |
| 인증서 관리 | 단위 과금 없음 | 무료 / Enterprise 견적 |
| **Agent Vault** | **대신 열쇠를 끼워 준 요청 1건** | 매달 5,000건 무료, 이후 **1,000건당 $2** |

- 즉 사람에게는 ‘좌석’, 에이전트에게는 **‘사용량’**으로 받는다. 에이전트가 많이 일할수록 매출이 따라 늘어나는 구조다.
- 기업용 상위 플랜은 SSO·SCIM, 감사 로그를 외부 보안 시스템(SIEM)으로 보내기, 기록 보관 기간 조절 같은 **‘관리·감사’ 기능**으로 차별화한다.

## 숫자
| 항목 | 내용 |
|---|---|
| 이번 투자 | 시리즈 B $4,000만, 기업가치 $6억 (10/27) |
| 투자자 | Elad Gil 주도(시리즈 A에 이어), Y Combinator·Gradient 추가 참여, Gallery·Pace·Dynamic Capital 등 |
| 재무 | “오래전부터 현금흐름 흑자, 지금까지 투자받은 돈보다 은행 잔고가 많다”(CEO, 회사 블로그) |
| 규모 | 하루 100억 건 비밀값 보호, 오픈소스 GitHub 별 3만 개+(확인 시점 30,032개) |
| 채용 | 100개+ 직무 |

## 왜 중요한가
- **‘에이전트도 직원처럼 권한을 나눈다’가 제품이 됐다.** CEO 블라드 마치야코: “직원에게 회사 모든 시스템 권한을 주지 않듯, 에이전트도 마찬가지여야 한다.” 투자자 Elad Gil은 에이전트를 “기업 안의 새로운 사용자 집단”이라고 불렀다.
- **오픈소스 → 기업 매출의 정석 경로.** 무료 설치판으로 개발자를 먼저 모으고, 회사가 커지면 감사·SSO·지원이 필요해져 유료로 올라오는 구조다. 흑자인데도 투자를 받은 이유가 ‘에이전트 시장 선점’이라는 점이 시장의 방향을 보여 준다.
- **개인에게도 같은 교훈.** 증권사 APP SECRET이나 MT5 계정, 각종 API 키를 에이전트 설정 파일에 그대로 넣는 대신 **“에이전트는 가짜 값, 실제 키는 별도 관문”** 구조를 쓰면 키가 새도 피해가 줄어든다. 꼭 이 제품이 아니어도 설계 원칙으로 기억해 둘 만하다.

출처: [Infisical 시리즈 B 블로그 (10/27)](https://infisical.com/blog/series-b) · [PR Newswire 발표 (10/27)](https://www.prnewswire.com/news-releases/infisical-raises-40-million-at-600-million-valuation-to-secure-the-ai-agent-economy-302920994.html) · [Infisical 가격표](https://infisical.com/pricing) · [Agent Vault 문서](https://docs.agent-vault.dev/) · [Axios Pro Rata (10/27)](https://www.axios.com/pro/all-deals/2026/10/27/pro-rata-premium-first-look-infisical-intel-radnet)
