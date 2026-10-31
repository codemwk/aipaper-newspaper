---
title: "디자인: Archify — 말로 물으면 검증된 인터랙티브 HTML 다이어그램·한 페이지 답이 나온다. 에이전트 스킬"
date: 2026-11-01T07:07:00+09:00
category: "디자인/UI·UX"
slug: "archify-interactive-diagrams"
summary: "tt-a1i/archify가 아이디어·계획·코드베이스를 탐색 가능한 단일 HTML 다이어그램(또는 결론 우선 원페이지)으로 만드는 에이전트 스킬이다. 아키텍처·워크플로·시퀀스 등 10종, finalize 전 validate·deliver·check. Claude Code·Codex·Cursor·OpenCode·Copilot. Apache-2.0. BeWisp 주간 스타 +3.2K대."
---

## 한줄 요약
Mermaid ‘슬롭’ 대신 **레이아웃·라벨·교차까지 검사한 뒤** 브라우저에서 바로 열리는 맵을 받게 하는 스킬이다([archify.si](https://archify.si/), [GitHub](https://github.com/tt-a1i/archify)).

## 무엇을 하나
| 모드 | 결과 |
|---|---|
| Map | 아키텍처·워크플로·시퀀스·데이터플로·라이프사이클·ERD·클래스·트리·타임라인·워터폴(10종) |
| One-page | 결론 먼저 → 패널별 표·단계·차트·코드·다이어그램, 출처 번호·커밋 고정 |
| 전달물 | **의존성 없는 단일 HTML**. PNG/SVG/WebM 내보내기, 라이트·다크 |

설치 예: `npx skills add tt-a1i/archify` 후 “Use Archify to diagram …” / “answer as one page …”.

## 품질 게이트
`finalize`가 schema·교차·라벨 여백 등 검사 → 스테이징 렌더 후 원자적 교체 → 파일 해시 재확인. 브라우저 체크(해상도별 overflow)는 옵션. **빈 차트 칸은 0이 아니라 에러.**

## 왜 중요한가
- 디자인·PM·엔지니어가 같은 ‘설명 아티팩트’를 PR·메일에 붙일 수 있다. 지난주 BeWisp 주간 스타에서 archify가 상위권(+약 3.2K)에 올랐다([BeWisp weekly](https://bewisp.com/weekly)).
- 한계: 주장의 사실성까지 보증하지 않음. 호스팅 협업 툴이 아니라 **로컬 스킬**.
