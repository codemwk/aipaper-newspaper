---
title: "GitHub 트렌드: OpenHarness·ohmo — 오픈 에이전트 하네스 + 메신저에서 PR까지 (약 15.9K★)"
date: 2026-10-03T07:08:00+09:00
category: "GitHub 트렌드"
slug: "openharness-ohmo"
summary: "HKUDS/OpenHarness(~15.9K★, MIT). pip install openharness-ai → oh setup/oh. 43+ 툴·스킬·MCP·권한·스웜. ohmo는 Feishu/Slack/Telegram/Discord 게이트웨이로 Claude Code·Codex 구독 재사용. dry-run으로 실행 전 점검."
---

## 한줄 요약
[HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness)(2026-10-03 기준 **약 15.9K★**)는 “모델=두뇌, 코드=하네스”를 내건 **오픈소스 에이전트 인프라**다. `pip install openharness-ai` 후 `oh setup` → `oh`로 돌리고, 동봉 **ohmo**는 Feishu·Slack·Telegram·Discord에서 장시간 세션·브랜치·테스트·PR을 돌리는 **퍼스널 에이전트 앱**이다. Claude Code / Codex **기존 구독**을 브리지해 추가 API 키 없이 쓸 수 있다고 README가 명시한다. Raven·Agent-Reach와 같은 “하네스 붐”의 연구·자가호스팅 축.

## 제품으로 보면 (코드 없이)
- **루프**: 스트리밍 툴콜 → 권한/훅 → 파일·셸·웹·MCP → 다시 모델. 자동 컴팩트·MEMORY.md로 멀티데이 세션.
- **거버넌스**: Default/Auto/Plan, 경로·명령 deny, Pre/PostToolUse. `--dry-run`은 모델·툴·MCP를 **실행하지 않고** ready/warning/blocked를 보여 준다.
- **생태계**: anthropics/skills·claude-code 플러그인 포맷 호환 주장. Windows는 `openh` 별칭(PowerShell `oh`=Out-Host 충돌).

## 왜 중요한가
폐쇄형 코딩 에이전트만으로는 퍼스널 OS를 조립하기 어렵다. OpenHarness는 **검사 가능한 하네스**를 원본으로 두고, ohmo로 **채팅 UX**를 붙인 패키지다. “에이전트를 산다” vs “하네스를 소유한다”의 선택지를 만든다.

## 기억할 것
- [GitHub](https://github.com/HKUDS/OpenHarness) · README Quick Start / ohmo gateway
