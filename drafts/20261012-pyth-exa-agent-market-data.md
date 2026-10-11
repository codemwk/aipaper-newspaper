---
title: "AI 트레이딩: Pyth × Exa — 에이전트가 ‘웹 리서치 + 실시간·역사 시세’를 한 워크플로로, MCP는 Pro 키 필요"
date: 2026-10-12T07:06:00+09:00
category: "AI 트레이딩"
slug: "pyth-exa-agent-market-data"
summary: "10/9 A-Team Insight: Pyth Network와 Exa가 에이전트용 시세+웹리서치 파일럿. Pyth MCP(https://mcp.pyth.network/mcp)로 심볼 검색·최신가·역사·60초 틱·캔들. 가격 도구는 Pyth Pro API 키. 상용 요금은 미정·파일럿 단계."
---

## 한줄 요약
온체인·기관 시세 네트워크 **Pyth**와 AI 검색 **Exa**가 **에이전트가 뉴스·기업 정보와 시세를 한 흐름에서** 쓰게 하는 협업을 **초기 테스트** 중이라고 10/9 [A-Team Insight](https://a-teaminsight.com/blog/pyth-and-exa-explore-new-market-data-model-for-ai-agents/)가 전했다. 프로덕션 전사 배포·확정 요금은 **아직 없다**.

## 어떻게 붙나 (문서 기준)
- **엔드포인트**: `https://mcp.pyth.network/mcp` (호스티드, Streamable HTTP).
- **도구**: `get_symbols`(키 선택) · `get_latest_price`(최대 100피드, **키 필요**) · `get_historical_price` · `get_price_range`(최대 60초 창) · `get_candlestick_data` · 날짜 변환 유틸.
- **키**: 클라이언트가 `Authorization: Bearer <Pyth Pro key>`를 보낸다. 서버는 키를 갖지 않는다. `get_symbols`는 키 없이 가능, 키 있으면 `entitled` 플래그.
- **스킬**: 포트폴리오·변동성·FX·CSV보내기 등 **9개 MCP Skills** 템플릿을 문서가 안내.
- **파일럿 초점**(인터뷰): 이벤트 드리븐 리서치, 실적 발표 후 가격 경로, 크로스에셋 비교, 포트폴리오 모니터링. Cahill(Douro/Pyth)은 전통 벤더 다단계 라이선스가 **추론·학습·재배포** 앞에서 느려진다고 본다.

## 왜 중요한가
eToro·Axi·Ludus가 **브로커·논지 보드** 쪽 MCP라면, Pyth는 **시세 레이어**를 에이전트 표준 소켓으로 내민다. “Bloomberg 터미널을 에이전트에 통째로”가 아니라 **기여 기관 시세 + 명시적 엔타이틀먼트**로 AI 네이티브 앱 요금을 다시 짜려는 실험이다. 리스크·컴플라이언스: 에이전트가 시세와 웹 문장을 섞을 때 **출처·시각·심볼 식별**을 기계가 읽게 남겨야 한다고 기사도 강조.

## 기억할 것
- 역사 데이터는 문서상 **2025-04 이후**.
- ARR $11.5M 등 성장 수치는 **별도 Pyth/커뮤니티 주장** — 이번 Exa 파일럿의 성과 지표가 아니다.

출처: [A-Team — Pyth and Exa](https://a-teaminsight.com/blog/pyth-and-exa-explore-new-market-data-model-for-ai-agents/) · [Pyth MCP docs](https://docs.pyth.network/price-feeds/pro/mcp)
