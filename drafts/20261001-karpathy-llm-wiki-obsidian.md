---
title: "세컨드 브레인/PKM: Karpathy LLM Wiki — Obsidian 커뮤니티 플러그인으로 들어오는 위키화(다운로드 ~56K)"
date: 2026-10-01T07:08:00+09:00
category: "세컨드 브레인/PKM"
slug: "karpathy-llm-wiki-obsidian"
summary: "Obsidian Community Plugin Karpathy LLM Wiki(green-dalii). 노트·PDF·Office→wiki/ 엔티티·컨셉 페이지, PPR 그래프 검색, 임베딩/벡터DB 없음. 다운로드 ~56K, v1.27.2. GitHub green-dalii/obsidian-llm-wiki ★~676."
---

## 한줄 요약
Andrej Karpathy가 제안한 **LLM Wiki** 패턴을 **Obsidian 안에서** 돌리는 커뮤니티 플러그인이 올라와 있다([플러그인 페이지](https://community.obsidian.md/plugins/karpathywiki)). 원본 노트는 건드리지 않고 `wiki/` 아래 소스·엔티티·컨셉 페이지를 만들고, 질의응답은 위키링크 그래프 위 **Personalized PageRank**로 컨텍스트를 고른다. 임베딩·벡터 DB 없이, 로컬 Ollama/LM Studio도 가능. 페이지 표기 **Downloads ~56k**, 현재 버전 **1.27.2**(2026-10-01 확인). 저장소 [green-dalii/obsidian-llm-wiki](https://github.com/green-dalii/obsidian-llm-wiki) ★~676.

## 제품으로 보면
- **설치**: Community plugins → Karpathy LLM Wiki → 프로바이더 키(또는 로컬) → Ingest.
- **인제스트**: Markdown + PDF + 이미지 + Office(MinerU 백엔드 등). UI·위키 출력 **11개 언어**(한국어 포함).
- **유지보수**: Lint + Smart Fix All(중복·죽은 링크·고아 페이지).
- **차별점(자사 표)**: nashsu/llm_wiki(데스크톱)·CLI 스킬형 구현과 달리 **원클릭 Obsidian 플러그인**.

## 왜 중요한가
사용자가 LLM Wiki를 직접 만들고 싶다고 했던 관심과 직결된다. 에이전트 스킬형 위키와 **에디터 내장형**이 동시에 성숙하는 구간이다.

## 기억할 것
- [Community plugin](https://community.obsidian.md/plugins/karpathywiki) · [GitHub](https://github.com/green-dalii/obsidian-llm-wiki) · Karpathy LLM Wiki 원개념
