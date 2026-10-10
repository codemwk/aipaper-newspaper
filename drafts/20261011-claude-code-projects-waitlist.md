---
title: "AI 도구: Claude Code Projects — Pro·Max 대기열 일괄 개방, ‘코디네이터 대화’가 클라우드 스레드를 병렬로 돌린다"
date: 2026-10-11T07:03:00+09:00
category: "AI 도구"
slug: "claude-code-projects-waitlist"
summary: "10/9 ClaudeDevs 발표: Claude Code Projects 대기열의 Pro·Max 사용자를 일괄 입장. 한 대화가 작업을 나눠 병렬 클라우드 스레드(브랜치·테스트·PR)를 돌리고 노트북을 꺼도 이어짐. 베타, Free/Team/Enterprise·터미널 CLI는 아직."
---

## 한줄 요약
Anthropic 개발자 계정 **ClaudeDevs**가 10월 9일, **Claude Code Projects** 대기열에 있던 **모든 Pro·Max** 사용자를 들였다고 알렸다. 프로젝트는 **폴더+채팅**이 아니라 **코디네이터 대화**다 — 목표가 들어오면 **스레드(대개 클라우드 세션)**를 병렬로 띄워 브랜치·테스트·PR까지 맡긴다([문서](https://claude.com/resources/articles/projects-redesigned)).

## 제품이 하는 일
- **병렬 스레드**: 버그·리뷰·여러 레포 lint 같은 일을 스레드로 쪼개 동시에 진행. 클라우드 스레드는 **노트북을 닫아도** 계속.
- **공유 맥락**: 프로젝트 지시·메모리(문서·2차 보도는 MEMORY.md 인덱스·지시 상한 등을 언급하나, **공식 수치·한도는 제품 UI/문서로 확인**할 것).
- **진입 경로**: `claude.ai/code`, 데스크톱 Code 탭, 모바일. **터미널 CLI·VS Code/JetBrains 확장·Free/Team/Enterprise는 아직**이라는 2차 정리와, 공식 “점진 롤아웃·대기열” 문구가 공존 — 사이드바에 Projects가 없으면 대기열이 여전히 유효할 수 있다.
- GitHub 앱이 연결된 **github.com** 레포 전제(코딩 작업 기준, 2차 가이드).

## 왜 중요한가
Cursor 클라우드 에이전트·GitHub Agentic Workflows와 같은 **“사람=코디네이터, 모델=워커”** 구도가 Claude 구독 안에도 들어왔다. 사용량 한도를 **유휴 서브에이전트가 빨리 태운다**는 현장 반응이 X에 잇따른다 — Pro $20 / Max 배수 요금제에서 **병렬=비용**이 체감된다.

출처: [Projects redesigned](https://claude.com/resources/articles/projects-redesigned) · ClaudeDevs 10/9 대기열 개방 발표(X) · [2차 정리](https://blog.laozhang.ai/en/posts/claude-code-projects)
