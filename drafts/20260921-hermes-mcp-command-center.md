---
title: "Hermes Agent v0.21 — Bot Mode·MCP 커맨드 센터·크론 기억"
date: 2026-09-21T07:10:00+09:00
category: "Agent"
slug: "hermes-mcp-command-center"
summary: "NousResearch/hermes-agent v0.21.0(2026-08-31 Pantheon). 데스크톱 Bot Mode(에이전트 사회), hermes peer DM, 크론 연속 메모리, 서브에이전트 실시간 steer, MCP 서버 대시보드(헬스·비용·hermes:// 딥링크). Skills 보드 2위권."
---

## 한줄 요약
[Hermes Agent v0.21.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31)(2026-08-31)은 “도구 모음”이 아니라 **이름이 있는 봇들의 사회**로 데스크톱을 재정의한다. Agent-Leaderboard Skills 표에서도 hermes-agent는 상단권이다.

## 지금 뭐가 뜨나
- **Bot Mode**: 프로필별 이름·아바타, 그룹 채팅, @멘션. `hermes peer`로 봇↔봇 DM.
- **Cron + memory**: 스케줄 작업이 이전 출력을 이어받고(`continuity`), 변경 없으면 LLM 스킵 가능.
- **delegate_task steer**: 실행 중 자식 에이전트 코스 수정·조기 중단·부분 결과 유지.
- **MCP command center**: 드래그 임포트, 백그라운드 헬스/재인증 알림, 서버별 스키마 토큰·30일 사용량, `hermes://` 설치 딥링크(확인 후).
- 보안: AGENTS.md·스킬·메모리 **쓰기 항상 승인**, 시크릿 레닥션 강화. 데스크톱 브라우저를 에이전트가 직접 조작.

## 왜 중요한가
MCP 서버가 늘수록 병목은 “연결”이 아니라 **함대 운영 UI**다. Hermes는 그 UI를 제품화했다. OpenClaw·Cursor와 함께 “에이전트 OS” 후보를 고를 때 비교 축이 된다.

## 기억할 것
- [릴리즈 노트](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31) · [리포](https://github.com/NousResearch/hermes-agent)
