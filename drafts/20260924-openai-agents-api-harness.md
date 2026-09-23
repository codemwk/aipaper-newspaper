---
title: "AI Models: OpenAI Agents API — Codex 하네스를 관리형 API로"
date: 2026-09-24T07:12:00+09:00
category: "AI Models"
slug: "openai-agents-api-harness"
summary: "OpenAI Agents API 퍼블릭 베타(2026-09-10). Codex와 동일 하네스. MCP·서브에이전트·compaction·tool search. 호스티드 샌드박스 또는 Blaxel/E2B/Vercel 등. 추가 API 수수료 없음(토큰·툴만)."
---

## 한줄 요약
[OpenAI Agents API](https://openai.com/index/introducing-the-agents-api/)는 Codex를 돌리던 **에이전트 하네스+인프라**를 개발자 API로 연 퍼블릭 베타다. 세션 하나에 모델·툴·환경을 넣고, OpenAI가 컨텍스트·툴·서브에이전트 조율을 유지한다.

## 핵심 기능
- `sessions.create`로 태스크·모델·툴·환경 지정. 예시에 **MCP** 툴 타입.
- **멀티에이전트**: 서브에이전트 병렬, 각자 컨텍스트.
- **장시간**: 컨텍스트 한계 접근 시 자동 compaction.
- **툴 효율**: tool search로 정의 지연 로드, programmatic tool calling으로 병렬·필터.
- **환경**: OpenAI 호스티드 샌드박스 또는 Blaxel·Cloudflare·Daytona·DigitalOcean·E2B·Modal·Oracle·Runloop·Vercel 등 파트너.
- 하네스 오픈소스(Codex). **Agents API 추가 수수료 없음** — 토큰·툴 사용분만.

## 왜 중요한가
트레이딩 MCP·퍼스널 에이전트·대시보드 OS처럼 “하루 이상 도는 일”에 필요한 층이다. 직접 오케스트레이션을 짜지 않고 **검증된 Codex 하네스**를 빌려 쓸 수 있게 됐다.

## 기억할 것
- [Introducing the Agents API](https://openai.com/index/introducing-the-agents-api/) · [MCP connections 문서](https://developers.openai.com/api/docs/guides/agents-api/tools/mcp)
