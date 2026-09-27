---
title: "GitHub: Vercel AI SDK 7 — WorkflowAgent·HarnessAgent로 ‘프로덕션 에이전트’ 두께"
date: 2026-09-28T07:12:00+09:00
category: "GitHub"
slug: "vercel-ai-sdk-7-agents"
summary: "AI SDK 7(2026-06-25 블로그, 주간 DL 1,600만+ 주장). WorkflowAgent 내구성, 툴 승인·타임아웃·SandboxSession, HarnessAgent(Claude Code·Codex 등), MCP Apps, realtime·video experimental."
---

## 한줄 요약
[Vercel AI SDK 7](https://vercel.com/blog/ai-sdk-7)은 채팅 헬퍼를 넘어 **오래 가는 에이전트 런타임**을 표준화한다. 배포 중에도 이어지는 `WorkflowAgent`, 사람/정책 툴 승인, Claude Code·Codex를 감싸는 `HarnessAgent`, MCP Apps UI. “프로토타입 에이전트”와 “프로덕션 에이전트” 사이의 뼈대다.

## 한 줄로 짚는 축
- **개발**: `reasoning` 통일 옵션, 툴별 typed context, `uploadFile`/`uploadSkill`, MCP Apps(iframe UI), TUI.
- **실행**: 툴 승인(HMAC 옵션), `@ai-sdk/workflow` 내구성, total/step/chunk/tool 타임아웃, `SandboxSession`.
- **하네스**: Codex·Claude Code·Pi 등을 `HarnessAgent` 한 인터페이스로.
- **관측**: 전역 telemetry, Node tracing channel, step 성능 통계.
- **확장**: provider-agnostic realtime, experimental `generateVideo`.

## 왜 중요한가
스킬·MCP가 많아질수록 앱 쪽은 **승인·재개·관측·샌드박스**가 없으면 사고난다. Anthropic·OpenAI 정렬 이슈가 나오는 주에, SDK 7은 “모델 바깥 가드레일”을 코드로 고정하는 레이어로 읽힌다. `npx @ai-sdk/codemod v7` 마이그레이션 경로가 공식.

## 기억할 것
- [vercel.com/blog/ai-sdk-7](https://vercel.com/blog/ai-sdk-7) · `pnpm add ai@latest`
