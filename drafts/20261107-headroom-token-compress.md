---
title: "GitHub: headroom — 도구 출력·로그·RAG를 LLM 앞에 압축, 코딩 에이전트 토큰 약 20% 절감"
date: 2026-11-07T07:06:00+09:00
category: "GitHub"
slug: "headroom-token-compress"
summary: "headroomlabs-ai/headroom이 약 7.9만★(11/6 기준). 도구 출력·로그·파일·RAG 청크를 모델에 넣기 전 압축하고, 필요 시 역조회한다. 코딩 에이전트 입력 약 20%, JSON 60–95% 절감 주장. 라이브러리·프록시·에이전트 래핑·MCP로 붙인다. Apache-2.0."
---

## 한줄 요약
에이전트 비용의 상당수는 “틀린 답”이 아니라 **도구가 쏟아내는 로그를 그대로 컨텍스트에 넣는 것**이다. [headroom](https://github.com/headroomlabs-ai/headroom)은 그 앞에 두는 **로컬 우선 컨텍스트 압축 레이어**다. 11/6 API 기준 **약 79,017★**, Apache-2.0, 최근 푸시 11/6.

## 무엇을 하나
- 압축 대상: 도구 출력, 로그, 파일, RAG 청크, 히스토리.
- 주장 수치(README): 코딩 에이전트 입력 **~20%↓**, JSON **60–95%↓**, “같은 답”.
- 붙이는 법: 라이브러리 / 프록시 / `headroom run -- claude`형 래핑 / **MCP 도구**.
- 설계 포인트: 압축만 하고 끝내지 않고 **가역 검색**으로 원문을 다시 꺼낼 수 있게 한다(상세는 레포 문서).

## 왜 중요한가
reader-signal의 **orca / headroom / harness 토큰 절약** 테마 직접 히트다. 모델 업그레이드 없이 청구서를 깎는 쪽이고, Conductor·Claude Code·MCP 스택 위에 **한 겹** 더 얹는 패턴이다.

## 주의
절감률은 워크로드·툴 출력 형태에 민감하다. “같은 답”은 벤치·블라인드 평가를 공개 README 한 줄로 단정하지 말고, 자기 에이전트 로그로 A/B 할 것. 스타 수는 급등할 수 있어 날짜를 함께 적을 것.
