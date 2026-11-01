---
title: "디자인: desigma — Rust로 만든 오프라인 ‘무료 Figma 대안’. .fig 열고 React·SwiftUI 코드 내보내고, 에이전트용 MCP까지(초기 알파)"
date: 2026-11-02T07:10:00+09:00
category: "디자인/UI·UX"
slug: "desigma-rust-figma-alternative"
summary: "deepfounder-ai의 desigma는 윈도·맥·리눅스 네이티브 디자인 툴(MIT/Apache-2.0)이다. 오토 레이아웃·컴포넌트 변형·변수 모드·Smart Animate 프로토타입·화이트보드·슬라이드, 프레임별 CSS·Tailwind·SwiftUI·Compose·React 코드. .fig는 역공학 디코더라 실제 파일 호환은 불완전, 빌드 미서명, 협업·플러그인 미지원. ★약 935."
---

## 한줄 요약
좌석 요금도, 클라우드 계정도, API 호출 한도도 없이 **내 PC에서 에이전트가 직접 디자인 파일을 읽는** 길을 노린 오픈소스 툴이다. 작성자 스스로 “아직 실무 대체품은 아니다”라고 적었다([GitHub](https://github.com/deepfounder-ai/desigma), [Reveneau](https://reveneau.com/ainews/desigma-open-source-figma-alternative-rust-182-stars), [Product Hunt](https://www.producthunt.com/products/desigma)).

## 지금 되는 것 (README 기준)
- **편집**: 프레임·오토 레이아웃, 변형/속성 있는 컴포넌트, 색·숫자·문자·불리언 **변수와 모드**, 펜·셰이프 빌더 등 벡터 도구, 다양한 그라디언트·블렌드.
- **프로토타입**: 트리거·오버레이·이징·스프링·**Smart Animate**, 키프레임 모션 타임라인.
- **그 밖**: 화이트보드(스티키·커넥터), 16:9 덱(발표자 노트·PDF).
- **Dev 모드**: 프레임에서 CSS·Tailwind·SwiftUI·Jetpack Compose·React 생성.
- **가져오기**: Figma REST JSON, 그리고 비공개 형식인 `.fig`(커뮤니티 역공학 기반). Product Hunt 소개엔 **열린 파일을 에이전트가 편집하는 MCP 서버**도 있다고 적혀 있다.
- 성능: CPU 렌더러(tiny-skia) + 공간 인덱스·256px 타일 캐시로 레이어 5,000개 페이지에서도 한 프레임 안쪽.

## 아직 안 되는 것
- 협업, 플러그인, 코드 서명 빌드 — 첫 실행 때 OS 보안 경고를 직접 넘겨야 한다.
- `.fig` 실제 파일엔 빈틈 예상(합성 파일로만 테스트).

## 왜 중요한가
- 디자인 툴 경쟁 축이 ‘누가 AI 기능이 많나’에서 **‘에이전트가 파일에 얼마나 싸고 직접 닿나’**로 옮겨 가는 신호. Figma가 자체 편집 모델·MCP로 문을 넓히는 동안, 반대편에선 로컬·오픈 파일 쪽 실험이 나온다.
- 실무 팁: 원본 말고 **사본 .fig**로 먼저 열어 볼 것. 10월 11일 생성된, 3주 남짓 된 프로젝트다.
