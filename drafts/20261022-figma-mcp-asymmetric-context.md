---
title: "디자인/UI·UX: Figma, MCP 파트너 20곳 추가하면서도 “완벽한 규약은 아니다” — 딜런 필드가 말한 ‘비대칭 컨텍스트 공유’란"
date: 2026-10-22T07:01:00+09:00
category: "디자인/UI·UX"
slug: "figma-mcp-asymmetric-context"
summary: "Figma가 Config India에서 Figma MCP 파트너 20곳 추가(Amp·ClickUp·Dia·JetBrains Junie·Linear·Meta Muse·Mistral·Notion·OpenCode·Sarvam Agents 등). MCP로 코드 레이어 생성, Specs 편집, 캔버스 이미지 생성, Weave 워크플로 실행 가능. 그러나 공동창업자 딜런 필드는 TechCrunch(10/20)에 “MCP는 완벽한 규약이 아니고 프런티어 랩에 유리하다”, “더 많이 열수록 남용 위험도 커진다”고 말함. 9/30 X에선 Anthropic이 자기 아티팩트·클라우드 자원은 MCP로 열지 않는다며 ‘비대칭 컨텍스트 공유’를 지적. 이후 오픈소스 에이전트 Pi 지원 예정이라고 밝힘."
---

## 한줄 요약
디자인 데이터는 이제 **에이전트가 읽어 가는 자산**이다. Figma는 문을 더 넓히면서도, 그 문이 **한쪽으로만 열리는 문**이 될 수 있다고 경고했다([TechCrunch](https://techcrunch.com/2026/10/20/figma-co-founder-dylan-field-thinks-mcp-is-not-a-perfect-protocol/)).

## 무엇이 열렸나
10/15 Config India에서 Figma는 **MCP 파트너 20곳**을 새로 붙였다. Amp, ClickUp, Dia, JetBrains Junie, Linear, Meta Muse, Mistral, Notion, OpenCode, Sarvam Agents 등이다. 이제 다른 AI 도구에서 Figma MCP로
- **코드 레이어**(캔버스 위 실제 코드 프로토타입)를 만들고,
- **Specs**(팀과 에이전트가 함께 보는 마크다운 맥락 문서)를 고치고,
- 캔버스에 **이미지를 생성**하거나 게시된 **Weave 워크플로**를 돌릴 수 있다([Figma 블로그](https://www.figma.com/blog/build-by-design/), [릴리스 노트](https://www.figma.com/release-notes/)).

예를 들어 OpenCode는 디자인 시스템 맥락을 받아 더 정확한 코드를 만들고, 결과 프로토타입을 다시 Figma로 보내 검토받는다.

## 그런데 왜 “완벽하지 않다”고 했나
필드는 기자 브리핑에서 이렇게 말했다(TechCrunch).
- “MCP는 완벽한 규약이 아니다. 개선할 여지가 많다.”
- “**프런티어 랩에 더 유리하다.**”
- 더 많은 데이터를 MCP로 노출할수록 **남용 가능성**도 커지므로 완전히 열 수는 없다.

배경엔 9/30 그의 X 글이 있다. MCP 공동 제작자가 Figma의 오픈소스 에이전트 **Pi** 미지원을 비판하자, 필드는 “MCP를 만든 Anthropic은 정작 자기 **아티팩트·클라우드 자원**은 MCP로 열지 않는다”며 “논쟁은 ‘열림 vs 닫힘’으로만 그려지고 **비대칭적 컨텍스트 공유** 문제는 무시된다”고 했다. 이후 Figma는 Pi를 지원하겠다고 덧붙였다.

## 무슨 뜻인가 — 쉬운 말로
MCP는 “앱의 데이터·기능을 AI가 쓰게 하는 표준 플러그”다. 문제는 방향이다. Figma·Notion 같은 앱은 데이터를 **내보내고**, 그 데이터로 똑똑해지는 건 대화창을 가진 **모델 회사**다. 반대로 모델 회사 안에서 만들어진 결과물(아티팩트 등)은 앱 쪽으로 잘 돌아오지 않는다. 필드의 불만은 이 **일방통행**이다.

## 왜 중요한가
- **디자인 팀**: Figma 파일·라이브러리·가이드라인이 점점 ‘에이전트용 교과서’가 된다. 어떤 에이전트에 어디까지 열지 **권한 정책**이 디자인 운영의 일부가 된다.
- **도구 회사**: “MCP 지원”은 기본이 됐고, 이제 경쟁은 **무엇을, 누구에게, 얼마나** 여느냐다.
- 독자 관점(Figma Agent·디자인 시스템 기사 저장 이력): 가이드라인 마크다운, Specs, MCP가 한 묶음으로 움직이고 있다. 브랜드 규칙을 **에이전트가 읽는 문서**로 갖고 있는 팀이 유리하다.

출처: [TechCrunch (10/20)](https://techcrunch.com/2026/10/20/figma-co-founder-dylan-field-thinks-mcp-is-not-a-perfect-protocol/) · [Figma — Build by design (10/15)](https://www.figma.com/blog/build-by-design/) · [Figma 릴리스 노트](https://www.figma.com/release-notes/) · [TLDR Design (10/21)](https://tldr.tech/design/2026-10-21)
