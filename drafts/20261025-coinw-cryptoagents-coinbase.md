---
title: "AI 트레이딩: CoinW ‘CryptoAgents’ — AI 13명이 강세·약세로 토론해 3~5분 만에 리포트, ‘이 분석이 틀리는 조건’까지 적는다. 같은 주 Coinbase는 “에이전트에게 문을 열었다”"
date: 2026-10-25T07:08:00+09:00
category: "AI 트레이딩"
slug: "coinw-cryptoagents-coinbase"
summary: "거래소 CoinW가 10/23 CryptoAgents를 출시. 종목만 고르면 AI 전문가 13명이 데이터 분석→강세 vs 약세 토론→전략 작성→리스크 검토→사후 검토를 거쳐 3~5분 안에 신뢰도 점수·무효화 조건·근거 출처(수집 시각 포함)가 달린 리포트를 낸다. BTC·ETH·SOL과 일부 미국 주식·ETF·금·은·원유 지원. 주문 실행이 아닌 리서치 도구. 같은 주 Coinbase는 10/22 MCP로 ChatGPT·Claude 등이 코인·주식·파생 매매를 하도록 열었지만, 별도 포트폴리오에 잃어도 되는 돈만 넣으라고 권고."
---

## 한줄 요약
오픈소스 **TradingAgents**가 보여 준 ‘AI 투자위원회’ 구조가 거래소 제품이 됐다. CoinW의 **CryptoAgents**는 AI 13명이 서로 반대편에서 토론하고, 결론에 **“이게 틀리는 조건”**을 붙인다([CoinW 공지, 10/23](https://www.coinw.com/help-center/announcement-center/product-updates/productupdates/2026-10-23/coinw-cryptoagents-is-now-live-13-ai-experts-come-together-for-your-research-ses/8170)).

## CryptoAgents가 하는 일
1. 종목 선택(프롬프트 불필요, 버튼 하나)
2. 데이터 분석 → **강세 분석가 vs 약세 분석가 토론** → 매매 전략 작성 → **리스크 검토** → 사후 검토
3. 3~5분 뒤 리포트: **신뢰도 점수**, **무효화 조건**(무엇이 이 분석을 약하게/뒤집게 하나), 전문가별 분석·데이터 출처·**수집 시각**까지 추적 가능

지원 자산: BTC·ETH·SOL 등 주요 코인, 일부 미국 주식·ETF, 금·은·원유. **주문을 대신 넣는 기능은 공지에 없다** — 리서치 도구다.

## 같은 주, Coinbase는 실행 쪽 문을 열었다
- 10/22 “Coinbase is open for AI agents”: MCP 서버(agents.coinbase.com/mcp)를 연결하면 ChatGPT·Claude·Claude Code·Codex CLI·Perplexity Computer 등이 **코인·미국 주식·파생상품**을 대화로 매매.
- 안전장치: 에이전트가 접근할 **포트폴리오를 직접 선택**, 실행 전 **주문 미리보기**, 언제든 연결 해제.
- 그래도 회사 권고는 **“별도 포트폴리오를 만들고, 잃어도 되는 돈만 넣어라.”** “조금만 사 줘”의 ‘조금’을 AI가 해석하는 위험, 숨은 문장으로 에이전트를 조종하는 **프롬프트 인젝션** 위험은 사용자 몫이다([24/7 Wall St. via Yahoo](https://finance.yahoo.com/markets/crypto/articles/coinbase-now-lets-ai-agents-175721525.html)).

## 왜 중요한가
- **리서치와 실행이 갈라지고 있다**: CoinW는 ‘판단 근거’를, Coinbase·IBKR은 ‘제한된 실행’을 판다. 개인 자동매매를 설계할 때도 이 둘을 **분리**하는 게 정석 — 분석 에이전트는 마음껏, 주문 에이전트는 격리 계좌·한도·승인.
- **무효화 조건**은 사람 트레이더에게도 좋은 습관이다. MT5 EA를 돌릴 때 “이 전략이 멈춰야 하는 시장 조건”을 먼저 적어 두는 것과 같다.
- 다만 13명이든 100명이든 **같은 모델들의 토론**이다. 다양한 의견처럼 보여도 같은 데이터·같은 편향을 공유할 수 있다는 점은 기억할 것.

> 지난번 저장하신 TradingAgents·MT5 에이전트 안전장치 기사들과 이어지는 소식입니다 — ‘AI 투자위원회’가 거래소 기본 기능이 되는 중.

출처: [CoinW — CryptoAgents is now live (10/23)](https://www.coinw.com/help-center/announcement-center/product-updates/productupdates/2026-10-23/coinw-cryptoagents-is-now-live-13-ai-experts-come-together-for-your-research-ses/8170) · [Coinbase AI 에이전트 매매 분석 (10/23)](https://finance.yahoo.com/markets/crypto/articles/coinbase-now-lets-ai-agents-175721525.html) · [Outposts — Coinbase](https://outposts.io/project/coinbase/article/coinbase-pitches-ai-agent-trading-via-its-connector-cmvfcsz6n000l06jq71hhf9z3)
