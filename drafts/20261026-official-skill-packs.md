---
title: "GitHub 트렌드: ‘공식 스킬 꾸러미’가 뜬다 — 구글 android/skills(~9.7천★, 스킬 33개)와 Anthropic knowledge-work-plugins(~3.3만★, 주간 +2.6천). 디자인 플러그인엔 /critique·/handoff·/accessibility"
date: 2026-10-26T07:09:00+09:00
category: "GitHub 트렌드"
slug: "official-skill-packs"
summary: "이번 주(10/19–25) GitHub 주간 트렌딩에 플랫폼 회사가 직접 만든 ‘에이전트용 업무 설명서’ 저장소 두 개가 올랐다. 구글 안드로이드팀의 android/skills는 Compose 이전·Navigation 3·권한 보안·온디바이스 LLM 등 33개 스킬을 담아 10/21·10/23 연속 릴리스. Anthropic의 knowledge-work-plugins는 영업·법무·재무·마케팅·디자인·소상공인 등 직무별 플러그인 모음으로 주간 +2.6천 별. 코드 대신 ‘일하는 절차’를 배포하는 흐름."
---

## 한줄 요약
이번 주 GitHub 인기 목록에서 눈에 띄는 건 새 앱이 아니라 **“에이전트에게 우리 방식으로 일하는 법을 알려 주는 설명서 묶음”**이다. 그것도 구글·Anthropic이 **공식으로** 낸 것([Githot 주간 트렌딩](https://githot.dev/en/weekly)).

## 1) google: android/skills — 안드로이드 개발 ‘공식 요령집’
- **무엇**: 안드로이드 개발 작업을 에이전트가 제대로 하도록 돕는 `SKILL.md` 묶음. 별 약 9,700개, Apache-2.0.
- **최근**: v1.0.16(10/21)에서 3개 추가 → v1.0.17(10/23) 11개 갱신, **총 33개**([릴리스](https://github.com/android/skills/releases)).
  - 새 스킬 예: **litert-lm**(휴대폰 안에서 공개 LLM을 돌리는 앱 만들기), **anr-audit-and-fix**(앱 ‘응답 없음’ 위험 점검), **projected-hardware**(오디오·디스플레이 안경 같은 XR 기기 다루기).
  - 그 외 분야: Jetpack Compose, 내비게이션, 성능·프로파일러, 권한·인텐트 보안, Wear OS, TV, 자동차, XR.
- **설치**: Android CLI의 `android skills add` 명령으로 프로젝트·에이전트별로 넣는다. 저장소엔 Claude·Codex용 플러그인 폴더도 같이 있다.
- 쉽게 말하면: “구글이 권장하는 최신 방식”을 에이전트가 **추측하지 않고 문서대로** 따르게 하는 것. 오래된 블로그 글로 학습한 AI가 구식 코드를 쓰는 문제를 줄인다.

## 2) anthropics/knowledge-work-plugins — 직무별 ‘AI 동료 세팅’
- **무엇**: Claude Cowork(데스크톱 에이전트 앱)·Claude Code용 직무 플러그인 모음. 별 약 3.3만, 이번 주 +2.6천, Apache-2.0.
- **폴더**: 영업, 법무, 재무, 마케팅, 인사, 고객지원, 데이터, 엔지니어링, 제품관리, 바이오 연구, **디자인**, **소상공인** 등. 각 플러그인 = 스킬 + 도구 연결(MCP) + 슬래시 명령. 코드·서버 없이 마크다운·JSON 파일뿐.
- **최근 커밋 예**(10/21): 영업 플러그인 2.1.0 — “모든 문장 옆에 출처 링크를 달아 확인할 수 있게”.
- **디자인 플러그인 명령**:
| 명령 | 하는 일 |
|---|---|
| `/critique` | 사용성·시각 위계·접근성·일관성 구조화 피드백 |
| `/design-system` | 컴포넌트·토큰·패턴 감사·문서화 |
| `/handoff` | 개발 전달 명세(치수·토큰·상태·예외) |
| `/ux-copy` | 마이크로카피·오류 문구·빈 화면 문구 |
| `/accessibility` | WCAG 2.1 AA 점검 |
| `/research-synthesis` | 인터뷰·설문·사용성 테스트 정리 |
- Figma 등을 연결하면 더 강해지고, 연결 없이 스크린샷만 줘도 동작한다.

## 왜 뜨나
- 같은 호 AI 도구 기사처럼 Agent Skills가 **중립 표준**이 되자, 플랫폼 회사가 “우리 제품은 이렇게 쓰라”는 공식 스킬을 배포할 이유가 생겼다. 문서 사이트 → **에이전트가 읽는 문서**로의 이동.
- ‘무엇을 만들 수 있나’보다 **‘어떤 절차로 일하나’가 공유 자산**이 되는 흐름. 디자이너라면 디자인 플러그인의 명령 구성(비평→시스템→전달→카피→접근성)이 그대로 **팀 리뷰 체크리스트**로 쓸 만하다.

출처: [Githot 주간 트렌딩 (10/19–25)](https://githot.dev/en/weekly) · [android/skills 릴리스](https://github.com/android/skills/releases) · [Android 개발자 문서 — skills](https://developer.android.com/tools/agents/android-cli/commands/skills) · [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (별 수는 10/26 GitHub API 기준)
