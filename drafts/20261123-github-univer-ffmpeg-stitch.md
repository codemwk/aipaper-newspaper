---
title: "GitHub 이번 주: 에이전트에게 ‘엑셀’, ‘영상 편집기’, ‘디자인 도구’를 쥐여 주는 저장소들 — Univer, ffmpeg-skill, stitch-skills"
date: 2026-11-23T07:40:00+09:00
category: "GitHub 트렌드"
slug: "github-univer-ffmpeg-stitch"
summary: "11/22 GitHub 주간 트렌딩에서 눈에 띈 흐름은 ‘코딩 에이전트에게 사무·창작 도구를 붙이는’ 저장소다. 이번 주 가장 많이 오른 Univer(+7,240★)는 내 제품 안에 스프레드시트·문서 편집기를 넣고 사람과 AI 에이전트가 함께 쓰게 하는 오피스 SDK. ffmpeg-skill(+3,598★)은 컷·자막·화면비·음량·플랫폼별 내보내기 등 FFmpeg 도구 42개를 에이전트용으로 묶어 클라우드·API 키 없이 로컬에서 영상을 편집한다. 구글의 stitch-skills(+2,431★)는 Stitch 디자인 도구를 Claude Code·Cursor·Codex에서 부르는 스킬 묶음이다."
---

## 한줄 요약
이번 주 트렌딩의 공통점: **에이전트가 ‘코드’ 말고 ‘일하는 도구’를 직접 만진다.** 표, 영상, 디자인 화면이다([GitStock 주간 스냅샷 11/22](https://gitstock.org/trending/weekly/2026-11-22)).

## 1) Univer — 내 제품 안의 ‘AI 오피스’ (+7,240★, 약 3.1만★)
- 한 줄로: **구글 시트·문서 같은 편집기를 내 앱 안에 넣는 SDK**다. 사람과 AI 에이전트가 같은 표·문서를 편집한다([GitHub](https://github.com/dream-num/univer)).
- 오픈소스 부분(Apache 2.0): 셀 서식·병합·틀 고정, **수식 계산**, 필터·정렬·데이터 검증·조건부 서식, 댓글, 문서 편집.
- 에이전트 연결: 앱용 API(Facade API)와 이벤트로 에이전트가 표를 읽고 고친다. 모델과 도구 연결은 내 앱이 맡는다. 예시는 **견적서를 편집·계산·저장**하는 흐름이다.
- 상용 부분: 실시간 협업·편집 이력·오피스 파일 가져오기/내보내기(Server SDK), AI SDK 확장은 **별도 유료 라이선스**다. ‘오픈 코어’ 모델이다.

## 2) ffmpeg-skill — 에이전트용 로컬 영상 편집기 (+3,598★, 약 9,700★)
- 영상 처리 엔진 FFmpeg를 **에이전트가 실수 없이 쓰도록 42개 도구로 쪼개** 놓았다. 각 도구의 입력·출력이 기계가 읽는 규칙(contract)으로 정해져 있다([GitHub](https://github.com/kajisho5/ffmpeg-skill)).
- 할 수 있는 일: **컷 편집, 자막, 화면비 바꾸기(세로 영상), 음량 맞추기, 플랫폼별 내보내기.** MCP 서버도 있어 Claude Code·Cursor·Codex에서 부른다.
- **클라우드도, API 키도 없다.** 내 컴퓨터에서만 돈다.

## 3) stitch-skills — 구글 Stitch를 코딩 에이전트에서 (+2,431★, 약 1.2만★)
- 11/17 전한 구글 디자인 도구 **Stitch**(문장으로 여러 화면 흐름 만들기)를 **Codex·Claude Code·Cursor·Gemini CLI에서 쓰는 스킬 묶음**이다([GitHub](https://github.com/google-labs-code/stitch-skills)). Apache 2.0.
- 세 꾸러미: 디자인(stitch-design), 빌드·컴포넌트(stitch-build), 유틸리티. 예: **이미 있는 프런트엔드 코드를 Stitch 디자인으로 되돌려 올리기**(code-to-design).
- 전제: Stitch MCP 서버 설정이 필요하다.

## 왜 중요한가
세 저장소 모두 같은 문제를 푼다. **에이전트는 똑똑하지만 손에 쥔 도구가 엉성하면 결과도 엉성하다.** 그래서 도구를 작고 분명한 단위로 쪼개 주는 쪽으로 간다(ffmpeg 42개, Stitch 스킬, Univer API). 1인 스튜디오에 바로 쓸 만한 건 ffmpeg-skill이다. 촬영본 하나를 **“릴스·쇼츠용 세로 15초 3개, 자막 붙여서”** 같은 지시로 로컬에서 처리할 수 있다. 같은 주 트렌딩에는 11/18 전한 claude-trading-skills(+3,113★), 11/17 전한 Plannotator(+3,396★)도 다시 올랐다.
