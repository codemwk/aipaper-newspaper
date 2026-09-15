---
title: "Ar9av/obsidian-wiki — 에이전트 스킬로 키우는 LLM Wiki(크로스 에이전트)"
date: 2026-09-16T07:35:00+09:00
category: "Second Brain"
slug: "ar9av-obsidian-wiki-skills"
summary: "Karpathy LLM Wiki 패턴의 스킬 프레임워크. 마크다운 스킬만으로 Claude Code·Cursor·Codex·Gemini CLI 등이 볼트를 컴파일·질의. 런타임·벤더 락인 없음. ★3k+."
---

## 한줄 요약
[Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki)는 Karpathy **LLM Wiki** 아이디어를 **에이전트 스킬(마크다운)** 세트로 구현한다. 폴더를 가리키고 “기억하라”고 하면, 원재료를 연결된 마크다운 위키로 **컴파일**하고 `/wiki-query`·`/wiki-digest`로 묻는다.

## 핵심 설계
- 모든 스킬이 파일이라 Claude Code·Cursor·Codex·Windsurf·Gemini CLI 등 **에이전트만 바꾸면** 동일 볼트 유지. `setup.sh`가 스킬 디스커버리.
- 흐름: `/wiki-ingest` → 증류·링크 → `/wiki-query` / `/wiki-narrate` / `/wiki-digest week`.
- 크로스 에이전트 이력: `/wiki-codex "주제"`처럼 **다른 에이전트 세션에서 토픽만 뽑아** 위키에 넣는 경로(PyPI `obsidian-wiki` 문서에도 동일 패턴).
- Obsidian은 뷰어(그래프·백링크). 소유권은 로컬 마크다운.

## 왜 중요한가
어제 다룬 GD4AI **플러그인**(PPR 검색·임베딩 없음)과 같은 테마다. 차이는 실행면: 플러그인 UI vs **어느 코딩 에이전트든 스킬로 성장**. 퍼시스턴트 위키를 짓는 사용자에게는 “RAG 재질의” 대신 **컴파일·유지보수(린트·중복·주간 다이제스트)**가 품질 변수다.

## 기억할 것
- 저장소: [github.com/Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki)
- 원패턴: [Karpathy llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
