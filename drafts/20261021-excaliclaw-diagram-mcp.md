---
title: "디자인/UI·UX: ExcaliClaw — 손그림 느낌 다이어그램을 AI가 ‘겹치지 않게’ 그려 주는 협업 화이트보드, 좌표는 서버가 계산하고 무료 요금제에도 MCP 무제한"
date: 2026-10-21T07:02:00+09:00
category: "디자인/UI·UX"
slug: "excaliclaw-diagram-mcp"
summary: "TLDR Design 10/20이 소개한 ExcaliClaw: 브라우저에서 쓰는 손그림 스타일 다이어그램 협업 공간(자동 저장, 컬렉션·검색, 실시간 커서, 링크 공유, JSON 내보내기·Miro 등에서 가져오기). 호스팅 MCP 서버(excaliclaw.com/mcp, OAuth 로그인, API 키 불필요)로 Claude Code·Claude Desktop·Cursor·VS Code Copilot·Codex CLI·OpenCode가 흐름도·ER 다이어그램·스티키 노트를 생성 — 에이전트는 노드·관계만 말하고 배치는 서버가 계산. 사람이 열어 둔 그림을 실시간으로 보고 수정, 변경 직전 버전 기록, 내 아이콘 라이브러리 재사용, PNG/SVG 내보내기. 요금 Free €0, Starter €9/월(5명), Pro €29/월(20명), Enterprise 문의, MCP·AI는 전 요금제 무제한."
---

## 한줄 요약
AI에게 “구조도 좀 그려 줘”라고 하면 대개 상자가 겹치고 선이 엉킨다. 언어 모델은 좌표 계산에 약하기 때문이다. **ExcaliClaw**는 역할을 나눴다. **에이전트는 ‘무엇이 무엇과 연결되는지’만 말하고, 배치는 서버가 계산한다**([ExcaliClaw](https://excaliclaw.com/ai-diagrams-mcp)). 10/20 TLDR Design이 소개했다.

## 무엇인가
브라우저에서 바로 쓰는 **손그림 스타일 다이어그램 협업 공간**이다([홈](https://excaliclaw.com/)).
- 모든 그림 자동 저장, 폴더(컬렉션) 정리와 즉시 검색
- 링크 공유로 함께 그리기, 실시간 커서
- 공개 링크·사용자명 공유, JSON 내보내기, Miro 등 다른 도구에서 가져오기

## 에이전트가 할 수 있는 일
주소 하나(`excaliclaw.com/mcp`)를 MCP 서버로 등록하면, 처음 한 번 브라우저로 로그인(OAuth)한다. **API 키를 복사해 둘 필요가 없다.** 지원 클라이언트: Claude Code·Claude Desktop·Claude.ai, Cursor, VS Code(Copilot Chat), Codex CLI, OpenCode, OpenClaw.
- **그리기**: 흐름도·아키텍처도, ER(데이터 관계) 다이어그램, 스티키 노트
- **함께 작업**: 사람이 **지금 열어 둔 그림**을 보고 고치거나, 사람이 바꿀 때까지 기다렸다가 이어서 작업
- **버전 기록**: 에이전트가 바꾸기 **직전 상태**까지 저장돼 되돌릴 수 있다
- **재사용**: 내 아이콘·도형 라이브러리를 불러 쓰고 저장
- **내보내기**: PNG·SVG, 원하면 공개 URL

## 요금
| 요금제 | 가격 | 인원 |
|---|---|---|
| Free | €0 | — |
| Starter | €9/월 | 최대 5명 |
| Pro | €29/월 | 최대 20명 |
| Enterprise | 문의 | — |

**MCP·AI 사용은 무료 요금제를 포함해 전부 무제한**이다.

## 왜 중요한가
요즘 디자인 도구의 공통 원리가 여기서도 보인다: **AI는 의미를, 도구는 기하학을.** 10/08에 소개한 diagram-design(편집 디자인 스킬)이 ‘모양새 규칙’을 에이전트에 가르쳤다면, ExcaliClaw는 아예 **배치 엔진을 서버에 두고** 에이전트에게는 노드와 관계만 받는다. 결과물이 덜 ‘AI 같고’, 사람이 이어서 손대기 쉽다.
활용 예: 브랜드 워크숍 후 Claude에게 회의 메모를 주고 “고객 여정 흐름도”를 그리게 한 뒤, 팀이 같은 캔버스에서 손으로 고치는 식. 손그림 스타일은 **‘아직 확정이 아니다’라는 신호**를 줘서 초기 논의에 잘 맞는다.

출처: [ExcaliClaw — AI 다이어그램 MCP](https://excaliclaw.com/ai-diagrams-mcp) · [ExcaliClaw 홈·요금](https://excaliclaw.com/) · [TLDR Design (10/20)](https://tldr.tech/design/2026-10-20)
