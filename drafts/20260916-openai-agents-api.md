---
title: "OpenAI Agents API 퍼블릭 베타 — Codex 하네스를 관리형 API로"
date: 2026-09-16T07:25:00+09:00
category: "GitHub Hot"
slug: "openai-agents-api"
summary: "공식 2026-09-10. Agents API public beta. 세션·오케스트레이션·컨텍스트·샌드박스를 OpenAI가 운영. OpenAI 호스팅·셀프·E2B·Modal·Vercel 등. API 추가 수수료 없음(토큰·툴만)."
---

## 한줄 요약
[OpenAI(2026-09-10)](https://openai.com/index/introducing-the-agents-api/)가 **Agents API**(퍼블릭 베타)를 냈다. Codex를 돌리는 **관리형 하네스**를 `v1/agents/sessions` 한 호출로 쓸 수 있게 한 것이다.

## 무엇이 포함되나
- 개념: Agent(모델·지시·툴·MCP) / Environment(샌드박스) / Session(내구 작업) / Events·Items.
- 하네스가 하는 일: 명령·코드 실행, 스킬 적용, MCP·툴 연결, 작업 중 스티어링, 컨텍스트 요약, 서브에이전트 위임, 재개.
- 환경: **OpenAI 호스팅 샌드박스**, 자체 인프라, 파트너(Blaxel·Cloudflare·Daytona·DigitalOcean·E2B·Modal·Oracle·Runloop·Vercel 등).
- 과금: Agents API **추가 수수료 없음** — 모델 토큰·툴만. 베타 헤더 `OpenAI-Beta: agents=v1`.
- 주의: 현재 데이터 레지던시 **미국**, **ZDR 미지원**(셀프 샌드박스여도 Agents API ZDR 비대상 — 공식 문서).

## 왜 중요한가
어제·그제 다룬 오픈소스 하네스·MCP 프레임과 맞닿되, 여기는 **“하네스 운영을 벤더가 맡는”** 축이다. 빌더는 도구·지식·워크플로에 집중하고, 세션·복구·샌드박스는 API에 맡긴다. 락인·데이터 거버넌스는 트레이드오프로 남는다.

## 기억할 것
- [Introducing the Agents API](https://openai.com/index/introducing-the-agents-api/) · [Overview](https://developers.openai.com/api/docs/guides/agents-api/overview) · [Quickstart](https://developers.openai.com/api/docs/guides/agents-api/quickstart)
