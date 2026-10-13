---
title: "GitHub 트렌드: context-mode(~2.8만★) — 코딩 에이전트의 ‘컨텍스트 다이어트’, 도구 출력은 샌드박스에 두고 필요한 줄만 꺼낸다"
date: 2026-10-14T07:10:00+09:00
category: "GitHub 트렌드"
slug: "context-mode-agents"
summary: "mksglu/context-mode ~28,143★(2026-10-14). MCP 도구 호출이 쏟아내는 원본 데이터(Playwright 스냅샷 56KB, 이슈 20개 59KB)를 컨텍스트 밖 샌드박스에 보관하고 요약·검색 결과만 넣는 MCP 서버+훅. 세션 이벤트를 SQLite/FTS5에 기록해 압축(compaction) 뒤에도 하던 일을 이어감. 17개 플랫폼 지원, 라이선스 ELv2."
---

## 한줄 요약
에이전트가 멍청해지는 순간은 모델이 약할 때보다 **컨텍스트 창이 쓰레기로 찰 때**가 많다. [mksglu/context-mode](https://github.com/mksglu/context-mode)는 그 문제를 겨냥한 MCP 서버로, 10/14 `gh` 기준 **약 28,143★**이다.

## 무엇을 해결하나 (쉬운 말로)
- **문제**: MCP 도구를 한 번 부를 때마다 원본 데이터가 통째로 컨텍스트에 들어온다. README 예시로 Playwright 스냅샷 **56KB**, GitHub 이슈 20개 **59KB**, 액세스 로그 하나 **45KB**. 30분이면 컨텍스트의 **40%**가 사라지고, 대화가 압축되면 에이전트는 **어떤 파일을 고치던 중이었는지** 잊는다.
- **해법 1 — 샌드박스**: 원본은 컨텍스트 밖에 두고 필요한 결과만 돌려준다. README 주장 **315KB → 5.4KB(98% 감소)**.
- **해법 2 — 세션 연속성**: 파일 수정·git 작업·태스크·에러·사용자 결정을 **SQLite**에 기록하고 **FTS5/BM25 검색**으로 관련된 것만 다시 꺼낸다. 이어 하지 않으면 이전 세션 데이터는 즉시 삭제.
- **해법 3 — 라우팅 강제**: 훅(preToolUse·postToolUse·preCompact·sessionStart 등)으로 무거운 도구 호출을 샌드박스로 돌린다. Claude Code·Copilot CLI·OpenCode 등 **17개 플랫폼**.

## 지금 뜨는 흐름
어제 다룬 ‘하네스·메모리’ 스타 랭킹(claude-mem ~100K★ 등)과 같은 줄기다. 다만 claude-mem이 **“기억을 더 넣는”** 쪽이라면 context-mode는 **“덜 넣는”** 쪽 — 같은 동전의 양면이다. 이번 주 GitHub 트렌딩 상위권도 스킬 팩·에이전트 메모리·플러그인 스펙(cursor/plugins ~11.2K★)이 차지했다. 모델 경쟁과 별개로 **에이전트의 작업 환경 엔지니어링**이 가장 활발한 오픈소스 영역이다.

## 기억할 것
- 라이선스는 **Elastic License 2.0(ELv2)** — 소스 공개지만 OSI 오픈소스는 아니다. 관리형 서비스로 재판매 제약.
- “98% 감소”·대기업 사용 배지는 저장소 자체 표기. 내 작업에서 압축 빈도·토큰 사용이 실제로 줄었는지 직접 재 보는 게 맞다.

출처: [GitHub mksglu/context-mode](https://github.com/mksglu/context-mode) · [GitHub Trending (weekly)](https://github.com/trending?since=weekly) · [GitHub cursor/plugins](https://github.com/cursor/plugins)
