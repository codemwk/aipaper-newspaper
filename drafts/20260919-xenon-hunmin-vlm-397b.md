---
title: "제논 Hunmin VLM 397B — 화면을 보고 클릭하는 오픈 CUA, ScreenSpot Pro 2위"
date: 2026-09-19T07:20:00+09:00
category: "AI Models"
slug: "xenon-hunmin-vlm-397b"
summary: "2026-09-18 서울경제. 제논이 Qwen 3.5-397B 기반 컴퓨터 조작 VLM Hunmin VLM 397B를 오픈소스 공개. ScreenSpot Pro 75.6(HF 2위), OSWorld +22.3p. B200 8장 후학습. OneAgent에 연동 예정."
---

## 한줄 요약
[서울경제(영문)](https://en.sedaily.com/technology/2026/09/18/xenon-open-sources-computer-operating-ai-model-hunmin-vlm)(2026-09-18)에 따르면, 제논(**Xenon**)은 화면 요소를 찾아 **실제 PC를 조작**하는 **Hunmin VLM 397B**를 오픈소스 공개했다. 베이스는 **Qwen 3.5-397B**.

## 무엇이 바뀌었나
- 질문 답변을 넘어 버튼·입력란을 식별하고 클릭·입력을 수행한다. 전작 Hunmin 32B·VLM 235B 계열의 **한국어 성능 유지 + CUA 강화**.
- 벤치(회사·보도): ScreenSpot Pro **75.6** → Hugging Face 스크린 인식 보드 **2위**, 한국 개발사로는 유일하다고 주장(보드 등재 48개 기준). OSWorld(Linux 360태스크) **70.5**(베이스 대비 **+22.3**), WindowsAgentArena도 베이스 대비 **+9.1**.
- 학습 효율: low-rank 전이 + FP8 SFT/RL을 **Nvidia B200 8장**으로 후학습했다고 밝혔다. 원본·FP8(용량 약 절반)·평가 조건도 함께 공개 예정.
- 제품: 235B의 브라우저·PC 조작을 **OneAgent**에 이미 붙였고, 397B로 기업 업무 범위를 넓힌다.

## 왜 중요한가
컴퓨터 사용 에이전트(CUA)가 클로즈드 프론티어만의 영역이 아님을 보여 주는 **국내 오픈웨이트** 신호다. Chrome DevTools MCP·Playwright MCP가 “브라우저 도구”라면, Hunmin은 **픽셀·접근성 트리 수준의 조작 모델** 쪽이다. 벤치 숫자는 과제 세트에 민감하니, 자체 OSWorld 재현이 다음 과제.

## 기억할 것
- [서울경제 보도](https://en.sedaily.com/technology/2026/09/18/xenon-open-sources-computer-operating-ai-model-hunmin-vlm) · Xenon / Hunmin VLM 397B
