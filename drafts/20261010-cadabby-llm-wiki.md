---
title: "세컨드 브레인 / PKM: Cadabby — PARA 폴더 세금 버리고, Karpathy식 LLM Wiki(flat wiki/)로 옮긴 실전 후기"
date: 2026-10-10T07:18:00+09:00
category: "세컨드 브레인 / PKM"
slug: "cadabby-llm-wiki"
summary: "naikoob이 10/6 Abby(PARA+MCP 도구)에서 Cadabby(LLM Wiki)로 피벗한 글을 공개. note_move·백링크 수리가 ‘폴더 세금’. raw/ 수집 + flat wiki/ + account/ 고객 경계. 상태·관계는 frontmatter·wikilink·MOC."
---

## 한줄 요약
LLM Wiki를 “써 보고 싶다”는 사람 앞에서, 실무자가 **PARA 자동화 코드를 짜다 포기하고** flat wiki로 옮긴 기록이 나왔다. [@naikoob — Introducing Abby Cadabby](https://naikoob.github.io/blog/second-brain/ai/architecture/2026/10/06/introducing-abby-cadabby.html)(10/6).

## Abby가 보여 준 것
speckit으로 `note_capture`·`note_move`·`note_archive`·`vault_lint` 계약을 단단히 짰다. 그런데 코드 감사 결과, 상당량이 **Inbox→Projects→Archive 경로 이동**, 이동 시 **백링크 수리**, 폴더 `index.md` 동기화 — 이른바 **폴더 세금**이었다. 에이전트는 트리 브라우징보다 검색·링크로 움직이는데, 사람은 폴더 분류에 토큰을 쓰고 있었다.

## Cadabby = LLM Wiki 실전형
- `raw/` — 스크래치·트랜스크립트 수집.
- `wiki/` — 상록 지식 **평탄** 배치. 경로가 곧 정체성(이동 없음).
- `account/<client>/` — 고객 맥락 격리(일반 wiki 오염·크로스 검색 누수 방지).
- 생명주기는 폴더가 아니라 frontmatter `status`, 관계는 `[[wikilink]]`·MOC.
- 도구도 `note_move` 대신 `kb_scaffold`·`kb_graph`·`kb_search`·`kb_inspect`.

## 왜 중요한가
Karpathy LLM Wiki 플러그인(이미지 근거 등)과 맞물려, “두 번째 뇌” 담론이 **폴더 정리 자동화**에서 **그래프·수집/위키 이층 구조**로 옮기는 증거다. AiPaper 독자(LLM Wiki 관심)에게는 “스펙부터 짜도 잘못된 추상화면 폴더 로봇이 된다”는 교훈이 크다.

출처: [Introducing Abby Cadabby](https://naikoob.github.io/blog/second-brain/ai/architecture/2026/10/06/introducing-abby-cadabby.html) · [naikoob/cadabby](https://github.com/naikoob/cadabby)
