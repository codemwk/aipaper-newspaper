---
title: "디자인/UI·UX·GitHub: OpenPencil — .fig 열고 AI·MCP 붙인 오픈소스 디자인 에디터(~8.7K★)"
date: 2026-09-30T07:07:00+09:00
category: "디자인/UI·UX"
slug: "openpencil-ai-editor"
summary: "open-pencil/open-pencil. AI-native 오픈소스 에디터. .fig/.pen 읽기·쓰기, 100+ AI 툴, CLI·MCP·Vue SDK, WebRTC P2P 협업. Tauri ~15MB. 데모 app.openpencil.dev. 2026-09-29 기준 ★~8.7K."
---

## 한줄 요약
[open-pencil/open-pencil](https://github.com/open-pencil/open-pencil)은 **오픈소스 AI 네이티브 디자인 에디터**다. 네이티브 **`.fig`·`.pen`**을 열고, 채팅으로 노드를 만들고 고치는 **100+ 도구**, headless CLI·XPath·**MCP 서버**, Claude Code/Codex/Gemini CLI 연동, 토큰 추출·JSX/Tailwind 내보내기, Vue SDK까지 한 툴킷으로 묶는다. 데스크톱은 Tauri v2(~15MB), 웹 데모는 [app.openpencil.dev/demo](https://app.openpencil.dev/demo).

## 제품으로 보면
- **모델 연결**: OpenRouter·Anthropic·OpenAI·Google·DeepSeek 등 사용자 키/엔드포인트.
- **프로그래머블**: `openpencil tree|find|node`, Figma Plugin API `eval`, 린트·포맷 변환.
- **협업**: 서버·계정 없는 **WebRTC P2P** 커서/팔로우.
- **상태**: Active development — 쓸 수 있으나 거친 모서리 있음(README).

## 왜 중요한가
“Figma 대체” 구호보다, **파일을 에이전트·CI가 읽을 수 있는 프로그래밍 표면**으로 여는 쪽이 핵심이다. 디자인 시스템을 git에 두고 에이전트가 고치는 실험에 바로 꽂힌다.

## 기억할 것
- [GitHub](https://github.com/open-pencil/open-pencil) · [openpencil.dev](https://openpencil.dev) · [llms.txt](https://openpencil.dev/llms.txt)
