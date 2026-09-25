---
title: "Second Brain: claude-obsidian — 로컬 Markdown 위키를 Claude Code가 키운다"
date: 2026-09-26T07:08:00+09:00
category: "Second Brain / PKM"
slug: "claude-obsidian-second-brain"
summary: "AgriciDaniel/claude-obsidian(GitHub, ~15k★). Karpathy LLM Wiki 패턴. 소스 드롭 → 링크·인용 달린 Obsidian 페이지. wiki-ingest·query·lint·autoresearch 스킬. 벤더 락인 없는 로컬 퍼스트 Notion 대안 포지션."
---

## 한줄 요약
[claude-obsidian](https://github.com/agricidaniel/claude-obsidian)은 Obsidian + Claude Code(및 호환 스킬 호스트)용 **자기조직화 세컨드 브레인**이다. 자료를 넣으면 에이전트가 읽고 링크·파일링해 **소유권 있는 평문 Markdown 그래프**로 만든다. GitHub 기준 별 ~15k.

## 핵심 워크플로
- **패턴**: Andrej Karpathy [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — RAG로 매번 재검색하기보다 **한 번 컴파일된 위키를 유지**.
- **스킬 예**: `wiki`(볼트 진단·라우팅), `wiki-ingest`(소스→페이지+출처), `wiki-query`(볼트 근거만으로 답), `wiki-lint`(죽은 링크·고아·메타 공백), `autoresearch`(예산 있는 웹 리서치).
- **철학**: 사용자는 소싱·질문, LLM은 요약·교차참조·북키핑. Obsidian은 IDE, 에이전트는 프로그래머.

## 왜 중요한가
AiPaper·LLM Wiki 관심과 직결. kepano/obsidian-skills·llm-wiki-kit이 “플러그인·키트”였다면, 여기는 **Claude Code 스킬 번들로 볼트 운영체제**를 주는 쪽. 스타 수치는 시점마다 변하니 저장소에서 확인.

## 기억할 것
- [GitHub](https://github.com/agricidaniel/claude-obsidian) · [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
