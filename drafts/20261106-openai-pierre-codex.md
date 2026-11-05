---
title: "GitHub: OpenAI, Pierre 인수 — Codex에 Git 저장·디프·리뷰 UX를 붙이는 한 수"
date: 2026-11-06T07:08:00+09:00
category: "GitHub"
slug: "openai-pierre-codex"
summary: "OpenAI가 11/4 Pierre Computer Company 인수를 발표했다. Codex 앱의 파일 트리·디프는 이미 Pierre의 Trees·Diffs 라이브러리다. 인수 후 Code Storage(Git 기반 코드 저장)를 Codex로 가져오겠다는 목표. 오픈소스는 유지, 거래 조건·일정은 미공개. 규제 승인 등 종결 조건이 있다."
---

## 한줄 요약
OpenAI가 **Pierre**를 사들여, 코딩 에이전트 Codex를 **‘코드 쓰는 챗’에서 ‘브랜치·리뷰·저장까지 한곳’** 으로 키우려 한다([OpenAI 11/4](https://openai.com/index/openai-to-acquire-pierre)).

## 지금 뭐가 뜨나
- **이미 쓰는 중**: Codex 앱의 파일 브라우즈·변경 리뷰는 Pierre **Trees·Diffs**. Diffs Edit 모드로 리뷰 화면에서 바로 한 줄 수정, Highlights는 타이핑·에이전트 스트리밍에 맞춘 고속 하이라이터.
- **Code Storage**: 앱이 Git으로 코드·히스토리를 저장하는 서비스. 종결 후 Codex에 기능을 흡수하는 것이 목표. 그전까지 고객은 계속 사용 가능하다고 안내.
- **맥락**: 같은 주 OpenAI는 사내 Git 백엔드 **Pando**로 엔지니어·에이전트 동시 스케일을 공개한 바 있다. Axios는 GitHub를 겨냥한 움직임으로 해석했다.
- **오픈소스**: Pierre OSS는 계속 오픈소스·기여 예정. 금액·일정 미공개. 규제 승인 등 종결 조건.

## 왜 중요한가
에이전트가 병렬로 브랜치를 치면 **디프·리뷰·저장 UX**가 IDE만큼 중요해진다. Cursor·Claude Code가 에디터·터미널을 차지했다면, OpenAI는 **Git 주변 도구**를 자사 Codex 안으로 끌어들이는 중이다. 멀티 에이전트 워크플로를 쓰는 팀이 ‘어디에 PR을 쌓을지’를 다시 보게 된다.

## 주의
발표일 기준 OpenAI와 Pierre는 별도 회사. 종결 전 로드맵·가격은 확정이 아니다.
