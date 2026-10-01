---
title: "Second Brain/PKM: mcp-obsidian — 볼트를 MCP로 열어 에이전트에 붙이기(~4.5K★)"
date: 2026-10-02T07:09:00+09:00
category: "Second Brain/PKM"
slug: "mcp-obsidian-bridge"
summary: "MarkusPfundstein/mcp-obsidian이 Obsidian Local REST API 플러그인 위로 MCP 서버를 얹는 사실상 표준 경로. 2026-10-02 ~4.5K★. 로컬 볼트↔Claude/Cursor 연결의 기본 레고."
---

## 한줄 요약
세컨드 브레인 쪽에서 MCP 수요가 커지며 [`MarkusPfundstein/mcp-obsidian`](https://github.com/MarkusPfundstein/mcp-obsidian)이 계속 쓰이는 브리지다. 설명: Obsidian REST API 커뮤니티 플러그인을 통해 볼트와 대화. 2026-10-02 `gh` 기준 **4,457★**, 최근 푸시도 활발.

## 제품으로 보면
- 구조: Obsidian 앱 + Local REST API → MCP 서버 → Claude Desktop·Cursor 등 클라이언트.
- 대안 축: 앱 안에 MCP를 내장하는 플러그인형(istefox/obsidian-mcp-connector 등), 파일시스템 직결 Rust 바이너리(lstpsche/obsidian-mcp) — 트레이드오프는 **앱 의존 vs 속도·오프라인**.
- LLM Wiki·Karpathy식 위키 플러그인(어제 다룸)과 역할이 다름: 위키가 **구조**, MCP가 **에이전트 I/O**.

## 왜 중요한가
퍼스널 OS에서 “읽기 전용 RSS 신문” 다음에 오는 단계는 **에이전트가 내 노트에 쓸 수 있는가**다. MCP-Obsidian은 그 최소 연결 상자다. 권한·삭제·경로 allowlist는 직접 잠가야 한다.

## 기억할 것
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)
