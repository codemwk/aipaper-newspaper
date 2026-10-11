---
title: "디자인/UI·UX: CopilotKit ‘Open Intelligent UI’ — ChatGPT Intelligent UI의 오픈소스 판, AG-UI로 내 앱·내 컴포넌트에 꽂는다"
date: 2026-10-12T07:01:00+09:00
category: "디자인/UI·UX"
slug: "open-intelligent-ui"
summary: "10/9 CopilotKit이 Open Intelligent UI를 공개. OpenAI가 ChatGPT 안에만 넣은 Interactive UI(차트·맵·계산기·폼)를 오픈소스로 가져오고, AG-UI로 임의 에이전트·임의 모델을 붙인다. 저장소 CopilotKit/OpenIntelligentUI ~2.6K★, 모체 CopilotKit ~37.9K★."
---

## 한줄 요약
OpenAI가 10/7 ChatGPT에 넣은 **Intelligent UI**(답을 글 대신 버튼·차트·폼·도구로 조립)는 **ChatGPT 안에만** 있다. CopilotKit은 **10/9** [Open Intelligent UI](https://www.copilotkit.ai/blog/introducing-open-intelligent-ui)로 같은 경험을 **내 제품**에 옮기는 오픈소스 스택을 냈다. 에이전트는 **AG-UI**로 붙이고, 생성 UI는 승인 CDN만 로드하는 iframe에서 돈다.

## 어떻게 동작하나
- **스펙트럼**: Controlled(에이전트가 **이미 가진 디자인 시스템 컴포넌트**만 씀) ↔ Open(에이전트가 HTML/인터랙션을 **즉석 생성**). 블로그는 여행 플래너(라이브 맵+위키 사진)와 뱀 게임을 예시로 든다.
- **스트리밍**: UI가 생성되는 동안 조각이 흘러 들어오고, 끝난 인터페이스는 **standalone HTML**로 다운로드 가능.
- **모델 역할 분리**(블로그 주장): 답 작성은 OpenAI, 포맷 선택은 TypeSafe의 Jev — “사실이면 텍스트, 추세면 차트” 같은 라우팅.
- **표준**: A2UI·MCP Apps가 AG-UI 위에 올라탄다고 명시. LangChain Deep Agents 기본 예제를 Mastra·Google ADK 등으로 갈아끼울 수 있다고 한다.
- **스타 수**(2026-10-12 `gh` 확인): [OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI) **~2,641★**, [CopilotKit](https://github.com/CopilotKit/CopilotKit) **~37,940★**.

## 왜 중요한가
어제·그제 Framer Skills·PhotoCraft가 “에이전트가 **디자인 도구** 안에서 그린다”면, 이건 “에이전트 답이 **제품 UI 자체**가 된다”. OpenAI 디자인팀 Andrew Chen이 말한 “생성 UI의 난제는 생성보다 **소속에 맞게 느껴지게** 하는 것”을, CopilotKit은 **당신 컴포넌트 카탈로그**로 풀겠다는 주장이다. 보안상 승인 CDN·격리 iframe은 필수 전제 — “아무 스크립트나 실행”이 아니다.

## 기억할 것
- ChatGPT Intelligent UI API는 **여전히 없음**(블로그가 출발점으로 삼은 불만).
- 데모는 OpenAI 키 + TypeSafe 키가 필요하다고 안내 — 완전 로컬 무료는 아니다.

출처: [CopilotKit — Open Intelligent UI](https://www.copilotkit.ai/blog/introducing-open-intelligent-ui) · [OpenAI GPT-6 Intelligent UI](https://openai.com/index/gpt-6-for-everyone/) · [GitHub OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI)
