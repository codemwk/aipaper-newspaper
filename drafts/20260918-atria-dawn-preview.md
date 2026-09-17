---
title: "Atria Dawn Preview — 상하이AI랩 744B MoE 에이전트 모델, MIT로 조용히 공개"
date: 2026-09-18T07:25:00+09:00
category: "AI Models"
slug: "atria-dawn-preview"
summary: "HF 2026-09-11 업로드·카드 갱신. Shanghai AI Lab InternLM org의 Atria-Dawn-Preview. GLM-5.2 계열 744B MoE, 컨텍스트 256K, MIT. Discovery·Creation·Delivery·Cyber 네 축. BF16·FP8 체크포인트·API 콘솔."
---

## 한줄 요약
[Hugging Face `internlm/Atria-Dawn-Preview`](https://huggingface.co/internlm/Atria-Dawn-Preview)(업로드 **2026-09-11**, 카드·아카이브 갱신 지속)와 arXiv [2609.15818](https://arxiv.org/abs/2609.15818)(**2026-09-14** 제출) 기준, 상하이 AI Lab은 **Atria Dawn Preview**를 공개했다. **744B** MoE 기반의 **에이전틱** 지시 모델이다.

## 무엇이 바뀌었나
- 카드 표현: GLM-5.2 파운데이션 위 **에이전트형** 프리뷰. 목표를 **실행·검증·재현 가능한 결과**로 밀어붙이는 루프(분석→설계→도구→코드→실험→복구).
- 네 축: **Discovery**(딥리서치·실험 계획), **Creation**(소프트웨어·시각화·ML), **Delivery**(문서·발표 산출물), **Cybersecurity**(인가 환경에서의 취약점 검증·패치).
- 컨텍스트 **256K**(카드 표 기준). BF16 풀 체크포인트와 **FP8** 양자화본. 라이선스 **MIT**. Hugging Face·ModelScope.
- 벤치(벤더 보고): BrowseComp 92.5, CyberGym 86.5, DeepSearchQA 96.0 등. SWE-bench Pro 59.6·Terminal-Bench 2.1 78.3은 클로즈드 플래그십 대비 중위권으로 카드 자신이 보여 준다. **독립 재현은 아직 부족**하다고 보는 게 맞다.
- 배포: SGLang `v0.5.13.post1+`, vLLM `v0.23.0+`. 카드에 **지역별 API 콘솔** 링크. 텍스트 전용(이미지 입력 거부)이라고 명시.

## 왜 중요한가
9월 초 Claude Fable·GPT-6 Astra·Gemini 3.8 파동 다음에, **중국 랩의 초대형 오픈 가중치 에이전트**가 ‘발표문 없이 카드부터’ 뜨는 패턴이다. 로컬·사내 서빙이 가능한 MIT 744B급은 연구·보안 평가용으로 의미가 크고, 일상 앱 사용자에게는 **호스팅/가격이 열릴지**가 다음 신호다.

## 기억할 것
- [HF 모델 카드](https://huggingface.co/internlm/Atria-Dawn-Preview) · [논문 2609.15818](https://arxiv.org/abs/2609.15818)
- 숫자·벤치는 **벤더 표** — 파이프라인에 넣기 전 자체 평가 권장
