---
title: "디자인/UI·UX: AI에게 ‘브랜드’를 넘기는 파일 — BRAND.md v0.3이 그은 선, “리디자인해도 살아남으면 BRAND, 바뀔 수 있으면 DESIGN”"
date: 2026-10-25T07:03:00+09:00
category: "디자인/UI·UX"
slug: "brand-md-vs-design-md"
summary: "DESIGN.md가 ‘에이전트가 읽는 디자인 시스템’의 표준처럼 퍼지는 사이, 브랜드 전략·말투까지 담는 오픈 표준 BRAND.md가 v0.3에서 DESIGN.md와의 경계를 명문화했다. 4층 구조(전략·보이스·비주얼·거버넌스), 23개 섹션(필수 15), 마스터 브랜드→제품 브랜드 상속. 판별 규칙은 한 줄: 완전한 리디자인 뒤에도 남아야 하면 BRAND.md, 리포지셔닝 없이 바뀔 수 있으면 DESIGN.md. 독일 디자인 회사의 비교 글은 BCP(준수 검사), Brando Schema(의미 어휘)까지 5가지 방식을 나란히 놓았다."
---

## 한줄 요약
에이전트에게 “우리 브랜드답게 써 줘”는 통하지 않는다. 읽을 파일이 없으니까. 이번 주말 해설은 **브랜드를 AI가 읽는 파일로 만드는 방법**들 — 그중 BRAND.md가 v0.3에서 그은 경계선이 브랜드 스튜디오에게 특히 쓸모 있다([thebrand.md](https://thebrand.md/)).

## BRAND.md: 50쪽 가이드를 파일 하나로
- 프로젝트 루트에 두는 **마크다운 + YAML 머리말** 파일. AGENTS.md가 코딩 에이전트에게 지시를 주듯, BRAND.md는 모든 AI 도구에 브랜드 맥락을 준다. MIT 라이선스, 23개 섹션(필수 15·선택 8).
- **4층 구조**

| 층 | 담는 것 |
|---|---|
| 전략 Strategy | 개요·대상·포지셔닝·성격·레퍼런스·약속·가드레일 |
| 보이스 Voice | 정체성·태그라인·메시지 기둥·자주 쓰는 표현·어휘·톤 규칙(“이렇게 말한다 / 절대 이렇게 안 말한다” 표) |
| 비주얼 Visual | 승인된 **원형**만 — 로고 불변 요소·핵심 색·서체·이미지 영역·아트 디렉션 |
| 거버넌스(선택) | 네이밍·주장(claims)·접근성 약속 — “절대 지어내지 않는다” |

- **상속**: 마스터 브랜드 파일 아래 제품 폴더마다 BRAND.md를 두고 다른 부분만 덮어쓴다. 브랜디드 하우스(Google→Maps)·보증형(Marriott→Courtyard)·서브 브랜드(Apple→iPhone)·독립형(P&G→Tide) 4가지 구조를 지원.

## v0.3의 핵심: DESIGN.md와의 경계
> **완전한 비주얼 리디자인 뒤에도 살아남아야 하면 BRAND.md, 회사를 리포지셔닝하지 않고도 바뀔 수 있으면 DESIGN.md.**

- 색 램프·시맨틱 역할·타입 스케일·레이아웃·컴포넌트·모션 = **DESIGN.md** (표면마다 하나씩: 웹사이트·제품·발표자료)
- 의존 방향은 한쪽뿐: DESIGN.md가 `brand: ../BRAND.md`를 선언하고, BRAND.md는 디자인 파일을 모른다.
- 같은 정체성이 마케팅 사이트에선 ‘문예지’처럼, 제품에선 ‘연구 아카이브’처럼 보여도 정상 — 그래서 브랜드 파일이 디자인 시스템을 소유하면 안 된다는 논리.

## 다른 방식들과 비교 (schwarzdesign/nxttool 정리)
| 방식 | 성격 | 잘 맞는 곳 |
|---|---|---|
| DESIGN.md(Google Labs, 알파) | 토큰 + 사용 규칙, 린터(WCAG 대비 검사), Tailwind·DTCG 내보내기 | UI 생성·코딩 에이전트 |
| BRAND.md | 전략·말투·비주얼 원형 한 파일 | 카피·프로젝트 맥락 전달 |
| Brand Context Protocol | JSON 스키마, 주장·가격·채널 규칙 **검사·차단** | 규제 많은 마케팅 |
| Brando Schema 1.3 | Schema.org Brand 확장 어휘(CC BY 4.0) | 자체 지식 아키텍처 |
(비교 글을 쓴 nxttool은 자체 모듈형 브랜드 시스템도 파는 회사라는 점은 감안할 것 — [원문](https://www.nxttool.com/en/news/machine-readable-brand-systems/))

## 왜 중요한가
이번 달 Figma 가이드라인·Webflow DESIGN.md·Char design.md까지 ‘에이전트가 읽는 디자인 시스템’은 많이 다뤘다. 그런데 그건 **화면의 규칙**이다. 브랜드 스튜디오가 파는 건 그 위층 — **왜·누구에게·어떤 말투로**다.
ANDRSN 관점: 브랜드 전환 프로젝트의 산출물에 **BRAND.md(정체성) + 표면별 DESIGN.md(적용)**를 함께 넘기면, 고객사가 쓰는 모든 AI 도구가 그 브랜드로 말하게 된다. 납품물이 PDF 가이드에서 **‘살아 있는 파일’**로 바뀌는 지점이다. ANDRSN STUDIES 콘셉트에도 “이 리브랜딩의 BRAND.md”를 첨부해 보면 차별점이 된다.

출처: [BRAND.md 공식 사이트·v0.3](https://thebrand.md/) · [BRAND.md 스펙 (GitHub)](https://github.com/caiopizzol/brand.md) · [nxttool — Machine-readable brand systems compared (10/3, 10/17 갱신)](https://www.nxttool.com/en/news/machine-readable-brand-systems/) · [design.md (Google Labs)](https://github.com/google-labs-code/design.md)
