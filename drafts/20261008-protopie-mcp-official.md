---
title: "디자인/UI·UX: ProtoPie MCP 정식 출시 — 팀 컴포넌트 라이브러리로 프로토타입을 만들고, ‘요소 ID’로 정확히 고치고, React Native 코드까지"
date: 2026-10-08T07:06:00+09:00
category: "디자인/UI·UX"
slug: "protopie-mcp-official"
summary: "인터랙티브 프로토타이핑 툴 ProtoPie가 10/7 MCP를 정식화했다. Studio MCP가 팀의 ProtoPie 라이브러리 컴포넌트를 인스턴스로 배치하고, 레이어·씬·변수·트리거 ID를 프롬프트에 넣어 정밀 수정. Code MCP는 React·React Native·Flutter·SwiftUI·Compose·Qt/QML·ArkTS 지원. Core는 Pro 플랜, Enterprise는 Code MCP·Dev View 포함."
---

## 한줄 요약
AI는 화면을 몇 초 만에 그리지만, **“눌러 보면 진짜처럼 움직이는”** 프로토타입에서는 늘 무너졌다. 인터랙션 프로토타이핑 툴 **ProtoPie**가 10월 7일 **ProtoPie MCP를 정식 출시**하며 그 간극을 노렸다([ProtoPie 블로그](https://www.protopie.io/blog/protopie-mcp-official)).

## 무엇이 새롭나
- **우리 팀 라이브러리로 만든다**: Studio MCP가 활성화된 ProtoPie 라이브러리를 탐색해 컴포넌트를 **인스턴스로** 추가한다. 에이전트가 만든 새 화면도 기존 디자인 시스템 안에 머문다.
- **ID로 정확히 지목**: 레이어·씬·변수·컴포넌트·트리거·리스폰스의 **ID를 복사해 프롬프트에** 넣는다. “왼쪽 위 그 버튼…” 대신 “[ID]의 인터랙션을 바꿔”. 복잡한 프로토타입일수록 효과가 크다.
- **코드 생성 확장**: Code MCP가 **React, React Native(신규), Qt/QML, Flutter, SwiftUI, Compose, ArkTS**를 공식 지원.

## 패키지와 가격 구조
1. **MCP Core** — 내 AI로 Studio MCP를 써서 프로토타입 제작·수정. **Pro 플랜**에 포함.
2. **MCP Enterprise** — Studio MCP + **Code MCP + Dev View**로 개발 단계까지. **Enterprise 플랜**.
흐름은 “프롬프트 → 프로토타입 → 검증(ProtoPie Connect로 실제 하드웨어 테스트) → 코드”다. 10월 13일(미 동부 19시)에는 자동차 HMI 프로토타이핑 웨비나도 연다.

## 왜 중요한가
Figma 에이전트 정식 출시(10/6), Webflow MCP의 네이티브 Interactions(10/2)에 이어, 디자인 툴들의 공통 문법이 굳어지고 있다 — **① 에이전트는 팀 컴포넌트만 쓰게, ② 사람이 지목할 수 있는 정밀 핸들(ID·잠금)을 주고, ③ 결과는 다시 사람이 만질 수 있게**. ProtoPie가 특히 강한 곳은 **자동차·가전·의료기기처럼 실제 하드웨어와 묶인 인터랙션**이다. 코드 생성 대상에 Qt/QML·ArkTS(화웨이 HarmonyOS)가 있는 것도 그 시장을 보여 준다.

출처: [ProtoPie MCP is Now Official](https://www.protopie.io/blog/protopie-mcp-official)
