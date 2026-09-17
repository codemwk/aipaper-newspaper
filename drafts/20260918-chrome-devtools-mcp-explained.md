---
title: "GitHub 해설: Chrome DevTools MCP — 에이전트가 브라우저를 ‘보고’ 고치게 하는 도구"
date: 2026-09-18T07:40:00+09:00
category: "GitHub"
slug: "chrome-devtools-mcp-explained"
summary: "ChromeDevTools/chrome-devtools-mcp. 에이전트가 라이브 Chrome에서 디버그·성능 트레이스·DOM 검사. Agent-Leaderboard MCP 보드 상위(오늘 README 3위권). 스타 ~5.2만(2026-09-17 조회)."
---

## 한줄 요약
[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)는 코딩 에이전트(Cursor·Claude·Copilot 등)가 **실제 Chrome**을 조종·검사하게 하는 **공식 계열 MCP 서버**다. 오늘은 설치 명령이 아니라 **왜 보드 상단에 붙어 있는지**만 풀어서 본다.

## 무엇이 바뀌었나 / 무엇을 하나
- 에이전트는 원래 코드를 짜도 **브라우저에서 어떻게 깨지는지**를 직접 못 본다. 이 서버가 DevTools 능력을 MCP 도구로 노출한다.
- 예: 성능 트레이스 시작·분석, 네트워크·콘솔 오류, 폼 제출 재현, 레이아웃/CSS 이상, LCP 진단. Chrome for Developers 블로그에 예시 프롬프트가 정리돼 있다.
- Agent-Leaderboard **MCP Servers** 표(오늘 README)에서 **chrome-devtools-mcp**는 awesome-mcp-servers·TrendRadar 다음 **상단권**. GitHub 스타는 조회 시점 약 **52,198**.
- `npx chrome-devtools-mcp@latest` 형태의 MCP 등록이 문서에 나와 있고, “DevTools for agents” 묶음으로도 안내된다.

## 왜 중요한가
비개발자에게 필요한 한 줄: **챗봇이 웹을 ‘추측’하지 않고, 열린 페이지를 계측한다**. 자동매매 대시보드·옵시디언 웹 클립·사내 툴 UI를 에이전트에게 맡길 때, Playwright MCP와 함께 **브라우저 관측** 조합의 기본 부품이 됐다. 리더보드에서 스타가 쌓이는 이유도 그 실용성이다.

## 기억할 것
- 저장소: [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- 배경: [Chrome Developers — DevTools MCP](https://developer.chrome.com/blog/chrome-devtools-mcp) · 순위: [Agent-Leaderboard](https://github.com/jaychempan/Agent-Leaderboard)
