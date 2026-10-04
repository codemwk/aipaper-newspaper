---
title: "디자인/UI·UX: Figma 원격 MCP, ‘승인된 클라이언트만’ 쓰기 허용 — MCP 공동 창시자 반발, 좌석별 호출 한도까지"
date: 2026-10-05T07:09:00+09:00
category: "디자인/UI·UX"
slug: "figma-mcp-catalog-gate"
summary: "Figma 문서: MCP Catalog에 등재된 클라이언트만 원격 서버 연결(대기자 명단). 9/30 Figma 커뮤니티 리드 확인, Pi 제작자 David Soria Parra 공개 요청. 쓰기(캔버스 생성·수정)는 원격만, 데스크톱 MCP는 읽기 전용·제한 없음. 베타 무료→향후 사용량 과금. Dev/Full 좌석 일 200~600회."
---

## 한줄 요약
[Figma 개발자 문서](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)는 이제 이렇게 적혀 있다: “**Figma MCP Catalog에 등재된 클라이언트만** Figma MCP 서버에 연결할 수 있다. 새 클라이언트 개발자는 대기자 명단에 등록하라.” 9월 30일 Figma 커뮤니티 리드가 X에서 이를 확인했고, MCP 공동 창시자이자 오픈소스 코딩 하네스 **Pi**를 만든 David Soria Parra가 공개적으로 “MCP의 개방 생태계 취지에 어긋난다”고 반발했다([AI Agents Listing 10/2](https://aiagentslisting.com/news/figma-restricts-remote-mcp-access-to-an-approved-client-list)).

## 무엇이 걸려 있나
- **원격 MCP(mcp.figma.com)만 ‘쓰기’가 된다**: 프레임·컴포넌트·변수·오토레이아웃 생성·수정, FigJam 보드 편집, 라이브 UI 캡처를 Figma로 보내기, 코드 생성, Code Connect. 로컬 **데스크톱 MCP는 읽기 전용**이고 화이트리스트 대상이 아니다.
- **등재 목록**(보도 기준): Claude·Claude Code, ChatGPT·Codex, Cursor, Xcode, VS Code, Kiro, Grok, Google Antigravity, GitHub Copilot CLI, Notion, Slack, Devin, Replit, Warp, Factory, Augment, Rovo Studio, Android Studio. Pi는 없다.
- **허점**: 검사가 OAuth 클라이언트 이름 기준이라 이름을 ‘Codex’로 바꾸면 통과됐다는 HN 댓글이 있다(미확인 커뮤니티 보고). OpenCode 등재에 **8개월 법무 검토**가 걸렸다는 댓글도.
- **돈**: 원격 쓰기는 현재 베타 무료, 향후 **사용량 기반 유료화** 예정. 호출 한도는 좌석별 — 무료 view/collab 월 6~20회, Professional·Organization Dev/Full 일 200회, Enterprise Dev/Full **일 600회·분당 20회**(보도 인용).

## 왜 중요한가
지난 몇 주 Figma Agent·Weave·Code Connect를 다루며 본 ‘디자인 캔버스를 에이전트에 연다’는 흐름에, **누가 열쇠를 쥐는가**라는 플랫폼 정치가 붙었다. 9월 아마존이 Meta Muse 쇼핑 에이전트를 막은 것과 같은 패턴 — 프로토콜은 개방형이어도 **쓰기 권한은 플랫폼이 고른 에이전트에게만** 간다. 자체 하네스나 소규모 에이전트로 Figma 자동화를 설계한다면, 지금은 등재 클라이언트(Claude Code·Cursor·Codex 등) 위에 올리는 게 현실적이고, 한도·유료화 일정을 비용표에 넣어 둬야 한다.

## 기억할 것
- 정책 문구는 Figma 공식 문서로 확인, 등재 목록·한도·HN 우회 내용은 보도 인용.
- [Figma 원격 MCP 설치 문서](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) · [AI Agents Listing 10/2](https://aiagentslisting.com/news/figma-restricts-remote-mcp-access-to-an-approved-client-list)
