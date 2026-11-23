---
title: "AI 도구: Anthropic ‘Claude Ship’ — PR을 올리면 Claude가 리뷰하고, 고치고, 팀 규칙이 허락하면 ‘승인’까지. 사람은 정말 봐야 할 변경만"
date: 2026-11-24T07:20:00+09:00
category: "AI 도구"
slug: "claude-ship-review-fix-approve"
summary: "Anthropic이 11/23 Claude Ship 베타를 공개했다. 이미 정식 출시된 Code Review에, 실패한 CI·머지 충돌·리뷰 지적을 알아서 고치는 PR Steward와 저장소에 둔 정책 파일대로 일상적 변경을 승인하는 Claude Approvals를 붙였다. 개발자는 Claude Code에서 /ship 한 번으로 푸시·PR·리뷰·수정까지 맡긴다. Claude Team·Enterprise, GitHub 저장소 대상이며 토큰 과금. Claude Code 팀에서는 6~9월 머지된 PR이 두 배 넘게 늘고 되돌린 비율은 40% 넘게 줄었다고 한다."
---

## 한줄 요약
에이전트가 코드를 빨리 쓰게 되자 **막히는 곳이 ‘PR 이후’로 옮겨 갔다.** 리뷰를 기다리고, 지적을 고치고, 승인해 줄 사람을 찾는 일이다. 11/23 공개된 **Claude Ship**은 이 세 단계를 Claude에게 맡긴다([Anthropic](https://claude.com/resources/articles/introducing-claude-ship), [문서](https://code.claude.com/docs/en/claude-ship), [The Verge](https://www.theverge.com/ai-artificial-intelligence/1040134/anthropic-claude-ship-ai-pull-requests)).

## 세 단계
- **Code Review (정식 출시)**: 여러 관점으로 PR을 검토하고, 찾은 문제를 **스스로 반박 검증**한 뒤 분류해 남긴다. 저장소마다 Quick·Standard·Deep 수준을 고른다.
- **PR Steward (베타)**: PR을 ‘초록불’로 유지하는 담당. 실패한 CI, 머지 충돌, 리뷰 지적이 오면 고친다. **푸시할 때마다 무엇을 바꿨고 어떻게 되돌리는지** 댓글을 단다. `@claude`로 지시하고 `@claude stop`으로 멈춘다. **스스로 승인·머지는 하지 않게** 설계됐다.
- **Claude Approvals (베타)**: 팀이 저장소에 쓴 **정책 파일**(`.claude/approvals.yml`)대로 일상적 변경은 승인하고, 특정 경우엔 사람 서명을 요구한다. 회사 표현으로 **“더 똑똑한 CODEOWNERS.”** 처음엔 **관찰 모드**로 돌려 믿음이 생긴 뒤 브랜치 보호 규칙에 연결하라고 권한다.

## 쓰는 법과 비용
- 개발자: Claude Code에서 **`/ship`** 한 번. 푸시 → PR 열기 → 리뷰 → 지적·실패 수정까지. 머지 가능 여부는 본인 권한과 브랜치 규칙을 따른다.
- 관리자: 저장소별로 켜고, 리뷰 수준·실행 시점·**월 지출 한도**를 정한다. 기존 브랜치 보호와 필수 체크는 그대로 쓴다.
- **토큰 과금**이다. PR 수·크기·리뷰 수준·Steward 작업량에 따라 비용이 늘어난다. Approvals는 기본료가 없지만, 정책에 Claude 리뷰를 쓰면 관찰 모드에서도 리뷰 비용이 든다.
- Claude **Team·Enterprise**, **GitHub** 저장소 대상. 데이터 무보존(ZDR)·HIPAA·고객 관리 암호키 조직은 쓸 수 없다. 자격 있는 Enterprise는 1만 달러 이상 크레딧을 받을 수 있다(2027-01-15까지 신청).

## 회사가 밝힌 효과
Claude Code 팀에서는 Claude 리뷰를 여러 검토 층 중 하나로 두고, **6월~9월 머지된 PR이 두 배 넘게** 늘었고 **되돌린(revert) 비율은 40% 넘게** 줄었다. 고객 피드백을 읽은 PM이 Claude에게 PR을 열게 하고, 리뷰·문서 검토·정책 승인을 거쳐 **그날 저녁 머지**된 사례도 소개했다. 모두 회사 자체 수치다.

## 왜 중요한가
핵심은 **“사람 승인을 없앤다”가 아니라 “어떤 변경에 사람이 필요한지를 파일로 적는다”**는 점이다. 문서 오타, 의존성 소폭 업데이트처럼 위험이 낮은 변경은 정책이 통과시키고, 결제·인증·배포 설정은 사람에게 넘기는 식이다. 혼자 여러 에이전트를 돌리는 개인 개발자에게도 같은 원리가 통한다. **승인 규칙을 글로 먼저 써 두면**, 에이전트에게 맡길 범위가 자연스럽게 정해진다. 다만 Team 이상 요금제 전용이라, 개인은 당장 `/ship`만 시험해 볼 수 있다.
