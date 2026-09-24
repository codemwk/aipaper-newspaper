---
title: "GitHub Hot: Cloudflare security-audit-skill — 코딩 에이전트를 ‘보안 감사관’으로"
date: 2026-09-25T07:07:00+09:00
category: "GitHub Hot"
slug: "cloudflare-security-audit-skill"
summary: "cloudflare/security-audit-skill(~21.3k★). 정찰→커버리지 헌팅→검증→구조화 findings→독립 재검증→리포트 6단계. Cloudflare 취약점 디스커버리 하네스의 단일 레포 출발점."
---

## 한줄 요약
[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)은 코딩 에이전트용 **보안 감사 스킬**이다. “취약점 찾아줘” 한 마디를 **재현 가능한 다단계 워크플로**로 바꾼다(~21.3k★, 2026-09-25 기준).

## 어떻게 동작하나
1. **정찰** — 아키텍처·신뢰 경계·입력면 → `architecture.md`, `coverage-ledger.json`
2. **커버리지 주도 헌팅** — 격리된 헌터 + 커버리지 크리틱
3. **후보 검증** — 새 검증자가 후보를 반증 시도
4. **구조화 출력** — `confirmed` / `needs_validation` / `rejected` → `findings.json` + 스키마 검증
5. **독립 레코드 재검증**
6. **타깃 중립 리포트** — `REPORT.md` 등

`npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`로 설치. Cloudflare 블로그 [Build your own vulnerability harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness)에서 설명한 하네스의 **단일 레포 시드**.

## 왜 중요한가
에이전트 스킬이 “예쁜 프롬프트 모음”을 넘어 **검증기·스키마·커버리지 장부**를 동반하는 쪽으로 성숙한다. 보안을 ‘한 번 물어보기’가 아니라 **감사 프로세스 제품**으로 보는 신호.

## 기억할 것
- [GitHub](https://github.com/cloudflare/security-audit-skill) · [Cloudflare 블로그](https://blog.cloudflare.com/build-your-own-vulnerability-harness)
