---
title: "디자인: “AI야, 우리 브랜드대로 만들어” — Brandrail은 규칙을 MCP로 건네고 검사까지, InstaLanding은 ‘말 대신 완성된 HTML’을 레퍼런스로"
date: 2026-11-15T07:03:00+09:00
category: "디자인 / UI·UX"
slug: "brandrail-instalanding-design-rules"
summary: "11/14 공개된 두 오픈소스가 같은 문제를 다른 방식으로 푼다. Brandrail은 디자인 토큰·컴포넌트 규칙을 Claude Code·Cursor 같은 코딩 에이전트에 MCP로 먼저 건네고, 만든 코드를 브랜드 기준으로 채점해 고치게 한다. InstaLanding은 ‘프리미엄 SaaS 느낌’ 같은 말 대신 한 파일짜리 HTML 템플릿을 주고 에이전트가 디자인 시스템을 뽑아 기존 앱을 갈아입히게 한다."
---

## 한줄 요약
AI 코딩 도구가 만든 화면은 대개 **색과 여백이 제멋대로**이고, 어디서 본 듯한 ‘AI 느낌’이 난다. 11/14 나온 두 오픈소스는 이 문제를 각자 다르게 푼다. **규칙을 건네고 검사하기**(Brandrail)와 **완성품을 보여주기**(InstaLanding)다.

## Brandrail — 규칙을 먼저 주고, 만든 뒤 채점한다
- MIT 라이선스의 **로컬 MCP 서버 + CLI 검사기**다. Claude Code, Cursor, GitHub Copilot, Codex, Windsurf, Gemini CLI에 붙는다([Tech Bytes 보도](https://techbytes.app/posts/brandrail-make-claude-code-and-cursor-follow-your-design-system/)).
- 에이전트가 쓸 수 있는 **읽기 전용 도구 7개**: 가이드라인 조회, 디자인 토큰 조회, 컴포넌트 찾기, 컴포넌트 문서, 페이지 템플릿(대시보드·로그인 등), **기존 UI 라이브러리 → 사내 컴포넌트 대응표**, 그리고 **코드 조각 채점(validate_snippet)**.
- 채점 결과와 고칠 점이 에이전트에게 바로 돌아가 **스스로 고친다**. React·Angular·Vue·웹 컴포넌트·HTML을 지원한다.
- 대응표는 Material UI, Bootstrap, Ant Design, Chakra UI, PrimeNG 컴포넌트를 자사 디자인 시스템 컴포넌트로 바꿀 때 쓴다.
- 계정 없이도 기본 토큰으로 돌고, 코드는 내 컴퓨터 밖으로 나가지 않는다고 한다. 자기 브랜드 키트를 쓰려면 무료 조직 계정이나 API 키가 필요하다. 터미널에서는 바뀐 파일만 검사하거나(`check --changed`) 실행 중인 사이트를 훑을 수 있다.

## InstaLanding — 형용사 대신 ‘실물’을 준다
- 외부 의존성 없는 **한 파일짜리 HTML 템플릿** 모음이다. 랜딩 페이지와 함께 **디자인 시스템 24종**(타이포·색·간격 토큰 포함), WebGL 셰이더·패럴랙스 같은 **모션 연구 15종**이 들어 있고 무료다([TheNextGenTechInsider](https://www.thenextgentechinsider.com/pulse/new-open-source-html-library-enables-ai-agents-to-execute-precise-ui-reskinning)).
- 사용법: 템플릿 HTML을 에이전트에게 주고 **“여기서 타이포·색·레이아웃 원칙을 뽑아 우리 앱 컴포넌트에 입혀라. 비즈니스 로직·API·상태 관리는 건드리지 마라”**라고 지시한다.
- 슬로건은 “**엔지니어링은 두고 미감만 바꿔라**”. 이미지나 Figma 시안보다 **코드가 에이전트에게 가장 정확한 레퍼런스**라는 주장이다.

## 왜 중요한가
두 접근은 디자인 시스템의 두 얼굴이다. **규칙(무엇을 하면 안 되는가)**과 **본보기(이렇게 생겨야 한다)**. 브랜드를 만드는 쪽에서 보면 납품물이 바뀌는 신호다. 가이드 PDF 대신 **에이전트가 조회하고 검사받을 수 있는 규칙 서버**와 **에이전트가 그대로 읽을 수 있는 레퍼런스 HTML**을 함께 넘기는 시대가 오고 있다. 다만 Brandrail 정보는 출시 보도와 저장소 기준이라, 실제 채점 품질은 직접 써봐야 안다.
