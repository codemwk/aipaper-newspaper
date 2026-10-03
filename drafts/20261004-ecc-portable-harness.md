---
title: "GitHub 트렌드: ECC(everything-claude-code) — Claude·Codex·Cursor·OpenCode를 넘나드는 포터블 에이전트 하네스"
date: 2026-10-04T07:09:00+09:00
category: "GitHub 트렌드"
slug: "ecc-portable-harness"
summary: "affaan-m/ECC(~272k★). 스킬·instincts·메모리·보안·리서치 우선 워크플로. Claude Code 플러그인·npx ecc-universal 설치. 모델이 아니라 하네스 계약을 판다."
---

## 한줄 요약
[affaan-m/ECC](https://github.com/affaan-m/ECC)(Everything Claude Code, 조회 시점 **~27만★**): Claude Code·Codex·OpenCode·Cursor 등을 겨냥한 **에이전트 하네스 최적화 키트**. 스킬·에이전트·룰·훅·MCP·메모리·보안 스캔·오케스트레이션을 묶는다. README 포지션이 명확하다 — **성능은 모델이 아니라 하네스**. openclaw와 함께 “트렌딩 = 하네스” 신호의 다른 축(코딩 에이전트 특화).

## 실무로 보면
- **설치(문서 기준)**: Claude Code는 마켓플레이스에 ECC 추가 후 플러그인 설치. 멀티 하네스 안내는 `npx ecc-universal@… install --guided` 형태(버전은 릴리스 노트 확인).
- **가져갈 것**: 프로젝트마다 새로 쓰던 MCP·프롬프트 스파게티를 **스킬/룰 패키지**로 고정.
- **주의**: 스타 폭증 레포는 권한·훅·외부 스크립트 표면을 배포 전에 리뷰. “기본 ON 확장”(어제 Claude Code Mods)과 겹치면 거버넌스 이슈.

## 왜 중요한가
팀이 Cursor↔Claude Code↔Codex를 섞어 쓸 때 **프롬프트 자산이 이식 가능**해야 한다. ECC는 그 “npm for agent habits”에 가깝다.

## 기억할 것
- [github.com/affaan-m/ECC](https://github.com/affaan-m/ECC)
