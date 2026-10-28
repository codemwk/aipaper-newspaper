---
title: "AI 도구: GitHub Copilot 안에서 이미지 생성·편집 — 코딩하다 “빈 화면용 일러스트 하나” 하면 GPT Image 2.5 Flare가 그려 프로젝트 폴더에 저장. ‘AI로 만듦’ 워터마크는 켜고 끌 수 있다"
date: 2026-10-29T07:10:00+09:00
category: "AI 도구"
slug: "copilot-image-generation"
summary: "GitHub가 10/28 Copilot 채팅에서 이미지를 생성·편집하는 기능을 공개 미리보기로 출시(VS Code, Copilot 앱, Copilot CLI). 선택한 추론 모델이 GPT Image 2.5 Flare 기반 이미지 도구를 불러 결과를 대화 안에 미리 보여 주고 작업 폴더에 바로 저장한다. Pro·Pro+·Business·Enterprise 대상, 채팅 모델과 별도로 이미지 토큰만큼 AI 크레딧 차감. 조직 관리자는 정책으로 끌 수 있고, ‘Made with AI’ 워터마크는 기본 꺼짐·선택 사항."
---

## 한줄 요약
앱을 만들다 아이콘·빈 화면 일러스트·OG 이미지가 필요하면 지금까지는 다른 도구로 나갔다 와야 했다. 이제 **Copilot 대화창에서 말로 그리고, 결과가 바로 프로젝트 폴더에 들어간다**([GitHub Changelog](https://github.blog/changelog/2026-10-28-generate-and-edit-images-directly-in-copilot/)).

## 어떻게 작동하나
- 이미지를 요청하면, 지금 쓰는 추론 모델이 **전용 이미지 생성 도구(GPT Image 2.5 Flare)**를 호출한다.
- 결과를 **대화 안에 미리 보기**로 띄우고, 작업 공간에 **파일로 저장**.
- 새 요청이든 코딩 도중이든 같은 대화에서 가능. 기존 이미지 편집도 된다.
- 사용처: VS Code, GitHub Copilot 앱, Copilot CLI.

## 요금·관리
| 항목 | 내용 |
|---|---|
| 대상 | Copilot Pro, Pro+, Business, Enterprise (공개 미리보기) |
| 과금 | 채팅 모델과 **별도**, 이미지 토큰 기준으로 요금제의 AI 크레딧 차감 |
| 관리 | 조직·엔터프라이즈 관리자가 모델 정책으로 이미지 생성 끄기 가능 |
| 워터마크 | ‘Made with AI’ 표시 선택 가능 — **기본은 꺼짐** |

## 왜 중요한가
- 같은 날 GitHub가 공개한 디자인 시스템 기반 프로토타입 도구 Replica와 합치면, **Copilot 앱이 ‘코드 + 화면 시안 + 이미지 자산’을 한 대화에서 만드는 작업대**가 되어 간다.
- 다만 이미지가 코드 저장소에 바로 들어오는 만큼, 팀이라면 **워터마크·출처 표기 규칙과 크레딧 한도**를 먼저 정해 두는 게 좋다. 브랜드 자산은 여전히 사람의 최종 검수 대상이다.
