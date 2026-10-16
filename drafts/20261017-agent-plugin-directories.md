---
title: "GitHub 트렌드: ‘에이전트 앱스토어’가 생기고 있다 — Anthropic 공식 플러그인 디렉터리(~4만★)·cursor/plugins·mattpocock/skills(~29만★), 한 스킬을 5개 에이전트에 설치"
date: 2026-10-17T07:10:00+09:00
category: "GitHub 트렌드"
slug: "agent-plugin-directories"
summary: "이번 주 GitHub: anthropics/claude-plugins-official(~4.04만★, 주간 +2.2K, 10/16 하루 +1.5K), cursor/plugins(~1.19만★, 주간 +1.2K), mattpocock/skills(~29.4만★, 주간 +1.2만), SwiftUI-Agent-Skill(+900). 공통점: 명령·에이전트·스킬·MCP 설정을 ‘플러그인’ 한 폴더로 묶어 마켓플레이스에서 설치·자동 업데이트. 같은 스킬 묶음을 Claude Code·Codex·Copilot·Gemini CLI·기타 에이전트에 각각 설치. 신뢰·버전 관리가 새 숙제."
---

## 한줄 요약
스마트폰 초기에 앱스토어가 생기던 장면이 코딩 에이전트 판에서 반복되고 있다. 이번 주 GitHub 주간 상위권에는 개별 도구보다 **“도구를 담아 배포하는 그릇”**이 많았다 — 회사가 직접 운영하는 **공식 플러그인 디렉터리**들이다([GitStock 주간](https://gitstock.org/trending/weekly/2026-10-16), [Shareuhack 주간](https://www.shareuhack.com/zh-TW/posts/github-trending-weekly-2026-10-16)).

## 주요 레포 (10/17 기준 별 수)
- **anthropics/claude-plugins-official (~4.04만★, 주간 +2,217)**: Anthropic이 관리하는 Claude Code 플러그인 디렉터리. 자사 제작(`/plugins`)과 파트너·커뮤니티 제작(`/external_plugins`)을 나누고, 외부 플러그인은 품질·보안 기준 심사를 거친다. 터미널에서 `/plugin > Discover`로 둘러보고 한 줄로 설치([GitHub](https://github.com/anthropics/claude-plugins-official)). Context Pill 집계로 10/16 하루에만 +1,552★.
- **cursor/plugins (~1.19만★, 주간 +1,214)**: Cursor 플러그인 규격과 공식 플러그인. 눈에 띄는 것: 대화 기록에서 핵심만 뽑아 `AGENTS.md`를 갱신하는 **continual-learning**, 병렬 서브에이전트로 브랜치를 깊게 감사하는 **thermos**, PR 차이를 중요도별 캔버스로 그리는 **pr-review-canvas**, 에이전트가 안정적으로 쓰는 CLI 설계 패턴 **cli-for-agent**([GitHub](https://github.com/cursor/plugins)).
- **mattpocock/skills (~29.4만★, 주간 +12,147)**: TypeScript 교육자 Matt Pocock의 “진짜 엔지니어를 위한 스킬”. GSD·BMAD·Spec-Kit처럼 **과정 전체를 장악하는 프레임워크 대신**, 작고 고쳐 쓰기 쉬운 스킬을 조합하자는 철학. 뉴스레터 구독자 약 6만 명([GitHub](https://github.com/mattpocock/skills)).
- **twostraws/SwiftUI-Agent-Skill (~6.2K★, 주간 +900)**: SwiftUI 앱 개발 지식을 Claude Code·Codex 등에 넣는 스킬.

## 플러그인 = ‘폴더 하나’
Anthropic 디렉터리가 정한 구조를 보면 개념이 쉽다. 플러그인 하나는 메타데이터 파일, **MCP 서버 설정**, **슬래시 명령**, **에이전트 정의**, **스킬**, 설명서를 한 폴더에 담는다. 그리고 한 번 공개한 이름(slug)은 **바꿀 수 없다** — 사용자가 그 이름으로 설치했기 때문에, 바꾸면 설치가 깨진다. 패키지 관리자(npm 등)가 오래전에 겪은 문제를 그대로 물려받은 셈이다.

## 한 스킬, 다섯 에이전트
mattpocock/skills의 설치 안내가 현재 상황을 압축한다. 같은 스킬 묶음을 **Claude Code**(Anthropic 공식 디렉터리 경유, 자동 업데이트), **Codex**(자체 플러그인 마켓, 시작 시 업데이트), **GitHub Copilot**(CLI·VS Code, 매일 업데이트), **Gemini CLI**(수동), **그 외 에이전트**(`npx skills`)에 각각 다른 방식으로 넣는다. 플러그인으로 설치하면 자동으로 갱신되고, 파일 복사로 넣으면 직접 고칠 수 있지만 업데이트는 손으로 해야 한다. 둘 다 깔면 스킬이 두 번 들어간다는 주의까지 붙어 있다.

## 왜 중요한가
경쟁의 축이 “어느 모델이 똑똑한가”에서 **“어느 에이전트에 좋은 일하는 방식이 많이 깔려 있나”**로 옮겨 가고 있다. 1인 스튜디오나 소규모 팀에겐 기회다 — 자기 작업 노하우(브랜드 검수, 리서치 정리, 디자인 QA)를 스킬로 묶으면 여러 에이전트에 그대로 배포된다. 동시에 Anthropic 디렉터리조차 “플러그인 안의 MCP 서버·파일을 우리가 통제하거나 검증할 수 없다”고 경고한다. 원칙은 앱스토어 초창기와 같다: **공식·심사된 출처에서, 버전을 고정하고, 어떤 파일을 읽고 쓰는지 확인한 뒤** 설치할 것.

출처: [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · [cursor/plugins](https://github.com/cursor/plugins) · [mattpocock/skills](https://github.com/mattpocock/skills) · [GitStock 주간 10/16](https://gitstock.org/trending/weekly/2026-10-16) · [Context Pill 10/16](https://contextpill.com/issues/2026-10-16)
