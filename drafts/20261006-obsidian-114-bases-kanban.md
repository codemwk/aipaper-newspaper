---
title: "세컨드 브레인 / PKM: Obsidian 1.14 공개 — 볼트 밖 .md 열기·Bases 칸반·하이라이트 6색, ‘에이전트가 쓴 파일’을 읽기 쉬워졌다"
date: 2026-10-06T07:02:00+09:00
category: "세컨드 브레인 / PKM"
slug: "obsidian-114-bases-kanban"
summary: "10/5 Obsidian 1.14(데스크톱·모바일 공개): 볼트 밖 Markdown 파일 열기·OS 기본 앱 지정·macOS Quick Look, Bases 칸반 뷰와 Group 메뉴, 이모지로 지정하는 하이라이트 6색, 대형 볼트 퍼지 검색·입력 지연 개선. 새 인스톨러(Electron 43.7.5) 재설치 필요."
---

## 한줄 요약
[Obsidian 1.14](https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/)가 10월 5일 데스크톱·모바일 공개 버전으로 나왔다. 세 가지 큰 변화: **볼트 밖 Markdown 파일 열기**, **Bases 칸반 뷰**, **하이라이트 색상**. AI 기능은 여전히 플러그인·BYOK 몫이지만, 이번 업데이트는 **LLM Wiki·에이전트 워크플로를 쓰는 사람에게 체감이 큰** 기본기 개선이다.

## 바뀐 것
- **볼트 밖 .md 열기**: “Open file from outside the vault…” 명령, OS의 ‘다음으로 열기’에 Obsidian 등록, **.md 기본 앱 지정**, macOS에선 앱이 꺼져 있어도 **Quick Look 미리보기**. 이미지·링크는 그 파일 폴더 기준으로 해석되고, Outline·Outgoing links도 쓴다. (최신 인스톨러 재설치 필요)
- **Bases 칸반**: 노트를 열(column)로 정리하고 카드 드래그로 그룹 이동. 새 Group 메뉴로 그룹 속성 선택·순서 변경·숨기기, 테이블·카드·리스트에서도 그룹 접기.
- **하이라이트 6색**: 하이라이트 앞에 🔴🟠🟡🟢🔵🟣 이모지를 붙이거나 서식 메뉴에서 선택. `==` 입력 시 색 제안.
- **대형 볼트**: 퀵 스위처·링크 제안 퍼지 검색이 볼트 크기와 무관하게 동작하고 더 빨라짐, 속성 재계산으로 인한 주기적 입력 지연 수정, `[[##` 전체 헤딩 검색 프리즈 수정.
- 신뢰하지 않은 볼트를 열면 ‘작성자를 신뢰하나요’ 창이 떠 있는 동안 테마·스니펫을 일시 비활성화.

## LLM Wiki 관점에서 왜 중요한가
- **에이전트 산출물 검토**: Claude Code·Codex가 저장소 곳곳에 남기는 `README`·`AGENTS.md`·리서치 노트를 **볼트로 옮기지 않고** Obsidian으로 바로 열어 Outline·링크로 훑을 수 있다. “Obsidian은 IDE, LLM은 프로그래머, 위키는 코드베이스”라는 Karpathy 구도에서 IDE가 볼트 밖까지 넓어진 셈.
- **Bases 칸반 = 위키 파이프라인 보드**: frontmatter에 `status: raw / compiled / reviewed` 같은 속성을 두면, 에이전트가 ingest한 페이지를 칸반으로 보면서 사람이 **검토 단계를 드래그로 관리**할 수 있다.
- **색 하이라이트 = 사람 vs AI 표시**: 예컨대 🟢는 내가 확인한 사실, 🟡는 AI 요약처럼 규칙을 정하면 위키의 신뢰도를 눈으로 구분할 수 있다(이건 활용 아이디어, 공식 기능 설명 아님).

## 기억할 것
- 개발자: Electron 43.7.5, MathJax 4.1.3, 툴팁·노티스·탭 CSS 변수 추가.
- [Obsidian 1.14 Desktop 변경 로그](https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/) · [Mobile](https://obsidian.md/changelog/2026-10-05-mobile-v1.14.4/)
