---
title: "GitHub 트렌드: 이번 주 급상승 — 접근성 트리로 PC를 다루는 agent-desktop, 내 PC의 ‘AI 팀’ Orkas, 에이전트 비용 한곳에 Nasiko, 지포스 BF16 해제"
date: 2026-11-02T07:06:00+09:00
category: "GitHub 트렌드"
slug: "github-week-desktop-agents"
summary: "10/26~11/1 급상승 저장소의 공통점은 ‘에이전트를 내 컴퓨터로’. Vercel Labs agent-desktop(픽셀 대신 OS 접근성 트리, ★6.7K), Orkas(로컬 커맨더+전문 에이전트 16개, ★7.2K), Nasiko(이미 쓰는 코딩 에이전트 사용량·비용 집계·라우팅, ★11.4K), gpu-unlock(지포스 텐서 처리량 최대 2배 주장, ★14.1K)."
---

## 한줄 요약
이번 주 별이 몰린 곳은 클라우드가 아니라 **내 책상 위 컴퓨터**였다([Early Signal 주간](https://earlysignal.news/weekly/2026-w44)). 별 수는 11/2 오전 GitHub API 기준.

## 저장소별 한 줄
| 저장소 | 무엇을 하나 | 왜 뜨나 |
|---|---|---|
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) ★약 6.7K | 앱 화면을 스크린샷이 아니라 **OS 접근성 트리**로 읽어 요소마다 안정적인 참조를 JSON으로 준다. 에이전트는 그 참조로 클릭·입력하고 다시 스냅샷으로 결과 확인 | 픽셀 추측형 컴퓨터 사용의 고질병(버튼 위치 틀림, 재시도 위험)을 피함. Rust, Apache-2.0 |
| [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) ★약 7.2K | 목표를 말하면 ‘커맨더’가 할 일로 쪼개 내장 전문 에이전트 16개와 Claude Code·Codex·OpenCode 등에 배분. 프로젝트·예약 자동화 | 맥·윈도 무료 앱, 로컬 우선, MIT |
| [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) ★약 11.4K | 이미 돌리는 코딩 에이전트를 찾아 **사용량·비용을 모으고** 요청을 원하는 모델로 라우팅 | 기존 하네스 설정을 안 바꿔도 됨 — 에이전트 여러 개 쓰는 팀의 청구서 정리 |
| [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) ★약 14.1K | 리눅스 커널 모듈로 지포스 20/30/40 시리즈의 FP16/BF16/TF32 텐서 처리량을 **최대 2배**로 올린다고 주장 | 로컬 학습·추론 비용. 단 드라이버 로드 전 개입하는 비공식 방식, 라이선스 미표기 — 보증·안정성 리스크 |

## 왜 중요한가
- 흐름은 셋: **(1) 화면을 ‘구조’로 읽는 컴퓨터 사용, (2) 여러 에이전트를 지휘하는 로컬 커맨더, (3) 그 비용을 한눈에.** 에이전트 함대를 운영하는 쪽(orca·headroom 류)이 이제 데스크톱 앱 형태로 내려오는 중.
- gpu-unlock은 성능 수치가 저자 주장이고 하드웨어 수준 개입이라 실험용 머신에서만.
