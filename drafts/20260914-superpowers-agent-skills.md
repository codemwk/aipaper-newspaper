---
title: "GitHub 핫: Superpowers — 코딩 에이전트에게 ‘스킬을 의무’로 씌우는 방법론"
date: 2026-09-14T07:35:00+09:00
category: "GitHub Hot"
slug: "superpowers-agent-skills"
summary: "obra/superpowers. TDD·디버깅·브레인스토밍·서브에이전트 리뷰를 강제하는 에이전트 스킬 프레임워크. MIT. 스타 약 28.6만(2026-09-13 API)."
---

## 한줄 요약
[obra/superpowers](https://github.com/obra/superpowers)는 코딩 에이전트가 자신감·시간 압박에 단계를 건너뛰는 문제를, **관련 스킬이 있으면 반드시 따르게** 만드는 방법론·스킬 묶음이다. 2026-09-13 GitHub API 기준 스타 약 **286,161** / 포크 약 **25,600**, MIT.

## 무슨 기능이 ‘핫’한가 (코드 없이)
- **의무 워크플로**: 세션 시작 시 스킬 목록을 알고, 작업 전 “매칭 스킬?”을 검사. 있으면 로드·준수, 아니면 실패로 취급하는 설계.
- **라이브러리**: test-driven-development(RED-GREEN-REFACTOR), systematic-debugging, brainstorming, writing/executing-plans, subagent-driven-development(스펙 준수→코드 품질 2단 리뷰), git worktree·브랜치 마무리 등.
- **멀티 에이전트**: Claude Code, Codex, Cursor, OpenCode, Gemini CLI, Copilot CLI 등 README에 설치 경로가 정리됨.

## 왜 중요한가
트렌딩이 “더 센 모델”이 아니라 **하네스·스킬·방법론**으로 기운 신호다. ECC·Karpathy CLAUDE.md·OmniRoute와 같은 줄 — 모델은 바꿔도 **작업 규율을 파일로 고정**하자는 쪽. 개인 트레이딩·뉴스 파이프라인에도 같은 패턴이 먹힌다: 스킬 = 재현 가능한 절차.

## 기억할 것
- 저장소: [github.com/obra/superpowers](https://github.com/obra/superpowers)
- 스킬이 많아도 **도메인 검증(테스트·페이퍼트레이딩)**을 대체하지 않는다. 방법론 ≠ 수익.
