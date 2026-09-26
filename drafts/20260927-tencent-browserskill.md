---
title: "GitHub: Tencent BrowserSkill — 에이전트가 ‘로그인된 내 탭’을 잠시 빌린다"
date: 2026-09-27T07:07:00+09:00
category: "GitHub"
slug: "tencent-browserskill"
summary: "Tencent/BrowserSkill(MIT). 격리 빈 브라우저 대신 로컬 CLI+확장으로 기존 인증 세션 탭을 에이전트에 대여. 작업 후 탭 반환. GitHub·Slack 등 ‘이미 로그인된 상태’ 자동화에 초점."
---

## 한줄 요약
텐센트가 오픈소스한 **[BrowserSkill](https://github.com/Tencent/BrowserSkill)**은 에이전트용 “깨끗한 브라우저” 대신, **이미 로그인해 둔 로컬 브라우저 탭을 잠시 빌려** 작업을 하게 한다([Medium 해설](https://medium.com/coding-nexus/tencent-just-open-sourced-browserskill-the-missing-bridge-between-ai-agents-and-your-browser-90333257104c)). 어제 WeKnora·skills.sh와 다른 포인트는 **인증 상태 재사용**이다.

## 왜 핫한가 (쉬운 말로)
- 에이전트에게 “내 GitHub 이슈 확인해”라고 하면, 새 브라우저는 로그인부터 막힌다.
- BrowserSkill은 로컬 데몬·확장으로 **Agent Window**를 띄워 기존 세션을 쓴 뒤 탭을 되돌린다.
- 원격 에이전트는 페어링/게이트웨이로 로컬 브라우저에 연결하는 문서가 있다.
- MIT, “내 쿠키를 클라우드에 올리지 않고” 자동화하려는 수요와 맞닿음 — 다만 **로컬 권한·피싱형 프롬프트** 위험은 사용자가 직접 관리해야 한다.

## 왜 중요한가
Inoreader·대시보드·사내툴처럼 로그인 벽이 높은 워크플로에서, Playwright식 헤드리스만으로는 부족한 구간을 메운다. 보안 사고 뉴스가 많은 주에는 “무엇을 빌려줄지” 화이트리스트가 필수다.

## 기억할 것
- [github.com/Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)
