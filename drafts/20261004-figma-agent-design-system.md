---
title: "디자인: Figma Agent가 디자인 시스템을 유지보수한다 — 문서·벌크 업데이트·패턴 추출·퍼블리시 전 리뷰"
date: 2026-10-04T07:02:00+09:00
category: "디자인 / UI·UX"
slug: "figma-agent-design-system"
summary: "Figma Help: 에이전트로 컴포넌트 문서 대량 작성, 스타일/변수 벌크 수정, 화면에서 패턴·토큰 추출, 퍼블리시 전 missing state·하드코드 점검. Check designs는 Org/Enterprise."
---

## 한줄 요약
[Figma Learn — AI workflows](https://help.figma.com/hc/en-us/articles/41159677390999-AI-workflows-collection-Use-the-Figma-agent-to-improve-your-design-system): 디자인 시스템 매니저의 반복 업무 네 축을 **Figma agent**에 넘기는 공식 워크플로 모음이다. (1) 캔버스에 **문서 초안** (2) 아이콘·네이밍·variant **벌크 정리** (3) 실제 화면에서 **패턴·컬러·타이포 변수 추출** (4) 퍼블리시 전 **누락 상태·일관성 리뷰**. 문서가 좋아질수록 에이전트가 라이브러리 컴포넌트를 더 정확히 고른다는 **피드백 루프**를 강조한다. Org/Enterprise의 **Check designs**는 잘못된 컬러·라이브러리·하드코드 값 스캔.

## 실무로 보면
- **문서 skill**: 템플릿을 컨텍스트로 주면 스펙·variant·중첩 인스턴스까지. 작성 후 컴포넌트 description과 동기화하면 사람·에이전트 공통 컨텍스트가 됨.
- **벌크 프롬프트 예**: 아이콘 flatten+kebab-case, 24px→16px 스트로크 축소, shadow 스타일 일괄 제거.
- **시스템화**: 카드 UI에서 새 컴포넌트 초안, CSS 변수 목록을 캔버스에 붙여 **코드↔Figma 갭** 찾기.
- **퍼블리시 게이트**: “missing states?”, “merge 가능한가?”, “유사 컴포넌트 구조와 불일치?”를 에이전트 1차 리뷰로.

## 왜 중요한가
어제·그제 다룬 Motion·Weave·Riffs가 **생성·모션 재료**였다면, 이번은 **디자인 시스템 운영**. UI UX Pro Max류 “시스템 생성” 관심과도 맞닿는다 — 생성 다음 문제는 **유지보수 부채**다.

## 기억할 것
- [Use the Figma agent to improve your design system](https://help.figma.com/hc/en-us/articles/41159677390999-AI-workflows-collection-Use-the-Figma-agent-to-improve-your-design-system)
