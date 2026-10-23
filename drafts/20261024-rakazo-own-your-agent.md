---
title: "GitHub 트렌드: Rakazo(~5.4천★, 주간 +1.2천) — ‘내 서버에서 도는 개인 에이전트’. Claude Duet·Muse 같은 비서를 모델·컴퓨터까지 직접 고르는 오픈소스로"
date: 2026-10-24T07:09:00+09:00
category: "GitHub 트렌드"
slug: "rakazo-own-your-agent"
summary: "elie222/rakazo(Apache-2.0, 8월 생성)가 GitHub 주간 트렌딩 15위(10/23 GitStock, 이번 주 +1,166★, 약 5,425★). 스스로를 Grok Bot·Meta Muse·OpenAI dots·Claude Duet 등의 ‘셀프호스팅 대안’이라고 소개. 대화·기억·루틴·기록을 가진 상주형 봇, 공유 ‘팀 컴퓨터’와 격리된 개인 컴퓨터, 브라우저·터미널·파일·데스크톱 접근, 하위 에이전트 위임, 음성 모드. 모델은 직접 가져오고(로컬 포함), 실행 환경은 Docker·E2B·Daytona 등에서 고른다. 웹·데스크톱·iPhone·Android. 아직 베타. 같은 주 상위권은 rea·orca·VoiceStudio 등 이미 다룬 ‘에이전트 운영’ 도구들."
---

## 한줄 요약
대기업들이 일제히 ‘개인 에이전트 앱’을 내는 주에, GitHub에선 그 반대 방향이 떴다. **Rakazo**는 “에이전트를 **빌려 쓰지 말고 소유하라**”는 오픈소스다([GitHub](https://github.com/elie222/rakazo), [GitStock 주간 트렌딩](https://gitstock.org/trending/weekly/2026-10-23)).

## 쉽게 말하면
Claude Duet이나 Meta Muse 같은 ‘항상 켜져 있는 비서’를 **내 컴퓨터나 내 서버에** 띄우는 프로그램이다. 회사 서버 대신 내가 정한 곳에서 돈다.

## 무엇이 들어 있나
- **상주형 봇**: 봇마다 대화·**기억**·**루틴(정기 작업)**·기록을 따로 가진다
- **컴퓨터 두 종류**: 여럿이 같이 쓰는 ‘팀 컴퓨터’와 격리된 ‘개인 컴퓨터’. 봇이 브라우저·터미널·파일·그래픽 데스크톱을 직접 쓴다
- **위임**: 다른 봇이나 잠깐 쓰고 버리는 하위 에이전트에게 일을 넘긴다
- **음성 모드**: 말로 답하기·받아쓰기·봇에게 전화 걸기(ElevenLabs·OpenAI·Cartesia·Fish Audio 키를 직접 연결)
- **모델은 직접**: 내 API 키로, 또는 로컬 모델로
- **실행 환경 선택**: Docker(로컬 기본), E2B, Daytona 등 원격 샌드박스
- **앱 연결**: Composio·Pipedream, 원격 MCP, OpenAPI 문서. 연결 자격증명은 서버에서 암호화되고 API로 다시 돌려주지 않는다
- **어디서나**: 웹, 데스크톱(Electron), iPhone, Android

설치는 Docker 기반 설치 스크립트 하나로 시작하고, VPS에 올리면 봇이 24시간 켜져 있다. **아직 베타**다.

## 지금 GitHub에서 무엇이 인기인가 (이번 주 맥락)
주간 상위권은 리버스 엔지니어링 에이전트 rea, 여러 코딩 에이전트를 한 화면에서 굴리는 orca, 로컬 음성 스튜디오 VoiceStudio, 공식 플러그인 디렉터리들 — 모두 **“에이전트를 어떻게 운영하나”** 도구다. Rakazo는 그 흐름이 **코딩 밖 일상 비서**로 넘어오는 신호다. 인기 이유는 단순하다: **모델·데이터·비용을 내가 통제**하고 싶은 사람이 많다.

## 쓰기 전에
봇에게 브라우저·터미널·메일을 쥐여 주는 구조라, 셀프호스팅이면 **보안 책임도 내 몫**이다. 공개 서버에 올릴 땐 HTTPS·접근 제어부터.

출처: [GitHub — elie222/rakazo](https://github.com/elie222/rakazo) · [GitStock 주간 트렌딩 (10/23)](https://gitstock.org/trending/weekly/2026-10-23)
