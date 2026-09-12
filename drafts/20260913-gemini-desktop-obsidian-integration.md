---
title: "제미니 데스크톱, Obsidian·폴더 스코프를 테스트 중 — 세컨드 브레인이 에이전트 작업대가 되나"
date: 2026-09-13T07:40:00+09:00
category: "Second Brain"
slug: "gemini-desktop-obsidian-integration"
summary: "TestingCatalog(2026-09-05) 비공개 빌드: Ask/Assign 토글, 폴더 범위, macOS Finder로 폴더 넘기기, Obsidian 연결. 미출시·일정 미정. 패턴만 읽고 권한 설계를 먼저."
---

## 한줄 요약
2026-09-05 TestingCatalog이 Gemini 데스크톱 **비공개 빌드**에서 **Obsidian 연결**, **Ask/Assign 모드**, **작업 폴더 스코프**, macOS **Finder에서 폴더를 Gemini로 보내기** 등을 확인했다고 전했다. Google 공식 출시 발표는 없고, **언제·그대로 나올지 미정**이다.

## 왜 Obsidian인가
Obsidian 볼트는 DB가 아니라 **로컬 폴더의 마크다운**이다. 이미 “폴더를 읽을 수 있는 에이전트”라면 볼트 접근은 한 걸음이다. Finder 액션과 같은 빌드에 등장한 이유도 여기에 가깝다 — **노트 앱 연동 = 사실상 폴더 연동**.

Ask는 기존 채팅, Assign은 Spark형 에이전트에 가깝고 **기본/이전/이번 작업 폴더**를 고른다. OpenAI Codex 데스크톱의 Chat/Work 구조에 대한 Google 쪽 응답으로 읽히는 보도가 많다. 커스텀 MCP가 이미 로드맵에 있다면 전용 Obsidian 커넥터는 **파일럿**이거나 내부 사용 흔적일 수도 있다.

## 왜 중요한가
세컨드 브레인 사용자에게는 “붙여넣기 천장”이 깨지는 방향이다. 동시에 **기본 폴더 = 평생 노트 전체**가 되기 쉽고, 작업 전 Drive 백업 옵션 같은 것은 편의이자 **데이터 이동**이다. 출시 전에 할 일은 제품 대기가 아니라 **볼트 분리(업무/개인)·허용 폴더 목록·백업 정책**을 적어 두는 것이다.

## 기억할 것
- 1차 추적: TestingCatalog 2026-09-05 보고(요약 해설 예: Progressive Robot). **유출 ≠ 로드맵 확정.**
- Spark macOS 베타가 Ultra·미국·18+로 시작한 전례상, 초기 게이트가 좁을 수 있다.
