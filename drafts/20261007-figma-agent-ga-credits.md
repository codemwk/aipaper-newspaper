---
title: "디자인/UI·UX: Figma 에이전트 정식 출시 — 이제 크레딧이 빠진다, ‘가이드라인 파일’과 동료 에이전트 실시간 보기"
date: 2026-10-07T07:05:00+09:00
category: "디자인/UI·UX"
slug: "figma-agent-ga-credits"
summary: "10/6 Figma Design 에이전트·Weave 도구가 오픈 베타에서 GA로. 베타 사용량은 무료였지만 이제 Figma Make와 같은 AI 크레딧 예산을 공유한다. 라이브러리에 붙이는 Markdown 가이드라인(3~8개·100KB 미만 권장), 캔버스에서 동료 에이전트 작업 보기, 커스텀 스킬. Full 시트 중심 제공."
---

## 한줄 요약
5월 베타로 나온 **Figma 디자인 에이전트**가 10월 6일 **정식 출시(GA)**됐다([The Verge](https://www.theverge.com/tech/1004953/figmas-ai-agent-for-product-design-is-now-generally-available)). AiPaper가 9/29에 예고했던 대로 **GA와 함께 과금이 시작**됐다 — 베타 기간 사용분은 크레딧에서 빠지지 않았지만, 이제부터는 **Figma AI 크레딧을 소모**한다([Figma 도움말: AI credit updates](https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ)).

## 무엇이 새로 들어왔나
- **가이드라인 파일**: 게시된 디자인 라이브러리에 Markdown 파일을 붙이면, 그 라이브러리를 켠 파일에서 에이전트가 **자동으로 규칙을 참고**한다. Figma는 **주제별 3~8개, 합계 100KB 미만**을 권한다 — 컨텍스트가 클수록 크레딧이 더 든다([도움말](https://help.figma.com/hc/en-us/articles/43509372175511-Add-guidelines-files-to-a-design-library)).
- **멀티플레이어 에이전트**: 동료의 에이전트가 공유 캔버스에서 무엇을 하는지 **실시간으로** 보인다([릴리스 노트](https://www.figma.com/release-notes/)).
- **커스텀 스킬**: `/repair-library-usage`(낡은 컴포넌트·변수 바인딩을 최신 라이브러리로 교체, 애매하면 손대지 않고 주석), `/document-component-enhancement`(컴포넌트 스펙 초안) 같은 슬래시 명령. Uber는 7개 플랫폼 컴포넌트 문서화를 `/create-api`·`/create-color` 스킬로 돌린다([Figma 블로그](https://www.figma.com/blog/figma-agent-and-design-systems/)).
- 지연 시간 개선, 파일 간 검색.

## 돈은 어떻게 나가나
- 에이전트는 **Figma Make 등 다른 AI 기능과 같은 크레딧 통**에서 차감. 프롬프트 복잡도·에이전트가 한 작업 수·붙인 라이브러리/파일에 따라 **매번 다르다**. Make를 많이 썼다면 에이전트 잔량이 0으로 보일 수 있다.
- Weave 도구는 도구별 **고정 크레딧**.
- 8/25부터 추가 크레딧 애드온은 같은 가격에 Professional **2배**, Organization·Enterprise **1.6배**로 늘었다. 좌석 기본 크레딧은 그대로.
- Organization·Enterprise는 **베타 기간 사용량 CSV**를 내려받아 앞으로의 비용을 가늠할 수 있다.
- 사용 대상: Professional·Organization·Enterprise(일부 Education)의 **Full 시트**, Starter는 제한적. Collab·Dev·View 시트는 드래프트에서만.

## 왜 중요한가
디자인 에이전트의 경쟁력은 결국 **“우리 팀 규칙을 얼마나 잘 지키나”**다. 가이드라인 파일은 Stitch·Linear의 DESIGN.md 흐름을 Figma가 라이브러리 단위로 흡수한 것이고, 동시에 **규칙을 길게 쓸수록 비용이 오르는** 구조를 만들었다. 이제 디자인 시스템 문서도 “짧고 단정하게”가 비용 최적화다.

## 체크포인트
- 크레딧 소모량은 Figma 스스로 “변동·변경 가능”이라고 명시. 첫 달은 **관리자 대시보드로 사용량부터 확인**할 것.
