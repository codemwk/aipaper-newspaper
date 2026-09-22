---
title: "llm-wiki-kit — PDF·URL·유튜브를 넣어 ‘세션을 넘는’ Karpathy LLM Wiki"
date: 2026-09-23T07:06:00+09:00
category: "Second Brain"
slug: "llm-wiki-kit-persistent"
summary: "iamsashank09/llm-wiki-kit. Karpathy LLM Wiki 패턴의 MCP 키트. pip install → init → serve. PDF·URL·YouTube 수집, [[wikilink]] 자동, SQLite FTS5, wiki_lint·wiki_graph. 마크다운 폴더라 Obsidian과 공존. 어제 obsidian-llm-wiki(6인 페르소나)와 다른 ‘키트형’ 각도."
---

## 한줄 요약
[llm-wiki-kit](https://github.com/iamsashank09/llm-wiki-kit)은 “매 채팅마다 논문을 다시 설명하는” 문제를 겨냥한다. 에이전트가 **위키를 유지**하고, PDF·URL·YouTube를 넣으면 교차 참조가 쌓인다. [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 패턴을 MCP 서버로 감싼 키트다.

## 어떻게 쓰나(개념만)
1. `pip install "llm-wiki-kit[all] @ git+https://github.com/iamsashank09/llm-wiki-kit.git"`
2. `llm-wiki-kit init --agent claude`로 위키 루트 생성
3. Claude/Codex/Cursor에 `llm-wiki-kit serve --root …` MCP 등록
4. “이 PDF ingest” → 페이지·인덱스·링크 생성. `wiki_lint`로 깨진 링크·고아 페이지 점검, `wiki_graph`로 HTML 지도.

## 어제 기사와 다른 점
- **9/22 obsidian-llm-wiki**: 볼트를 **6인 페르소나 MCP 팀**으로 컴파일하는 플러그인/헤드리스 스택.
- **오늘 llm-wiki-kit**: **폴더형 위키 + MCP serve**에 초점. 소스는 그냥 마크다운이라 Obsidian·VS Code에서 그대로 연다. 스타는 작지만(수십 대) 패턴이 명확하다.

## 왜 중요한가
세컨드 브레인 전쟁에서 “플러그인 하나”가 아니라 **위키를 누가 유지하느냐**가 쟁점이다. 에이전트가 책무(ingest·lint·그래프)를 지고 사람은 소스만 고르는 분업이 AiPaper·대시보드 메모리 모듈과 맞닿아 있다.

## 기억할 것
- [github.com/iamsashank09/llm-wiki-kit](https://github.com/iamsashank09/llm-wiki-kit) · Karpathy LLM Wiki 패턴
