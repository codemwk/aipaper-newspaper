---
title: "AI 트레이딩: IBKR Connector 1.2.0 ‘저장한 스크리너를 채팅에서 실행’ + YC 스타트업 Instinct ‘1인 투자회사’용 에이전트 — 검색은 열리고, 실행은 아직 조심스럽다"
date: 2026-10-15T07:09:00+09:00
category: "AI 트레이딩"
slug: "ibkr-screeners-instinct"
summary: "Interactive Brokers(10/14) IBKR Connector 1.2.0: 연결된 AI(ChatGPT·Claude·Grok·Claude Code·Cursor 등)에서 저장해 둔 스크리너를 이름으로 불러 실행, 기본 상위 10개·최대 50개 순위 목록과 Client Portal 딥링크. AI가 스크리너를 직접 만드는 기능은 예고. 같은 날 YC W26 Instinct는 시장·뉴스·소셜을 24시간 감시하는 에이전트 플랫폼을 대기자 명단으로 공개 — 실제 성능·수익은 미검증."
---

## 한줄 요약
AI와 증권 계좌의 연결이 “잔고 조회”를 지나 **“내 종목 발굴 규칙을 AI가 돌리는”** 단계로 들어섰다. Interactive Brokers는 MCP 커넥터에 **저장된 스크리너 실행**을 붙였고, 같은 날 YC 스타트업 **Instinct**는 개인을 “포트폴리오 매니저”로, 에이전트를 “투자회사 직원”으로 놓는 플랫폼을 공개했다.

## IBKR Connector 1.2.0 — 무엇이 되나
- **이름으로 스크리너 호출**: “내 ‘저PBR 반도체’ 스크리너 돌려줘”라고 하면 AI가 그 스크리너의 **조건(파라미터)을 먼저 보여 주고** 결과를 채팅에 반환([FX News Group](https://fxnewsgroup.com/forex-news/platforms/ibkr-connector-enables-running-of-saved-screeners-through-ai/)).
- **결과 형식**: 순위·티커·회사명 목록, 기본 **상위 10개**, 요청 시 **최대 50개**. 각 결과에 **Client Portal 딥링크** — 원본 데이터 확인은 증권사 화면에서.
- **다음 단계(예고)**: 자연어로 설명하면 **AI가 스크리너를 만들어 저장·수정·삭제**.
- **연결 범위**: ChatGPT·Claude·Grok 공식 커넥터 외에 Claude Code·Cursor·ChatGPT Workspaces 등 **MCP 지원 도구 전반**. (AiPaper 9/20 기사에서 다룬 ‘임의 MCP 클라이언트 개방’의 후속 기능.)

## Instinct — ‘1인 투자회사’ 피치
- **누구**: YC **Winter 2026**, 창업자 **Joon Won Song**(CEO, 전 Squarepoint Capital 퀀트 개발자)·**Eunju Moon**(CTO, USC 양자컴퓨팅 박사과정 중퇴), 팀 5명, 샌프란시스코([YC](https://www.ycombinator.com/companies/instinct-xyz)).
- **무엇**: 수천 개 시장을 **24시간 감시·조사**하는 에이전트 팀. 고래 포지션 추적, 한국 소셜 트렌드 같은 신호, 차트 시각화, “세계관을 트레이드로 구성”(예: 인텔 롱 + S&P 헤지 + 50일선 이탈 시 청산 조건)([instinct.xyz](https://instinct.xyz/)).
- **소셜 레이어**: 트레이드를 공유하고 팔로워가 **원탭 카피**. 사이트에 레버리지 상품별 앱 수수료 표기가 함께 보인다.
- **상태**: 10/14 발표, **대기자 명단(얼리 액세스)**. RuntimeWire는 “공개 자료로는 실제 기능과 투자 성과가 검증되지 않았다”고 짚었다([RuntimeWire](https://runtimewire.com/article/instinct-ai-trading-agents-launch)).

## 왜 중요한가
두 소식은 같은 방향의 다른 끝이다. IBKR은 **사람이 만든 규칙(스크리너)을 AI가 실행**하게 하고 결과 검증은 증권사 화면으로 돌려보낸다 — 보수적이고 감사 가능한 설계. Instinct는 **AI가 기회를 찾고 사람은 판단만** 하는 반대편을 판다. 자동매매를 설계한다면 지금 현실적인 조합은 “규칙은 내가 쓰고(스크리너·조건), 탐색·요약은 AI가, 주문은 증권사 화면에서 사람이”다. ‘$10억을 굴리는 첫 1인 투자회사가 2년 안에 나온다’(YC 소개문) 같은 문장은 **비전이지 실적이 아니다**. 레버리지·카피트레이딩 결합은 손실도 복제된다는 점을 잊지 말 것.

출처: [FX News Group: IBKR Connector 1.2.0](https://fxnewsgroup.com/forex-news/platforms/ibkr-connector-enables-running-of-saved-screeners-through-ai/) · [Instinct (YC)](https://www.ycombinator.com/companies/instinct-xyz) · [instinct.xyz](https://instinct.xyz/) · [RuntimeWire](https://runtimewire.com/article/instinct-ai-trading-agents-launch)
