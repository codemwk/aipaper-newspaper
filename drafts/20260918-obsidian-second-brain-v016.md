---
title: "obsidian-second-brain v0.16 — ‘말없이 깨지던’ 윈도우·CJK·동시쓰기 고침"
date: 2026-09-18T07:50:00+09:00
category: "Second Brain"
slug: "obsidian-second-brain-v016"
summary: "2026-09-14/15. eugeniughelbur/obsidian-second-brain v0.16.0 The Silent Failure. Windows python3 스토어 스텁, CJK 구두점 오탐, 훅 10k 절단, 동시 편집 유실, MCP 기록 자동화 등. 스타 ~4.5k."
---

## 한줄 요약
[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) **v0.16.0 — The Silent Failure**([릴리즈](https://github.com/eugeniughelbur/obsidian-second-brain/releases/tag/v0.16.0), 태그 시각 **2026-09-14**)는 Claude Code 등 CLI 에이전트용 **옵시디언 볼트 메모리** 툴킷의 최신 안정화 판이다. 테마는 **에러 없이 조용히 실패하던 구멍**을 막는 것.

## 무엇이 바뀌었나
- **Windows**: `python3`가 Microsoft Store 별칭이라 SessionStart 훅이 컨텍스트를 안 넣고, 시크릿·태그 검증이 스킵되던 문제. 인터프리터를 이름 조회가 아니라 **실행해서** 고른다. (하드웨어 실기기 검증은 이슈로 열어 둠.)
- **CJK 볼트**: 쓰기 훅이 한글·중문·일문 구두점을 영문 “치환 금지”로 오인해 매 저장마다 경고하던 문제 수정.
- **큰 매뉴얼**: 훅 출력 1만 자 한도로 잘린 `_CLAUDE.md`를 “이미 로드됨”이라고 거짓말하던 버그 → 미로드 포인터·네이티브 `@` 임포트 경로.
- **동시 편집**: 읽기-수정-쓰기 경쟁으로 한쪽 수정이 사라지던 경우 → `write_exact_if_unchanged` / `NoteChangedError`.
- **추가**: OKF v0.2 내보내기, 소스 `capture_scope` 헬스체크, `rewrite_policy: unattended`, MCP 쓰기 후 인덱싱·로그 북키핑 등.

## 왜 중요한가
어제·그저께 다룬 LLM Wiki 플러그인·vault-bridge와 다른 갈래다. 여기는 **에이전트 세션이 볼트를 깨지 않게** 만드는 운영 레이어. 자동화 인제스트를 돌리는 사람에게 “성공한 척하는 실패”가 가장 위험하다. v0.16은 그 침묵을 줄이는 릴리즈다.

## 기억할 것
- [릴리즈 v0.16.0](https://github.com/eugeniughelbur/obsidian-second-brain/releases/tag/v0.16.0) · [저장소](https://github.com/eugeniughelbur/obsidian-second-brain) (~4,482★ 조회 시점)
