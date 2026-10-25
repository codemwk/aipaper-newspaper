---
title: "AI 도구: Anthropic이 ‘Agent Skills’를 리눅스재단 산하 AAIF에 기증 — 스킬 100만 개·설치 2.8억 회의 표준이 ‘한 회사 것’에서 ‘모두의 것’으로. OpenAI·허깅페이스·알리바바도 같은 날 프로젝트 기증"
date: 2026-10-26T07:06:00+09:00
category: "AI 도구"
slug: "aaif-agent-skills-donated"
summary: "10/22 Agentic AI Foundation(AAIF, 리눅스재단 산하)이 새 프로젝트 4개를 발표. Anthropic의 Agent Skills(SKILL.md 폴더 표준), OpenAI의 Open Responses(여러 모델 회사에 같은 형식으로 요청하는 규격), Hugging Face의 OpenEnv(에이전트 훈련 환경), Alibaba의 OpenSandbox(에이전트 실행 샌드박스). Anthropic은 Agent Skills가 ChatGPT·Cursor·GitHub Copilot·VS Code 등 70개 이상 플랫폼에 들어갔고, 스킬 100만 개가 공개돼 약 2억 8,000만 번 설치됐다고 밝혔다. AAIF 프로젝트는 1년 만에 3개→10개."
---

## 한줄 요약
에이전트에게 일을 가르치는 ‘스킬 폴더’ 표준이 **특정 회사 소유에서 중립 재단 소유로** 넘어갔다. MCP에 이어 두 번째 기증이다([Anthropic, 10/22](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)).

## Agent Skills가 뭐였더라
- **스킬 = 폴더 하나.** 그 안에 `SKILL.md`(이 일은 이렇게 한다는 설명서)와 필요한 스크립트·참고 자료를 넣으면, 에이전트가 필요할 때 꺼내 읽고 그 절차대로 일한다.
- Claude Code를 만들다 “일반 지식은 되는데 **회사 실무 절차**를 모른다”는 문제에서 출발. 2025년 10월 출시 후 몇 주 만에 개발자들이 GitHub에 수천 개를 올리고 Codex·Cursor·OpenCode용 로더를 만들었다. 2025년 12월 공개 표준으로 분리.

## 숫자와 이번 결정
| 항목 | 내용 |
|---|---|
| 채택 플랫폼 | 70개+ (ChatGPT, Cursor, GitHub Copilot, VS Code 등) |
| 공개된 스킬 | 약 100만 개 |
| 설치 횟수 | 약 2억 8,000만 회 |
| 기증 대상 | 이름·로고, GitHub 조직, agentskills.io 도메인 |
| 관리 | Anthropic·Google·OpenAI 등 엔지니어가 **개인 자격**으로 관리, 리드는 David Soria Parra·Mahesh Murag |
| 다음 로드맵(제안) | 버전 릴리스, 공식 제안 절차, **스킬 작성·설치자를 위한 보안 가이드** |

- AAIF 회원이 아니어도 표준을 쓰거나 기여할 수 있다.

## 같은 날 들어온 나머지 3개
([AAIF 발표](https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects), AGNTCon + MCPCon 북미, 산호세)
| 프로젝트 | 기증 | 쉽게 말하면 |
|---|---|---|
| **Open Responses** | OpenAI | OpenAI Responses API를 바탕으로, 요청·스트리밍 형식을 한 번 정해 두면 **여러 모델 회사에 거의 그대로** 보낼 수 있게 하는 공용 규격 |
| **OpenEnv** | Hugging Face | 에이전트를 강화학습으로 **훈련·평가하는 ‘연습장’**을 컨테이너로 만들어 서로 바꿔 끼우게 하는 틀(MCP·Gym 인터페이스) |
| **OpenSandbox** | Alibaba | 코딩·GUI 에이전트가 코드를 **안전하게 실행하는 격리 공간**. Docker·Kubernetes 런타임, 다국어 SDK |
- 이로써 AAIF는 MCP, AGENTS.md, goose, A2A 등과 함께 **1년 만에 10개 프로젝트**를 품게 됐다.

## 왜 중요한가
- **에이전트 스택의 ‘공용 부품’ 지도가 그려졌다**: 도구 연결(MCP) · 일하는 법(Skills) · 프로젝트 규칙(AGENTS.md) · 모델 호출 형식(Open Responses) · 훈련장(OpenEnv) · 실행 격리(OpenSandbox). 경쟁사들이 각자 한 칸씩 내놓고 중립 재단에 맡기는 모양새다.
- **스킬 보안이 다음 숙제**: 스킬은 스크립트를 포함할 수 있어, 남이 만든 스킬 설치는 남의 코드를 돌리는 것과 같다. 로드맵에 ‘설치자용 보안 가이드’가 들어간 이유.
- 사용자 입장: 한 번 써 둔 SKILL.md(예: 우리 브랜드 톤으로 보도자료 쓰기)가 **Claude·ChatGPT·Cursor를 오가도 계속 쓸 수 있는 자산**이 될 가능성이 커졌다. 같은 호 GitHub 트렌드 기사(구글·Anthropic의 공식 스킬 저장소)가 그 실물이다.

출처: [Anthropic — Donating Agent Skills to the AAIF (10/22)](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) · [AAIF — Four New Projects (10/22)](https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects)
