---
title: "GitHub 이번 주: ‘대답’이 아니라 ‘승인’으로 끝나는 팀 에이전트 SoduWork, 코드베이스를 지식 그래프로 바꾸는 graphify, MCP로 조종하는 무료 영상 편집기 Concat"
date: 2026-11-25T07:45:00+09:00
category: "GitHub 트렌드"
slug: "github-soduwork-graphify-concat"
summary: "11/24까지 일주일 GitHub 상승 목록에서 아직 지면에 안 나온 세 저장소를 골랐다. SoduWork(약 7,600★, 일주일 +6,000)는 한 하네스가 일하고 다른 모델의 하네스가 검토한 뒤 사람이 서명해야 끝나는 팀용 에이전트 엔진이다. graphify(약 15만 3천★)는 코드·문서·SQL 스키마·PDF를 로컬에서 지식 그래프로 바꾸고 모든 연결에 신뢰도 표시를 붙인다. Concat(약 2만★)은 JSON-RPC API와 MCP로 에이전트가 조종하는 로컬 우선 무료 영상 편집기다."
---

## 한줄 요약
이번 주 GitHub 상위권은 여전히 에이전트 도구다. 반복해서 다룬 저장소(rea, orca, CLI-Anything, open-code-review 등)는 빼고, **새로 눈에 띈 세 개**를 쉬운 말로 정리했다([MostStarred 주간](https://moststarred.com/trending/week), [HIMIAO 주간 Vol.7](https://himiao.ai/en/news/2026-11-23-github-weekly-7), [GitStock 11/24](https://gitstock.org/trending/weekly/2026-11-24)).

## 1. SoduWork — “요청은 요청한 사람이 승인해야 끝난다”
- 저장소: [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork). 10/29에 만들어져 약 **7,600★**, 일주일에 **+6,046.** MIT 라이선스, 직접 설치(self-hosted).
- 구호가 핵심이다. **“채팅은 답으로 끝나지만, SoduWork의 요청은 요청한 사람이 서명해야 끝난다.”**
- 작동 방식:
  - **한 하네스가 일하고, 다른 모델의 하네스가 검토.** 예: Pi가 작업하고 OpenCode(다른 모델)가 수락 기준에 맞춰 검사, 떨어지면 이유와 함께 되돌린다.
  - 사람이 요청을 올리면 **AI가 수락 기준을 쓰고**, 나나 동료에게 배정한다. 배정받은 사람의 에이전트가 일하고, 사람이 승인한다.
  - 잘 된 대화는 **플러그인으로 저장**해 팀 자산으로. 공유 전 검토, 팀·개인별 권한, 회수 가능.
  - 단순 단계는 싼 모델·로컬 모델, 중요한 단계는 강한 모델로 나눈다. 역할·사용량·비용·감사 기록 제공.
- 지원 하네스: Pi, OpenCode, DeepSeek Harness, Qwen Code, Kimi Code, Codex.

## 2. graphify — 코드베이스를 ‘질문할 수 있는 지도’로
- 저장소: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify). 약 **15만 3천★**, Apache 2.0.
- 코드와 문서, SQL 스키마, 설정 파일, PDF까지 **하나의 지식 그래프**로 바꾼다. 내 컴퓨터에서 문법 분석(tree-sitter)으로 만들고, **벡터 DB를 쓰지 않으며**, 모든 연결에 **신뢰도 표시와 이유**가 붙는다.
- Claude Code·Cursor·Codex·Gemini CLI 등 20여 에이전트에서 `/graphify` 스킬로 묻는다.
- 저장소 자체 벤치마크는 판정 일치도 90.6%(카파 0.81)를 주장한다(자체 측정).
- 세컨드 브레인 관점에서도 흥미롭다. “기억으로 찾기 어려워진” 저장소를 **노트처럼 연결된 지도**로 바꾼다는 발상이 LLM Wiki와 닮았다.

## 3. Concat — 에이전트가 조종하는 무료 CapCut 대안
- 저장소: [jub0t/Concat](https://github.com/jub0t/Concat). 약 **2만★**, 일주일 +1,696, AGPL-3.0, 베타.
- **무료·오픈소스·로컬 우선·크로스플랫폼** 영상 편집기. 가장 큰 특징은 **JSON-RPC API와 MCP**로 스크립트·에이전트가 편집을 조종할 수 있다는 점이다.
- “편집기를 배우지 않고 에이전트에게 말로 시키는” 흐름(어제 OpenMotion, 11/23 ffmpeg-skill)과 같은 줄에 있다. 차이는 **사람이 쓰는 타임라인 편집기**가 그대로 있어서, 에이전트가 만든 초안을 사람이 손으로 다듬기 좋다는 점이다.

## 왜 중요한가
세 저장소 모두 같은 방향을 가리킨다. **에이전트에게 일을 시키되, 결과를 사람이 확인할 수 있는 형태로 남기는 것.** SoduWork는 승인 절차로, graphify는 이유가 붙은 연결로, Concat은 사람이 다시 열 수 있는 타임라인으로. 모두 아직 빠르게 바뀌는 초기 프로젝트라, 중요한 작업엔 작은 범위부터 시험하는 게 좋다.
