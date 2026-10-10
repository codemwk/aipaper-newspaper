---
title: "GitHub: google/skills — GCP·에이전트 플랫폼 ‘스킬 팩’이 2.1만★, npx skills add 한 줄로 에이전트에 꽂는다"
date: 2026-10-11T07:05:00+09:00
category: "GitHub"
slug: "google-skills-agent-repo"
summary: "google/skills(~21.1K★)는 Google Cloud·Agent Platform·Genkit 등용 Agent Skills 모음. npx skills add google/skills로 설치. IAM·GKE 추론·RAG·에이전트 배포 레시피까지 ‘문서가 아니라 에이전트가 읽는 절차’로 묶인다."
---

## 한줄 요약
Google이 **Agent Skills** 규격에 맞춘 공식 스킬 저장소 **[google/skills](https://github.com/google/skills)**를 공개·확장하고 있다. 2026-10-11 기준 스타 **약 2.11만**. 설치는 `npx skills add google/skills` — 에이전트(프로젝트/글로벌)에 **GCP 작업 절차**를 붙이는 형태다.

## 무엇이 들어 있나 (README 기준)
- **온보딩·IAM·Foundation Builder** 등 Cloud 시작 레시피.
- **멀티프로덕트 솔루션**: 에이전트 게이트웨이 보안, 에이전틱 분석, 보더리스 레이크하우스, GKE Inference 마이그레이션, AlloyDB 하이브리드 검색·RAG 등.
- **Agent Platform**: 엔드포인트·레지스트리·튜닝·프롬프트·RAG 엔진·Eval 플라이휠·알림.
- **Genkit** Dart/Go/JS/Python 개발 스킬, Gemini API·LiveAPI, GKE TPU 진단.

코드 덤프가 아니라 **“이 작업을 할 때 에이전트가 따를 체크리스트·워크플로”**다. Framer Skills·Claude 스킬과 같은 **지시 자산화** 흐름의 클라우드 버전.

## 왜 중요한가
에이전트 생산성은 모델보다 **도메인 스킬 라이브러리**에 달려 있다. Google이 자사 콘솔 지식을 skills.sh 생태계로 내보내면, Cursor·Claude Code 사용자가 **할로시네이션 적은 GCP 런북**을 공유 포맷으로 가져갈 수 있다. 반대로 스킬이 틀리면 **자신 있게 잘못된 인프라**를 만들 위험도 커진다 — 리뷰·버전 고정이 필수다.

출처: [google/skills](https://github.com/google/skills) · [agentskills.io](https://agentskills.io/home)
