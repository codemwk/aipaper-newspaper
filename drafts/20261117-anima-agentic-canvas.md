---
title: "디자인: Anima ‘Agentic Canvas’ — 디자이너는 손으로, 에이전트는 코드로, 같은 ‘진짜 HTML’을 고친다. 무료·가입 없이 브라우저에서"
date: 2026-11-17T07:25:00+09:00
category: "디자인"
slug: "anima-agentic-canvas"
summary: "디자인→코드 회사 Anima가 무료 브라우저 도구 Agentic Canvas(agentgrid.io)를 공개했다. 겉은 Figma 같은 캔버스인데, 안에는 실제 HTML·CSS가 저장된다. 프레임은 실제 페이지, 오토 레이아웃은 CSS flexbox다. Claude·ChatGPT·Claude Code·Codex·Cursor가 MCP로 같은 캔버스를 읽고 고친다. HTML·Figma·이미지·PDF·SVG로 시작하고 HTML·PNG·SVG·PDF로 내보낸다."
---

## 한줄 요약
에이전트가 만든 페이지를 디자이너가 고치려면 지금은 두 가지 길뿐이다. 코드 편집기에서 HTML을 읽거나, 프롬프트를 다시 쓰고 기다리거나. **Agentic Canvas**는 세 번째 길이다. **디자이너와 에이전트가 같은 화면(같은 HTML)을 함께 만진다**([Reveneau 정리, Anima 블로그 인용](https://reveneau.com/ainews/agentic-canvas-anima-agentgrid-figma-alternative-mcp-agents)).

## 무엇인가
- **겉은 캔버스, 속은 웹페이지**: Anima CEO Avishay Cohen의 설명은 이렇다. “프레임은 실제 페이지이고, 오토 레이아웃은 CSS flexbox, 그리드는 CSS grid다.” 디자이너는 끌고, 크기 바꾸고, 정렬하고, 스타일을 입힌다.
- **에이전트는 MCP로 접속**: Claude, ChatGPT, Claude Code, Codex, Cursor가 열린 캔버스를 읽고 바꾼다. 캔버스 탭을 열어 두면 에이전트의 수정이 그대로 보인다.
- **시작과 끝**: HTML, Figma 파일, 이미지, PDF, SVG에서 시작하거나 에이전트에게 페이지를 만들라고 한다. 내보내기는 HTML, PNG, SVG, PDF.
- **가입 없음**: agentgrid.io에서 계정 없이 브라우저로 돈다. 클라우드 저장도 없다. 공개 URL로 게시하려면 선택적으로 계정을 만든다.
- Anima는 Figma를 HTML·React로 바꾸는 회사다. 자사 도구 사용자가 180만 명이라고 밝혔다(회사 주장).

## 한계
‘디자인→코드’ 시장은 이미 붐빈다. Figma, Lovable, v0, Bolt, Anima의 기존 제품까지 대부분 채팅을 붙였다. 차별점은 하나다. **에이전트가 채팅창 너머가 아니라 ‘파일의 정식 사용자’**라는 점. Claude Code나 Cursor를 이미 쓰는 팀은 에이전트는 그대로 두고 **작업 표면만 바꾸면** 된다.

## 왜 중요한가
지난 두 주 AiPaper의 디자인 기사에는 한 방향이 있었다. A2UI, Meta Astryx, KT KDS 하네스 모두 **“에이전트가 디자인을 읽고 쓰는 구조”**였다. Agentic Canvas는 그 구조를 **가장 가벼운 형태**로 보여 준다. 설치도 가입도 없다. 결과물이 그림이 아니라 **개발자가 그대로 가져갈 수 있는 페이지**라는 점이 핵심이다. 랜딩 페이지 시안을 에이전트로 뽑고 눈으로 다듬어 바로 HTML로 넘기는 1인 스튜디오 작업 흐름에 잘 맞는다. 다만 신생 도구라 큰 프로젝트·협업 기능은 아직 검증되지 않았다.
