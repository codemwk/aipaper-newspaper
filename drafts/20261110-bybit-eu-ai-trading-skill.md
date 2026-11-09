---
title: "AI 트레이딩: Bybit EU ‘AI Trading Skill’ — 문장 하나로 설치, 실계좌 주문은 매번 CONFIRM. 출금 권한은 절대 금지"
date: 2026-11-10T07:05:00+09:00
category: "AI 트레이딩"
slug: "bybit-eu-ai-trading-skill"
summary: "MiCAR 규제 아래 있는 Bybit EU가 11/9 웹서밋에서 MIT 오픈소스 스킬을 공개했다. ChatGPT·Claude·Gemini·Cursor·Codex에 SKILL.md 링크 하나만 주면 현물·현물 마진 주문, 잔고 조회, 시세 스트림까지 자연어로. 메인넷 쓰기 작업은 요약 카드 후 CONFIRM 입력, 키는 Read+Trade만. 다만 자동 업데이트·클라우드 AI 키 노출은 따져볼 점."
---

## 한줄 요약
거래소가 MCP 서버 대신 **‘스킬 파일’**로 에이전트에 문을 열었다. Bybit EU는 11/9 리스본 웹서밋 첫날 **AI Trading Skill**(v1.0.1, MIT)을 공개했다. AI에게 “이 SKILL.md를 읽고 스킬로 저장해서 Bybit EU 거래를 도와줘”라고 한 줄 보내면 끝이다([GitHub BYBIT-EU/skills](https://github.com/BYBIT-EU/skills), [Bitcoins News](https://bitcoinsnews.com/bybit-eu-releases-open-source-tool-letting-ai-chatbots-trade-crypto-directly-109100)).

## 할 수 있는 것
- **시세**: 실시간 가격·캔들·호가·체결, WebSocket 스트림.
- **현물 주문**: 시장가·지정가, 취소·정정, 주문 내역.
- **현물 마진**: 차입·상환, 레버리지 2~10배(스킬 문서의 오류 코드 기준).
- **계정·자산**: 잔고, 수수료율, 입금 주소·입출금 기록, 내부 이체, 코인↔코인·법정화폐↔코인 전환.
- **범위 밖**: 선물·옵션·Earn·카피트레이딩·봇은 Bybit EU에 없으므로 제외.

## 안전장치 (README·SKILL.md 기준)
- **기본은 메인넷**이고, 메인넷의 모든 쓰기 작업은 구조화된 요약 카드를 보여준 뒤 사용자가 **CONFIRM**을 입력해야 실행된다. 테스트넷은 자유 실행.
- 스킬 내부 규칙의 우선순위가 명시돼 있다: **안전 > 응답성 > 편의**. “빠르게 하려고 확인을 건너뛰지 말 것.”
- API 키는 **Read + Trade만**, 출금 권한은 “절대” 켜지 말라고 반복한다. IP 바인딩과 잔고를 제한한 서브계정 사용을 권장.
- API 응답의 텍스트 필드는 표시만 하고 실행하지 않는다(프롬프트 인젝션 방어). 모듈 로드가 실패하면 읽기 전용으로 떨어진다.

## 따져볼 점
- **키의 행방**: 로컬 CLI(Claude Code·Cursor)에서는 서명이 로컬에서 이뤄지지만, ChatGPT·Gemini 같은 **클라우드 AI에서는 대화창에 키를 붙여 넣는 방식**이라 키가 AI 제공사 서버로 간다. 스킬 문서도 위험도를 ‘중간’으로 적었다.
- **자동 업데이트**: 세션 시작 때 Bybit 매니페스트를 확인해 새 파일을 내려받는다(SHA256 검증). 편하지만, 내가 검토한 그 파일이 다음 주에도 그대로라는 보장은 없다는 뜻이다.
- CONFIRM은 “방향·수량을 사람이 본다”는 의미일 뿐, 모델이 잘못 해석한 수량·티커를 사람이 놓치면 그대로 나간다. 지난번 저장하신 RiskGate 같은 MT5 안전 계층이나 어제 다룬 MUTEX MCP처럼 **서버 쪽 한도**는 이 스킬에 없다.

## 왜 중요한가
지금까지 브로커들은 MCP 서버를 열었다(PrimeXBT·B2BROKER·Axi·MT5). Bybit EU는 **설치 없는 마크다운 스킬**로 같은 일을 한다. 진입 장벽은 더 낮고, 규제(MiCAR) 거래소가 공식 배포한다는 점이 다르다. 11/10 행사에서 ‘주문장 위의 에이전트’ 라이브 시연도 예고돼 있다.
