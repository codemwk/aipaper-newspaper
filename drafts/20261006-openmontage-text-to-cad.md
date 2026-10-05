---
title: "GitHub 트렌드: 코딩 에이전트에 ‘전문 스튜디오’를 붙인다 — OpenMontage(~64K★) 영상 제작, text-to-cad(~17K★) 3D 설계"
date: 2026-10-06T07:08:00+09:00
category: "GitHub 트렌드"
slug: "openmontage-text-to-cad"
summary: "일간 트렌딩 두 저장소의 공통점: Claude Code·Codex 같은 범용 코딩 에이전트를 스킬·MCP로 특정 직군 작업대로 바꾼다. OpenMontage는 12개 제작 파이프라인·100+ 툴·700+ 스킬 파일(60초 애니 단편 총비용 $1.33 예시, AGPLv3). text-to-cad는 STEP·STL·3MF 생성, 제조성 검사·도면, 3D 프린팅·CNC 서비스 연결(MIT)."
---

## 한줄 요약
이번 주 일간 트렌딩에서 눈에 띄는 패턴: 새 모델이 아니라 **“이미 쓰는 코딩 에이전트에 특정 분야의 작업대를 꽂아 주는”** 저장소가 뜬다. 대표가 영상 제작의 [OpenMontage](https://github.com/calesthio/OpenMontage)와 3D 설계의 [text-to-cad](https://github.com/earthtojake/text-to-cad)다.

## OpenMontage — 에이전트를 영상 프로덕션으로
- 자칭 “최초의 오픈소스 에이전트형 영상 제작 시스템”. **12개 제작 파이프라인, 100개 이상 툴, 700개 이상 스킬·제작 지식 파일**. 약 6.4만 스타, 라이선스 AGPLv3.
- 말로 원하는 영상을 설명하면 에이전트가 **리서치 → 대본 → 에셋 생성 → 편집 → 최종 합성**을 한다. Veo·Kling 같은 생성 모델로 클립을 만들 수도, 무료 스톡·공개 아카이브에서 **실제 촬영 영상을 찾아 편집**할 수도 있다.
- README 예시: Kling v3 클립 6개 + 내레이션 + 무료 음악 + 단어 단위 자막으로 만든 60초 애니메이션 단편, **총비용 $1.33**. Blender로 물리 애니메이션을 만들어 FFmpeg로 붙인 예시도 있다.

## text-to-cad — 에이전트에게 CAD 능력을
- “에이전트에 CAD 초능력을.” 약 1.7만 스타, MIT. Claude Code·Codex·Cursor·Gemini·Grok 등 플러그인/스킬 지원 에이전트에 설치.
- 3D 모델을 **STEP·GLB·STL·3MF**로 생성, **제조 가능성(DFM) 검사**, 엔지니어링 도면 생성, 3D 프린팅·판금·CNC 가공 서비스 연결까지. 대화창 안에서 돌려 보는 CAD 뷰어 카드를 띄우고, 사용자가 선택한 부분을 에이전트가 읽는다.
- 내부는 오픈소스 CAD 커널(Open CASCADE·build123d) 위의 `cadgen` 패키지 + 로컬 MCP 서버.

## 왜 중요한가
어제 다룬 impeccable(디자인)에 이어 이번 주 OpenMontage(영상)·text-to-cad(제조)까지 — **스킬 파일 + 로컬 MCP 서버 + 결과 뷰어**라는 같은 틀이 직군을 하나씩 먹어 들어간다. 의미는 두 가지다. (1) 전문 툴 회사의 경쟁자가 ‘다른 툴’이 아니라 **‘범용 에이전트 + 무료 스킬팩’**이 된다. (2) 사용자 입장에선 새 앱을 배우는 대신 **이미 익숙한 에이전트 하나에 작업대를 갈아 끼우는** 쪽으로 학습 비용이 옮겨 간다.

## 기억할 것
- OpenMontage는 AGPLv3 — 서비스에 넣으려면 소스 공개 의무 확인.
- [GitHub: OpenMontage](https://github.com/calesthio/OpenMontage) · [GitHub: text-to-cad](https://github.com/earthtojake/text-to-cad) · [text-to-cad 문서](https://www.texttocad.dev)
