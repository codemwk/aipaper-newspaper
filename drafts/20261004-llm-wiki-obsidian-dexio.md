---
title: "PKM: Obsidian에서 Karpathy LLM Wiki 돌리기 — raw/wiki/SCHEMA·ingest·query·lint (Dexio 가이드 2026-10-01)"
date: 2026-10-04T07:10:00+09:00
category: "세컨드 브레인 / PKM"
slug: "llm-wiki-obsidian-dexio"
summary: "Dexio(2026-10-01): Obsidian 볼트에 raw·entities/concepts·SCHEMA.md·index.md·log.md. 유지자는 Claude Code/Codex, Hermes llm-wiki, Karpathy Wiki 플러그인(~56k DL) 등. 그래프·린트로 위키 형태 점검."
---

## 한줄 요약
[Dexio 가이드](https://dexio.wiki/guides/llm-wiki-obsidian/)(2026-10-01 업데이트): Karpathy LLM wiki 패턴을 Obsidian에 옮기려면 **전용 볼트(또는 최상위 폴더)**에 `raw/`(에이전트가 안 고침), 에이전트가 쓰는 wiki 페이지, **`SCHEMA.md` / `index.md` / `log.md`**를 둔다. 연산은 **ingest · query · lint** 세 가지. 유지자는 (1) 폴더에서 돌리는 Claude Code/Codex (2) Hermes 번들 `llm-wiki` 스킬 (3) Obsidian 커뮤니티 플러그인(Karpathy LLM Wiki ~**56k** 다운로드, Auto LLM Wiki 등 — 가이드가 2026-10-01 기준 수치 인용). Obsidian은 **읽기·그래프**, 에이전트는 **마크다운 파일**.

## 실무로 보면
- **레이아웃 예**: `entities/ concepts/ comparisons/ queries/` + `raw/articles|papers|transcripts|assets`.
- **스키마**: 파일명·프론트매터·태그 화이트리스트·위키링크 최소 2개·200줄 분할·모순 시 양측 날짜 병기.
- **세션 시작 루틴**: SCHEMA + index + log 최근 20–30줄 읽고 시작 — 중복 페이지 방지. Hermes는 raw sha256으로 재ingest 스킵.
- **그래프**: path 그룹·orphan·missing file 필터로 허브/공백 확인.
- **한계**: 에이전트 2개가 동시에 index/log를 쓰면 충돌. 멀티에이전트·감사 추적이 필요하면 호스트형(Dexio MCP 등) 검토 — 가이드가 제품도 소개하므로 **패턴과 벤더를 분리**해서 읽을 것.

## 왜 중요한가
어제 Obsidian Copilot V4가 **채팅 UX**였다면, 오늘은 **위키 운영 계약(스키마)**. 사용자가 관심 두는 LLM Wiki를 “아이디어”에서 **폴더 규약+린트**로 고정하는 실용 브리핑이다.

## 기억할 것
- [Dexio: LLM wiki in Obsidian](https://dexio.wiki/guides/llm-wiki-obsidian/) · [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
