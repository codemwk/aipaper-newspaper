---
title: "세컨드 브레인 / PKM: ‘검색되는 엉망도 엉망이다’ — 메모와 결정을 다른 파일에 두는 decisions.md 습관, 그리고 기억을 칸막이로 나눈 ChatGPT ‘잠긴 대화’"
date: 2026-10-21T07:11:00+09:00
category: "세컨드 브레인 / PKM"
slug: "decisions-md-locked-memory"
summary: "10/20 TLDR Design·HeyDesigner가 함께 소개한 디자이너 안톤 스텐의 글 ‘Where decisions live’(10/16): 프로젝트 폴더마다 running-notes.md(시간순, 지저분해도 되는 관찰·질문·시도)와 decisions.md(최신 결정이 맨 위, 날짜 필수, 바뀐 결정은 지우지 않고 위에 새로 추가)를 분리. 에이전트에게 맥락을 많이 주는 것만큼 ‘탐색과 확정’, ‘옛 정보와 현재 정보’를 구분하는 구조가 중요하다는 주장. 같은 날 OpenAI는 ChatGPT ‘잠긴 대화(Locked Chats)’ 출시: 4자리 PIN·Face ID/Touch ID, 별도 섹션·검색 제외, 메모리 켜면 잠긴 대화끼리만 공유하는 별도 메모리(일반 메모리로 새지 않음). 종단간 암호화·보존 기간 변경은 아님, PIN 재설정 시 전부 영구 삭제. 무료~Enterprise·Edu 요금제에 순차 배포."
---

## 한줄 요약
AI가 내 기록을 다 읽을 수 있게 되자 새 문제가 생겼다. **무엇이 ‘지금 유효한’ 정보인지** AI가 구분하지 못한다. 10/20 디자인 뉴스레터들이 함께 소개한 글 한 편과, 같은 날 나온 ChatGPT 기능 하나가 같은 답을 가리킨다: **기억에는 칸막이가 필요하다.**

## 1. running-notes.md와 decisions.md
디자이너 **안톤 스텐**은 프로젝트 폴더마다 파일 두 개를 둔다([Where decisions live](https://www.antonsten.com/articles/where-decisions-live/), 10/16).
- **`running-notes.md`** — 시간순. 관찰, 질문, 해 본 것, 나중에 중요할지 모를 디테일, 아직 바뀌는 생각. **지저분해도 된다.**
- **`decisions.md`** — 엄격하다. 어디로 결론 났는지, **최신 결정이 맨 위**, 모든 항목에 **날짜**. 결정이 바뀌면 옛 결정을 **지우지 않고** 그 위에 새 결정을 쓴다. 팀 회의 결정뿐 아니라 혼자 내린 디자인 결정도 적는다.
- 나머지 역할: 슬랙은 토론, 회의는 결론(그는 Granola로 회의를 기록한다).

핵심 문장은 이것이다. “구분이 없으면 **모든 옛 생각이 현재 결정과 같은 무게**를 갖는다. 에이전트에게 물으면, 출처까지 완벽하게 달린, **아무도 더는 믿지 않는 답**이 돌아온다.” 날짜가 붙은 결정 기록은 **제품 생각의 버전 기록**이 된다. 결론: “검색되는 엉망도 여전히 엉망이다.”

## 2. ChatGPT ‘잠긴 대화’ — 메모리를 따로 쓰는 방
OpenAI가 10/20 출시했다([TechCrunch](https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/)).
- **4자리 PIN** 또는 Face ID·Touch ID로 잠근다. 잠긴 대화는 별도 섹션으로 옮겨지고 **일반 기록·고정·검색에서 빠진다.** 임시 대화와 달리 언제든 다시 열 수 있다.
- **메모리 분리**: 메모리가 켜져 있으면 잠긴 대화들은 **그들끼리만 공유하는 별도 메모리**를 쓴다. 잠근 뒤의 새 내용은 **일반 메모리에 들어가지 않는다.**
- **한계**: 종단간 암호화나 별도 암호 금고가 **아니다.** 보존 기간도, 잠그기 전에 이미 기억된 내용도, ‘모델 개선’ 설정도 그대로다. **PIN을 재설정하면 잠긴 대화·파일이 전부 영구 삭제**된다.
- 무료·Go·Plus·Pro·Business·Enterprise·Edu에 순차 배포(의료용 ChatGPT 제외). 임시·보관·그룹 대화, 예약 작업이나 회의 녹음이 있는 대화는 잠글 수 없다.

## 둘을 합치면: 내 볼트에 적용하기
- **현재와 과거를 나눈다**: 프로젝트 노트마다 `decisions.md`를 두고, 에이전트 지시문(CLAUDE.md 등)에 “사실 판단은 decisions.md 우선, running-notes는 배경으로만”이라고 적는다.
- **맥락을 나눈다**: 개인·재무·건강처럼 업무와 섞이면 안 되는 기억은 별도 볼트나 폴더로 분리해, 에이전트가 기본적으로 읽지 않게 한다. ChatGPT의 잠긴 대화가 바로 이 원리를 제품으로 만든 것이다.
- **날짜는 필수**: AiPaper 제목 앞에 [10/21]을 붙이는 것도 같은 이유다 — 언제의 정보인지 모르면 정보가 아니라 위험이 된다.

출처: [Anton Sten — Where decisions live (10/16)](https://www.antonsten.com/articles/where-decisions-live/) · [TLDR Design (10/20)](https://tldr.tech/design/2026-10-20) · [TechCrunch — ChatGPT now lets you lock your chats (10/20)](https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/)
