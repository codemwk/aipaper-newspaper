---
title: "세컨드 브레인 팁 — Obsidian을 ‘캐시’로 쓰면 Claude 한도가 덜 닳는다"
date: 2026-09-14T07:45:00+09:00
category: "Second Brain"
slug: "obsidian-claude-cache"
summary: "XDA(2026-09-09). CLAUDE.md+SKILL.md+인덱스 포인터로 2–4k 토큰만 싣고 필요한 노트만 열기. Projects/Memory보다 로컬 라우팅이 싼 이유."
---

## 한줄 요약
[XDA(2026-09-09)](https://www.xda-developers.com/stopped-hitting-claude-rate-limits-after-turning-obsidian-vault-into-its-cache/)가 정리한 실전법: Obsidian 볼트를 DB가 아니라 **라우팅 캐시**로 둔다. 작은 `CLAUDE.md`·`SKILL.md`·`/index/` 포인터가 “어디를 열지” 알려 주고, 에이전트는 폴더 전체를 긁지 않는다.

## 핵심 패턴
- **포인터 우선**: 활성 프로젝트·이번 주·영역별 인덱스 → 관련 노트 2–3개만 로드.
- **비용 감각**: 저자 기준 SKILL≈400 + 스키마≈400 + 노트 1–2k씩 → 세션 베이스 **2–4k**. 두꺼운 Project 지식베이스를 매 턴 재주입하는 것보다 싸다.
- **Projects/Memory와 역할 분리**: claude.ai Projects는 웹·매 메시지 상속, Memory는 합성 프로필. **로컬 파일 경로·최신 초안 위치**는 볼트 인덱스가 더 정확.
- 댓글/후속이 강조하는 보완: 인덱스에 **한 줄 사실**을 직접 적기, 프로젝트당 파일 하나+상태 라인, 결정문 날짜 고정, 변하는 값은 **스크립트 명령**을 캐시.

## 왜 중요한가
어제 LLM Wiki·Gemini–Obsidian 보도와 같은 줄기 — **컨텍스트를 프롬프트에 붙이지 말고 파일 그래프에 둔다.** 한도(5시간 롤링+주간 캡)는 메시지 수가 아니라 **토큰**이다. 세컨드 브레인을 AI 작업대로 쓸수록 “무엇을 읽히지 않을지”가 생산성이다.

## 기억할 것
- Obsidian은 편집기일 뿐, 본질은 **마크다운 폴더 + 인덱스**. Claude Code가 아닌 다른 CLI에도 같은 패턴 적용 가능.
- 포인터는 썩는다. **주간 신선도 패스**를 별도 짧은 세션으로 돌릴 것.
