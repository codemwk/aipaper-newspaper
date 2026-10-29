---
title: "AI 도구: 같은 날 두 갈래 — Gemini는 ‘채팅 안에서 문서·PDF를 만들고 고치기’, Claude는 ‘Docs·Sheets·Slides 옆 사이드바로 들어가기’"
date: 2026-10-30T07:08:00+09:00
category: "AI 도구"
slug: "gemini-claude-edit-office-files"
summary: "10/29 구글은 Gemini 앱에서 문서·PDF·프레젠테이션·스프레드시트·마크다운·코드를 생성하고 미리 보고 직접 고칠 수 있게 했다(PDF는 웹·모바일, 나머지는 웹, 모든 사용자·지원 언어). 같은 날 Anthropic은 Claude for Google Workspace를 유료 플랜 공개 베타로 냈다 — Docs·Sheets·Slides 사이드바 + Claude에서 파일을 만드는 커넥터, 기본은 변경마다 승인 카드."
---

## 한줄 요약
AI와 문서 작업을 합치는 방법이 두 갈래로 갈렸다. **채팅창이 문서 편집기가 되거나(Gemini)**, **AI가 문서 편집기 옆자리로 들어가거나(Claude)**.

## Gemini: 채팅 안의 문서
- 파일을 **생성 → 미리 보기 → 직접 수정**까지 채팅 안에서. 전체 화면으로 키워 직접 타이핑하거나, 문장을 드래그해 질문하거나, Gemini에게 고치라고 시킨다([Google 블로그](https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/)).
- 예: 손글씨 강의 노트를 올려 **PDF 공부 자료**를 만들고, 특정 부분만 골라 다시 쓰게 하기.
- 지원: **PDF는 웹·모바일**, Google Docs·Sheets·슬라이드·마크다운·TXT·코드는 **웹만**. Gemini 앱이 되는 모든 언어·모든 사용자.

## Claude: 문서 옆 사이드바
- **Claude for Google Workspace** 공개 베타(유료 플랜). 열린 Doc·Sheet·Slide 옆 사이드바에서 작업하고, 따로 커넥터로 Claude 대화에서 구글 파일을 만들거나 고친다([Claude News](https://claudenews.com/news/claude-now-works-with-google-docs-sheets-and-slides)).
- Docs: 문장·서식 수정 제안/적용. Sheets: 수식·피벗 테이블·차트. Slides: **덱의 기존 레이아웃으로** 새 슬라이드, 일부 레이아웃 문제 지적.
- 기본 모드는 **변경마다 승인 카드**. ‘모두 수락’ 모드도 있고, 팀·엔터프라이즈는 관리자가 커넥터를 켜야 한다.

## UI 관점에서 본 차이
| | Gemini | Claude |
|---|---|---|
| 작업의 중심 | 채팅 | 파일 |
| 편집 방식 | 채팅 속 캔버스에서 직접 타이핑 + 부분 선택 수정 | 사이드바 제안 → 승인 카드 |
| 잘 맞는 일 | 새 자료를 처음부터 만들기 | 이미 있는 팀 문서를 다듬기 |

## 왜 중요한가
- 제품 UI 패턴으로 보면 **“생성은 채팅, 마무리는 편집기”**의 경계가 무너지는 중이다. 오늘 Figma·Canva 기사와 같은 흐름 — 결과물이 언제나 **사람이 다시 손댈 수 있는 형태**로 남는다.
- 매일 쓰는 AiPaper 같은 개인 대시보드도, 결과를 ‘읽기만’이 아니라 **바로 고칠 수 있게** 두는 게 다음 단계다.
