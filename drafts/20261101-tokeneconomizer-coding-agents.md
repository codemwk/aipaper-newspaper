---
title: "GitHub: Microsoft TokenEconomizer — 코딩 에이전트를 바꾸지 않고 저장소 경험으로 비용 18–31%↓"
date: 2026-11-01T07:11:00+09:00
category: "GitHub 트렌드"
slug: "tokeneconomizer-coding-agents"
summary: "Microsoft Research 등이 10/30 TokenEconomizer를 공개했다. Claude Code·Codex·Copilot CLI·Pi 플러그인으로, 같은 저장소 세션에서 반복 사실(마이크로스킬)·안 쓰는 도구 제거·실패 루프 개입만으로 SWE-Bench 조합에서 평균 비용 18.4–30.9% 감소(Pass@1은 5중 4에서 상승). 에이전트 가중치는 그대로. Apache-2.0."
---

## 한줄 요약
모델을 작게 만드는 게 아니라, **같은 레포에서 매번 다시 배우는 낭비**를 플러그인이 걷어 낸다([GitHub](https://github.com/microsoft/TokenEconomizer), [arxiv 2610.22732](https://arxiv.org/abs/2610.22732)).

## 세 가지 장치
1. **Micro-skills** — 반복 실패·주기적 리뷰로 “이 레포에선 `python -m pytest`” 같은 사실을 모아 세션 시작에 주입(기본 off).
2. **Tool pruning** — 안 쓰는 도구 정의를 요청마다 보내지 않게 에이전트 설정에서 제외(기본 on).
3. **Loop guard** — 같은 실패가 반복되면 판정 모델이 방향 전환 메모(기본 on). **세션을 스스로 죽이지는 않음.**

학습 내용은 `~/.tokeneconomizer`에 로컬 보관. 별도 API 키 없음(에이전트 로그인 사용).

## 숫자(논문·README)
- SWE-Bench 277태스크 × 5 에이전트–모델: 평균 비용 **−18.4~30.9%**, 30개 레포×조합 셀 모두 더 저렴, Pass@1은 **5 중 4**에서 상승.
- Web-Bench −16~21%. 새 레포 보안 감사 벤치에서도 −6~20%.

## 왜 중요한가
- 헤드룸·orca 같은 ‘토큰 절약’ 관심사(리더 시그널)의 공식 연구실 버전. **에이전트 UX를 바꾸지 않는 흑상자 절감**이라 도입 마찰이 낮다. 지원 버전 범위가 좁으니(예: Claude Code 2.1.300–310) 업그레이드 시 확인 필요.
