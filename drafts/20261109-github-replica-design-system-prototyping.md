---
title: "디자인: GitHub Design의 오픈소스 ‘Replica’ — 우리 디자인 시스템 부품으로만 프로토타입을 짓는다"
date: 2026-11-09T07:05:00+09:00
category: "디자인"
slug: "github-replica-design-system-prototyping"
summary: "GitHub Design이 10/28 MIT 라이선스로 공개한 Replica는 팀의 기존 컴포넌트·패턴·문서를 기준으로 Copilot 앱 안에서 자연어 프로토타입을 만든다. 선택적으로 자체 호스팅 ‘Replica Hub’에 올려 댓글 피드백을 받는다. ‘예쁘게’보다 ‘우리 제품답게’를 택한 접근이다."
---

## 한줄 요약
AI 프로토타입 도구의 흔한 불만은 “그럴듯하지만 우리 제품 같지가 않다”였다. GitHub Design이 10/28 공개한 **Replica**는 반대로 **우리 디자인 시스템의 컴포넌트·패턴·문서**를 기준으로 삼아 프로토타입을 만든다. MIT 라이선스 오픈소스다([GitHub Changelog](https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/)).

## 어떻게 쓰나
- **디자이너가 가이드를 정의**하고, 디자이너·PM·엔지니어 누구나 **GitHub Copilot 앱에서 자연어**로 프로토타입을 만들고 다듬는다. 결과는 대화 옆에서 바로 보고 테스트한다.
- **로컬로 시작** 가능. 팀 공유가 필요하면 **자체 호스팅 Replica Hub**에 프로토타입을 올려 동료가 둘러보고 댓글을 남긴다.
- 도구와 가이드를 팀 워크플로에 맞게 수정할 수 있다(오픈소스).

## 왜 중요한가
Figma의 코드 레이어, Framer의 Agent Templates처럼 최근 흐름은 **‘에이전트가 읽을 수 있는 디자인 시스템’**이다. Replica의 특징은 그 지침을 디자이너가 쓰고 비디자이너가 쓰게 하는 **역할 분리**다. 디자인 시스템이 문서가 아니라 ‘에이전트의 작업 제약’이 되는 사례. 저장해 두신 DESIGN.md·Stitch·TypeUI 계열 글과 이어지는 소식이다.

## 주의
공식 글은 품질 수치나 비교 데이터를 내놓지 않았다. 사용하려면 GitHub Copilot 앱이 전제이고, Hub는 직접 호스팅·운영해야 한다. 디자인 시스템이 허술한 팀이라면 결과도 그만큼 평범해진다.
