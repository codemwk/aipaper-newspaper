---
title: "Second Brain: nashsu/llm_wiki — 문서→지속 위키 데스크톱, 스타 ~20K (RAG 대안)"
date: 2026-09-29T07:07:00+09:00
category: "Second Brain"
slug: "nashsu-llm-wiki-desktop"
summary: "GitHub nashsu/llm_wiki (~20,045★, 2026-09-28 갱신). 크로스플랫폼 데스크톱이 소스를 읽어 상호링크 위키를 점진 구축. Karpathy LLM Wiki — ‘매번 RAG’ 대신 북키핑을 LLM에. 로컬 Markdown 소유."
---

## 한줄 요약
[nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)는 문서를 넣으면 LLM이 **조직화된 상호링크 지식베이스**를 자동 유지하는 **크로스플랫폼 데스크톱** 앱이다(TypeScript, 작성 시점 GitHub API 기준 **약 20,045 stars**, 2026-09-28 활발히 갱신). 전통 RAG처럼 질문마다 처음부터 검색·답변하지 않고, **위키 페이지가 자산으로 쌓인다**.

## 왜 뜨나
- **Karpathy LLM Wiki** 패턴의 제품화: “어려운 건 생각보다 **북키핑**” — LLM이 링크·인덱스·정리를 맡음.
- 동시기에 [TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)(~27K★)가 Chat Memory·Skill·**LLM-Wiki**·Code-Graph를 팀 메모리로 묶는 등, “위키형 메모리”가 에이전트 인프라 키워드가 됨.
- Obsidian 플러그인·MCP 서버 계열([AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) 등)과 함께 **로컬 Markdown 소유** 스택이 선택지로 정리되는 중.

## 왜 중요한가
AiPaper·퍼스널 OS의 “읽은 뉴스가 다음날 사라지지 않게” 하려면, 채팅 로그가 아니라 **컴파일된 위키**가 필요하다. llm_wiki는 그 UX를 앱으로 포장한 대표 사례다.

## 기억할 것
- [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) · [Karpathy gist — LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
