---
title: "세컨드 브레인 / PKM: Karpathy LLM Wiki 플러그인 1.28 — 노트 속 ‘스크린샷·다이어그램’도 위키의 근거가 된다"
date: 2026-10-08T07:02:00+09:00
category: "세컨드 브레인 / PKM"
slug: "karpathy-llm-wiki-1-28-images"
summary: "Obsidian용 Karpathy LLM Wiki 플러그인 v1.28.0: 노트에 박힌 이미지를 주변 문단과 함께 분석하는 옵션, 공급자별 커스텀 헤더(OpenCode 프리셋), 막힌 출처에서도 끊기지 않는 스트리밍, 태그 어휘 통일. 새 기능은 전부 기본 꺼짐, 기존 위키는 다시 쓰지 않는다."
---

## 한줄 요약
노트를 LLM이 관리하는 **연결된 위키**로 바꿔 주는 Obsidian 플러그인 **Karpathy LLM Wiki**가 **v1.28.0**을 냈다. 핵심은 하나 — **노트에 붙여 둔 이미지도 이제 ‘증거’로 읽힌다**([Obsidian Stats 릴리스 노트](https://www.obsidianstats.com/plugins/karpathywiki), [GitHub](https://github.com/green-dalii/obsidian-llm-wiki)).

## 무엇이 바뀌었나
- **이미지 분석(옵트인)**: 표를 캡처한 스크린샷, 문단을 설명하는 다이어그램처럼 **진짜 내용이 이미지에 있는** 노트가 많다. 설정을 켜면 노트 안의 로컬 이미지(`![[…]]`)를 **바로 옆 문단과 함께** 분석해, 시각 정보가 텍스트와 같은 위키 페이지에 들어간다. 이미지당 10MiB, 20MiB 묶음 전송, **원격 URL은 내려받지 않음**. 모델이 무엇을 봤는지 감사할 수 있게 ‘이미지별 근거’ 섹션을 남기는 옵션도 있다.
- **공급자별 커스텀 헤더**: 라우팅 헤더·테넌트 ID가 필요한 엔드포인트도 이제 연결 가능. OpenCode 프리셋과 `/v1/responses` 방식 변형 포함.
- **스트리밍 복구**: 일부 서비스가 브라우저 교차 출처 요청을 막아 답변이 ‘뱅글뱅글’만 돌던 문제 — 데스크톱 전송으로 재시도한다.
- **태그 어휘 하나로**: 프롬프트가 허용한 태그와 실제 저장 단계의 태그 목록이 달라 태그가 사라지던 문제를 통일.
- 출시 빌드에서 몰래 꺼져 있던 **ChatGPT 플랜(Codex OAuth) 로그인**도 이제 실제로 동작.

## 이 플러그인의 성격 (복습)
임베딩·벡터 DB를 쓰지 않는다. 내가 쓴 `[[위키링크]]` 그래프 위에서 **Personalized PageRank**로 관련 페이지를 찾는다. 원본 노트는 건드리지 않고 `wiki/` 폴더에만 새 페이지를 만든다. 한국어 포함 11개 언어 UI·출력, Ollama·LM Studio로 **완전 로컬** 운용도 가능.

## 왜 중요한가 (LLM Wiki를 만들 계획이라면)
세컨드 브레인의 맹점은 “캡처해 둔 이미지는 검색도, 연결도 안 된다”였다. 1.28은 그 구멍을 메운다. 다만 이미지 분석은 **비전 모델 호출 = 비용**이니, 먼저 한 폴더에서 켜 보고 근거 섹션으로 품질을 확인한 뒤 넓히자. 업그레이드는 Community plugins에서 클릭 한 번, **기존 위키 형식은 그대로**다.

출처: [Obsidian Stats — Karpathy LLM Wiki 1.28.0](https://www.obsidianstats.com/plugins/karpathywiki) · [GitHub 저장소](https://github.com/green-dalii/obsidian-llm-wiki)
