---
title: "Design: pen.dev — .pen 파일을 Git에 두고, MCP로 캔버스를 조작하는 에이전트 디자인"
date: 2026-09-28T07:03:00+09:00
category: "Design/UI·UX"
slug: "pen-dev-agentic-canvas"
summary: "pen.dev(구 Pencil). .pen 문서를 Git에 저장. 데스크톱/IDE 호스트에 외부 MCP 클라이언트 연결. get_editor_state·execute·browser 등 툴. 문서 최종 갱신 2026-09-24."
---

## 한줄 요약
[pen.dev](https://docs.pen.dev/getting-started/ai-integration)는 **에이전트가 직접 다루는 디자인 캔버스**다. 디자인은 `.pen` 파일로 남고, Claude Code·Codex·ChatGPT 등 외부 클라이언트가 **로컬 MCP**로 연결해 `execute`로 편집한다. Figma MCP가 “디자인→코드”라면, pen.dev는 **디자인 파일 자체가 에이전트 워크스페이스**다.

## 어떻게 붙나
- **통합 에이전트**: 데스크톱 앱에서 `.pen`을 열고 모델·프롬프트로 변형.
- **외부 MCP**: 앱/IDE 확장 실행 → Settings→MCP에서 클라이언트 활성화 → 클라이언트에 `pencil` 서버 표시 확인. Unix 소켓(macOS/Linux)·네임드 파이프(Windows).
- **공개 툴(문서)**: `get_style`, `read_skill`, `get_app_state`, `execute`; 데스크톱 타겟 시 `browser`; `-enable_spawn_agents` 시 `spawn_agents`.
- **주의**: 잘못된 문서를 고치지 않으려면 프롬프트에 `.pen` 전체 경로를 넣고 `get_app_state()`로 활성 문서를 확인하라(공식 트러블슈팅).

## 왜 중요한가
디자인 산출물이 **바이너리 SaaS에만** 있으면 에이전트·CI가 끼어들기 어렵다. `.pen`+Git+MCP는 “디자인도 코드처럼 브랜치·리뷰·자동화”하는 실험이다. 대시보드·랜딩 UI를 에이전트 함대에 맡길 때, Figma·Framer와 **병렬로 둘 후보**다.

## 기억할 것
- [docs.pen.dev AI Integration](https://docs.pen.dev/getting-started/ai-integration) (Last updated Sep 24, 2026)
