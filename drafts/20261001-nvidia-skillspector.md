---
title: "GitHub 트렌드: NVIDIA SkillSpector — 에이전트 Skills·MCP를 설치 전에 훑는 보안 스캐너(~18.8K★)"
date: 2026-10-01T07:07:00+09:00
category: "GitHub 트렌드"
slug: "nvidia-skillspector"
summary: "NVIDIA/SkillSpector. Claude Code·Codex·MCP skills의 취약점·악성 패턴·프롬프트 인젝션·데이터 유출·공급망 리스크를 설치 전 점검. 2026-09-30 푸시 활발, ★~18.8K(2026-10-01 조회)."
---

## 한줄 요약
[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)는 **AI 에이전트 스킬 보안 스캐너**다. README 기준 Claude Code·Codex·**MCP skills**를 대상으로 취약점, 악성 패턴, 프롬프트 인젝션, 데이터 유출, 공급망 위험을 **설치하기 전에** 찾는다. 2026-10-01 `gh` 조회 기준 ★ **약 18,795**, 최근 푸시 2026-09-30.

## 제품으로 보면(평이한 말)
- skills·MCP 서버가 생산성 플러그인 스토어가 되면서, 브라우저 확장과 같은 **신뢰 문제**가 생겼다.
- SkillSpector는 그 레이어에 **정적/패턴 스캔**을 얹는 NVIDIA 오픈소스 실험이다(엔터프라이즈 보증서와는 별개).
- 에이전트 스택을 고를 때 "어떤 모델"만큼 "어떤 스킬을 허용할지"가 운영 항목이 됐다는 신호.

## 왜 중요한가
어제 n8n-mcp·obsidian-skills를 다뤘다면, 오늘은 **그 생태계의 백신**이다. 퍼스널 OS·사내 에이전트에 커뮤니티 스킬을 붙일 때 체크리스트 1순위로 넣을 만하다.

## 기억할 것
- [GitHub](https://github.com/NVIDIA/SkillSpector) · 설명: skills/MCP 설치 전 보안 스캔
