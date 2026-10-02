---
title: "GitHub 트렌드: Claude Code Mods 기본 ON — 프롬프트·툴콜을 프로세스 안에서 고치는 플러그인, Copilot·Codex는 옵트인"
date: 2026-10-03T07:07:00+09:00
category: "GitHub 트렌드"
slug: "claude-code-mods-default"
summary: "AIDevPulse(2026-10-02): Claude Code v2.1.287 Mods 기본 활성(샌드박스 없음·설치 사용자 권한). allowManagedModsOnly로 사용자 모드 차단 가능. Copilot sandbox CA·Codex Guardian 히스토리는 옵트인/오프 기본."
---

## 한줄 요약
[AIDevPulse](https://aidevpulse.com/2026/10/02/claude-code-mods-ship-on-by-default-while-copilot-and-codex-stay-opt-in-2026-10-02/)(2026-10-02) 정리: **Claude Code v2.1.287**부터 **Mods**가 기본으로 켜진다. Mod는 설정 훅(외부 명령)과 달리 **프로세스 안 JS/TS 핸들러**가 프롬프트·툴콜·턴을 읽고 고치거나, 권한 프롬프트 전에 승인/거절할 수 있다. Anthropic 문서상 **샌드박스 없음**, 설치 사용자 권한으로 실행. 반면 Copilot CLI의 sandbox CA trust, Codex Guardian 히스토리 툴은 **기본 오프·옵트인**. “에이전트 CLI 보안 표면”이 제품마다 비대칭이다.

## 실무로 보면
- **관리자 스위치**: managed settings의 `cc-plugin-sec-default@builtin` → `allowManagedModsOnly`로 사용자 설치·`--plugin-dir`·Claude가 쓴 모드를 막고, 설정 훅·빌트인은 유지.
- **Watcher**: 빌트인 `cc-plugin-you-should-know` 사이드 에이전트는 **기본 오프**. 텔레메트리·전송 범위가 문서에 불명확해 공유 이미지에서는 끈 채 두는 편이 안전하다는 권고.
- **채널 주의**: 보도 시점 npm `stable`이 아직 2.1.285(Mods 없음)일 수 있어, 태그 이동 **전에** managed 정책을 깔라는 타이밍 이슈.

## 왜 중요한가
코드 덤프가 아니라 **거버넌스 뉴스**. 퍼스널 OS·사내 코딩 에이전트를 배포할 때 “기본 ON인 확장 표면”이 있는지부터 점검 목록에 넣어야 한다.

## 기억할 것
- [AIDevPulse 브리핑](https://aidevpulse.com/2026/10/02/claude-code-mods-ship-on-by-default-while-copilot-and-codex-stay-opt-in-2026-10-02/) · Claude Code CHANGELOG / mods 문서
