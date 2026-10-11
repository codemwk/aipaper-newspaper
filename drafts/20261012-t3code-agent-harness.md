---
title: "GitHub: T3 Code(pingdotgg/t3code) — 구독을 되팔지 않는 ‘에이전트 하네스 컨트롤 플레인’, ~2.7만★"
date: 2026-10-12T07:09:00+09:00
category: "GitHub"
slug: "t3code-agent-harness"
summary: "Theo(pingdotgg) 팀의 T3 Code: Claude Code·Codex·Cursor·Grok Build·OpenCode·Antigravity를 로컬에서 遥控하는 웹·데스크톱·모바일 UI. 토큰 재판매 없음·MIT. npx t3@latest / brew cask. 스타 ~26,973."
---

## 한줄 요약
[T3 Code](https://github.com/pingdotgg/t3code)는 AI 코딩 **모델을 파는 앱이 아니라**, 이미 쓰는 에이전트 CLI를 **원격·모바일·데스크톱에서 조종하는 컨트롤 서피스**다. README 첫 질문에 “뭘 파냐?” → **Nothing.** 스타 **~26,973**(10/12), 라이선스 **MIT**.

## 어떻게 동작하나
- **지원 프로바이더**(문서): Codex CLI, Claude Code, Cursor CLI(`agent login`), Grok Build, OpenCode, Google Antigravity(설정에서 설치·Google 로그인).
- **클라이언트**: [t3.codes](https://t3.codes) 웹, Electron 데스크톱, iOS·Android 리모트 앱.
- **설치**: `curl -fsSL https://t3.codes/install.sh | sh` 또는 `npx t3@latest`. macOS `brew install --cask t3-code`, Windows winget/scoop.
- **철학**: Codex 데스크톱·Conductor·Cursor Glass 등에 영감을 받았으나 **오픈·포크 가능·원격**을 기준으로 다시 씀. Git 체크포인트·원버튼 GitHub PR 같은 워크플로를 사용자 문서가 강조.

## 왜 중요한가
“또 하나의 에이전트”가 아니라 **에이전트 오케스트라의 HUD**다. 구독은 Anthropic·OpenAI·Cursor에 그대로 두고, T3는 **세션·기기·UI**만 가져간다. cmux가 터미널 UX, gh-aw가 GitHub 워크플로라면 T3는 **멀티 프로바이더 리모컨**. 기업에선 “토큰 프록시 금지” 정책을 지키면서도 모바일 승인·모니터링을 넣고 싶을 때 후보가 된다.

## 기억할 것
- 프로바이더 CLI가 먼저 설치·로그인되어 있어야 한다.
- 상업 모델이 나중에 바뀔 수 있으니, 가치는 **MIT 포크 가능성**에 두라는 것이 프로젝트 스스로의 메시지다.

출처: [github.com/pingdotgg/t3code](https://github.com/pingdotgg/t3code) · [t3.codes](https://t3.codes)
