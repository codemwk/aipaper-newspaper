---
title: "AI 도구: ‘먼저 말 거는’ 에이전트 Claude Duet, 그리고 비밀번호를 보여 주지 않고 로그인시키는 1Password for Agents — 개인 에이전트의 ‘신뢰 장치’가 나온 주"
date: 2026-10-24T07:08:00+09:00
category: "AI 도구"
slug: "claude-duet-1password-agents"
summary: "Anthropic이 10/22 Claude Duet 연구 프리뷰(미국 Pro·Max, 대기자 명단; iOS·Android·claude.ai). 매일 아침 브리핑, 몇 시간마다 연결 앱 확인, 자체 가상 머신·브라우저로 사용자가 자리를 비워도 작업. 메시지 전송·결제·서명·삭제 전엔 반드시 승인, 증권 매매·계좌 간 송금은 승인해도 금지. Claude Opus 5.5 기반, 6,000개 이상 커넥터. 같은 날 1Password for Agents: 에이전트가 로그인 화면에서 특정 계정을 요청하면 사용자가 승인하고 1Password가 직접 채워 넣어 에이전트는 비밀번호·OTP를 보지 못함. Muse·Grok Bot 먼저, Claude Duet·ChatGPT Work·Townie는 곧. Individual·Family 추가 비용 없음."
---

## 한줄 요약
‘내 일을 대신하는 개인 에이전트’ 경쟁에 Anthropic이 **Claude Duet**으로 들어왔고, 같은 날 1Password가 그 에이전트들에게 **비밀번호를 보여 주지 않고 로그인시키는** 장치를 내놨다. 둘 다 결국 **“어디까지 맡길 수 있나”**에 대한 답이다.

## Claude Duet: 먼저 다가오는 에이전트
- **대상**: 전문직·소상공인. 미국 Pro·Max 대기자 명단부터, iOS·Android·claude.ai, 플랜 사용량 공유([Anthropic](https://claude.com/resources/articles/claude-duet))
- **하는 일**: 매일 아침 연결 앱 요약 브리핑 → 몇 시간마다 확인하고 **필요할 때만** 메시지. 일정 잡기부터 대시보드·매출 예측·웹앱 시제품까지
- **자리를 비워도**: 자체 **가상 머신 + 브라우저**에서 작업, 휴대폰·노트북을 켜 둘 필요 없음
- **연결**: Claude Marketplace의 6,000개 이상 커넥터(Gmail·Slack·QuickBooks·Stripe·Gusto·Docusign·HubSpot·Canva·Shopify 등). 구매는 Stripe Link 가상카드·Shop Pay로, 승인 후
- **경계선**: 메시지 전송·결제·서명·삭제 전엔 **무엇을 할지 보여 주고 승인 대기**. **증권 매매·계좌 간 송금은 승인해도 불가**. 카드번호·신분증 번호 유출을 막는 전용 분류기 추가
- **솔직한 한계**: 아직 스레드를 잘못 읽거나 급한 일을 잘못 판단할 수 있고, 개인 용무(티켓 예매 등)는 약하다고 회사가 직접 적었다

## 1Password for Agents: 비밀번호는 에이전트 눈에 안 보이게
- 에이전트가 로그인 화면에서 멈추면 **특정 계정 하나**를 요청 → 사용자가 1Password에서 승인 → **1Password가 사이트에 직접 자동 입력**. 에이전트는 비밀번호·OTP를 보지 못하고, 금고 전체에도 접근 못 함([1Password 블로그](https://1password.com/blog/1password-for-ai-agents))
- **연동**: Meta Muse·Grok Bot은 며칠 안에, Claude Duet·ChatGPT Work·dots·Town Townie는 곧. Browserbase·Browser Use·Perplexity·Ramp 등도 예정
- **가격**: 1Password.com의 Individual·Family 계정에 **추가 비용 없음**(.eu·.ca 계정은 아직 미지원)

## 왜 중요한가
지난 몇 주 개인 에이전트의 걸림돌은 성능이 아니라 **로그인과 승인**이었다. 비밀번호를 프롬프트에 붙여 넣거나, 매번 사람이 손으로 들어가 로그인하거나. 이번 주에 ‘승인 카드 + 대리 입력 + 금지 목록’이라는 **신뢰 3종 세트**가 업계 기본값으로 굳어지는 모습이다. 쓰는 쪽 체크리스트: **어떤 행동이 승인 대상인지, 무엇이 아예 금지인지**를 먼저 확인할 것.

출처: [Anthropic — Introducing Claude Duet (10/22)](https://claude.com/resources/articles/claude-duet) · [1Password — Introducing 1Password for Agents (10/22)](https://1password.com/blog/1password-for-ai-agents) · [TechCrunch — 1Password (10/22)](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/)
