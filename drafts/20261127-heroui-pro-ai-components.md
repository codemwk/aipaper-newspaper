---
title: "디자인: AI 화면에도 ‘표준 부품’이 생긴다 — HeroUI Pro 1.0, 생각 과정 접기(Reasoning)·모델 선택기·‘실행 전에 묻는’ 승인 카드를 React 컴포넌트로"
date: 2026-11-27T07:35:00+09:00
category: "디자인"
slug: "heroui-pro-ai-components"
summary: "React UI 라이브러리 HeroUI의 유료판 HeroUI Pro가 11월 첫 정식 버전 1.0을 내고 11/24 Product Hunt에 올랐다. 새 AI 컴포넌트 네 가지 — 스트리밍되는 생각 과정을 보여 주다 끝나면 1초 뒤 접는 Reasoning, AI 작업용 Loader, 모델과 노력 수준을 고르는 Model Selector, 에이전트가 실행 전에 질문을 하나씩 묻는 Approval Card — 가 핵심이다. MCP 서버와 ‘Design Taste’ 에이전트 스킬도 함께 제공한다."
---

## 한줄 요약
버튼·모달처럼, 이제 **“AI가 생각 중” “어느 모델로?” “이거 실행해도 될까요?”**도 디자인 시스템의 기본 부품이 됐다([HeroUI Pro 1.0 릴리스 노트](https://heroui.pro/docs/react/releases/v1-0-0), [Product Hunt](https://www.producthunt.com/products/heroui-pro-1-0?launch=1315348)).

## 새 AI 컴포넌트 네 가지
- **Reasoning:** 모델의 생각을 스트리밍으로 보여 주는 블록. 첫 글자에서 열리고, 끝나면 **1초 뒤 자동으로 접힌다**(사용자가 직접 열었으면 유지). 중단·실패 시엔 “5초 후 중단됨”, “생각을 끝내지 못함” 같은 문구로 상태를 보여 주고, 저장된 대화는 “9초 동안 생각함”으로 남는다. 접힌 상태에서도 **페이지 내 찾기(Ctrl+F)**로 열린다.
- **Chain of Thought:** 이제 Reasoning 안의 **단계 목록**(완료·진행 중·대기·오류)으로 들어갔다 — “레이아웃 읽기 → app/layout.tsx 확인” 같은 에이전트 작업 단계를 보여 주는 용도.
- **Model Selector:** 채팅 입력창에서 **모델과 노력(effort) 수준**을 고르는 선택기.
- **Approval Card:** 에이전트가 **행동하기 전에 질문을 하나씩** 묻는 카드.
- 그 밖에 채팅 스크롤 훅, “+N개 더” 출처 목록, 제안 항목을 버튼·링크로, 키보드로 쓰는 Agenda, 여러 컴포넌트 접근성 수정.

## 에이전트용 도구
- **MCP 서버**(mcp.heroui.pro)로 컴포넌트 문서·CSS·테마 토큰을 에이전트가 실시간 조회([MCP 문서](https://heroui.pro/docs/react/getting-started/mcp-server)).
- Cursor·Claude Code 등에서 쓰는 **React Pro / Design Taste 에이전트 스킬**([Skills 문서](https://heroui.pro/docs/react/getting-started/agent-skills)).

## 왜 중요한가
- AI 제품 UI의 반복 패턴이 **“생각은 보여 주되 끝나면 치운다”, “위험한 행동 전엔 한 번에 하나씩 묻는다”**로 굳어 가고 있다. 직접 대시보드나 개인 OS를 만든다면 이 두 원칙을 그대로 가져다 쓸 만하다.
- 지난번 저장하신 **디자인 시스템을 에이전트가 읽는 흐름(DESIGN.md·Astryx)**과 이어진다. 컴포넌트 라이브러리가 **MCP + 스킬**을 같이 내는 것이 표준이 되는 중이다.
- 주의: Pro는 유료 제품이고, 1.0에는 peer 의존성 상향 등 **호환성 깨지는 변경**이 있다. 업그레이드 전 Breaking Changes 확인 필요.

출처: [HeroUI Pro React 1.0.0 릴리스 노트](https://heroui.pro/docs/react/releases/v1-0-0) · [Product Hunt — HeroUI Pro 1.0](https://www.producthunt.com/products/heroui-pro-1-0?launch=1315348) · [LaunchPact 11월 디자인 런치 목록](https://www.launchpact.io/product-hunt-launches/november-2026/design)
