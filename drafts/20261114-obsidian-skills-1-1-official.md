---
title: "세컨드 브레인: Obsidian Skills 1.1.0 — 이제 Obsidian ‘공식’ 플러그인으로 Claude Code·Codex·Cursor에. 기존 설치자는 업데이트가 안 됐을 수 있다"
date: 2026-11-14T07:08:00+09:00
category: "세컨드 브레인 / PKM"
slug: "obsidian-skills-1-1-official"
summary: "kepano가 만든 에이전트용 Obsidian 스킬 모음이 11/12(한국 시각) 1.1.0으로 올라가면서 저장소가 obsidianmd/obsidian-skills로 옮겨졌다. 이제 Obsidian이 직접 배포하는 하나의 플러그인으로 Claude Code·Codex·Cursor 마켓플레이스에 올라간다. 버전 번호가 1.0.1에 멈춰 있어 그동안 Knap 스킬 같은 변경이 기존 설치본에 반영되지 않았다는 버그도 함께 고쳤다. 같은 주 ModelBrain 플러그인 0.1.2는 ‘빌드 증명’을 붙였다."
---

## 한줄 요약
에이전트가 Obsidian 볼트를 다룰 때 쓰는 ‘사용 설명서’가 **개인 프로젝트에서 Obsidian 공식 배포물**로 바뀌었다. 11/6에 소개한 kepano/obsidian-skills가 **obsidianmd/obsidian-skills**로 옮겨졌고(예전 링크는 자동 연결), 1.1.0이 나왔다([GitHub 릴리스](https://github.com/obsidianmd/obsidian-skills/releases/tag/1.1.0)).

## 바뀐 점
- **하나의 플러그인, 세 개의 에이전트**: Claude 마켓플레이스 옆에 **Codex·Cursor 마켓플레이스**가 추가됐다. Claude·Codex·ChatGPT·Cursor 디렉터리용 아이콘·README·라이선스도 붙었다.
- **중요: 기존 설치자는 직접 업데이트해야 한다**. 버전이 1.0.1에 멈춰 있어서 그동안 **Knap 스킬 등 변경 사항이 기존 설치본에 반영되지 않았다**. Claude Code 마켓플레이스로 설치했다면 `claude plugin update obsidian@obsidian-skills`를 한 번 실행하면 된다.
- **Obsidian CLI 스킬**: LaTeX처럼 백슬래시가 든 내용을 파일에 그대로 쓴다. CLI가 어떤 볼트를 고르는지, **오류가 나도 종료 코드가 0**이라는 점, 이름 변경·이동 시 링크 업데이트 대화상자를 기다린다는 점이 문서에 들어갔다. 에이전트가 “성공”으로 착각하기 쉬운 지점들이다.
- **설치 전 확인**: Obsidian CLI·Defuddle·Knap은 도구가 설치돼 있는지 먼저 확인하고, **설치하기 전에 묻는다**.
- 마크다운(표 안 별칭 파이프, YAML 속 위키링크 따옴표), Bases(정렬, 인라인 base 블록), Canvas(**CJK 글자 크기**) 관련 수정도 들어갔다. 한국어 캔버스를 쓴다면 반가운 수정이다.

## 같은 주: ModelBrain 0.1.2 — “이 플러그인, 공개 소스 그대로 빌드됐다”
‘볼트 검색과 AI 비서가 기억하는 내용을 한 패널에서’ 찾는 ModelBrain 플러그인은 11/11 0.1.2에서 기능 변경 없이 **배포 방식**만 바꿨다. 이제 GitHub Actions가 공개 소스로 빌드하고, 파일마다 **빌드 증명(attestation)**이 붙는다. Obsidian 심사팀도 main.js를 바이트 단위로 다시 빌드해 확인했다. 남은 경고는 “외부 프로그램 실행” 하나인데, 앱과 통신하는 방식이라 사실 그대로라고 밝혔다([Obsidian 포럼](https://forum.obsidian.md/t/modelbrain-search-your-vault-and-what-your-ai-assistants-remember-in-one-panel/121807/2)).

## 왜 중요한가
볼트에 에이전트를 붙이는 일이 ‘실험’에서 **관리 대상**으로 바뀌고 있다. 공식 배포, 버전 관리, 빌드 증명, 설치 전 확인이 그 신호다. LLM Wiki를 만들 계획이라면 지금 할 일은 두 가지다. ① 설치된 obsidian-skills 버전 확인 ② 볼트에 접근하는 플러그인이 **어디서 빌드됐는지** 확인.
