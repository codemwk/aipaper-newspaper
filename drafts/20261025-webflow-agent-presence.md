---
title: "디자인/UI·UX: Webflow ‘에이전트 프레즌스’ — Claude·Codex·Cursor가 내 사이트 어디를 고치는 중인지, 동료 커서처럼 캔버스에 보인다(전 요금제 무료)"
date: 2026-10-25T07:01:00+09:00
category: "디자인/UI·UX"
slug: "webflow-agent-presence"
summary: "Webflow가 10/23 ‘Agent presence’를 모든 워크스페이스에 공개. Webflow MCP로 연결된 AI 에이전트(Claude·Codex·Cursor·ChatGPT 등)가 작업하면 Designer 상단에 반짝이 표시 아바타, 편집 중인 요소 하이라이트, 작업 중인 페이지·컴포넌트 둘레에 도는 테두리가 뜬다. 내 에이전트뿐 아니라 팀원의 에이전트도 보여서, 에이전트가 끝나기 전에 덮어쓰거나 게시하는 사고를 막는다. 무료. 단 Webflow 자체 AI Assistant는 아직 미지원, Designer를 열어 둬야 보인다."
---

## 한줄 요약
지금까지 에이전트가 Webflow 사이트를 고치면 변경이 **‘어느새’ 나타났다**. 10/23부터는 에이전트가 **어디서 일하는지 사람 동료처럼 보인다**([Webflow 공지](https://community.webflow.com/updates/post/agent-presence-is-now-available-in-all-workspaces-jMfuP1tAE180gMM)).

## 화면에 뭐가 보이나
| 표시 | 의미 |
|---|---|
| 상단 바 아바타(반짝이 마크) | 지금 연결돼 일하는 에이전트 |
| 요소 하이라이트 | 에이전트가 편집 중인 바로 그 요소 |
| 페이지·컴포넌트 둘레를 도는 테두리 | 작업 범위(이 페이지/컴포넌트를 만지는 중) |
| Pages·Components 패널 옆 아바타 | 어느 페이지·컴포넌트에 에이전트가 들어가 있는지 |

- **대상**: Webflow MCP로 연결된 에이전트(Claude, Codex, Cursor, ChatGPT 등). 내 것과 팀원 것 모두.
- **조건**: Designer를 열어 둬야 보인다. Webflow 자체 AI Assistant에는 아직 적용 안 됨.
- **가격**: 전 요금제 무료.

## 실제로 막아 주는 사고
1. 에이전트가 히어로 섹션을 고치는 중인데 내가 같은 섹션을 손으로 수정 → 서로 덮어쓰기
2. 에이전트 작업이 반쯤 끝났는데 팀원이 **게시(Publish)** 버튼 → 반쪽짜리 페이지가 라이브로
테두리 하나로 “지금 건드리지 마” 신호가 생긴 셈이다.

## 왜 중요한가
이번 달 흐름은 **에이전트를 ‘보이지 않는 자동화’에서 ‘보이는 동료’로** 바꾸는 것이다. Figma는 팀원 에이전트를 캔버스에서 따라가 볼 수 있게 했고(10/6), Spline은 ChatGPT 옆에 진짜 편집기를 띄운다(아래 기사). 디자인 툴의 새 기본 UI 패턴은 “AI가 뭘 했나”의 결과 화면이 아니라 **“AI가 지금 뭘 하나”의 실시간 표시**다.
실무 팁: 에이전트에게 사이트를 맡길 땐 **페이지 단위로 범위를 나눠** 지시하면 테두리 표시와 맞물려 충돌이 확 줄어든다.

> 지난번 저장하신 Webflow·Framer 관련 기사들(DESIGN.md·Campaigns·MCP)과 이어지는 소식입니다 — 이번엔 ‘협업 화면’ 쪽 업데이트.

출처: [Webflow Community — Agent presence is now available in all workspaces (10/23)](https://community.webflow.com/updates/post/agent-presence-is-now-available-in-all-workspaces-jMfuP1tAE180gMM) · [bedooncode 정리](https://bedooncode.com/articles/webflow-brings-live-ai-agent/)
