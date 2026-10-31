---
title: "디자인: 공개 디자인 시스템 31곳 AI 준비도 — 중앙값 5/10. 토큰은 있는데 에이전트용 안내·llms.txt가 없다"
date: 2026-11-01T07:06:00+09:00
category: "디자인/UI·UX"
slug: "supernova-ai-ready-design-systems"
summary: "Supernova가 10월 점검(5–6일)으로 공개 디자인 시스템 31곳을 5개 항목(토큰·컴포넌트 API·MCP·llms.txt·소비자용 에이전트 가이드)으로 채점했다. 중앙값 5/10, 만점 없음. Ant/Atlassian/React Spectrum이 9점. 빠진 148점 중 135점이 에이전트 접근·문서·가이드 — 값싼 정적 파일 두 개면 중앙값이 7로 오른다고 추정."
---

## 한줄 요약
지난번 저장하신 디자인 시스템·에이전트 가이드(DESIGN.md, AGENTS.md) 관심과 이어지는 소식이다. 데이터가 없어서가 아니라 **에이전트에게 ‘어디를 보라’고 안 알려줘서** 점수가 낮다는 연구다([Supernova](https://www.supernova.io/blog/ai-ready-design-systems-2026-study)).

## 채점(각 2점, 총 10)
1. 토큰을 JSON/JS 패키지로
2. 컴포넌트 API를 타입·manifest로
3. 공식 MCP
4. 에이전트가 읽을 `llms.txt`(풀 마크다운)
5. **소비 팀**용 에이전트 가이드(기여용 AGENTS.md만 있으면 감점)

## 결과 스케치
- **9점**: Ant Design, Atlassian Design System, React Spectrum.
- **중앙값 5**. 0점 만점 없음. 정부계 5곳은 평균 3.2 vs 나머지 5.6.
- 토큰 28/31, 타입 API 26/31 — 거의 보편. MCP 공식 9, 풀마크다운 docs 3, 소비팀 가이드 3.
- GOV.UK·USWDS·Fluent는 **커뮤니티 MCP**가 먼저 생김 → 수요 신호이자 구버전 리스크.

## 왜 중요한가
- “토큰을 다시 짜라”보다 **`llms.txt` + 소비자용 스킬 파일**이 ROI가 크다는 실무 결론.
- 에이전트가 `node_modules` 안 가이드를 스스로 안 연다 — README에 안 쓰면 없는 것과 같다는 경고도 포함.
