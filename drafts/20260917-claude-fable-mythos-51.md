---
title: "Claude Fable 5.1 · Mythos 5.1 — 코딩·지식노동 최전선, 캐시 읽기값 ↓"
date: 2026-09-17T07:25:00+09:00
category: "AI Models"
slug: "claude-fable-mythos-51"
summary: "Anthropic 2026-09. Fable 5.1 일반 공개, Mythos 5.1은 사이버·생명과학 Trusted Access. 동일 가중치·다른 가드레일. 캐시 리드 75% 인하, EFS·제로 리텐션 경로."
---

## 한줄 요약
[Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-1)은 **Claude Fable 5.1**(일반)과 **Mythos 5.1**(신뢰 접근)을 공개했다. 같은 모델, **사이버·생명과학 가드레일 강도만 다름**.

## 무엇이 달라졌나
- 코딩·지식노동·장시간 문제해결 성능 강조. Terminal-Bench-Science 0.1 **52.6%**, Terminal-Bench 4.0 **55.8%**(Mythos는 **60.9%**), CursorBench 3.2.0 **73.4%** 등 자사 표.
- **가격**: 캐시 리드 **75% 인하**($0.25/M). 전형 워크로드 약 **25%**, 고에이전틱은 최대 ~**45%** 절감 추정. 입·출력은 Fable 5와 동일($10 / $50 per M).
- **EFS**(Enterprise Frontier Safeguards): 고객 클라우드에 모니터링 데이터 보관. 가을 단계 롤아웃 전까지 적격 고객 **제로 데이터 리텐션**.
- Fable는 취약점 **발견**은 허용, **익스플로잇 개발**은 제한. 사이버 가드레일 오탐 약 **60%** 감소 주장.
- Mythos: Cyber Verification Program · Life Sciences Verification Program. Claude Security도 Mythos 5.1 기반.
- API ID: `claude-fable-5-1`. AWS·GCP·Azure 포함.

## 왜 중요한가
어제 GPT-Live·Agents API 소식을 봤다면, 오늘은 **Anthropic 쪽 주력 코딩 모델 세대**다. “비싸서 Opus만 돌리던” 에이전트 루프를 Fable급으로 내릴 수 있는지, 캐시 가격이 관건. Mythos는 방어 보안·랩 연구용 **별도 문**이다.

## 기억할 것
- 발표: [Claude Fable & Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 시스템 카드·EFS: 동 페이지 및 [Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards)
