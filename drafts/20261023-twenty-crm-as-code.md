---
title: "GitHub 트렌드: ‘AI를 위해 설계한 오픈 세일즈포스’ Twenty — CRM을 클릭으로 꾸미지 않고 코드로 정의·버전 관리, 코딩 에이전트용 스킬까지(★5.9만)"
date: 2026-10-23T07:11:00+09:00
category: "GitHub 트렌드"
slug: "twenty-crm-as-code"
summary: "twentyhq/twenty(★약 5만 9,500, 포크 9,700)가 10/22 GitHub 일간 트렌딩 8위(+112). 설명은 ‘AI를 위해 설계한 Salesforce의 오픈 대안’. 핵심 아이디어: 거래·고객 같은 CRM 객체·필드·화면을 코드로 정의해(create-twenty-app, twenty app:publish) 다른 소프트웨어처럼 버전 관리·배포. Claude Code·Codex·Cursor용 공식 ‘Twenty 앱 스킬’ 제공. 클라우드 또는 Docker Compose 자체 호스팅. 10/21 v2.50.0: 좌석당 워크스페이스 AI 크레딧, Microsoft Teams 통화 녹음 AI 요약, 앱 권한을 Workspace Apps/User Apps로 재정의(호환성 깨지는 변경), 에이전트 엔진 개선."
---

## 한줄 요약
같은 날 GitHub 트렌딩 상위는 대부분 코딩 에이전트 도구(ponytail, orca, graphify…)였다. 그 사이에 조금 다른 이름이 끼어 있었다 — **업무용 고객관리(CRM) 소프트웨어 Twenty**. 설명 한 줄이 이유를 말한다: **“AI를 위해 설계한 Salesforce의 오픈 대안”** ([GitHub 트렌딩 10/22](https://githubtrending.today/archive/2026-10-22/), [저장소](https://github.com/twentyhq/twenty)).

## 무엇이 다른가 (쉽게)
보통 CRM은 관리자 화면에서 클릭으로 “거래 단계” “고객 등급” 같은 항목을 만든다. Twenty는 이걸 **코드 파일**로 정의한다.
- “거래(deal)라는 객체에 이름·금액·마감일 필드가 있다”를 짧은 설정 코드로 쓰고, 명령 한 줄로 내 워크스페이스에 **게시**.
- 그래서 CRM 구조가 앱 코드처럼 **버전 관리**된다 — 누가 언제 무엇을 바꿨는지 남고, 되돌릴 수 있다.
- 바로 이 점이 **AI 친화적**이다. 코딩 에이전트는 클릭은 못 해도 파일은 잘 고친다. Twenty는 Claude Code·Codex·Cursor 등에서 쓰는 **공식 ‘앱 스킬’** 을 제공해, “영업 파이프라인에 갱신일 필드와 알림을 추가해 줘” 같은 요청을 에이전트가 코드로 처리하게 한다.
- 설치: 클라우드(가입 1분) 또는 Docker Compose로 **자체 서버**.

## 10/21 v2.50.0에서 보이는 방향
- **좌석당 AI 크레딧**(워크스페이스 단위로 AI 사용량을 좌석 수에 연동)
- **Microsoft Teams 통화 녹음에 AI 요약** 자동 작성, ‘통화 요약 생성’ 명령
- 앱 권한을 **Workspace Apps / User Apps**로 나눠 서버에서 강제(호환성이 깨지는 변경이라 자체 호스팅 사용자는 확인 필요)
- 에이전트 엔진(대화 처리) 개선, UI 부품 정리 다수

## 왜 중요한가
“AI 시대의 업무 소프트웨어”가 어떤 모양일지에 대한 하나의 답이다: **사람이 클릭하던 설정을 에이전트가 읽고 고칠 수 있는 코드로 바꾼다.** 요금 체계도 “좌석 + AI 크레딧”으로 가고 있어, 어제 다룬 Town, 앞서 다룬 Notion·Figma의 ‘크레딧’ 전환과 같은 흐름이다. 1인 스튜디오라면 고객·프로젝트 관리 도구를 직접 꾸리면서 데이터를 내 서버에 두는 선택지로 볼 만하다(라이선스 조건은 저장소에서 확인 필요).

출처: [twentyhq/twenty (GitHub)](https://github.com/twentyhq/twenty) · [Release v2.50.0 (10/21)](https://github.com/twentyhq/twenty/releases) · [GitHub Trending 10/22 아카이브](https://githubtrending.today/archive/2026-10-22/)
