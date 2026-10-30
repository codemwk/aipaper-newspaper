---
title: "AI 모델: Clover-35B-A3B — 한 글자씩이 아니라 ‘블록째’ 써 내려가는 확산 언어모델, Apache 라이선스로 공개. 에이전트 작업에서 초당 680토큰"
date: 2026-10-31T07:03:00+09:00
category: "AI 모델"
slug: "clover-diffusion-moe"
summary: "Dream 7B를 만든 홍콩대 출신 팀 DiffuSpace가 10/30 확산(diffusion) 방식 MoE 언어모델 Clover-35B-A3B-Preview를 Apache 라이선스로 공개했다(총 35B, 활성 3B, 사고 모드 지원). 회사 발표로 SWE-bench Verified 73.6, Terminal-Bench 2.1 51.7로 같은 크기의 Qwen3.6-35B-A3B보다 높고, GB300 한 장에서 에이전트 작업 초당 680토큰. INT4로 16GB RTX 5070 Ti에서도 돈다."
---

## 한줄 요약
보통 언어모델은 **한 토큰씩 순서대로** 쓴다. Clover는 **한 블록을 통째로 놓고 노이즈를 걷어내듯 동시에** 채운다. 그 결과 “빠른데 똑똑하기도 하다”를 35B급에서 보여 주겠다는 모델이다([DiffuSpace 블로그](https://ofia-docs.france-ioi.org/huggingface/blog/Diffuspace/clover-35b-a3b-preview)).

## 스펙 (회사 발표)
| 항목 | 내용 |
|---|---|
| 구조 | MoE 확산 언어모델, 총 35B / 활성 3B, 사고 모드 |
| 라이선스 | **Apache**, 가중치·코드 Hugging Face·GitHub·ModelScope |
| 추론 지원 | SGLang, llama.cpp |
| 속도 | GB300 1장 에이전트 작업 **680 tok/s**, H200에서 515 tok/s(비교 설정 365) |
| 로컬 | INT4로 **RTX 5070 Ti 16GB**에서 MATH-500 101.8 tok/s |
| 점수 | SWE-bench Verified 73.6, Terminal-Bench 2.1 51.7, GPQA Diamond 83.8 |

## 에이전트에게 속도가 왜 중요한가
- 에이전트는 “판단 → 실행 → 결과 보기 → 수정”을 수십 번 반복한다. 한 단계가 빨라지면 같은 시간에 **더 많은 경로를 시도**할 수 있다.
- 데모 예: 웹 도구로 6가지 업무(송장 작성·수강 신청 등)를 처리하는 49개 과제에서 **중앙값 1.52초**, Gemini 3.6 Flash는 8.86초(회사 측정).

## 덤: ‘여러 판단을 한 번에’ 내리는 결정 모델 예고
- Clover 기반 결정 모델을 **나중에 공개** 예정. 같은 자료에 대한 관련 질문 최대 8개를 **한 번의 생성에서 동시에** 답하는 ‘Joint Mode’가 특징 — 계약서의 “통지가 기한 내였나”와 “보증금을 돌려줘야 하나”처럼 서로 얽힌 판단이 모순되지 않게 한다.

## 주의할 점
- 모든 수치는 **회사 자체 측정**이고, 이름 그대로 **Preview**다. 독립 벤치마크는 아직 없다.

## 왜 중요한가
- 10/20 다룬 Mercury 3에 이어 **확산 언어모델이 오픈웨이트·로컬 GPU 영역으로** 들어왔다. 16GB 그래픽카드에서 도는 빠른 코딩·도구 사용 모델은 개인 에이전트 실험에 바로 쓸 수 있는 선택지다.
