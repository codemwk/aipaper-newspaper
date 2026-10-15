---
title: "세컨드 브레인 / PKM: Notion 3.8 ‘에이전트를 위한 컨텍스트’ — MCP로 어떤 에이전트든 연결, 스킬을 Notion에 쓰고 어디서나, 사람·에이전트 변경 이력까지"
date: 2026-10-16T07:11:00+09:00
category: "세컨드 브레인 / PKM"
slug: "notion-38-agent-context"
summary: "Notion 3.8(10/13): 외부 MCP 에이전트가 워크스페이스를 읽고 문서·트래커를 업데이트(관리자 MCP 통제: 누가 어떤 AI 도구를 연결했는지·마지막 사용·개별 회수), Notion Agent는 150+ 도구와 MCP 연결, Skills API로 Notion에서 쓴 스킬을 GitHub로 동기화해 ChatGPT·Claude 등에서 재사용, 사람·에이전트 귀속 표시 버전 히스토리, DB 컬럼 권한, 동기화 DB 재구축(GitHub·Jira·Salesforce), Business/Enterprise는 ChatGPT Plus/Pro 구독으로 Notion AI 사용(마크업 없음)."
---

## 한줄 요약
“에이전트를 바꾸거나, 도구를 새로 들이거나, 동료가 새로 와도 **모든 걸 다시 설명할 필요는 없어야 한다.**” Notion이 2026-10-13 내놓은 **3.8**은 노트 앱을 **에이전트들이 공유하는 기억 장소**로 재정의하는 업데이트다([Notion 릴리스](https://www.notion.com/releases/2026-10-13)).

## 핵심 변화
- **어떤 에이전트든 MCP로**: MCP 호환 에이전트가 워크스페이스 맥락을 읽고 문서·작업 트래커를 업데이트. 에이전트를 갈아타도 맥락은 Notion에 남는다. 관리자용 **MCP 통제**로 누가 어떤 AI 도구를 연결했는지, 마지막 사용 시점을 보고, 다른 연결은 건드리지 않고 한 사람의 접근만 회수.
- **Notion Agent → 150+ 도구**: 반대 방향도 열렸다. Notion Agent·Custom Agent가 MCP로 HubSpot 파이프라인, Stripe 결제, Cloudflare 인프라 정보를 끌어와 문서를 만든다.
- **스킬을 한 번 쓰고 어디서나**: Notion에서 Skills를 작성·공유하고, 새 **Skills API**로 GitHub에 동기화해 ChatGPT·Claude 등에서 재사용. 이미 가진 스킬은 에이전트에게 MCP로 Notion에 재작성시키라는 안내.
- **사람·에이전트 변경 이력**: 페이지·DB 버전 히스토리에 강조 표시, DB 변경 상세, **누가(사람/에이전트) 바꿨는지 귀속**, 클릭 한 번 복원.
- **DB 컬럼 권한**: 속성별로 사람·에이전트의 보기/편집을 제한(예: 채용 DB에서 연봉 숨기기).
- **동기화 DB 재구축**: GitHub·Jira·Salesforce부터, 동기화 상태 실시간 표시.
- **“두 번 내지 마세요”**: Business·Enterprise에서 **ChatGPT Plus/Pro 구독**을 연결해 Notion AI 사용량을 충당, Notion은 마크업을 붙이지 않는다고 밝혔다.

## 왜 중요한가
지금까지 AiPaper에서 다룬 세컨드 브레인 흐름(LLM Wiki, Obsidian+에이전트, Cobrain·AI Twin)의 공통 질문은 “**누가 기억을 소유하나**”였다. Notion 3.8의 답은 “앱이 아니라 **공유 컨텍스트 계층**이 소유하고, 에이전트는 교체 가능한 손님”이다. 버전 이력의 에이전트 귀속은 어제 다룬 AI Twin의 ‘저장 전 검토’와 같은 문제의식 — **AI가 쓴 기억을 사람이 검증할 수 있어야** 한다. Obsidian 파(로컬·마크다운)와 Notion 파(클라우드·권한·DB)의 차이는 이제 “AI를 쓰느냐”가 아니라 **“어디에 맥락을 두고 누가 통제하느냐”**다.

출처: [Notion 3.8: Context for your agents (2026-10-13)](https://www.notion.com/releases/2026-10-13)
