---
title: "GitHub Hot: Google AX — 에이전트 워크로드용 ‘K8s 감각’ 오케스트레이터"
date: 2026-09-25T07:10:00+09:00
category: "GitHub Hot"
slug: "google-ax-agent-orchestrator"
summary: "google/ax(~10.3k★). Declarative Task/Workspace/Gateway/Model. Agent Substrate 위 샌드박스·네트워크 펜스. ax apply / watch / ssh. 안정화 전 breaking change 경고."
---

## 한줄 요약
[google/ax](https://github.com/google/ax)는 Google의 **오픈 에이전틱 오케스트레이션 런타임**이다. YAML로 Task·Workspace를 선언하면 샌드박스·워크스페이스 배선·네트워크 펜스를 맡긴다. Kubernetes를 써 본 사람에게 `ax apply`가 익숙하게 느껴지도록 설계.

## 핵심 프리미티브
- **Task** — 격리 샌드박스에서 에이전트 실행(CPU/메모리 한도)
- **Workspace** — Git 레포·MCP·스킬 패키지를 미리 배선해 에이전트가 warm start
- **Gateway** — 아웃바운드 호스트 allowlist
- **Model** — 플랫폼 LLM·시크릿(K8s secret) 설정
- 운영: `ax suspend`/`resume`, `ax ssh`로 실행 중 에이전트 관찰

> README 경고: 코어 개념이 아직 다듬어지는 중이며 **안정 릴리즈 전 major breaking change** 가능.

## 왜 중요한가
에이전트가 “노트북에서 한 세션”을 넘어 **클러스터 워크로드**가 되면, 마이크로서비스도 배치잡도 아닌 제3의 런타임이 필요하다. AX는 그 레이어를 공개 스펙으로 던진 실험.

## 기억할 것
- [GitHub](https://github.com/google/ax) · [agentexecutor.io](https://agentexecutor.io)
