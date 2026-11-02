---
title: "세컨드 브레인 / PKM: Notion 새 AI 크레딧제, 11/2부터 기존 워크스페이스에도 — 1인당 월 Standard 1,500·Select 500, 이월 없음. 그런데 외부 에이전트가 MCP·API로 읽고 쓰는 건 ‘공짜’"
date: 2026-11-03T07:09:00+09:00
category: "세컨드 브레인 / PKM"
slug: "notion-ai-credits-mcp"
summary: "Notion의 새 AI 사용량 체계가 신규 Business·Enterprise(10/19)에 이어 11/2부터 기존 워크스페이스에도 적용됐다. 매달 1인당 Standard 1,500(자동 모델 선택 작업), Select 500(모델 지정 에이전트·커스텀 에이전트) 크레딧. 서로 합치거나 넘길 수 없고 매달 초기화. 반면 Notion MCP·API의 일반 읽기·쓰기는 크레딧을 쓰지 않는다(레이트 리밋은 적용). AI 회의록은 12/1부터 과금."
---

## 한줄 요약
Notion 안의 AI는 ‘쓸 만큼 쓰는 뷔페’에서 **‘월 정량 식권’**으로 바뀌었다. 흥미로운 건 경계선이다 — **Notion 밖의 에이전트(Claude Code 등)가 MCP로 노트를 읽고 쓰는 건 크레딧이 안 든다**([Notion 도움말](https://www.notion.com/help/standard-select-and-notion-credits-eligible-features), [AI 크레딧 관리](https://www.notion.com/help/manage-your-ai-credits), [synon 정리](https://synon.co.jp/article/news/2026-11-02-obsidian-ai-daily)).

## 무엇이 어디서 차감되나
| 구분 | 주요 대상 | 양·조건 |
|---|---|---|
| Standard | Auto(자동 모델 선택) Notion Agent, AI 편집·번역, AI 블록·수식, AI 회의록(12/1~) | 1인당 월 1,500, 이월 없음 |
| Select | 모델을 직접 고른 Notion Agent, 커스텀 에이전트 | 1인당 월 500, 이월 없음 |
| Notion 크레딧 | 위 둘을 다 쓴 뒤(관리자 허용 시), 비싼 모델, 워크스페이스 부담 에이전트 | 관리자가 사용 승인 |
| 차감 없음 | **Notion MCP·API 일반 읽기·쓰기**, Workers(베타 기간) | 레이트 리밋은 적용 |

- 두 크레딧은 합산·교환·멤버 간 양도 불가. 다 쓰면 관리자가 Notion 크레딧 사용을 허용하지 않는 한 **다음 초기화까지 그 기능이 멈춘다**.
- AI 회의록은 12/1부터 Standard 차감(1시간 회의 약 10크레딧이 기준). 내 사용량은 설정 → Notion AI → Usage.
- 단, **API나 연결 앱을 통해 Notion Agent를 ‘실행’시키는 건** 크레딧을 쓴다 — 공짜인 건 데이터 읽기·쓰기다.

## 세컨드 브레인 사용자에게 무슨 의미인가
- 가격 구조가 **“생각은 바깥 에이전트로, 저장은 Notion으로”**를 유리하게 만든다. 외부 에이전트가 MCP로 정리·요약해 Notion에 써 넣으면 Notion AI 크레딧을 건드리지 않는다(외부 모델 비용은 별도).
- 반대로 Notion 안에서 모델을 골라 에이전트를 돌리는 습관이라면 **월 500 Select가 금방 바닥**날 수 있다. 무엇을 Auto로 돌릴지 정리해 둘 시점.
- Obsidian+에이전트 조합과 비교하면: Obsidian은 노트가 로컬 파일이라 처음부터 ‘바깥 에이전트’ 구조였고, Notion은 이번 가격표로 그 구조를 **공식적으로 허용**한 셈이다.
