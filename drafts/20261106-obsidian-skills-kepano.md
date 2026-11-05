---
title: "세컨드 브레인: kepano/obsidian-skills — Obsidian CLI·Bases·JSON Canvas를 에이전트에게 가르치는 공식급 스킬"
date: 2026-11-06T07:10:00+09:00
category: "세컨드 브레인"
slug: "obsidian-skills-kepano"
summary: "Obsidian CEO Steph Ango(kepano)의 obsidian-skills 저장소가 에이전트에게 Markdown·Bases·JSON Canvas·Obsidian CLI 사용법을 심는 스킬 묶음이다. 2026-01 생성 후 11/5 기준 GitHub 별 약 5.1만. vault를 RAG 조각이 아니라 에이전트가 조작 가능한 워크스페이스로 다루는 흐름의 기준점에 가깝다."
---

## 한줄 요약
Obsidian을 “노트 앱”이 아니라 **에이전트가 CLI와 오픈 포맷으로 다루는 작업면**으로 만들려면, 어떤 스킬을 심을지가 관건이다. kepano의 **obsidian-skills**가 그 기본기를 공개 저장소로 정리해 두었다([kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)).

## 지금 뭐가 뜨나
- **범위**: Obsidian Markdown, **Bases**, **JSON Canvas**, Obsidian CLI를 에이전트가 쓰도록 가르치는 스킬.
- **신호**: 생성 2026-01-02, 11/5 기준 별 약 **50,828**. PKM·에이전트 조합 저장소 중 최상위권.
- **위치**: 커뮤니티 플러그인 나열이 아니라, Obsidian 쪽 인물이 오픈 포맷·CLI를 **에이전트 인터페이스**로 표준화하려는 움직임.

## 왜 중요한가
지난번 저장하신 **Obsidian Copilot·claude-mem·LLM Wiki** 흐름과 직결된다. 플러그인마다 제각각이던 ‘에이전트↔볼트’ 계약을, **스킬 파일 + CLI + 오픈 포맷**으로 맞추면 Cursor·Claude Code·Codex가 같은 vault를 공유하기 쉬워진다. AiPaper·ANDRSN 리서치 vault를 에이전트 유지보수에 맡길 때의 출발점이다.

## 주의
별 수는 인기도이지 보안 보증이 아니다. 에이전트에 vault 쓰기 권한을 줄 때는 아래 기사(draft isolation) 같은 가드가 필요하다.
