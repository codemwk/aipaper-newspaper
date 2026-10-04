---
title: "GitHub 트렌드: 에이전트를 ‘직원’에서 ‘회사’로 — paperclip(~97K★)·openrig 조직도 + NVIDIA OpenShell 샌드박스"
date: 2026-10-05T07:07:00+09:00
category: "GitHub 트렌드"
slug: "paperclip-openshell-agent-fleet"
summary: "주간 트렌딩 테마: 에이전트 함대 운영. paperclip=목표·조직도·예산 상한·재시작 후에도 남는 티켓(‘OpenClaw가 직원이면 Paperclip은 회사’). openrig=YAML로 팀 토폴로지 정의·rig up. OpenShell(Apache 2.0)=커널 단 정책 강제+정책 변경 형식검증, 에이전트는 진짜 자격증명을 못 본다."
---

## 한줄 요약
[9/28–10/3 GitHub 트렌딩 주간 요약](https://www.tommyz.blog/blog/github-trending-weekly-2026-09-28-to-2026-10-03)의 두 번째 큰 줄기는 **“에이전트 여러 개를 어떻게 부리고, 어떻게 가둘 것인가”**였다. 탭 20개에 Claude Code를 띄워 놓고 뭐가 뭘 하는지 모르다가 재시작하면 다 날아가는 문제 — 그 해법이 세 갈래로 동시에 떴다.

## 1) paperclip — 에이전트 ‘회사’ 운영판
[paperclip](https://github.com/paperclipai/paperclip)(10/5 조회 약 9.7만★, MIT)은 셀프호스트 Node+React 앱이다. 목표를 정하고(“AI 노트앱으로 MRR $1M”), CEO·CTO·엔지니어·디자이너·마케터 역할에 **아무 에이전트나 고용**(OpenClaw, Claude Code, Codex, Cursor, Gemini CLI, Hermes 등), 계획을 승인하면 대시보드에서 작업·비용을 추적한다. 재시작에도 살아남는 티켓·스레드, 목표→프로젝트→작업으로 흐르는 컨텍스트, **예산 초과 시 자동 일시정지**가 핵심. 슬로건은 “PR이 아니라 **사업 목표**를 관리하라”, “OpenClaw가 직원이면 Paperclip은 회사”.

## 2) openrig — 팀 구조를 파일로
[openrig](https://github.com/mvschwarz/openrig)는 에이전트 팀의 **토폴로지를 YAML(RigSpec)**로 적고 `rig up` 한 번에 띄운다. Claude Code와 Codex를 한 시스템으로 묶고, 각 에이전트는 tmux 세션에 붙는다. 스냅샷·복원, 팀 묶음 아카이브, product-team·adversarial-review 같은 스타터 구성이 있다.

## 3) NVIDIA OpenShell — 함대를 위한 감옥
[OpenShell](https://github.com/NVIDIA/OpenShell)(Apache 2.0)은 “파일 읽고, 패키지 깔고, API 부르고, 자격증명 쓸 때 가장 유용한” 에이전트에게 그 힘을 주되 무제한 접근은 막는 런타임이다. 에이전트마다 샌드박스, **커널 단에서 모든 파일·시스템콜·네트워크 연결에 정책 검사**. 에이전트는 **진짜 자격증명을 보지 못하고**, 승인된 엔드포인트로 가는 요청에만 런타임이 붙여 준다. 정책을 바꿀 땐 **형식 검증**으로 새로 열리는 접근(새 호스트+자격증명 등)을 짚어 사람 검토로 넘긴다. 0.1.x부터 정기 릴리스 주기에 들어갔다.

## 왜 중요한가
퍼스널 OS·대시보드 관점에서 이건 **“에이전트 = 앱”이 아니라 “에이전트 = 인력”** 모델로의 전환이다. 필요한 기능이 조직도·예산·권한·감사로 회사 운영 소프트웨어를 닮아 간다. 트레이딩 봇처럼 돈이 걸린 에이전트일수록 OpenShell식 ‘자격증명은 런타임만 쥔다’ 패턴이 표준이 될 가능성이 크다.

## 기억할 것
- 별 수는 10/5 GitHub API 조회치. paperclip은 클라우드 버전 웨이트리스트 운영 중.
- [paperclip](https://github.com/paperclipai/paperclip) · [openrig](https://github.com/mvschwarz/openrig) · [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) · [주간 트렌딩 요약](https://www.tommyz.blog/blog/github-trending-weekly-2026-09-28-to-2026-10-03)
