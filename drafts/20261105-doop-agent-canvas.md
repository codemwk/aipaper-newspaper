---
title: "디자인: doop — 사람과 AI 에이전트가 같은 캔버스를 ‘실시간으로’ 고치는 오픈소스 디자인 툴"
date: 2026-11-05T07:03:30+09:00
category: "디자인"
slug: "doop-agent-canvas"
summary: "doop은 Paper.design의 무료 자체 호스팅 대안을 표방하는 오픈소스 디자인 툴이다. 캔버스의 각 프레임이 실제 HTML이고, 내장 MCP 서버로 에이전트가 프레임을 직접 고치며 진행 상황이 사람 화면에 실시간으로 보인다. 커서·코멘트·undo 공유, 6개 모델 계열 지원, docker compose 한 줄 실행. 11/1 데스크톱 v0.11.0. 라이선스는 AGPL-3.0."
---

## 한줄 요약
대부분의 디자인 툴은 “AI가 만들고 → 사람이 받아서 고친다”는 순서다. **doop**은 그 순서를 없앴다. 사람과 에이전트가 **같은 캔버스를 동시에** 편집한다([Not a Tech Guy 11/4](https://www.notatechguy.com/doop-open-source-canvas-lets-ai-agents-design-live-with-humans/)).

## 어떻게 동작하나
- **프레임 = 실제 HTML**: 캔버스는 프레임으로 나뉘고, 각 프레임은 샌드박스 iframe 안에서 돌아가는 라이브 HTML이다. 목업이 아니라 바로 코드다.
- **MCP 내장**: 외부 에이전트(Claude Code 등)가 MCP로 프레임에 직접 수정을 쓰고, 그 과정이 사람 화면에 실시간 반영된다.
- **내장 Doop Agent**: GPT, Claude, Gemini, DeepSeek, Kimi, Qwen 지원.
- **멀티플레이**: 라이브 커서, 따라가기 모드, 프레임별 ‘편집 중’ 표시, undo/redo, 스레드 코멘트, 활동 피드. 기본은 비공개, 이메일 초대나 보기/코멘트/편집 권한 링크로 공유.
- **설치**: `docker compose up` 한 줄, 내장 Postgres로 외부 서비스 없이 실행(프로젝트 설명 기준). 11/1 데스크톱 v0.11.0.
- **현황**: 별 약 1,700개, 라이선스 **AGPL-3.0**([저장소](https://github.com/kgoedecke/doop)).

## 왜 중요한가
지난번 저장하신 **Figma Agent·Studiolo** 같은 ‘캔버스 위 에이전트’ 흐름의 오픈소스 버전이다. Figma code layers가 상용 쪽에서 디자인→코드 간격을 줄인다면, doop은 **내 서버에서, 내가 고른 모델로** 같은 걸 해 볼 수 있게 한다. ANDRSN STUDIES 같은 시안 작업을 에이전트와 함께 라이브로 다듬기에 맞는 형태다.

## 주의
iframe 샌드박스와 MCP 접근 제어는 README에만 설명돼 있고 독립 검증은 없다. 모델이 만든 HTML을 돌리는 도구라 격리가 핵심이다. AGPL은 수정해 서비스로 제공하면 소스 공개 의무가 생긴다.
