---
title: "디자인: Webflow — 사이트에서 Brand·Design System 스킬을 자동 생성해 MCP 에이전트에 심는 Instructions"
date: 2026-11-07T07:02:00+09:00
category: "디자인"
slug: "webflow-agent-instructions"
summary: "Webflow가 사이트에 붙는 AI Agent Instructions(스킬·규칙)를 공식화했다. 기존 사이트에서 Brand Guidelines·Design System·Asset·CMS 가이드를 자동 생성하고, MCP로 연결된 Claude·Cursor 등이 변수·컴포넌트·CMS를 참조 토큰으로 읽는다. Shared Library로 워크스페이스 전 사이트에 배포 가능."
---

## 한줄 요약
에이전트에게 “우리 브랜드처럼”이라고 매번 붙여 넣는 시대는 끝났다. Webflow **Agent Instructions**는 스킬(자유형 가이드)과 규칙(모든 작업에 적용되는 고정 기준)을 **사이트에 저장**하고, MCP 서버로 연결된 도구가 그걸 읽게 한다([Webflow Help](https://help.webflow.com/hc/en-us/articles/52536649709971-Create-and-manage-AI-agent-instructions), 업데이트 10/22).

## 핵심 기능
- **자동 생성 스킬**: Brand Guidelines / Design System / Asset Guidelines / CMS Guidelines(컬렉션당, 한 번에 최대 5개). 생성은 백그라운드, **AI 크레딧 소모**. 새 스킬·규칙은 기본 Off → 검토 후 On.
- **참조 토큰**: 변수·스타일·컴포넌트·에셋·인터랙션·페이지·CMS·로케일·다른 스킬/규칙을 문서에 삽입. 에이전트가 **복사본이 아니라 현재 값**을 본다.
- **규칙 템플릿**: SEO 기본값, kebab-case 네이밍, 접근성(대비율·포커스·스크린리더).
- **가져오기/내보내기**: `.md`/`.mdc` zip. MCP로 CRUD도 가능.
- **Shared Library**: 컴포넌트·변수처럼 Instructions를 워크스페이스 다른 사이트에 설치·일괄 갱신.

## 왜 중요한가
Figma·Kittl·Framer가 “에이전트가 캔버스를 만지게” 했다면, Webflow는 **사이트 = 디자인 시스템의 진실 공급원**으로 잠그는 쪽이다. impeccable·UI UX Pro Max 같은 외부 스킬을 zip으로 들여오거나, 사이트에서 뽑은 스킬을 에이전트 쪽에보내 대칭을 맞출 수 있다.

## 주의
Site manager·Designer만 생성/수정. Marketer·Content editor는 읽기만. 자동 생성 품질은 사이트 정리 상태에 좌우되고, Webflow도 “세션 시작 때 Instructions를 먼저 읽히라”고 권한다.
