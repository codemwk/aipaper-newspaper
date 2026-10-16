---
title: "세컨드 브레인 / PKM: Obsidian Copilot 4.0.15 — Claude Code·Codex가 내 노트를 고치면 ‘바뀐 파일’ 카드와 줄 단위 비교가 뜬다, ‘에이전트가 관리하는 위키’의 검수 화면"
date: 2026-10-17T07:11:00+09:00
category: "세컨드 브레인 / PKM"
slug: "obsidian-copilot-review-agent-edits"
summary: "Obsidian Copilot 4.0.15(10/16 KST): Agent Chat에서 Claude Code·Codex·OpenCode가 노트를 수정하면 답변 끝에 ‘Files changed’ 카드(파일별 추가·삭제 줄 수, 생성·삭제 표시). 클릭하면 Obsidian 렌더링 그대로 삭제는 취소선·추가는 하이라이트, 화살표로 변경점 이동. 채팅 고정·북마크, 오류 시 에이전트가 보고서 초안(사용자 검토 후 전송). Safe 모드에서 Claude가 쓰기 전 확인, 거절된 편집은 ‘Didn’t edit’. 호환성: Copilot Plus 문서 파싱 종료 → Miyo가 PDF·EPUB를 내 컴퓨터에서 처리."
---

## 한줄 요약
LLM Wiki(에이전트가 내 노트를 정리·연결·갱신하는 방식)의 가장 큰 불안은 “**AI가 내 노트를 몰래 망가뜨리면?**”이다. Obsidian의 대표 AI 플러그인 **Copilot**이 2026-10-16(KST) 내놓은 4.0.15는 정확히 그 불안을 겨냥했다 — 에이전트가 무엇을 바꿨는지 **한눈에 보고 확인하는 화면**이다([릴리스 노트](https://github.com/logancyang/obsidian-copilot/releases/tag/4.0.15)).

## 새로 생긴 것
- **‘Files changed’ 카드**: Agent Chat에서 Claude Code·Codex·OpenCode가 노트를 고치면, 답변 끝에 바뀐 파일 목록이 붙는다. 파일마다 **추가·삭제된 줄 수**, 에이전트가 **새로 만든 파일과 지운 파일** 표시.
- **노트 그대로 보는 비교**: 파일을 누르면 Obsidian이 렌더링한 모습 그대로, **삭제는 취소선, 추가는 하이라이트**. 긴 노트에선 상단 화살표로 변경 지점을 하나씩 건너뛴다. 원치 않은 편집을 넘어가기 전에 잡아낼 수 있다.
- **채팅 정리**: 최근 채팅 메뉴에서 **고정(pin)**, Obsidian **북마크에 추가**, 원본 노트 열기, 채팅 링크 복사.
- **문제 보고**: Agent Chat에서 뭔가 잘못되면 에이전트가 **보고서 초안**을 제안하고, 사용자가 검토한 뒤에만 전송. 전체 창 스크린샷 첨부 가능.

## 안전장치 손질
- **Safe 모드에서 Claude가 노트를 쓰거나 고치기 전에 묻도록** 수정(10/3 Codex Safe 모드에 이어 정렬).
- 거절되거나 실패한 편집은 카드에 **‘Didn’t edit’**로 명확히 표시.
- **호환성 주의(Breaking)**: 유료 Copilot Plus의 클라우드 문서 파싱이 종료되고, 로컬 검색엔진 **Miyo가 PDF·EPUB를 내 컴퓨터에서** 읽는다(설정 → Copilot → Miyo에서 켜고 끔). 직전 4.0.14(10/9)에는 Claude Code·Codex에 반복 작업을 맡기는 **Miyo Automations(알파)**가 들어왔다 — 예: 어제 못 끝낸 할 일을 오늘 데일리 노트로 옮기기.

## 왜 중요한가
지금까지 ‘Obsidian + 에이전트’ 조합은 **맡기는 기능**(수집·요약·연결·정기 작업)이 먼저 늘었고, **검수 기능**은 뒤처져 있었다. 코딩에서 에이전트를 믿게 만든 건 결국 **diff(변경 비교)와 승인**이었다 — 같은 장치가 노트에 들어온 것이다. LLM Wiki를 직접 굴릴 계획이라면 추천 운영법은 이렇다: ① Safe 모드로 시작해 쓰기마다 승인, ② 하루 한 번 ‘Files changed’ 카드로 에이전트 작업 검토, ③ 신뢰가 쌓인 폴더(예: `wiki/`)부터 자동 승인 범위를 넓히기. 원본 자료(`raw/`)는 에이전트가 건드리지 않게 분리해 두는 Karpathy식 구조와 함께 쓰면 효과가 크다. 이 플러그인은 오픈소스이며 GitHub 별은 약 7,800개다.

출처: [Obsidian Copilot 4.0.15 릴리스](https://github.com/logancyang/obsidian-copilot/releases/tag/4.0.15) · [4.0.14 릴리스](https://github.com/logancyang/obsidian-copilot/releases/tag/4.0.14) · [CODISH — Obsidian Copilot V4 해설(10/16)](https://codish.de/obsidian-copilot-v4-wie-claude-code-und-codex-aus-einem-note-tool-ein-ai-command-center-machen/)
