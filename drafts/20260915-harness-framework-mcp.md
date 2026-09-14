---
title: "에이전트 스택 해설 — 하네스·프레임워크·MCP, 누가 루프를 소유하나"
date: 2026-09-15T07:35:00+09:00
category: "GitHub Hot"
slug: "harness-framework-mcp"
summary: "2026-09-14 MarkTechPost. Agent harness(루프·권한·복구 소유) vs framework(조립 골격) vs MCP(도구 전송 계약만). 2026-07-28 MCP는 상태 없는 코어. 실무는 하이브리드가 기본."
---

## 한줄 요약
[MarkTechPost(2026-09-14)](https://www.marktechpost.com/2026/09/14/agent-harness-vs-agent-framework-vs-mcp-which-layer-owns-the-loop-state-tools-permissions-and-recovery/)가 혼용되는 세 단어를 한 질문으로 가른다. **실행 루프·상태·도구 전송·권한·복구를 누가 소유하는가?**

## 세 층의 역할
- **Harness**(Codex 플랫폼, Claude Agent SDK/Claude Code): 고정 루프 + 세션/승인/샌드박스/컴팩션을 **제품 단위로 소유**.
- **Framework**(LangGraph, OpenAI Agents SDK, Microsoft Agent Framework 1.0): 루프 **골격·체크포인터·가드레일 훅**을 주고 정책은 당신이 씀.
- **MCP**: JSON-RPC 도구·리소스·프롬프트 **와이어 계약**. 루프·에이전트 상태 없음. 스펙도 “동의는 호스트가, MCP는 강제 못 함”이라고 명시. 2026-07-28 이후 코어는 사실상 **stateless**.

## 왜 중요한가
프레임워크가 하네스 레이어를 삼키고, 하네스는 SDK·app-server로 플랫폼이 되고, MCP는 elicitation·Tasks로 에이전트 모양 기능을 넓힌다. 그래도 실무 기본형은 **바깥 그래프(프레임워크) + 무거운 단계는 하네스 샌드박스 + 도구는 전부 MCP**다. “MCP만 붙이면 에이전트”는 오해다.

## 기억할 것
- 루프를 소유하고 싶으면 프레임워크, 검증된 권한·복구가 필요하면 하네스, 도구면은 MCP로 한 번만.
- A2A는 에이전트↔에이전트용으로 MCP와 별개.
