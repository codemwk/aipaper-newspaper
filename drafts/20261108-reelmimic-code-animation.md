---
title: "GitHub 트렌드: ‘이 영상 느낌으로 하나 만들어 줘’ — ReelMimic과 code-animation-prompts, 코딩 에이전트를 영상 스튜디오로"
date: 2026-11-08T07:08:00+09:00
category: "GitHub 트렌드"
slug: "reelmimic-code-animation"
summary: "이번 주 성장률 상위권에 ‘코딩 에이전트로 영상 만들기’ 레포 두 개가 나란히 올랐다. ReelMimic은 참고 영상의 컷 길이·BPM·전환·카메라를 분해해 같은 스타일의 새 2D 영상을 여러 에이전트가 나눠 만들고 서로 검수한다. code-animation-prompts는 341가지 시각 스타일을 Claude Code·Codex 스킬로 묶어 HTML 코드 애니메이션→MP4로 뽑는다."
---

## 한줄 요약
Neural Wire의 11/7 주간 성장률 집계에서 ReelMimic(+514%)과 code-animation-prompts(+488%)가 5위 안에 들었다([Neural Wire](https://neuralwire.co/articles/trending-ai-repos--nov-7-autonomous-security-desktop-control-and-visual-code-mapping/)). 둘 다 **영상 생성 모델이 아니라, 내 Claude Code·Codex를 영상 제작진으로 쓰는** 도구다.

## ReelMimic — 스타일은 배우고 소재는 안 베낀다
- 파일·폰 녹화·유튜브 링크를 넣으면 **샷 수·길이·BPM·전환·색·프레이밍·카메라 무빙**을 분해한다.
- 스토리보드·캐릭터·스타일 프레임으로 된 **계획을 먼저 보여주고 승인**을 받는다.
- 제작은 최대 **6개 에이전트가 분담**, 완성된 샷은 **다른 에이전트가 검수**(자기 작업을 자기가 채점하지 않음). 수정은 전후 스크린샷이 증거로 붙는다.
- 2D 전용 7개 엔진(벡터 모션그래픽, 수채화, 크레용 그림책, 픽셀, 종이 스톱모션, 화이트보드, 애니 셀). 30~60초 영상에 승인 후 **1~3.5시간**. MIT, 약 1.8k★(10/20 실수로 비공개 전환돼 스타 수가 초기화됐다고 README에 공지)([GitHub](https://github.com/edenfunf/reelmimic)).

## code-animation-prompts — 스타일 사전 341권
- 입자·네온·수묵·종이공예·미국 코믹스·잡지 레이아웃 등 **341개 스타일 프롬프트**(참고 스틸 196장), 오프라인 스타일 피커.
- Claude Code·Codex **에이전트 스킬**로 설치하면 필요한 스타일만 검색해 읽고, HTML/CSS 애니메이션을 짜고, 브라우저 렌더러로 **프레임 단위 MP4** 출력(오디오 합성 가능). 약 770★([GitHub](https://github.com/XiaoyeCodes/code-animation-prompts)).

## 왜 중요한가
저장해 두신 OpenMontage·ArtCraft·VoiceStudio 계열처럼 **“에이전트용 크리에이티브 스튜디오”**가 계속 커지는 중이다. 공통점은 ①계획 승인 ②역할 분리·교차 검수 ③스타일을 Markdown 파일로 관리 — 영상 품질보다 **제작 과정의 통제**를 파는 구조다.

## 주의
작업량이 전부 사용자의 Claude Code/Codex 구독 한도를 쓴다. 참고 영상의 저작권·초상권은 사용자가 책임진다. code-animation-prompts 라이선스는 GitHub에 표준 SPDX로 잡히지 않으니 LICENSE.md를 직접 확인할 것.
