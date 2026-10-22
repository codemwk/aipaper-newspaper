---
title: "디자인/UI·UX: Framer MCP 공개 — 이제 ChatGPT·Claude·Cursor가 Framer 사이트를 직접 고치고 ‘게시’까지 한다, 에디터를 안 열어도"
date: 2026-10-23T07:01:00+09:00
category: "디자인/UI·UX"
slug: "framer-mcp-remote"
summary: "Framer가 10/22 원격 MCP 서버 ‘Framer MCP’ 공개(주소 https://mcp.framer.com/mcp, Streamable HTTP + OAuth). Codex·ChatGPT, Claude/Claude Code, Cursor, Grok Bot 등에서 캔버스 편집·페이지 생성·CMS 컬렉션 관리·사이트 게시·프로젝트 설정까지. Framer 에디터를 닫아 둬도 작동하고, 연결한 Framer 계정 권한을 그대로 쓴다. 기존 로컬 CLI 브리지(@framer/agent)는 현지화 등 추가 기능 때문에 당분간 병행. 지난 9월 Framer Skills(외부 에이전트용 지침)에 이은 두 번째 단계."
---

## 한줄 요약
Framer가 10/22 **Framer MCP**를 내놨다. 내가 쓰는 AI 도구에 Framer를 ‘연결 앱’으로 붙이면, 에이전트가 **캔버스를 편집하고, CMS 콘텐츠를 관리하고, 사이트를 게시**한다. 데스크톱에서든 휴대폰 앱에서든 AI 도구가 돌아가는 곳이면 된다([Framer Updates](https://www.framer.com/updates), [시작 가이드](https://www.framer.com/help/articles/getting-started-with-framer-mcp/)).

## 어떻게 붙이나
- **주소 하나**: `https://mcp.framer.com/mcp` (원격 MCP, Streamable HTTP, OAuth 로그인).
- **디렉터리 설치**: ChatGPT 플러그인, Claude 디렉터리, Cursor 마켓플레이스, Grok Bot 연결 앱 목록에서 ‘설치’ → Framer 로그인 → 권한 승인.
- **권한**: 연결한 Framer 계정이 볼 수 있는 프로젝트는 다 다룰 수 있다. 회사 계정이라면 관리자가 MCP 연결 승인을 요구할 수 있다.
- **에디터 불필요**: 연결 후엔 Framer 창을 닫아도 에이전트가 작업한다. 결과는 나중에 캔버스에서 확인.

## 실제로 시킬 수 있는 일(가이드 예시)
- “이 프로젝트의 기존 스타일과 컴포넌트로 **반응형 요금제 페이지**를 만들어 줘”
- “CMS 컬렉션 목록 보여 줘”
- “홈 헤드라인을 ‘Design and publish without handoff’로 바꿔 줘”
- 끝나면 직접 게시하거나 **에이전트에게 게시까지** 시킨다.
팁: 프로젝트 이름이 아니라 **전체 프로젝트 링크**를 주라고 가이드가 권한다(엉뚱한 프로젝트를 여는 실수 방지).

## 무엇이 새로운가
9월 말 Framer는 외부 에이전트가 읽을 ‘Skills’ 지침과 로컬 CLI 브리지(`@framer/agent`)를 냈다. 이번엔 **설치 없는 원격 서버**라 비개발자도 클릭 몇 번으로 연결된다. 다만 현지화(localization) 같은 일부 작업은 아직 CLI 쪽에만 있어, 기능이 같아질 때까지 둘 다 지원한다.
같은 주 Figma는 MCP 파트너 20곳 확장(10/15), Webflow는 MCP에 분석 데이터를 붙였다(10/17). **웹 디자인 툴 3강이 모두 ‘에이전트가 들어오는 문’을 열었다.**

## 왜 중요한가 / 주의할 점
- 디자이너의 일이 “화면을 그리는 것”에서 **“에이전트가 지켜야 할 스타일·컴포넌트를 정해 두고 결과를 검수하는 것”** 으로 옮겨 간다. 어제 다룬 ‘Pure UI 상태 격자’ 같은 검수 습관이 더 중요해진다.
- **‘게시’ 권한**은 실제 고객이 보는 사이트를 바꾼다. 처음엔 게시는 사람이 누르는 규칙을 두는 게 안전하다.

> 지난번 저장하신 Framer 경제학·Framer Skills 기사와 이어지는 소식입니다.

출처: [Framer Updates — Framer MCP (10/22)](https://www.framer.com/updates) · [Getting started with Framer MCP](https://www.framer.com/help/articles/getting-started-with-framer-mcp/) · [Framer MCP 소개](https://www.framer.com/mcp/)
