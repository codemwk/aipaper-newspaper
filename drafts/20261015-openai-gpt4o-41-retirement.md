---
title: "AI 모델: OpenAI, GPT-4o·4.1 API 퇴역 예고 — 2027-01-14 종료, 대체는 gpt-6-luna, 그 전에 10/23 ‘o1·o3-mini·gpt-4-turbo’ 일괄 종료가 먼저 온다"
date: 2026-10-15T07:03:00+09:00
category: "AI 모델"
slug: "openai-gpt4o-41-retirement"
summary: "OpenAI 지원 중단 문서(10/14 공지): gpt-4o(2024-08-06·11-20), gpt-4o-mini, gpt-4.1, gpt-4.1-mini가 2027-01-14 API에서 제거, 권장 대체 gpt-6-luna. 파인튜닝 모델도 같은 날 종료. 이미 4월에 예고된 gpt-4-turbo·gpt-4-0613·o1·o3-mini·o4-mini·gpt-image-1 등은 8일 뒤인 2026-10-23 종료. Evals는 10/31 읽기 전용, Agent Builder·프롬프트 API는 11/30 종료."
---

## 한줄 요약
2년 넘게 수많은 자동화 스크립트·봇·사내 도구의 “기본값”이었던 **GPT-4o**와 **GPT-4.1** 계열에 종료일이 붙었다. OpenAI는 2026-10-14 사용 중인 개발자에게 통지하고 지원 중단 문서를 갱신했다([Deprecations](https://developers.openai.com/api/docs/deprecations)).

## 일정표 — 무엇이 언제 꺼지나
- **2026-10-23 (8일 뒤, 4/22 예고분)**: `gpt-4-turbo`, `gpt-4-0613`, `gpt-4-1106-preview`, `gpt-4o-2024-05-13`, `gpt-4.1-nano`, `gpt-3.5-turbo-0125`, `o1`, `o1-pro`, `o3-mini`, `o4-mini`, `gpt-image-1` 및 관련 파인튜닝. 대체는 대부분 `gpt-5.6-sol`/`gpt-5.6-terra`/`gpt-5.6-luna`, 이미지 쪽은 `gpt-image-2.5-sunburst`·`flare`.
- **2026-10-31**: Evals 플랫폼 기존 평가가 **읽기 전용**.
- **2026-11-30**: Evals 대시보드·API, **Agent Builder**, 재사용 프롬프트(`v1/prompts`) 종료.
- **2027-01-14 (10/14 신규 공지)**: `gpt-4o-2024-08-06`, `gpt-4o-2024-11-20`, `gpt-4o-mini-2024-07-18`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14` 제거 → 권장 대체 **`gpt-6-luna`**. 이 모델들을 기반으로 한 **파인튜닝 모델도 같은 날 함께** 꺼진다.

## 확인하는 법
OpenAI는 `GET /v1/models` 응답의 `shutdown_date` 필드로 종료일을 프로그램이 직접 확인하라고 안내한다. 정식(GA) 모델은 최소 6개월, 특화 변형은 3개월, `preview` 이름이 붙은 모델은 **2주** 만에도 내릴 수 있다는 규칙도 문서에 명시돼 있다.

## 누구에게 급한가
- **트레이딩·알림 봇**: 2024~2025년에 만든 시그널 요약·뉴스 분류 봇은 `gpt-4o-mini`나 `o3-mini`/`o4-mini`를 하드코딩한 경우가 많다. **o 계열은 10/23**이 먼저다.
- **파인튜닝 자산**: 4o·4.1 위에 튜닝한 모델은 대체 경로가 “새 베이스로 재학습”뿐인데, 문서상 신규 파인튜닝 작업 생성은 **2027-01-06 이후 기존 고객도 막힌다**. 사실상 튜닝 자산을 프롬프트·평가 세트로 옮겨 둘 시점이다.
- **Agent Builder 사용자**: 11/30 종료, Agents SDK나 ChatGPT Workspace Agents로 이전 안내.

## 왜 중요한가
모델 교체는 “이름만 바꾸면 되는 일”이 아니다. 출력 길이·형식·거절 패턴이 바뀌면 파싱이 깨지고, 단가 구조도 달라진다. 오늘 할 일은 단순하다: 코드베이스에서 모델 이름을 검색하고, **고정 스냅샷 대신 별칭 + 회귀 테스트 세트**를 갖춰 두는 것. 모델이 매달 바뀌는 시대에 자동화의 수명은 **평가 세트의 품질**이 결정한다.

출처: [OpenAI API Deprecations](https://developers.openai.com/api/docs/deprecations)
