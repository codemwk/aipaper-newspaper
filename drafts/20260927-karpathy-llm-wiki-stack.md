---
title: "Second Brain: Karpathy LLM Wiki Stack — ‘컴파일된 위키’ 레퍼런스가 모이는 중"
date: 2026-09-27T07:08:00+09:00
category: "Second Brain"
slug: "karpathy-llm-wiki-stack"
summary: "Karpathy LLM Wiki 패턴: raw는 사람이, wiki는 LLM이 유지. ScrapingArt/Karpathy-LLM-Wiki-Stack 등 빌드 가이드·구현체 확산. RAG(매번 해석) vs 위키(미리 컴파일) 비유. 어제 claude-obsidian과 다른 ‘스택 지도’ 각도."
---

## 한줄 요약
Andrej Karpathy의 **LLM Wiki** 아이디어([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))를 실행 가능한 스택으로 묶은 레포·가이드가 계속 늘고 있다. 대표적으로 [ScrapingArt/Karpathy-LLM-Wiki-Stack](https://github.com/ScrapingArt/Karpathy-LLM-Wiki-Stack)은 Obsidian + Claude Code 기준으로 raw/wiki/스키마 3층을 정리한다. 어제 **claude-obsidian** 단일 스킬 소개와 달리, 오늘은 **패턴 지도**다.

## 패턴을 한 장으로
| 층 | 누가 쓰나 | 역할 |
|---|---|---|
| `raw/` | 사람 | 논문·클립·PDF — 불변 소스 |
| `wiki/` | LLM | 요약·엔티티·교차링크 — 복리 지식 |
| 스키마/Skill | 공동 | 파일링 규칙·린트·워크플로 |

핵심 비유: 전통 RAG는 **인터프리터**(질문마다 원문을 다시 해석), LLM Wiki는 **컴파일러**(미리 구조화해 두고 질의는 위키를 읽음). Obsidian은 IDE, LLM은 프로그래머.

## 왜 중요한가
AiPaper처럼 매일 기사가 쌓이는 사용자에게 “즐겨찾기만”으로는 복리가 안 된다. ingest→lint→query 루프를 에이전트 스킬로 고정하면, 3일 RSS 창 밖의 장기 기억이 생긴다.

## 기억할 것
- [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · [LLM Wiki Stack](https://github.com/ScrapingArt/Karpathy-LLM-Wiki-Stack) · [julianoczkowski 가이드](https://github.com/julianoczkowski/karpathy-llm-wiki)
