---
title: "GitHub 이번 주: 에이전트 도구의 ‘뒷정리’가 화제 — Anthropic 오피스 스킬 Apache 2.0, ‘어느 줄의 버튼인지’ 알려주는 agent-browser, 비밀키를 출력하던 버그 수정"
date: 2026-11-15T07:06:00+09:00
category: "GitHub 트렌드"
slug: "github-office-skills-agent-browser"
summary: "46주차 GitHub 주간 트렌딩에서 새 기능보다 ‘신뢰’를 다듬는 변경이 눈에 띈다. anthropics/skills(+6천)는 Word·PDF·PowerPoint·Excel 스킬을 Apache 2.0으로 옮겼고, agent-browser 0.43(+4.6천)은 이름이 같은 버튼을 구분하는 힌트를 넣었다. addyosmani/agent-skills(+3.2천)는 비밀키 검사가 오히려 키를 화면에 찍던 버그를 고쳤다."
---

## 한줄 요약
46주차 GitHub 주간 트렌딩(11/13 집계) 상위권에는 **에이전트가 쓰는 도구를 믿고 쓸 수 있게 다듬는 변경**이 많았다. 숫자는 11/13 기준 주간 별 증가량이다([GitHub AI Weekly 14호](https://00011000.com/en/news/github-ai-weekly-2026-w46), [주간 트렌딩](https://git-trending-rank.github.io/post/trending-weekly-2026%E5%B9%B4%E7%AC%AC46%E5%91%A8/)).

## anthropics/skills (+6,055, 누적 약 19.4만) — 오피스 스킬을 마음 놓고 가져다 쓰게
- Anthropic의 공개 ‘에이전트 스킬’ 저장소다. 스킬은 에이전트에게 특정 작업 요령을 가르치는 **지침 + 스크립트 + 예시 묶음**이다.
- 11/6 커밋으로 **docx·pdf·pptx·xlsx 네 가지 오피스 스킬이 Apache 2.0**으로 바뀌었다. 저장소 대부분의 다른 스킬과 같은 조건이다. 스킬 폴더마다 라이선스 파일이 들어갔다([커밋](https://github.com/anthropics/skills/commit/2c5958ecac7cee2b583967a2c4981d0f4a75c579), [FoxaMind](https://foxamind.com/news/anthropic-moves-its-docx-pdf-pptx-and-xlsx-skills-to-the-apache-2-0-license/)).
- 쉽게 말해 **문서·스프레드시트·발표자료를 만드는 에이전트 스킬을 자기 제품에 넣거나 고쳐서 배포하기가 쉬워졌다**. 다만 커밋은 이전 라이선스가 뭐였는지 밝히지 않는다. 가져다 쓸 때는 해당 버전의 라이선스 파일을 직접 확인하자.

## vercel-labs/agent-browser (+4,601, 약 5만) — “어느 줄의 ‘삭제’ 버튼인가”
- 에이전트용 브라우저 자동화 도구다. 0.43.0은 **접근성 이름이 비어 있거나 똑같은 버튼**에 힌트를 붙인다. 아이콘, 테스트 ID, 같은 줄의 텍스트 등이다.
- 목록의 줄마다 “편집” 버튼이 똑같이 있는 화면에서, 에이전트가 **엉뚱한 고객의 레코드를 고치는 사고**를 줄이려는 변경이다. 그래도 돈이 오가거나 지우는 동작은 결과로 대상을 다시 확인하는 게 원칙이다.

## addyosmani/agent-skills (+3,199, 약 11.7만) — 보안 검사가 비밀을 흘리던 버그
- 코딩 에이전트용 엔지니어링 스킬 모음이다. 0.6.15에서 **커밋 전 비밀키 검사가 찾아낸 키를 그대로 터미널에 출력하던 문제**를 고쳤다. 그 출력이 CI 로그나 에이전트 대화 기록에 남을 수 있었다.

## 왜 중요한가
지난 몇 주 GitHub 트렌드가 “에이전트가 무엇을 할 수 있나”였다면, 이번 주는 **“에이전트가 한 일을 믿을 수 있나”**다. 라이선스가 명확하고, 누른 버튼이 어느 대상인지 알 수 있고, 보안 도구가 오히려 비밀을 흘리지 않는 것. 별 개수는 관심도일 뿐 품질 보증이 아니지만, 관심이 **안전장치 쪽으로 옮겨가는 흐름**은 분명하다.
