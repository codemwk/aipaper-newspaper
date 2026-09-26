---
title: "AI 모델: Claude Science — N=4 SYM 9루프 진폭, ‘수천 달러·수일’로 프론티어 계산"
date: 2026-09-27T07:09:00+09:00
category: "AI 모델"
slug: "claude-science-nine-loops"
summary: "Anthropic(2026-09-25): Claude Science(Fable 5.1)가 planar N=4 SYM 6입자 MHV 9루프 진폭을 부트스트랩·폼팩터 두 경로로 계산. 엔드유저 비용 대략 $1–2천. SLAC Lance Dixon 검증. 신이론이 아니라 알려진 방법의 자율 실행."
---

## 한줄 요약
[Anthropic 게스트 포스트(2026-09-25)](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)에서 물리학자 Matt von Hippel은 자신이 던진 챌린지 — **N=4 super Yang-Mills 9루프** — 를 Claude Science가 해결했다고 전한다. 한 문장 과제 + “잠자는 동안 계속” 지시로, **대략 수천 달러·수일** 규모. SLAC의 Lance Dixon이 검증했다.

## 사실만 정리
- **무엇**: planar N=4 SYM, six-particle(hexagon) MHV amplitude at **nine loops**.
- **어떻게**: Claude Science 하네스 + Fable 5.1. 부트스트랩 직접 경로와 form-factor 간접 경로 모두. SymPy 등 코드는 모델이 작성.
- **비용 감각**: 경로당 엔드유저 **약 $1,000–$2,000**(대부분 모델 가동). CPU 주 단위(~96 CPU·1주)는 예산의 일부(~$100대)로 언급.
- **의미의 한계(저자·Dixon)**: 새 물리 원리가 아니라 **기존 레시피의 완주**. Song He 그룹도 GPT-6 보조로 심볼 일부를 거의 동시에 완성. “머신에 스쿱당했다”는 감정보다 **검증 가능 산출물**이 핵심.

## 왜 중요한가
에이전트 하네스(규칙·장기 루프·도구)가 “코딩 보조”를 넘어 **전문가급 계산 실행**에 닿았다는 신호다. 동시에 OpenAI 이탈 사고와 나란히 두면, **능력과 통제가 같은 달에 충돌**하는 그림이 된다.

## 기억할 것
- [Anthropic: Yes, Claude can do Nine Loops](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)
