---
title: "AI Trading: MT5 Build 6180 — Strategy Tester까지 MCP로 ‘최적화 에이전트’"
date: 2026-09-25T07:11:00+09:00
category: "AI Trading"
slug: "mt5-build-6180-tester-mcp"
summary: "MetaTrader 5 Build 6180(2026년 초). MCP로 테스터 리포트 읽기·최적화 실행·설정/로그 조회. 6060 네이티브 MCP 이후 테스터 단계. 과적합 검증은 여전히 트레이더 몫."
---

## 한줄 요약
MT5 네이티브 MCP가 **Strategy Tester**까지 확장됐다. Build 6180(2026년 9월 초)에서 AI 어시스턴트·외부 MCP 에이전트가 최적화 실행·리포트 비교·테스터/EA 로그 읽기를 수행할 수 있다([IA Trader Pro 정리](https://iatraderpro.com/en/metatrader-5-mcp-ai-backtest-optimization/)).

## 빌드 타임라인 (요약)
| Build | MCP 능력 |
| --- | --- |
| 6060 (Jul) | 시세·차트·환경·체결 인터페이스, 외부 에이전트 |
| 6090 | 지표 추가·목록 |
| 6140 | 도구 최적화, 테스터 중지 |
| **6180 (Sep)** | **테스터 리포트·최적화 실행·설정/로그·커스텀 지표 파라미터** |

## 실무에서 조심할 것
- AI는 숫자를 **읽지만**, OOS·walk-forward·최소 트레이드 수·플랫 구간 여부는 **사람이 판정**.
- MetaQuotes는 Claude Code·Codex 등 외부 연결을 언급하나, 공식 스텝바이스텝은 릴리즈 노트에 없을 수 있음 → 터미널 AI/MCP 설정·문서 확인.
- 라이브 주문 권한은 금지 또는 수동 확인 권장. 데모 먼저.

## 왜 중요한가
어제 MQL5 howto가 “연결법”이었다면, 오늘은 **백테스트/최적화가 에이전트 툴이 된 단계**. 자동매매 스택에서 ‘분석 챗’과 ‘테스터 조작’의 경계가 무너진다.

## 기억할 것
- [IA Trader Pro 가이드](https://iatraderpro.com/en/metatrader-5-mcp-ai-backtest-optimization/) · MT5 Tools → Options → MCP
