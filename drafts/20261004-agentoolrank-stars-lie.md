---
title: "GitHub 트렌드: Stars lie — 669개 에이전트 툴을 활동 신호로 다시 순위 매기기 (AgentoolRank)"
date: 2026-10-04T07:11:00+09:00
category: "GitHub 트렌드"
slug: "agentoolrank-stars-lie"
summary: "DEV/AgentoolRank(2026-10-01): 669개 OSS 에이전트 툴 추적. 32%가 6개월+ 무커밋(5k★+ 68개 포함). 성장은 프레임워크·MCP·메모리. 순위=스타속도·90일 커밋·릴리스·이슈응답. MCP API 제공. 저자 이해충돌 disclosure."
---

## 한줄 요약
[DEV Community / AgentoolRank](https://dev.to/agentoolrank/stars-lie-669-open-source-ai-agent-repos-ranked-by-what-they-actually-do-1fdb)(2026-10-01): 별 수로 고르다 **몇 달 무커밋**인 프레임워크를 집어넣는 실패를 줄이려, 오픈소스 에이전트 관련 **669개** 레포를 GitHub API로 매일 추적한다. 핵심 통계 — **213/669(32%)**가 기본 브랜치에 **6개월 이상 커밋 없음**(별 5천+인데 조용한 프로젝트 **68개** 포함, 표에 MetaGPT·gpt-engineer 등). 최근 30일 별 증가 상위에는 Skills·LangChain·**ECC**·hermes-agent·DeepSeek Harness 등. 카테고리별 별 증가 합은 Agent frameworks가 가장 크고, **MCP-first 29개·합산 ~580k★**를 별도 축으로 본다. 저자가 AgentoolRank를 만든다고 **disclosure**.

## 실무로 보면
- **점수 구성**: (1) 30일 스타 **속도**(누적 별 아님) (2) 90일 기본 브랜치 커밋 (3) 6개월 릴리스 (4) 이슈 닫는 중앙값 — 퍼센타일 합산. 각각 약점(봇 커밋·런칭 하이프)이 있어 **네 지표를 나란히** 보여 준다고 설명.
- **커밋 폭주**: hermes-agent 등 90일 수만 커밋 — “에이전트가 자기 레포에 커밋”하는 신호일 수 있다고 해석.
- **에이전트에서 조회**: MCP `https://agentoolrank.com/api/mcp` — `search_tools` / `get_tool` / `get_alternatives`. 리포트는 agentoolrank.com/report, 데이터 CC BY 4.0.
- **이 기사의 성격**: 일일 모델 Elo 스탬프가 아님. **선정 방법론·생태계 위생** 브리핑.

## 왜 중요한가
오늘 openclaw·ECC 스타 폭증을 “인기”로만 읽지 말고, **활동·응답·릴리스**와 교차 검증하라는 실무 규칙. 퍼스널 OS에 의존성 고를 때 체크리스트로 쓸 수 있다.

## 기억할 것
- [Stars lie (DEV)](https://dev.to/agentoolrank/stars-lie-669-open-source-ai-agent-repos-ranked-by-what-they-actually-do-1fdb) · [agentoolrank.com/report](https://agentoolrank.com/report)
