---
title: "GitHub 핫: CloddsBot — ‘잠자는 동안 1,000개 시장을 도는’ 오픈소스 거래 에이전트"
date: 2026-09-13T07:10:00+09:00
category: "GitHub Hot"
slug: "cloddsbot-open-source-trading-agent"
summary: "alsk1992/CloddsBot. Claude 기반 셀프호스트 트레이딩 터미널이 예측시장·선물·DEX를 한데 묶고 트렌딩에 올랐다. 기능은 실하지만, 실자금 전에 풍크·버전·면책을 읽을 것."
---

## 한줄 요약
[CloddsBot](https://github.com/alsk1992/CloddsBot)은 “Claude + Odds”를 내건 **개인용 AI 트레이딩 터미널**이다. Polymarket·Kalshi 같은 예측시장, Binance·Hyperliquid 등 선물, Solana DEX·여러 EVM 체인까지 묶어 **자연어로 대화하며** 스캔·주문·포트폴리오를 돌리겠다는 설계다. 2026-09-12 기준 GitHub API로 **스타 약 2,465 / 포크 약 309**, MIT, 최근 업데이트도 활발하다.

## 무슨 기능이 ‘핫’한가 (코드 없이)
- **셀프호스트**: 내 머신에서 게이트웨이를 띄우고 Telegram 등 **여러 메신저·WebChat**으로 지시.
- **시장 폭**: README 기준 예측시장·선물·토큰 런치·일부 마이닝까지 “한 대화창”에 넣으려는 욕심.
- **스킬·전략 다발**: 뱃지상 스킬 121+, 전략·고래·차익·카피·DCA 등 “에이전트가 쓸 도구 상자”가 상품이다.
- **해커톤 기원**: Solana Colosseum Agent Hackathon에서 짧은 기간에 만든 풀스택 에이전트로 소개된다.

## 왜 중요한가 / 어디에 조심하나
오픈소스 **에이전트 트레이딩**이 “데모”를 넘어 **복제·클론 트래픽**을 모으는 신호다. 동시에 커뮤니티 감사·리뷰들은 (1) README가 수익을 약속하지 않는 점은 좋지만, (2) **풍크 코드 비중이 기능 대비 얇다**는 지적, (3) npm 옛 패키지와 GitHub 최신 릴리스 **버전 불일치** 이슈를 반복한다. 공식 README도 옛 npm `clodds`는 더 이상 유지하지 말고 **GitHub 릴리스 tgz**로 설치하라고 안내한다.

DXRG 실전 논문과 나란히 읽으면 메시지가 겹친다. **시장을 많이 붙인다고 엣지가 생기지 않는다.** 먼저 소액·페이퍼·풍크 한도·보호 주문부터.

## 기억할 것
- 저장소: [github.com/alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) (homepage: cloddsbot.com).
- “트렌딩 = 검증된 수익”이 아니다. 키·출금 권한·레버리지를 최소로, 코드 리뷰 없이 실자금은 비추천.
