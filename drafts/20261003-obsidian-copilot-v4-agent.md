---
title: "세컨드 브레인: Obsidian Copilot V4 Agent Chat — Claude Code·Codex·opencode를 볼트 안에서"
date: 2026-10-03T07:06:00+09:00
category: "세컨드 브레인"
slug: "obsidian-copilot-v4-agent"
summary: "logancyang/obsidian-copilot(~7.8K★). V4 Agent Chat: opencode(권장)·Claude Code·Codex 백엔드. Skills를 세 에이전트에 공유, Safe/Plan/Auto 권한. LLM Wiki 패턴(원문→위키→린트)을 볼트 UI에서 실행하는 현실 경로."
---

## 한줄 요약
[Obsidian Copilot](https://github.com/logancyang/obsidian-copilot)(2026-10-03 기준 **약 7.8K★**) V4는 채팅 플러그인이 아니라 **데스크톱 Agent Chat**이다. [문서](https://docs.obsidiancopilot.com/agent-mode-and-tools/)상 기본 백엔드는 **opencode**(호스트·BYOK·로컬), 또는 이미 쓰는 **Claude Code / Codex CLI** 로그인. Skills(`SKILL.md`)를 한곳에서 켜면 `.claude/skills`·`.agents/skills` 등으로 링크되어 `/`로 호출한다. 어제 mcp-obsidian 브리지·Karpathy LLM Wiki와 맞물려, **위키를 Obsidian에서 보고 에이전트가 허가된 범위에서 쓰는** 스택이 구체화된다.

## 무엇이 바뀌나
- **권한 UI**: Safe / Plan / Auto. 볼트는 샌드박스가 아니라고 문서가 못 박음 — Auto는 다른 파일·서비스까지 갈 수 있다.
- **멀티 에이전트(Plus)**: `@`로 다른 에이전트에 같은 질문을 보내고 요약. 읽기 연구용, 편집은 단일 에이전트 권장.
- **프로젝트·AGENTS.md**: 턴마다 설명하지 말고 재사용 컨텍스트. LLM Wiki의 “인덱스·린트 스킬”을 Copilot Skill로 붙이는 그림이 자연스럽다.

## 왜 중요한가 (AiPaper·퍼스널 OS)
세컨드 브레인이 “노트 앱”에서 **에이전트 작업 디렉터리**로 바뀐다. 퍼스널 OS 대시보드의 지식 모듈도 같은 권한·스킬 모델을 베끼면 설계가 빨라진다.

## 기억할 것
- [GitHub](https://github.com/logancyang/obsidian-copilot) · [Agent Chat 문서](https://docs.obsidiancopilot.com/agent-mode-and-tools/) · [V4 시작](https://docs.obsidiancopilot.com/getting-started/)
