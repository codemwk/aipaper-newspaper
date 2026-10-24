---
title: "디자인/UI·UX: Spline이 ChatGPT·Codex 안으로 — “의자 구성기 만들어 줘” 하면 대화창 옆에 진짜 3D 편집기가 열리고, 내가 손댄 부분은 AI가 다시 읽고 이어 간다"
date: 2026-10-25T07:02:00+09:00
category: "디자인/UI·UX"
slug: "spline-chatgpt-codex"
summary: "3D 웹 디자인 툴 Spline이 10/21 ChatGPT 플러그인을 공개(같은 플러그인이 Codex에서도 동작). 대화로 인터랙티브 3D 장면·랜딩 페이지·앱 화면을 요청하면 실제 Spline 파일이 만들어지고, 대화창 옆 패널에 로그인된 진짜 편집기가 열린다. 사용자가 중간에 물체를 옮기거나 재질을 바꾸면 ChatGPT가 다음 수정 전에 파일을 다시 읽어 그 변경을 존중한다. 2D 캔버스 Hana로 UI도 만든다. ‘게시해 줘’ 하면 공개 링크까지. 무료 포함 전 요금제, MCP 도구 호출 한도 차감."
---

## 한줄 요약
“3D 음악 플레이어 만들어 줘”라고 쓰면 ChatGPT가 **실제 Spline 파일**을 만들고, 대화창 옆 패널에 **로그인된 진짜 편집기**가 열린다. 중간에 내가 직접 고쳐도 AI가 그걸 **덮어쓰지 않고 이어서** 작업한다([Spline 블로그, 10/21](https://blog.spline.design/introducing-spline-for-chatgpt)).

## 무엇이 되나
- **3D**: 물체·재질·조명·카메라·애니메이션·인터랙션. Spline AI로 3D 모델·이미지 생성. 작업 중 **스크린샷으로 스스로 결과를 점검**.
- **2D UI**: Spline의 2D 캔버스 **Hana**에서 랜딩 페이지·앱 화면을 편집 가능한 디자인으로.
- **기존 파일 열기**: 패널에서 최근 파일 검색 → “이 장면 인터랙션이 어떻게 돌아가는지 설명해 줘”처럼 **먼저 묻고** 고칠 수도.
- **게시**: “게시하고 링크 줘” → 공개 링크 반환(공유·임베드).

## 사람과 AI가 같은 파일을 만지는 방식
같은 대화의 후속 요청은 **새 파일이 아니라 같은 파일**을 고친다. 내가 패널에서 그림자를 바꾸면, ChatGPT는 다음 수정 전에 파일을 **다시 읽고** 그 위에 쌓는다. “AI가 내 수정을 되돌려 버린다”는 생성형 디자인의 가장 흔한 불만을 구조로 막은 것.

## 조건
- ChatGPT 플러그인 디렉터리에서 추가 → Spline 계정 OAuth 로그인(비밀번호는 ChatGPT에 안 넘어감). 설치·API 키 불필요.
- **무료 포함 모든 요금제**. 단 AI가 수행한 Spline 동작은 요금제별 **MCP 도구 호출 한도**에서 차감.
- 기반은 Spline의 호스팅 MCP 서버 + ‘Spline Agent Skill’ → Claude·Cursor 등 다른 MCP 클라이언트에서도 같은 서버 사용 가능.
- Codex CLI에선 패널 대신 웹 편집기 링크를 준다([문서](https://docs.spline.design/generate/plugins/chatgpt)).

## 왜 중요한가
3D는 디자이너에게도 진입장벽이 높은 영역이었다. 이제 **제품 구성기(색·재질 바꾸기)·인터랙티브 히어로** 같은 브랜드 경험의 시안을 대화로 뽑고, 디테일은 손으로 다듬는 분업이 가능해졌다. 핵심은 ‘생성’이 아니라 **‘사람의 수정을 존중하는 순서’** — 위 Webflow 기사와 같은 흐름이다.
ANDRSN 관점: 리브랜딩 콘셉트 스터디에 **3D 로고·패키지 구성기**를 붙여 보여 주는 비용이 크게 내려갔다.

출처: [Spline 블로그 — Introducing Spline in ChatGPT (10/21)](https://blog.spline.design/introducing-spline-for-chatgpt) · [Spline 문서 — ChatGPT and Codex](https://docs.spline.design/generate/plugins/chatgpt) · [Spline MCP Server 문서](https://docs.spline.design/generate/spline-mcp-server)
