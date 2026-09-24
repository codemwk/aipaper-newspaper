---
title: "AI Content Gen: HeyGen HyperFrames — HTML을 쓰고, 에이전트가 영상을 연출"
date: 2026-09-25T07:06:00+09:00
category: "AI Content Gen"
slug: "heygen-hyperframes-html-video"
summary: "heygen-com/hyperframes(~52.8k★, Apache-2.0). ‘Write HTML. Render video. Built for agents.’ Remotion과 다른 HTML-first·seek 렌더. WebMCP/MCP. Video Agent에 엔진 재사용."
---

## 한줄 요약
[HyperFrames](https://github.com/heygen-com/hyperframes)는 HeyGen의 오픈소스 프레임워크다. 슬로건: **Write HTML. Render video. Built for agents.** 픽셀을 바로 찍는 생성기가 아니라, 에이전트가 **편집 가능한 HTML/CSS/JS 프로젝트**를 쓰고 헤드리스 브라우저가 프레임을 seek·캡처한다.

## 어떻게 동작하나
- 에이전트가 `index.html`·CSS·GSAP 타임라인 등을 생성 → Studio 프리뷰 또는 MP4/MOV/WebM/GIF/PNG 렌더.
- Remotion(프레임=순수 함수)과 달리 `window.__hf.seek(t)`로 애니메이션을 특정 시각에 멈춘 뒤 스크린샷(회사·엔지니어가 Remotion·WebVideoCreator 등 prior art를 인정).
- **WebMCP·호스티드 MCP**로 Studio/에이전트가 컴포지션을 쿼리·뮤테이트. AWS Lambda·GCP Cloud Run 배치 렌더 옵션.
- 유료 제품: 2026년 7월 릴리즈 노트상 HyperFrames가 HeyGen **Video Agent**에 포함. 오픈소스(엔진) + 패키지드 제품(수익) 분리.

## 왜 중요한가
“프롬프트 → 완성 클립”과 “에이전트 → 버전관리 가능한 소스 → 재렌더”는 다른 카테고리다. 브랜드 색 하나 바꿔 50개 변형을 뽑을 때 후자가 이긴다. 스타·다운로드 숫자는 크지만 커뮤니티 토론은 조용하다는 비판도 있으니 **이슈·라이선스(Apache-2.0)**를 직접 보고 판단할 것.

## 기억할 것
- [GitHub](https://github.com/heygen-com/hyperframes) · [hyperframes.heygen.com](https://hyperframes.heygen.com) (문서)
