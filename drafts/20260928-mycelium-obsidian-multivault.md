---
title: "Second Brain: Mycelium for Obsidian — 볼트는 나누고, AI 운영면은 하나로"
date: 2026-09-28T07:09:00+09:00
category: "세컨드 브레인"
slug: "mycelium-obsidian-multivault"
summary: "Wicked-Evolutions Mycelium. 멀티볼트 로컬 MCP. ~102툴(문서: 74는 앱 종료 시에도, 28은 Obsidian CLI). 교차 검색·위키링크 유지 편집·헬스. 시맨틱은 로컬 Ollama. kepano skills와 다른 ‘운영 레이어’."
---

## 한줄 요약
[Mycelium for Obsidian](https://wicked-evolutions.github.io/Mycelium-for-Obsidian/)은 **브랜드·클라이언트·아카이브·개인**처럼 볼트를 나눈 채, AI에는 **하나의 로컬 MCP 운영면**을 준다. “전부 한 볼트로 합쳐야 에이전트가 찾는다”는 함정을 피한다. 어제 Karpathy LLM Wiki 스택·kepano skills와 겹치지 않는 축은 **멀티볼트 운영**이다.

## 구조 (사이트·README 요약)
- **로컬 퍼스트**: 노트는 디스크 마크다운. 임베딩(옵션)은 **로컬 Ollama**. 무엇이 밖으로 나가는지는 연결한 AI 클라이언트에 달림.
- **툴 티어**: 사이트 기준 약 **102툴** — 다수는 Obsidian 종료 상태에서도 파일시스템으로 동작, 일부는 Obsidian 1.12+ CLI가 켜져 있을 때.
- **하는 일**: 전 볼트 검색(텍스트·태그·프론트매터·의미), 섹션/프로퍼티 단위 편집, 위키링크 유지 이동·이름변경, orphan·깨진 링크·헬스.
- **실측 예시(사이트)**: 16볼트·6,201노트 코퍼스에서 관련 노트만 깊게 읽고(~0.16%) 인용 합성 — 시맨틱 티어 없이도 렉시컬로 완주한 사례로 제시.

## 왜 중요한가
퍼스널 OS·LLM Wiki를 키울수록 **단일 거대 볼트**는 권한·노이즈·백업이 무거워진다. Mycelium은 “사람은 경계를 유지, 에이전트는 교차 운영” 패턴이다. `npx`/`OBSIDIAN_VAULTS` JSON으로 볼트 맵을 넘기는 설정이 핵심.

## 기억할 것
- [사이트](https://wicked-evolutions.github.io/Mycelium-for-Obsidian/) · [GitHub](https://github.com/Wicked-Evolutions/Mycelium-for-Obsidian)
