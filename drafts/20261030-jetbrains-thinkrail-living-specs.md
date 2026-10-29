---
title: "GitHub 트렌드: JetBrains ThinkRail 하루 +1,100★ — 에이전트마다 작업 공간을 따로 주고, ‘살아 있는 명세’로 프로젝트 기억을 남기는 가벼운 IDE"
date: 2026-10-30T07:09:00+09:00
category: "GitHub 트렌드"
slug: "jetbrains-thinkrail-living-specs"
summary: "JetBrains 인큐베이터 프로젝트 ThinkRail(Apache-2.0)이 10/29 GitHub 일간 트렌드 4위(+1,116★, 약 5.9천★). 10/27 기사에서 한 줄로 소개했던 도구가 일주일 새 두 배 넘게 컸다. pi 코딩 에이전트를 감싸, 작업마다 git worktree로 분리된 공간을 만들고, SPEC.md 그래프를 에이전트가 직접 읽고 고치며, UI 변경은 전/후 목업으로 보여 준다. 같은 날 트렌드엔 ‘에이전트에게 컴퓨터를 주는’ OpenMausBot·CopilotKit OpenBot도 올랐다."
---

## 한줄 요약
“바이브 코딩”의 불편함은 두 가지다. 에이전트 여러 개가 **같은 폴더를 동시에 건드리고**, 대화가 끝나면 **왜 그렇게 만들었는지가 사라진다**. ThinkRail은 이 둘을 IDE 차원에서 막는다([GitHub](https://github.com/JetBrains/thinkrail)).

## 핵심 기능 (README 기준)
- **작업 공간 분리** — 프로젝트에서 작업마다 `git worktree`(브랜치별 별도 폴더)를 잘라 준다. 에이전트들이 병렬로 일해도 내 작업본은 안전. 잘 된 브랜치만 합치고 나머진 버린다. PR이 합쳐지거나 일주일 조용하면 선반으로 자동 정리.
- **살아 있는 명세(living specs)** — 코드 옆에 연결된 `SPEC.md` 파일 그래프를 두고, 에이전트가 전용 도구로 **읽고·검색하고·고친다**. 대화가 끝나도 “의도”가 남는다.
- **진짜 IDE** — 에디터 탭·파일 트리·터미널, 파일과 diff에 리뷰 댓글을 달아 채팅으로 넘기기.
- **추측 대신 질문** — 에이전트가 애매하면 객관식 질문을 채팅에 띄우고, UI를 바꿀 땐 **전/후 목업**을 보여 줘 diff처럼 댓글을 달 수 있다.
- **스킬 재사용** — 다른 코딩 에이전트용으로 갖고 있던 Agent Skills를 그대로 읽는다. PR 생성은 내 `gh`로.

## 같은 날 트렌드의 이웃들
| 저장소 | 한 줄 설명 |
|---|---|
| milind-soni/OpenMausBot (~7.4천★, +1,190) | 봇 여러 명을 채팅 앱처럼 두고, 각자 모델·컴퓨터·연결 앱을 갖는 오픈소스 개인 에이전트 팀(Apache-2.0). 내 PC에 깔린 claude·codex·grok CLI를 그대로 씀 |
| CopilotKit/OpenBot (~8천★) | 회사가 자기 인프라에 두는 ‘AI 동료’ 템플릿(MIT). 봇마다 브라우저·파일·허용된 도구, 모든 행동을 사전 판단·사후 기록 |

출처: [GitStock 10/29 일간 트렌드](https://gitstock.org/trending/2026-10-29) · [OpenMausBot](https://github.com/milind-soni/OpenMausBot) · [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)

## 왜 중요한가
- 요즘 인기 도구의 공통점은 모델이 아니라 **“작업 단위 격리 + 기억 파일 + 사람 승인”**이다. ThinkRail은 이를 IDE로, OpenMausBot·OpenBot은 메신저·사내 플랫폼으로 푼다.
- 지난 10/27 ‘명세 주도 개발’ 기사에서 본 흐름이 한 주 만에 대형 IDE 회사 실험작의 급성장으로 이어졌다.
