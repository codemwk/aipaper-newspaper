---
title: "Design: Framer Skills·External Agents — 디자인 시스템을 ‘스킬’로 심다"
date: 2026-09-26T07:04:00+09:00
category: "Design / UI·UX"
slug: "framer-skills-external-agents"
summary: "Framer(2026-09-22 Skills). /skills로 디자인시스템·문체·CMS 워크플로 저장. @pages·@components·@styles 참조. External Agents: npx @framer/agent setup로 Claude Code·Cursor·Codex·Antigravity 연결 — 별도 MCP 서버 불필요. 변경은 브랜치."
---

## 한줄 요약
[Framer](https://www.framer.com)가 에이전트에게 **프로젝트별 작업 방식**을 가르치는 **Skills**(2026-09-22)와, Claude Code·Cursor·Codex 등을 캔버스에 직접 붙이는 **External Agents**를 공식화했다. “예쁜 랜딩을 한 번 생성”이 아니라 **반복 가능한 디자인 지시**다.

## 어떻게 동작하나
- **Skills**: `/skills`로 디자인 시스템·문체·CMS 규칙을 저장·갱신. `@pages`·`@components`·`@styles`로 프로젝트 자산을 가리킴. 리믹스·템플릿에 스킬이 따라가 템플릿 제작자가 가이드를 실어 보낼 수 있음([Updates: Skills](https://www.framer.com/updates/skills)).
- **External Agents**: `npx @framer/agent setup` 후 `/framer`로 프로젝트 권한. **별도 Framer MCP 서버 없이** 캔버스·컴포넌트·CMS·퍼블리시 접근. Antigravity·Windsurf 등 터미널/툴 호출 가능 에이전트 지원([External Agents](https://www.framer.com/agents/external/)).
- **안전장치**: 라이브 사이트 직수정지 아님(에디터 캔버스). 외부 에이전트 변경은 **자동 브랜치** — 머지·퍼블리시는 사용자 통제.

## 왜 중요한가
어제 UserTesting MCP가 “사람 검증”을 루프에 넣었다면, 오늘은 **사이트 빌더가 스킬+네이티브 브릿지**로 에이전트 워크벤치가 되는 장면이다. 디자인 토큰을 문서가 아니라 **실행 가능한 지시**로 옮기는 패턴.

## 기억할 것
- [Framer Skills](https://www.framer.com/updates/skills) · [External Agents](https://www.framer.com/agents/external/)
