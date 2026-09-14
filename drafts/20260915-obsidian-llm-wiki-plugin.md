---
title: "LLM Wiki × Obsidian — 임베딩 없이 위키링크 그래프로 묻는 플러그인"
date: 2026-09-15T07:50:00+09:00
category: "Second Brain"
slug: "obsidian-llm-wiki-plugin"
summary: "GD4AI/obsidian-llm-wiki. Karpathy LLM Wiki를 Obsidian 플러그인으로. Personalized PageRank 검색, 벡터DB 없음. 엔티티·컨셉 페이지, MinerU 인제스트, 16+ LLM 프로바이더. 로컬 퍼스트."
---

## 한줄 요약
[GD4AI/obsidian-llm-wiki](https://github.com/green-dalii/obsidian-llm-wiki)(별칭 Karpathy LLM Wiki 플러그인)는 노트·PDF·이미지·오피스를 **연결된 위키**로 컴파일하고, 질문 시 **임베딩/벡터DB 대신 Personalized PageRank**로 `[[위키링크]]` 그래프를 걷는다.

## 핵심 설계
Karpathy gist 패턴(원재료를 축적하지 말고 **위키 페이지로 컴파일·유지**)을 Obsidian 안에서 돌린다. 엔티티·컨셉 페이지 생성, 그래프 Q&A, 소스 페이지 인용, lint·Smart Fix, MinerU 기반 멀티포맷 인제스트, 16+ 프로바이더(Anthropic·OpenAI·Gemini·Ollama·LM Studio 등), UI/위키 출력 다국어. 유지보수에 DocTpoint가 2026-09부터 합류했다고 README가 적는다. 병행 흐름으로 [Ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki)(에이전트 스킬로 위키 성장), [captainyorgen/obsidian-second-brain](https://github.com/captainyorgen/obsidian-second-brain)(append가 아니라 **기존 페이지 재작성·모순 조정**)이 같은 테마를 확장한다.

## 왜 중요한가
사용자가 짓는 LLM Wiki와 직결된다. RAG가 끊는 “전체 볼트에 걸친 추론”을 **링크 그래프 + 컴파일**로 되찾자는 주장이다. funes가 *에이전트 세션 기억*이라면, 이 플러그인은 *지식 위키 편집기*다. 둘 다 “소유권 있는 마크다운/데이터”가 중심이다.

## 기억할 것
- 검색 엔진: PPR(그래프), 기본 가정은 로컬 퍼스트.
- 운영: 인제스트 게이트·중복 탐지·주간 lint가 위키 품질을 가른다.
