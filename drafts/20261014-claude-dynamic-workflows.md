---
title: "AI 도구: Claude Managed Agents ‘동적 워크플로’ 베타 — 에이전트가 직접 짜는 멀티에이전트 프로그램, 한 런에 최대 1,000 에이전트·동시 64"
date: 2026-10-14T07:03:00+09:00
category: "AI 도구"
slug: "claude-dynamic-workflows"
summary: "Claude Platform(10/9 베타): 메인 에이전트가 ‘워크플로’라는 오케스트레이션 프로그램을 직접 써서 단계(phase)별로 에이전트를 팬아웃·결과 결합. 한계는 런당 동시 64 스레드·총 1,000 에이전트·수명 24시간·세션당 열린 런 10개. 서브에이전트끼리는 직접 대화 불가, 샌드박스 파일만 공유. 비용은 일반 토큰과 동일 과금."
---

## 한줄 요약
지금까지 멀티에이전트는 사람이 “코디네이터 1 + 서브에이전트 N”을 미리 짜 주는 구조였다. Anthropic이 10/9 Claude Managed Agents에 베타로 넣은 **dynamic workflows(일명 flows)**는 **Claude가 작업을 보고 직접 오케스트레이션 프로그램을 작성**한다([문서](https://platform.claude.com/docs/en/managed-agents/workflow-runs.md), [릴리스 노트](https://platform.claude.com/docs/en/release-notes/overview.md)).

## 어떻게 동작하나
- **워크플로 = 프로그램**: “300개 계약서 중 지배권 변경 조항이 있는 것”처럼 한 대화에 안 들어가는 일을 받으면, 에이전트가 **단계(phase)**를 나누고(예: ‘계약서 읽기’ → ‘결과 대조’) 에이전트를 **동시에 팬아웃**한 뒤 결과를 다음 에이전트에 넘긴다. 리뷰 통과까지 반복, 실패한 에이전트 처리도 프로그램이 결정.
- **백그라운드 실행**: 서버가 런을 돌리는 동안 메인 에이전트는 다른 일을 하거나 턴을 끝낼 수 있다. 진행은 `workflow_run.*` 이벤트로 추적.
- **공유 방식**: 서브에이전트끼리는 **직접 메시지 불가**. 같은 세션 샌드박스의 **파일 시스템**이 유일한 채널.
- **한계(문서)**: 런당 **동시 64 스레드**, 런 전체 **최대 1,000 에이전트**, 수명 기본 **24시간**, 세션당 열린 런 **10개**. 런은 중첩 불가.
- **비용**: 런 자체 요금은 없고, 스레드가 쓴 토큰을 모델 단가로 과금. 세션 예산(budget)에 닿으면 모든 런이 일시정지.

## 현장 이야기 (10/12 AI Engineer NY 워크숍)
Clauding 정리에 따르면 Anthropic 발표자들은 flows를 **“테스트 타임 컴퓨트를 어려운 문제에 쏟아붓는 방법”**이라 설명했다. 단일 에이전트보다 **훨씬 비싸지만** 세부 누락이 적고, 모델은 실행 중 자기 예산을 모른다(세션 예산 노브로 통제). 반복 작업은 연구 프리뷰 **‘dreaming’**(메모리 저장소 재정리)과 묶어 점점 싸게 만든다는 그림.

## 왜 중요한가
“에이전트 팀 설계”가 사람의 일에서 **모델의 일**로 넘어간다. 대신 사용자는 **예산 상한·실패 처리 지시·결과 검증**을 설계해야 한다. 문서가 명시하듯 런이 `completed`로 끝나도 **작업이 통과했다는 뜻은 아니다** — 스레드별 결과 확인이 필수다.

출처: [Workflow runs 문서](https://platform.claude.com/docs/en/managed-agents/workflow-runs.md) · [Multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration.md) · [Claude Platform 릴리스 노트](https://platform.claude.com/docs/en/release-notes/overview.md) · [Clauding 워크숍 정리](https://clauding.de/en/posts/claude-dynamic-workflows-flows-orchestrierung/)
