---
title: "AI 트레이딩: ‘연구만’ vs ‘체결’ — MT5·cTrader·eToro 에이전트 권한 삼각"
date: 2026-09-28T07:10:00+09:00
category: "AI 트레이딩"
slug: "agent-trading-permission-triangle"
summary: "Finance Magnates(2026-09-03): MT5는 Strategy Tester·로그·최적화 등 연구·QA 쪽이 강화되고 라이브 판단 체결은 아직 제한. cTrader AI Agent Connect·eToro Agent Portfolios는 한도 안 실행. 빌드 나열이 아니라 권한 모델 비교."
---

## 한줄 요약
[Finance Magnates(2026-09-03)](https://www.financemagnates.com/forex/metatrader-5-ai-assistant-becomes-a-qa-engineer-for-trading-bots/)는 MT5 AI Assistant를 **트레이딩 봇 QA 엔지니어**에 비유한다. Strategy Tester 리포트·로그·최적화·차트 인디케이터는 MCP로 열리지만, **라이브 계좌에서의 판단·체결은 아직 막힌 단계**라고 정리한다. 같은 기사에서 cTrader·eToro는 **한도 안 자율 실행**으로 대비된다. 오늘은 빌드 번호이 아니라 **권한 삼각**이다.

## 세 꼭짓점 (공개 제품 서술 기준)
- **MT5 (MetaQuotes)**: MCP로 시장 설명·테스터·최적화·차트 준비. 라이브 실행은 보수적. FM은 MCP 도입 후 3주 **1조+ 토큰**(사측 공개치)을 인용.
- **cTrader (Spotware)**: [AI Agent Connect](https://blog.ctrader.com/your-ai-can-now-trade-for-you/) — Local/Remote MCP로 주문·계좌·차트·뉴스. **데모 먼저**, 결정은 트레이더 책임.
- **eToro Agent Portfolios**: 전용 서브포트폴리오·스코프 API 키·최소 자금. 에이전트가 그 한도 안에서만 운용.

## 왜 중요한가
자동매매·프롭·개인 에이전트를 붙일 때 첫 질문은 “어떤 모델인가”가 아니라 **기본 권한이 연구인가 체결인가**다. MT5를 쓰는 독자는 테스터 루프를 에이전트화하고, 실체결이 필요하면 cTrader/eToro식 **격리·한도**를 별도 설계해야 한다.

## 기억할 것
- [FM 기사](https://www.financemagnates.com/forex/metatrader-5-ai-assistant-becomes-a-qa-engineer-for-trading-bots/) · [cTrader 블로그](https://blog.ctrader.com/your-ai-can-now-trade-for-you/) · [eToro Agent Portfolios](https://www.etoro.com/news-and-analysis/etoro-updates/agent-portfolios-let-your-ai-agent-trade-for-you/)
