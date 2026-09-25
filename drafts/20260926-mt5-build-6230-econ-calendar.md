---
title: "AI Trading: MT5 Build 6230 — 경제캘린더·차트 EA 제어까지 AI Assistant 확장"
date: 2026-09-26T07:02:00+09:00
category: "AI Trading"
slug: "mt5-build-6230-econ-calendar"
summary: "MetaQuotes(2026-09-24 릴리즈 노트). Build 6230: EA 테스터 파라미터 준비, 차트 EA/스크립트/지표 부착·제거, Economic Calendar 조회. FX News Group: MQL5 Lite로 3조 토큰 처리 주장. 라이브 업데이트 배포."
---

## 한줄 요약
MetaTrader 5 **Build 6230**(릴리즈 노트 2026-09-24, 배포 2026-09-25)이 AI Assistant 도구를 한 단계 더 늘렸다. 어제 다룬 Build 6180(테스터 로그·최적화)에 이어, 이번에는 **매크로 캘린더 + 차트 위 MQL5 프로그램 제어**가 핵심이다.

## 무엇이 바뀌었나
- **EA 테스트 준비**: Assistant가 Expert Advisor 입력 파라미터를 읽고 Strategy Tester 실행을 준비.
- **차트 워크스페이스**: EA·스크립트 파라미터 조회, 차트에 실행/제거, 지표 상태 확인.
- **Economic Calendar**: 국가·이벤트 목록, 지표 값, ID로 레코드 검색 — 가격 데이터와 거시 이벤트를 같은 분석 루프에 넣을 수 있음.
- **수요 신호**: FX News Group은 출시 약 두 달 만에 무료 **MQL5 Lite**로 **3조(3 trillion) 토큰**을 처리했다고 MetaQuotes 측 수치를 전함.
- **MQL5**: 벡터/행렬 Sort, .NET CoreCLR 8+ 임포트, 복소 행렬 Products·Solutions 메서드 등([공식 릴리즈 노트](https://www.metatrader5.com/en/releasenotes/terminal/2470)).

## 왜 중요한가
에이전트가 “차트 설명”을 넘어 **테스트 준비 → 실행 환경 세팅 → 매크로 컨텍스트**까지 한 세션에서 잇는다. 실계좌 자동매매 판단은 여전히 제한적이라는 기존 기조는 유지하되, 리서치·QA 루프는 뚜렷이 길어진다.

## 기억할 것
- [MetaQuotes 릴리즈 노트](https://www.metatrader5.com/en/releasenotes/terminal/2470) · [FX News Group](https://fxnewsgroup.com/forex-news/platforms/mt5-build-6230-comes-equipped-with-expanded-ai-capabilities/)
