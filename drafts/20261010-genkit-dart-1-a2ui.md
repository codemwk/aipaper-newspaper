---
title: "디자인/UI·UX: Genkit Dart 1.0 — Flutter에 ‘생성형 UI(A2UI)’와 사람 승인 인터럽트를 넣는 안정판"
date: 2026-10-10T07:12:00+09:00
category: "디자인/UI·UX"
slug: "genkit-dart-1-a2ui"
summary: "Google이 10/8 Genkit Dart 1.0 안정판을 발표. Gemini·Claude·OpenAI 단일 API, 타입 세이프 flows, 도구+HITL interrupt, Dotprompt, OpenTelemetry. experimental A2UI로 에이전트가 날짜선택·폼·확인 카드를 네이티브 위젯으로 스트리밍."
---

## 한줄 요약
Flutter/Dart 앱에 에이전트 워크플로를 붙이는 **Genkit Dart**가 **1.0 안정판**이 됐다. 핵심은 모델 호출만이 아니라, **사람이 중간에 승인하는 도구**와 **텍스트 대신 네이티브 UI를 스트리밍하는 A2UI**다([Flutter 블로그 10/8](https://flutter.dev/blog/announcing-genkit-dart-1-0)).

## 1.0에 굳어진 것
- **한 API로 여러 모델**: Google Gemini, Anthropic Claude, OpenAI·호환 모델을 플러그인으로 등록.
- **Flows + 스키마**: `schemantic`으로 입출력 타입을 서버·Flutter 앱이 **공유**.
- **HITL interrupt**: 호텔 예약처럼 카드 결제 전 `.interrupt(...)`로 멈추고, 앱이 확인한 뒤 resume — 모델이 승인을 우회하지 못하게 도구 안에 넣는다.
- **미들웨어·Dotprompt·OTel**: 재시도, SKILL.md 로딩, 도구 승인 규칙, `.prompt` 파일, OpenTelemetry GenAI 규약.

## A2UI (experimental)
`genkit_a2ui`로 에이전트가 날짜 선택기·폼·확인 카드를 **점진적으로 네이티브 위젯**으로 보낸다. ChatGPT Intelligent UI·Claude 아티팩트와 같은 “답이 곧 UI” 흐름을 **Flutter 쪽**에서 연다.

## 왜 중요한가
모바일·데스크톱 제품 UI에서 에이전트 응답을 채팅 버블에만 가두지 않겠다는 신호다. 디자인 시스템·프로토타입 도구가 MCP로 열린 주와 맞물려, **런타임 UI도 에이전트 출력 형식**이 되고 있다.

출처: [Announcing Genkit Dart 1.0](https://flutter.dev/blog/announcing-genkit-dart-1-0)
