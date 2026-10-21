---
title: "AI 모델: Recursive ‘Flint’ — “AI가 거의 다 만든” 노트북용 코딩 모델, 400억 중 25억만 일하고 Apache 2.0 무료 공개"
date: 2026-10-22T07:08:00+09:00
category: "AI 모델"
slug: "recursive-flint-laptop-coder"
summary: "‘스스로 개선하는 AI’를 표방한 Recursive(CEO 리처드 소처, 5월 $6억 5,000만·기업가치 $46억 5,000만 투자)가 10/21 첫 모델 Flint 공개. 39.8B 파라미터 MoE 중 토큰당 약 2.5B만 활성, 문맥 262,144토큰, 지식 기준 2026-06, Apache 2.0(Hugging Face). 자동 연구 시스템 ‘Eureka Machine’이 사전학습~추론 최적화 거의 전 단계에 기여해 소규모 팀이 4개월 안에 처음부터 학습했다고 주장(저비트 학습으로 크기 71%↓). 회사 측정: M4 Pro 맥북프로에서 초당 약 131토큰(비슷한 모델 58~69), SWE-bench Verified 74.2%, Terminal-Bench 2.1 54.9%. 큰 작업은 잘게 나눠 줘야 한다고 회사도 인정. BF16 체크포인트는 약 80GB, 맥·엔비디아용 양자화판은 별도."
---

## 한줄 요약
‘AI가 AI를 만든다’는 말은 보통 먼 미래 얘기였다. Recursive는 그걸 **노트북에서 도는 코딩 모델**이라는 아주 실용적인 형태로 내놨다([TechCrunch](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/), [Hugging Face](https://huggingface.co/RecursiveSI/flint)).

## 무엇인가
- **누가**: 작년 설립된 Recursive. 5월에 GV·엔비디아·AMD Ventures 등에서 **$6억 5,000만(기업가치 $46억 5,000만)** 을 받고 등장했다. CEO는 전 Salesforce 수석 과학자 **리처드 소처**.
- **크기**: 전체 **398억** 파라미터 중 토큰마다 약 **25억**만 쓰는 전문가 혼합(MoE). 문맥은 **262,144토큰**, 지식 기준 시점 2026년 6월.
- **라이선스**: **Apache 2.0** — 무료로 내려받아 수정·상업 이용 가능. 클라우드가 아니라 **내 컴퓨터**에서 돌리니 오프라인 사용, 코드 비공개 유지, 토큰 요금 없음.
- **어떻게 만들었나**: 자동 연구 시스템 **‘Eureka Machine’** 이 아이디어를 내고 실험하고 결과로 다음 실험을 정하는 식으로, 사전학습부터 추론 최적화까지 거의 전 단계에 참여했다고. 덕분에 작은 팀이 **4개월 안에 처음부터** 만들었고, 저비트 학습으로 모델 크기를 **71% 줄였다**고 회사는 말한다.

## 숫자(모두 회사 측정)
| 항목 | 수치 |
|---|---|
| 속도(M4 Pro 맥북프로) | 초당 약 **131토큰** (비슷한 모델 58~69) |
| 속도(엔비디아 RTX Spark) | 초당 150토큰 이상 |
| SWE-bench Verified | 74.2% |
| Terminal-Bench 2.1 | 54.9% (웹 검색으로 얻은 답은 실패 처리) |

Wired의 윌 나이트는 메모리 48GB 맥에서 할 일 앱·웹 리서치 도구 등을 만들어 봤고, 작은 코딩 모델치고 요청을 매번 해냈다고 평했다(TechCrunch 인용).

## 현실 체크
- 회사도 “대형 유료 코딩 비서보다 **더 많은 안내가 필요**하다, 큰 작업은 작은 단계로 나눠라”고 인정했다.
- Hugging Face의 BF16 원본은 약 **80GB**이고 공식 서빙 키트는 B300/H200 GPU 기준이다. 노트북에선 **별도로 준비되는 양자화판**(애플 실리콘·엔비디아용)을 써야 한다.
- “AI가 만든 AI”는 아직 **사람이 감독하는 연구 보조** 수준이다. 재귀적 자기개선이 통제를 벗어날 수 있다는 우려가 업계의 큰 논쟁거리라는 점도 TechCrunch는 짚었다.

## 왜 중요한가
지난주 Meta의 Muse Spark Open(816B, 메모리 1TB 이상)과 정반대 방향이다. **“충분히 좋은 코딩 에이전트를 내 노트북에서, 공짜로”** 는 구독료·데이터 유출이 걱정인 개인·소규모 스튜디오에 현실적인 선택지다. 오늘 소개한 ai-memory 같은 도구로 Claude Code ↔ 로컬 모델 사이 인수인계를 붙이면, 비싼 작업은 클라우드, 반복 작업은 Flint로 나누는 구성도 가능하다.

출처: [TechCrunch (10/21)](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/) · [Hugging Face — RecursiveSI/flint](https://huggingface.co/RecursiveSI/flint) · [Recursive — Introducing Flint](https://recursive.com/updates/introducing-recursive-flint)
