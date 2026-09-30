---
title: "AI 트레이딩: OpenProphet — OpenCode+MCP로 돌리는 자율 트레이딩 에이전트 하네스(Alpaca)"
date: 2026-10-01T07:09:00+09:00
category: "AI 트레이딩"
slug: "openprophet-trading-agents"
summary: "JakeNesler/OpenProphet. 로컬 웹 UI+MCP로 다중 자율 트레이딩 에이전트. Alpaca 페이퍼/라이브 샌드박스, 권한·리스크 한도, SQLite 메모리. OSS 무료·셋업 가이드 유료. ★~113(소규모지만 구조가 선명)."
---

## 한줄 요약
[OpenProphet](https://openprophet.io/)([GitHub: JakeNesler/OpenProphet](https://github.com/JakeNesler/OpenProphet))는 **OpenCode로 붙인 임의 LLM**을 여러 **자율 트레이딩 에이전트**로 돌리는 오픈소스 하네스다. 에이전트마다 격리 샌드박스·**Alpaca** 페이퍼/라이브·스케줄·전략·리스크 한도를 두고, 하트비트 루프(관찰→논지→반박→실행→기억)를 돈다. 라이브 주문 툴은 **명시적으로 켜기 전 차단**이 기본 서사. 2026-10-01 ★~113 — 스타 수는 작지만 MT5 네이티브 MCP와 다른 **브로커 API형 에이전트** 레퍼런스다.

## 제품으로 보면
- **런타임**: macOS / Linux / Windows WSL, 로컬 대시보드.
- **모델**: OpenCode가 지원하는 Claude·GPT·Gemini 등.
- **수익 모델(사이트)**: 소프트웨어는 OSS. Premium Setup Guide **$46.99**, VIP Live Setup **$699.99**(일회).
- **위험 고지**: 환각·규칙 미준수로 계좌 전액 손실 가능 — **페이퍼 검증 필수**(공식 FAQ).

## 왜 중요한가
어제 MT5 Build 6180(테스터·리포트)을 다뤘다면, 오늘은 **증권·주식 API 쪽 에이전트 하네스**다. 플랫폼 내장 MCP vs 외부 오케스트레이터+브로커 두 갈래가 동시에 열린다.

## 기억할 것
- [openprophet.io](https://openprophet.io/) · [GitHub](https://github.com/JakeNesler/OpenProphet) · 페이퍼 먼저
