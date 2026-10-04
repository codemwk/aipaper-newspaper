---
title: "세컨드 브레인/PKM: PKM Assistant — Obsidian 볼트 안에 사는 에이전트, ‘프롬프트를 전부 보여 주는’ 기억 v3"
date: 2026-10-05T07:11:00+09:00
category: "세컨드 브레인 / PKM"
slug: "pkm-assistant-obsidian-agents"
summary: "JDHole/pkm-assistant v2.3.1(GPL-3.0, 무료). 에이전트별 brain index·영구 메모·세션 아카이브·L1/L2/L3 요약. Prompt Inspector로 시스템 프롬프트 섹션별 토큰 확인·수정. 9개 플랫폼(Ollama·LM Studio 로컬 포함), 내장 MCP 도구 23개, 하위 에이전트 위임, 웹·볼트 딥리서치. 현재 BRAT/ZIP 설치, 다운로드 155."
---

## 한줄 요약
[PKM Assistant](https://community.obsidian.md/plugins/pkm-assistant)는 Obsidian 볼트 **안에서** 여러 AI 에이전트를 만들고 돌리는 플러그인이다. 슬로건이 인상적이다: “마법은 없다. 당신의 에이전트는 **프롬프트**다. 그 재료를 보여 줄 테니 원하는 대로 바꿔라.” 작은 1인 프로젝트(다운로드 155, v2.3.1)지만, 지금까지 다룬 LLM Wiki·Copilot 계열과 결이 다르다.

## 무엇이 있나
- **Prompt Inspector**: 모델에 보내는 시스템 프롬프트를 섹션별로 펼치고 **토큰 수를 보여 주며 직접 수정**. 숨은 중간층이 없다.
- **Memory v3**: 에이전트마다 brain index, 영구 메모 노트, 세션 아카이브, **L1/L2/L3 계단식 요약** — 세션을 넘어 맥락이 이어진다.
- **멀티 에이전트·위임**: 성격·역할·도구가 다른 에이전트를 탭으로 전환. 리서치 같은 일은 **더 싼 작은 모델의 하위 에이전트**에 넘겨 토큰 절약. 에이전트끼리 주고받는 ‘메일’도 볼트 안 마크다운.
- **스킬·딥리서치**: 스킬은 마크다운 파일. 웹·볼트 병렬 리서치 후 **인용문+URL/위키링크(그리고 ‘지식의 빈틈’)**를 담은 살아 있는 리포트 노트 생성.
- **모델·도구**: Anthropic, OpenAI, Gemini, DeepSeek, Groq, OpenRouter, xAI, **Ollama·LM Studio(완전 로컬)**. 내장 MCP 도구 23개 + 외부 MCP 서버 연결.
- **보안·프라이버시**: 텔레메트리 없음, 경로 탈출 차단, 키 마스킹, 에이전트별 승인(YOLO / 경계에서만 묻기 / 모두 묻기). 단 API 키가 볼트 내 `.pkm-assistant/settings.json`에 저장되므로 **볼트 동기화·공유 시 주의**.

## 왜 중요한가
Karpathy식 LLM Wiki가 “지식을 위키로 컴파일”하는 쪽이라면, PKM Assistant는 **“볼트를 에이전트의 사무실로”** 만드는 쪽이다. 특히 Prompt Inspector는 퍼스널 OS 제품을 설계할 때 참고할 UI 패턴 — 사용자가 에이전트의 기억과 지시를 **눈으로 보고 고칠 수 있는가**가 신뢰의 핵심이 된다. 저자 스스로 “비개발자가 Claude Code로 100% 바이브 코딩”했다고 밝힌 점도 시대를 보여 준다.

## 기억할 것
- 아직 커뮤니티 카탈로그 승인 전 — BRAT(베타 플러그인 설치기) 또는 ZIP 수동 설치. 데스크톱 전용.
- [Obsidian Community: PKM Assistant](https://community.obsidian.md/plugins/pkm-assistant) · [GitHub JDHole/pkm-assistant](https://github.com/JDHole/pkm-assistant)
