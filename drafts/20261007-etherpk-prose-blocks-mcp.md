---
title: "세컨드 브레인 / PKM: EtherPK — Obsidian식 ‘글’과 Logseq식 ‘블록’을 한 문서에, 종단간 암호화 동기화와 로컬 MCP까지"
date: 2026-10-07T07:10:00+09:00
category: "세컨드 브레인 / PKM"
slug: "etherpk-prose-blocks-mcp"
summary: "9/30 공개 후 이번 주 Show HN에 오른 개인 PKM. 평문 Markdown 위에 문단·아웃라이너 블록 혼용, 중첩 위키링크, 로컬 폴더 또는 E2E 암호화 동기화, PWA·CRDT 공동편집·정적 사이트 발행. AGENTS.md를 볼트 옆에 생성하고 MCP 서버로 로컬 시맨틱 검색. 보호 문서는 에이전트 접근 차단."
---

## 한줄 요약
**EtherPK**(Ether Personal Knowledge)는 1인 개발자가 9월 30일 공개한 Markdown 기반 PKM이다. 이번 주 Hacker News ‘Show HN’에 “Obsidian·Logseq 대안”으로 올랐다([공식 블로그](https://blog.etherpk.com/introducing-etherpk), [HN 요약](https://wpnews.pro/news/show-hn-etherpk-an-obsidian-and-logseq-alternative-with-prose-and-blocks)). 눈에 띄는 건 **“에이전트가 내 노트를 다루는 방식”을 처음부터 설계에 넣었다**는 점이다.

## 핵심 기능
- **글 + 블록 한 문서에**: 블로그처럼 문단·제목으로 쓰다가, 아이디어 캡처할 땐 Logseq·Roam 같은 **아웃라이너 블록**으로. 제목 계층(H1·H2…)에서도 링크 관계를 추론한다.
- **중첩 위키링크**: `[[[[Nested]] Wikilinking]]`처럼 개념 안에 개념을 넣어 계층을 만든다. 백링크·태스크 패널은 개념별 필터.
- **데이터 소유권**: 표준 GFM Markdown. 내 컴퓨터 폴더(Chromium 파일 시스템 API) 또는 브라우저 저장소(OPFS)에 평문으로 두거나, 동기화 서버를 쓰면 **기기에서 암호화한 뒤 전송(E2E)** — 회사도 제목·파일명조차 못 본다. 대신 복구 코드를 잃으면 복구 불가.
- **어디서나**: 웹 우선, 모바일 **PWA**, 안드로이드 공유 대상으로 빠른 캡처. 회사 방화벽용 Docker·Node 빌드와 클라이언트 소스 공개(소스 공개형)를 예고.
- 그 밖에 CRDT **실시간 공동 편집**, 그래프 하나로 여러 **정적 사이트 발행**, 텔레메트리 없음.

## 에이전트 연동 — 여기가 포인트
- 폴더형 그래프 옆에 **`AGENTS.md`**를 자동 발행해, 에이전트가 노트 구조와 작업 규칙을 먼저 읽게 한다.
- MCP 서버 **`@appsoftwareltd/etherpk-mcp`**(헤드리스 클라이언트 포함)로 Claude Code·Codex·Cursor가 **로컬에서 시맨틱 검색(RAG)**하고 노트를 편집한다.
- **옵트인 원칙**: 에이전트는 일부러 연결해야만 쓰이고, 추가 암호로 잠근 **‘보호 문서’에는 접근할 수 없다**.

## 왜 중요한가
LLM Wiki를 Obsidian에서 돌리는 사람들이 부딪히는 두 벽은 **“에이전트가 볼트 규칙을 모른다”**와 **“민감한 노트까지 다 읽힌다”**였다. EtherPK는 AGENTS.md와 보호 문서로 이 둘을 기본값에서 해결하려 한다. 당장 갈아탈 일은 아니어도, 내 Obsidian 볼트에 **AGENTS.md 한 장과 ‘에이전트 금지 폴더’ 규칙**을 두는 건 오늘 바로 베낄 만한 아이디어다.

## 체크포인트
- 신생 1인 프로젝트다. 장기 유지·가격 정책은 아직 미지수 — 평문 Markdown·내보내기 덕분에 **탈출 비용이 낮다**는 점이 안전판.
