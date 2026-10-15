---
title: "디자인/UI·UX: ‘AI에게 먹이는 디자인 시스템’ 두 갈래 — TypeUI 디자인 스킬 94종, Sun*의 무료 디자인 시스템 ‘Nova’(Figma×React×MCP)"
date: 2026-10-16T07:06:00+09:00
category: "디자인/UI·UX"
slug: "typeui-nova-design-skills"
summary: "TypeUI(Robert Tanislav)가 Claude·Codex·Cursor용 ‘디자인 스킬’ 라이브러리를 공개(사이트 기준 94종): 미니멀·에디토리얼·브루탈리즘·럭셔리 등 스타일별로 파운데이션·컴포넌트·패턴·가이드라인을 AI가 읽는 형식으로. 일본 Sun*(10/14)는 1,000+ 프로젝트 경험의 디자인 시스템 Nova를 MIT 기반으로 무료 공개 — Figma 라이브러리·React·Storybook·MCP 서버, 일본어 지시로 Figma 화면과 React 코드를 동시 생성, 화면 설계 착수까지 최대 80% 단축(자사 추정). 수익은 유료 도입 지원."
---

## 한줄 요약
AI 코딩 도구가 만든 화면이 “어딘가 어설픈” 이유는 단순하다 — 모델은 **코드를 배웠지 디자인 시스템을 배운 게 아니다.** 여백은 들쭉날쭉, 색은 임의, 컴포넌트는 따로 논다. 이번 주 이 빈틈을 메우는 두 가지 방식이 나란히 나왔다: **스타일 라이브러리형(TypeUI)**과 **조직용 기반형(Sun* Nova)**.

## TypeUI — “템플릿이 아니라 명세”
- 크리에이터 Robert Tanislav가 공개한 **디자인 스킬** 모음. 보도 시점엔 “90+”, 10/16 현재 사이트에는 **94종**이 올라 있다([TypeUI](https://typeui.sh/design-skills)).
- 각 스킬은 **파운데이션**(타이포·색·간격·레이아웃) → **컴포넌트**(버튼·폼·카드·내비·모달) → **패턴**(조합 방식) → **가이드라인**(규칙·제약) 4단 구조. 미니멀·에디토리얼·브루탈리즘·코퍼레이트·플레이풀·럭셔리 같은 미학별, 대시보드·마케팅·이커머스·문서용 같은 용도별로 나뉜다.
- Codex·Claude·Cursor에 연결해 “이 스타일로 화면 만들어” 할 때 AI가 **간격·색을 추측하지 않고 규칙을 따르게** 하는 것이 목표. 제작자는 “10년 넘게, 5,000만 개 이상 프로젝트에 쓰인 제품을 디자인하며 배운 것”을 담았다고 설명한다([Designer Daily](https://www.designer-daily.com/typeui-releases-90-design-systems-to-teach-ai-how-to-build-better-interfaces-241179)).

## Sun* Nova — 무료로 풀고, 도입 지원으로 번다
- 일본 디지털 크리에이티브 스튜디오 **Sun\***가 2026-10-14 디자인 시스템 **Nova** 제공을 시작했다. 1,000개 이상 제품 개발 경험을 바탕으로 했고, 시스템 자체는 **MIT 라이선스 기반 무료**, 상업 이용 가능([보도자료](https://sun-asterisk.com/news/pressrelease/5807/)).
- 구성: 색·타이포·UI 컴포넌트·아이콘·도입/운영 가이드, **Figma 라이브러리 + React 컴포넌트 + Storybook**, 그리고 **MCP 서버**.
- 핵심 기능: ① 전용 Figma 플러그인으로 색·폰트·여백·모서리를 일괄 조정해 자사 브랜드화 ② MCP로 AI 에이전트와 연결해 **일본어 자연어 지시 → 규칙에 맞는 Figma 화면 + React 코드 동시 생성** ③ 프롬프트·SKILL로 새 컴포넌트·가이드라인 추가까지 AI 지시로 처리.
- 효과: 화면 설계 착수까지 **최대 80% 단축**(자사 추정 — 화면 40개·공통 컴포넌트 60개·디자이너 1+프론트 2명 기준).
- 비즈니스: 프로토타입·제품 개발·디자인 시스템 구축 **지원 서비스는 유료(개별 견적)**. 오픈소스로 신뢰를 얻고 컨설팅으로 수익화하는 전형적 구조.

## 왜 중요한가
어제 Figma가 “디자인 시스템에 가이드라인·코드 소스를 붙여 에이전트에게 먹인다”고 했고, 오늘 두 사례는 그걸 **도구 밖에서, 공짜로** 한다. 디자이너의 일은 화면을 하나씩 그리는 것에서 **“AI가 지킬 규칙을 쓰는 것”**으로 옮겨 가는 중이다. ANDRSN 관점에선 Sun*의 모델이 흥미롭다 — 스튜디오가 자기 노하우를 **오픈 디자인 시스템이라는 ‘쇼룸’**으로 공개하고, 그걸 본 고객에게 맞춤 구축을 판다. ANDRSN STUDIES와 같은 “먼저 보여주기” 전략의 디자인 시스템 버전이다.

출처: [TypeUI Design Skills](https://typeui.sh/design-skills) · [Designer Daily](https://www.designer-daily.com/typeui-releases-90-design-systems-to-teach-ai-how-to-build-better-interfaces-241179) · [Sun* プレスリリース (2026-10-15)](https://sun-asterisk.com/news/pressrelease/5807/) · [Nova](https://nova.sun-asterisk.com/)
