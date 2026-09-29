---
title: "디자인/UI·UX: Penpot MCP — 오픈소스 캔버스에 에이전트를 붙이는 공식 경로"
date: 2026-09-30T07:06:00+09:00
category: "디자인/UI·UX"
slug: "penpot-mcp-server"
summary: "Penpot Help. 원격·로컬 MCP로 토큰·컴포넌트·페이지 읽기/쓰기. 포커스 페이지·단일 활성 탭 제약. npx @penpot/mcp@stable 또는 design.penpot.app 원격 URL+userToken. 쓰기 전 읽기 프롬프트 권장."
---

## 한줄 요약
[Penpot MCP server 도움말](https://help.penpot.app/mcp/)은 Cursor·Claude Code 등 MCP 클라이언트가 **열린 Penpot 파일**을 자연어로 읽고 고치게 하는 공식 경로다. 토큰 생성·베리언트 정리·레이어 네이밍·디자인→HTML/CSS 추출까지 “디자인 유지보수 + 핸드오프”를 에이전트 루프에 넣는다. (9/28 Enterprise 요금 기사와 별개로, **에이전트 연결면**을 다룬다.)

## 구조
- **3조각**: MCP 서버 ↔ Penpot 안 MCP 플러그인 ↔ 클라이언트. 항상 **현재 포커스 페이지**, **한 브라우저 탭만** MCP 활성.
- **원격**: Account → Integrations → MCP Server에서 키·URL(`userToken` 포함). `npx -y add-mcp -g -n penpot <URL>`.
- **로컬**: `npx @penpot/mcp@stable`, 플러그인을 `localhost:4400/manifest.json`으로 로드.
- **주의**: 탭이 sleep되면 실패. Chrome은 해당 사이트를 Always keep active 권장. 쓰기 전에 list/inspect부터.

## 왜 중요한가
Figma MCP가 유료 생태계의 기본값이라면, Penpot MCP는 **셀프호스트·오픈 캔버스** 쪽 대칭 이동이다. 디자인 시스템을 에이전트에 열어줄 때 권한·탭·키 수명까지 운영 이슈가 된다.

## 기억할 것
- [help.penpot.app/mcp](https://help.penpot.app/mcp/)
