---
title: "enquire-mcp — Obsidian 메모리에 age_days·stale ‘신선도’를 붙이다"
date: 2026-09-21T07:05:00+09:00
category: "Second Brain"
slug: "enquire-mcp-freshness"
summary: "oomkapwn/enquire-mcp. 로컬 하이브리드 검색+PDF/OCR+Dataview/Bases. v3.10+에서 age_days·stale·선택적 recency-weight. 기본 읽기 전용, --enable-write로만 기록. Claude·Cursor·Codex·OpenClaw 공통 MCP."
---

## 한줄 요약
[enquire-mcp](https://github.com/oomkapwn/enquire-mcp) / [소개 사이트](https://oomkapwn.github.io/enquire-mcp/)는 Obsidian 볼트를 **에이전트 공용 메모리 MCP**로 만든다. 키워드는 단순 RAG가 아니라 **인용 경로 + 신선도(`age_days`/`stale`)**다.

## 지금 뭐가 뜨나
- 검색: BM25·TF-IDF·임베딩·RRF·(옵션) BGE 리랭크·HNSW/int8. 마크다운뿐 아니라 **PDF/OCR 페이지 인용**.
- 구조화 도구: Canvas 파싱, Dataview식 LIST/TABLE, Base 필터.
- **Freshness (v3.10 계열)**: 히트에 나이·stale 플래그, `obsidian_stale_notes`, 선택 `--recency-weight`.
- 기본 **읽기 전용**. 쓰기는 `--enable-write` 게이트. serve 중 enquire 자체 **아웃바운드 HTTP 0** 주장(클라이언트·터널은 별개).
- 설치: `npm i -g @oomkapwn/enquire-mcp` → `enquire-mcp serve --vault …` / `configure --client …`.

## 왜 중요한가
어제 obsidian-wiki가 “컴파일형 위키 스킬”이었다면, 오늘은 **검색 결과에 유통기한을 찍는 메모리 계층**이다. 세컨드브레인·퍼스널 AI 저널에서 틀린 답의 상당수는 “예전에 맞았던 노트”다.

## 기억할 것
- [GitHub](https://github.com/oomkapwn/enquire-mcp) · [docs 사이트](https://oomkapwn.github.io/enquire-mcp/) · [v3.10 PR](https://github.com/oomkapwn/enquire-mcp/pull/276)
