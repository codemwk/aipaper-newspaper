---
title: "librarian-mcp — Karpathy LLM Wiki를 Obsidian 사서 MCP로 제품화"
date: 2026-09-19T07:45:00+09:00
category: "Second Brain"
slug: "librarian-mcp-llm-wiki"
summary: "ngmeyer/librarian-mcp. 볼트/마크다운 폴더에 trigram 검색·백링크·BFS·Louvain 클러스터·D3 그래프·자동 wikilink. Obsidian 미실행 단독 바이너리. LLM Wiki 패턴의 MCP 실현."
---

## 한줄 요약
[ngmeyer/librarian-mcp](https://github.com/ngmeyer/librarian-mcp)는 Andrej Karpathy식 **LLM Wiki** 패턴을 **MCP 서버**로 만든 프로젝트다. Claude 등 에이전트에게 옵시디언 볼트(또는 일반 마크다운 폴더)의 **사서** 역할을 준다.

## 무엇이 바뀌었나
- **단독 바이너리**: 파일을 직접 읽는다. Obsidian을 켜 둘 필요 없고, 켜 둔 상태와도 충돌하지 않는다고 설명한다.
- 도구 예: trigram 전문 검색, 백링크/아웃링크, daily note, 태그 통계, orphan·hub·bridge, **BFS 순회·최단 경로**, Louvain **커뮤니티 탐지**, D3 **인터랙티브 그래프 HTML**, MarkItDown 기반 import, `library_suggest_links`(미링크 멘션).
- 포인트: 임베딩 RAG에만 의존하지 않고 **위키링크 그래프 + 로컬 검색**으로 “이미 정리된 지식”을 에이전트가 인용하게 한다. 본지가 다룬 Ar9av obsidian-wiki·vault-bridge·obsidian-second-brain과 **같은 문제, 다른 인터페이스(MCP)**.

## 왜 중요한가
세컨드 브레인 경쟁은 “노트 앱”이 아니라 **에이전트가 볼트를 깨지 않고 읽고 링크하게 하는 프로토콜**로 옮겨 갔다. librarian은 그 중 **그래프·사서 UX**에 특화. 스타 수는 아직 작아(조회 시점 수십) 실험 단계로 읽되, 패턴 자체는 재사용 가치가 있다.

## 기억할 것
- [ngmeyer/librarian-mcp](https://github.com/ngmeyer/librarian-mcp) · 관련: Ar9av/obsidian-wiki, LLM Wiki gist 계열
