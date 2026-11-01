---
title: "세컨드 브레인: LLM Wiki 플러그인 v4 — 로컬 위키는 그대로, 원하면 Cloudflare 무료 플랜에 ‘여러 에이전트가 같이 쓰는 위키’"
date: 2026-11-02T07:07:00+09:00
category: "세컨드 브레인/PKM"
slug: "llm-wiki-v4-hosted"
summary: "카파시식 LLM Wiki를 Claude Code·Codex·Cursor 등에서 쓰게 해 주는 praneybehl/llm-wiki-plugin이 v4.0(10/29)을 냈다. 선택형 호스팅 위키(Workers Free에서 동작), 충돌 시 409+diff를 돌려주는 원자적 동시 쓰기, BM25+벡터 하이브리드 검색, MCP 8도구·에이전트별 토큰, 마이그레이션 CLI, 기본 꺼진 ‘결정 레이어’. 로컬 위키는 마이그레이션 불필요."
---

## 한줄 요약
지난번 저장하신 LLM Wiki·Obsidian 에이전트 관심과 이어지는 소식이다. 개인 노트북 안의 LLM Wiki를 **여러 에이전트가 동시에 읽고 쓰는 공유 위키**로 키우는 길이 열렸다([릴리스 노트](https://github.com/praneybehl/llm-wiki-plugin/releases)).

## v4.0에서 바뀐 것
- **호스팅 위키(선택)**: Cloudflare Worker 하나 + 위키마다 SQLite Durable Object. 배포 버튼과 비밀값 하나(`ADMIN_TOKEN`). **Workers 무료 플랜에서 동작**.
- **안전한 동시 쓰기**: create·put·edit·append·move 등 원자적 커밋. `append`는 충돌이 없고, 그 밖의 충돌은 **HTTP 409 + 현재 리비전 + diff**를 돌려준다. 커밋마다 작성자 기록.
- **하이브리드 검색**: 키워드(BM25) + 벡터를 RRF로 합침. 벡터가 빠지면 서버가 재전송.
- **에이전트 접속**: `/mcp`에 MCP 도구 8개, JSON API, 에이전트별 토큰, claude.ai 같은 클라이언트용 OAuth. 웹 UI에 검색·백링크·히스토리·diff·리뷰 플래그.
- **이사 도구**: 로컬→호스팅 `import`(SHA-256 검증·재개), Git 커밋으로 남는 **pull 전용 미러**.
- **결정 레이어(기본 꺼짐)**: 검색 관련성·그래프 근거·신뢰 못 할 텍스트를 작은 결정 모델로 거르는 게이트.
- v4.0.1(같은 날): 배포 폼의 Vectorize 설정값(384차원·cosine) 안내 추가.

## 왜 중요한가
- 세컨드 브레인의 다음 문제는 ‘한 에이전트가 잘 쓰기’가 아니라 **‘여러 에이전트가 덮어쓰지 않기’**다. 409+diff, 작성자 기록, 읽기 전용 미러는 그 문제에 대한 실무형 답.
- 로컬 마크다운·스크립트는 그대로라 Obsidian 볼트와 병행 가능. 다만 호스팅을 켜면 노트가 Cloudflare로 올라가므로, 민감 노트는 로컬 위키에 남기는 분리 운영이 안전하다.
