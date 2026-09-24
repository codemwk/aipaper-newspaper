---
title: "Second Brain: Tencent WeKnora — RAG·에이전트·Wiki를 한 지식 베이스에"
date: 2026-09-25T07:09:00+09:00
category: "Second Brain / PKM"
slug: "tencent-weknora-knowledge"
summary: "Tencent/WeKnora(~29.7k★, MIT, v0.8.x). 오픈소스 LLM 지식 프레임워크: 문서→쿼리 가능 RAG, 자율 추론 에이전트, 자기유지 Wiki. weknora.weixin.qq.com."
---

## 한줄 요약
[WeKnora](https://github.com/Tencent/WeKnora)는 텐센트가 공개한 **LLM 지식 플랫폼**이다. 같은 지식 베이스 위에서 **RAG 검색 → 멀티스텝 에이전트 → Wiki 정리**를 돌린다. README 한 줄: find the answers, and put knowledge to work.

## 어떻게 동작하나
- 팀 문서를 모아 시맨틱 검색·추론·최신성 유지.
- **세 모드가 한 KB를 공유**: RAG로 찾기, 에이전트로 다단계 태스크, Wiki로 지식 구조화.
- 웹(weknora.weixin.qq.com), Chrome 확장, ClawHub 스킬, npm 패키지 등 클라이언트 확장.
- 라이선스 MIT, 릴리즈 v0.8.x대(README 배지 기준).

## 왜 중요한가
어제 kepano/obsidian-skills·ai-memory가 “볼트·에이전트 메모리”였다면, 오늘은 **엔터프라이즈형 오픈 지식 런타임**(RAG+에이전트+위키) 신호다. LLM Wiki 계열 관심과 직결: “검색만”이 아니라 **유지·재작성되는 위키**.

## 기억할 것
- [GitHub](https://github.com/Tencent/WeKnora) · [사이트](https://weknora.weixin.qq.com) · [Docs](https://weknora.weixin.qq.com/docs/)
