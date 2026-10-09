---
title: "GitHub 트렌드: cmux(~28K★) — AI 코딩 에이전트용 macOS 터미널, 세로 탭·알림·멀티태스킹에 초점"
date: 2026-10-10T07:14:00+09:00
category: "GitHub 트렌드"
slug: "cmux-agent-terminal"
summary: "manaflow-ai/cmux(~28K★). Ghostty 기반 오픈소스 macOS 터미널. 세로 탭과 알림으로 여러 코딩 에이전트 세션을 동시에 돌리는 워크플로를 겨냥. ‘에이전트 오케스트레이션 UI’가 IDE 밖 터미널로 확장되는 사례."
---

## 한줄 요약
에이전트를 여러 개 띄우면 터미널 창이 먼저 무너진다. **cmux**는 Ghostty를 바탕으로 한 **macOS 오픈소스 터미널**로, **세로 탭·알림·프로그래밍 가능함**을 내세워 AI 코딩 에이전트 멀티태스킹을 겨냥한다([manaflow-ai/cmux](https://github.com/manaflow-ai/cmux), 스타 약 **2.8만**).

## 무엇을 풀려 하나
- 에이전트는 오래 돌고, 로그가 쏟아지고, 승인이 끼어든다. 일반 터미널 탭만으로는 “哪個이 끝났는지”를 놓치기 쉽다.
- cmux는 **알림**과 **세로 탭 조직**으로 세션을 눈에 보이게 두고, 에이전트 워크플로에 맞게 **조작·스크립트** 가능성을 강조한다.

## 왜 중요한가 (코드 덤프 없이)
Paperclip이 “회사처럼 에이전트 조직도”라면, cmux는 **실행 표면**이다. IDE 에이전트(Cursor)·클라우드 에이전트·CLI 에이전트가 늘수록 **터미널 UX 자체가 생산성 병목**이 된다. 스타 속도는 “에이전트 런타임을 고르는 도구” 수요를 보여 준다.

출처: [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)
