---
title: "GitHub 이번 주: ‘전부 Rust로 다시 짜지 말고 느린 5%만’ — 에이전트가 함수 하나씩 옮기고 실제 호출로 검증하는 fast-anything, 7만 5천 별 넘긴 /last30days"
date: 2026-11-26T07:45:00+09:00
category: "GitHub 트렌드"
slug: "github-fast-anything-last30days"
summary: "11/18–11/25 GitHub에서 새로 만들어진 저장소 중 fast-anything(11/21 생성, 약 3,600★, MIT)이 눈에 띈다. 앱을 프로파일링해 느린 함수만 골라 코딩 에이전트가 Rust로 옮기게 하고, 실제로 기록한 호출 최대 500개를 다시 돌려 결과가 같을 때만 바꿔 끼운다. 주간 별 증가 1위는 레딧·X·유튜브·폴리마켓의 ‘사람들 반응’으로 주제를 조사하는 에이전트 스킬 /last30days(약 7만 5천★, +5천 이상)였다."
---

## 한줄 요약
이번 주 GitHub의 분위기는 일본 Shareuhack 정리 그대로다. **“에이전트의 일을 검증 가능한 단위로 쪼갠다.”** 그 대표 사례 두 개를 쉬운 말로 풀었다([Shareuhack 11/25 주간](https://www.shareuhack.com/ja/posts/github-trending-weekly-2026-11-25), [GitStock 11/25 주간](https://gitstock.org/trending/weekly/2026-11-25)). 반복해서 다룬 저장소(Plannotator, Univer, ffmpeg-skill, Astryx, open-code-review, Modern Web Guidance, Claude Trading Skills 등)는 뺐다.

## 1. fast-anything — 느린 함수만 Rust로, 증명하고 바꿔 끼우기
- 저장소: [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything). **11/21 생성, 약 3,600★**(Shareuhack 집계, 주간 신규 3위). MIT.
- 구호: **“Rust로 다시 짜지 마라. 느린 5%만 다시 짜라.”** 앱 전체를 옮기면 몇 달, 실행 시간 대부분은 몇몇 함수에 몰려 있다는 관찰에서 출발.
- 순서:
  1. `scan` — 앱을 돌려 **시간 × 옮기기 쉬운 정도**로 함수 순위.
  2. `port` — 그 함수의 **실제 호출을 최대 500개 기록**하고, 함수 하나짜리 Rust 패키지와 작업 지시서(TASK.md)를 만든다. Claude·Codex 같은 에이전트가 이걸 받아 옮긴다.
  3. `verify` — 기록한 호출을 **전부 다시 돌려** 원본과 비교. NaN·무한대·-0.0·비ASCII 문자·빈 입력 같은 **경계 사례도 자동 추가.**
  4. `enable/disable` — 한 블록만 바꿔 끼우고, 끄면 **바이트 단위로 원상복구.**
- **꼼수 방지:** 기록한 호출 5개 중 1개는 에이전트가 볼 수 없게 숨겨 두고 검증 때만 쓴다. 보여 준 예시만 맞추는 ‘시험용 답안’은 떨어진다. 맞지만 오히려 느린 포팅도 켜지지 않는다.
- README 예시: 파이썬 이름 중복 제거 700개 **4.91초 → 42ms(116배)**. 지원 언어는 Python·Node/TS·Ruby·Java·Go·PHP·C/C++·C#·R 등. Claude Code·Codex 플러그인과 MCP 서버 포함.
- 쉽게 말해: **에이전트에게 코드를 맡기되, “믿어라” 대신 “실제 기록으로 증명해라”**를 기본값으로 만든 도구.

## 2. /last30days — “편집자가 아니라 사람들의 반응으로 검색”
- 저장소: [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill). 약 **75,000★**, 이번 주 **+5,369**(GitStock 기준 주간 최다). 9월에 소개했을 때보다 훨씬 커졌고 지금은 v4 파이프라인이다.
- 주제를 주면 **레딧, X, 유튜브, Hacker News, 폴리마켓, 웹**을 동시에 훑고, **추천수·좋아요·실제 돈이 걸린 배팅 확률**로 점수를 매긴 뒤 AI가 **근거 있는 요약 한 장**으로 묶는다.
- 설정 없이 레딧·HN·폴리마켓·GitHub가 바로 되고, 회사 이름을 넣으면 **특허 출원·채용 페이지**도 본다. 마법사로 X·유튜브·틱톡·arXiv·Techmeme 추가.
- 설치: Claude Code 플러그인, 또는 `npx skills`로 Codex·Cursor·Copilot·Gemini CLI 등 50개 이상 호스트.

## 왜 중요한가
- 두 도구의 공통점은 **입력과 출력이 남는다**는 것이다. fast-anything은 기록한 호출과 검증 결과가, /last30days는 원문 링크가 남는다. 에이전트 결과를 믿을지 말지는 이 **흔적**에서 결정된다.
- 실전 팁(Shareuhack 권고와 같음): fast-anything은 **결정적인 작은 순수 함수**부터, /last30days는 **기밀이 아닌 조사**부터. 인기 ≠ 사실이니 요약을 그대로 사실로 쓰지 말고 원문을 확인할 것.
