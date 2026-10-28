---
title: "디자인/UI·UX: GitHub Design이 만든 ‘Replica’ 오픈소스 공개 — 아무 AI 시안이 아니라 ‘우리 디자인 시스템 부품’으로만 프로토타입을 만든다. 디자이너는 규칙을, 팀 전원은 말로"
date: 2026-10-29T07:03:00+09:00
category: "디자인/UI·UX"
slug: "github-replica-prototyping"
summary: "GitHub가 10/28 사내 디자인팀이 만든 AI 프로토타이핑 도구 Replica를 MIT 라이선스로 공개. 팀의 실제 컴포넌트·패턴·문서를 지침으로 삼아, 기획자·엔지니어 누구나 GitHub Copilot 앱에서 말로 ‘진짜 제품처럼 동작하는’ 시안을 만든다. 실행 중인 시안이 대화창 옆 캔버스에 뜨고, 회사가 직접 운영하는 Replica Hub에 올려 팀원이 눌러 보고 댓글을 단다(Hub 없이 로컬만으로도 시작 가능). 시안을 보거나 리뷰하는 데는 Copilot 구독이 필요 없다."
---

## 한줄 요약
AI 프로토타입 도구는 많지만 대부분 **“그럴듯한데 우리 제품 같지 않은”** 화면을 낸다. GitHub Design의 Replica는 반대로 **우리 팀 부품 상자 안에서만** 만들게 한다([GitHub Changelog](https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/)).

## 어떻게 쓰나
- **디자이너가 지침을 정한다**: 컴포넌트, 패턴, 승인된 가이드.
- **누구나 말로 만든다**: 기획자·엔지니어가 GitHub Copilot 앱에서 “이런 화면 만들어 줘”라고 하면, 실행 중인 시안이 **대화창 옆 캔버스**에 뜬다.
- **함께 본다**: 회사가 자체 서버에 두는 **Replica Hub**에 올리면 팀원이 직접 눌러 보며 댓글. 시안을 보거나 리뷰하는 사람은 Copilot 구독이 필요 없다.

## 구성
| 부분 | 역할 |
|---|---|
| Starters | 시안을 시작할 기본 앱(최소형 / 마이크로소프트 CoreAI 디자인 시스템 기반 샌드박스) + Copilot용 공용 스킬 |
| Replica 플러그인 | Copilot에 캔버스를 붙여 실행 중인 시안을 옆에 표시 |
| Replica Hub(선택) | 시안 호스팅·댓글. 활동 기록은 회사 DB에 90일 보관 |
| 빌드 액션 | Hub 게시용 빌드(로컬 작업엔 불필요) |

- 로컬만 쓰면 Copilot 앱·Git·Node.js(macOS/Linux)면 충분. Hub를 쓰려면 리눅스 서버와 전용 도메인(와일드카드 DNS·HTTPS)이 필요하다([README](https://github.com/github/replica)).
- Copilot 요금제 없이 **자기 모델 제공자 키(BYOK)**로도 쓸 수 있다(공개 미리보기).
- 공개 직후라 저장소 스타는 아직 수십 개 수준 — 성숙도는 이제부터다.

## 왜 중요한가
- 최근 흐름(Figma의 디자인 시스템 가이드, Supernova Agent, DTCG 1주년)과 같은 결론이다: **AI 시대 디자이너의 일은 화면을 그리는 것에서 ‘AI가 따를 부품과 규칙’을 관리하는 것으로** 옮겨 간다.
- 스튜디오 관점에서 보면, 클라이언트 브랜드의 컴포넌트·가이드를 Replica식으로 정리해 두면 **기획 회의에서 바로 ‘동작하는 시안’**을 띄우는 워크플로가 된다. 시안이 우리 시스템 안에서 나오니 ‘AI 티’도 덜 난다.
