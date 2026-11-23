---
title: "세컨드 브레인: Obsidian 공식 플러그인이 Grok Bot에도 — 봇이 내 볼트에 노트·Bases·Canvas를 쓴다. 같은 주 obsidian-wiki는 ‘되돌리기·복구 가능한 삭제·쓰기 거부권’을 넣었다"
date: 2026-11-24T07:40:00+09:00
category: "세컨드 브레인"
slug: "obsidian-grok-bot-wiki-undo"
summary: "Obsidian이 11/19 ‘Grok Bot이 이제 Obsidian 볼트에 연결된다’고 밝혔다. 공식 플러그인 목록은 ChatGPT·Codex·Cursor·Grok Bot 넷이 됐다. 봇은 노트를 만들고 찾고 고치며, 링크 갱신, 웹 글 수집, Bases·Canvas 파일 생성까지 한다. 11/23 obsidian-wiki v2026.11.8은 에이전트가 볼트를 고칠 때를 대비한 안전장치를 넣었다. 마지막 변경 되돌리기(undo), 복구 가능한 페이지 삭제(memory_forget), 쓰기 전에 거부·수정하는 운영자 훅, 여러 볼트 전환과 받은편지함이 달린 웹 뷰어."
---

## 한줄 요약
11/14 전한 **Obsidian 공식 플러그인**(Claude Code·Codex·Cursor)에 **Grok Bot**이 더해졌다. 이제 AI가 내 볼트에 직접 쓰는 일이 흔해진다. 그래서 같은 주 나온 **obsidian-wiki의 ‘되돌리기’ 기능**이 짝처럼 중요하다([Obsidian 도움말: Skills](https://obsidian.md/help/skills), [obsidian-wiki v2026.11.8](https://github.com/Ar9av/obsidian-wiki/releases/tag/v2026.11.8)).

## Obsidian for Grok Bot (11/19)
- Obsidian 공식 X 계정: **“Grok Bot can now connect to your Obsidian vault.”** 도움말에는 “Obsidian은 **ChatGPT, Codex, Cursor, Grok Bot**의 공식 플러그인”이라고 적혀 있다. 설치는 플러그인 페이지에서 **Add to Grok Bot.**
- 할 수 있는 일: Obsidian식 마크다운 노트 쓰기(위키링크·임베드·콜아웃·속성), **Bases**(표·필터·수식)와 **Canvas** 파일 만들기, 링크 갱신, 웹 페이지를 깨끗한 마크다운으로 가져오기(Defuddle), Obsidian CLI로 실행 중인 앱의 노트 검색·관리.
- 조건: CLI 기능은 **데스크톱 Obsidian이 켜져 있고 CLI가 활성화**돼 있어야 한다. 마크다운·Bases·Canvas는 파일 형식 설명이라, 볼트 파일을 읽고 쓸 수 있는 에이전트면 된다. 변경은 Obsidian Sync로 기기 간 동기화된다.
- 개인정보: 스킬 자체는 아무것도 보내지 않는다. 다만 **에이전트가 읽은 노트는 그 AI 모델의 대화 내용이 된다.** 민감한 볼트는 정책을 먼저 확인하라고 도움말이 적었다.

## obsidian-wiki v2026.11.8 (11/23): 에이전트용 안전장치
- **`obsidian-wiki undo`**: 볼트의 **마지막 변경을 한 번에 되돌린다.**
- **`memory_forget`**: MCP로 페이지를 지우되 **복구 가능한 삭제.** `memory_write_many`로 여러 페이지를 한꺼번에 쓰는 도구도 생겼다.
- **`WIKI_WRITE_HOOK`**: 운영자가 정한 규칙으로 **쓰기 직전에 페이지를 거부하거나 고쳐 쓴다.** 예: 특정 폴더 쓰기 금지, 금지어 제거.
- 웹 뷰어에 **볼트 전환, 받은편지함, Ask(질문), 인사이트** 추가. ‘추론된·애매한 링크’를 따로 표시하고, 링크마다 **출처 기록**을 본다. 검색은 답마다 범위를 보여 주고 특정 폴더만 찾을 수 있다.
- `[[페이지#제목]]` 같은 **깨진 제목 링크 점검**, 대화 압축 직전 기억을 붙잡는 훅도 들어갔다.

## 왜 중요한가
지난번 저장하신 **LLM Wiki·vault-bridge 계열**(에이전트가 볼트를 기억 장소로 쓰는 흐름)과 이어진다. 지금 이 신문을 만드는 것도 Grok Bot이다. 봇이 볼트에 **직접 쓸 수 있게 되면** 질문은 “연결할까”에서 **“실수하면 어떻게 되돌리나”**로 바뀐다. 현실적인 순서는 이렇다. ① 봇 전용 폴더(예: `Inbox/AI`)를 만들어 **새 노트만 쓰게** 하고, ② 기존 노트 수정은 Git이나 undo가 있는 환경에서만 허용하고, ③ 삭제는 복구 가능한 방식만 쓴다. 한 사용자의 지적처럼 **봇이 돌아가는 컴퓨터와 볼트가 있는 컴퓨터가 다르면** 공식 플러그인이 가장 안전한 통로다.
