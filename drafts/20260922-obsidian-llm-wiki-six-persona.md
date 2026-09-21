---
title: "obsidian-llm-wiki — 마크다운 볼트를 6인 페르소나 MCP 팀으로 컴파일"
date: 2026-09-22T07:12:00+09:00
category: "Second Brain"
slug: "obsidian-llm-wiki-six-persona"
summary: "2233admin/obsidian-llm-wiki(★~33). 마크다운 볼트→Claude Code/Codex/OpenCode/Gemini CLI용 6-persona MCP 팀. headless-first, 인용하고 추측하지 않음. Karpathy식 위키 컴파일 각도. MCPVault ‘파일 게이트’와 다른 ‘역할 팀’ 레이어."
---

## 한줄 요약
[2233admin/obsidian-llm-wiki](https://github.com/2233admin/obsidian-llm-wiki)(★약 33)는 마크다운 볼트를 **6개 페르소나 MCP 팀**으로 컴파일해 Claude Code·Codex·OpenCode·Gemini CLI에 붙인다. 카피는 **headless-first**, **cites, doesn’t guess**.

## 지금 뭐가 뜨나
- **각도**: 단순 파일 CRUD MCP가 아니라, 볼트를 **역할이 나뉜 위키 팀**으로 재구성(Karpathy식 “LLM wiki compilation” 감성).
- **클라이언트**: GUI Obsidian 플러그인 의존보다 **헤드리스 CLI 에이전트**를 전제로 한다.
- **신뢰 규칙**: 답할 때 **인용하고 추측하지 않는다**는 설계 문장 — 세컨드브레인에서 환각을 줄이려는 명시적 계약.
- **배치**: MCPVault가 “볼트 파일 포트”라면, 이 리포는 **그 위에 얹는 페르소나·워크플로 레이어**로 읽으면 겹침이 적다.

## 왜 중요한가
세컨드브레인×에이전트 스택이 “검색 한 방”에서 **팀·위키·인용 규약**으로 분화 중이다. 스타 수는 작아도, ‘추측 금지’를 README 전면에 둔 설계는 퍼스널 지식 OS에 바로 이식할 체크리스트다. MCPVault(파일 포트)와 같이 두면 “연결”과 “역할 분담”을 한 스택에서 나눌 수 있다.

## 기억할 것
- [obsidian-llm-wiki](https://github.com/2233admin/obsidian-llm-wiki) · 6-persona MCP · cites don’t guess
