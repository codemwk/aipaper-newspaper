---
title: "세컨드 브레인 / PKM: 개인 LLM Wiki는 된다, 팀은 ‘게이트·날짜·읽은 횟수’가 필요하다 — Harbor가 정리한 실패 패턴"
date: 2026-10-13T07:08:00+09:00
category: "세컨드 브레인 / PKM"
slug: "llm-wiki-team-harbor"
summary: "Karpathy LLM Wiki는 개인용 패턴. Harbor(10/6)는 팀 공유 시 필요한 세 가지로 승인 게이트, 클레임 날짜·폐기, 에이전트가 실제로 읽은 페이지 카운트를 든다. 도구 스냅샷: Obsidian 플러그인 ~5.8만 다운로드, nashsu/llm_wiki ~20.6K★. 공유 메모리에 거짓이 들어가면 97–99% 재주장(관련 논문 인용)."
---

## 한줄 요약
Karpathy식 LLM Wiki는 **개인**에게는 잘 작동한다. [Harbor](https://gethrbr.com/blog/karpathy-llm-wiki)는 **2026-10-06** 글에서, 같은 위키를 **팀이 나누면** gist가 빠뜨린 세 가지 — **게이트(승인)**, **날짜·폐기**, **읽힘/인용 카운트** — 가 필요하다고 정리했다. 어제·그제 Cadabby 등 “개인 위키 구현” 기사와 결이 다르다.

## 핵심
- **패턴 복습**: raw(불변) / wiki(LLM이 씀) / schema(`CLAUDE.md`·`AGENTS.md`). 연산은 ingest·query·lint. `index.md`+`log.md`가 뼈대.
- **도구 스냅샷**(Harbor 표, 2026-10-06 기준 + 오늘 스타 재확인): Karpathy Obsidian 플러그인 **~58,173 다운로드**(팀 협업 없음이라고 README), [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) 데스크톱 **~20,565★**(2026-10-13 `gh`), claude-obsidian·llm-wiki-compiler·synthadoc·codealmanac 등 — 표의 세 번째 열이 거의 전부다: **Built for: one person**.
- **팀에서 깨지는 방식**: “누구나 쓰고 아무도 안 읽음”, 인덱스 오류 증폭, 에이전트가 잘못된 항목을 재인용. 공유 에이전트 메모리 연구(arXiv:2609.30813, Harbor 인용)에서는 반박 없는 거짓 믿음이 들어오면 프로브의 **97–99%**에서 재주장, 소스 타입 게이트 시 **6–9%**로 떨어졌다고 요약한다.
- **팀 처방전**: (1) 누구나 초안, **사람·정책이 promote** (2) 클레임에 **출처 날짜·폐기** (3) 작업에 **관련 페이지를 실어 보내고**, 읽힘·인용을 **센다**(자주 쓰임 ≠ 참).

## 왜 중요한가
AiPaper 독자(그리고 ANDRSN 내부)가 LLM Wiki를 “두 번째 뇌”로 쓰는 다음 단계는 **팀·브랜드 지식**이다. 게이트 없는 공유 위키는 자신감 있는 오정보를 양산한다. Harbor는 엔지니어링 **결정 규칙**에 특화한 제품으로 자신을 위치시키지만, 글 자체의 체크리스트는 도구 비의존으로 읽을 수 있다.

## 기억할 것
- 개인 연구 위키는 gist 그대로. 팀 위키는 **git ≠ 진실**.
- 위키 vs RAG 소규모 비교(arXiv:2605.18490)는 합성이 낫고 토큰은 ~21× — 비용 트레이드오프.

출처: [Harbor — Karpathy LLM wiki for teams](https://gethrbr.com/blog/karpathy-llm-wiki) · [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) · [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
