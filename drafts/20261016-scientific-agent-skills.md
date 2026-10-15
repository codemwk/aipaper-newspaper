---
title: "GitHub 트렌드: Scientific Agent Skills(~5만★) — 코딩 에이전트를 ‘AI 과학자’로, 177개 연구 스킬·100+ 데이터베이스가 뜨는 이유"
date: 2026-10-16T07:09:00+09:00
category: "GitHub 트렌드"
slug: "scientific-agent-skills"
summary: "K-Dense-AI/scientific-agent-skills(MIT, 10/16 기준 50,381★, 10/15 하루 +1,091★로 GitStock 트렌딩 3위): 생물·화학·의학·물리·지구과학·데이터분석 등 177개 스킬 + PubChem·ChEMBL·UniProt·ClinicalTrials.gov·FRED 등 100+ DB 사용법. 개방형 Agent Skills 표준이라 Cursor·Claude Code·Codex·Antigravity에서 공용. 스크립트 있는 스킬은 테스트 스위트 동봉. 같은 날 트렌딩엔 Anthropic 공식 플러그인 디렉터리·토큰 절약형 하네스들."
---

## 한줄 요약
10/15 GitHub 트렌딩에서 눈에 띈 건 “새 앱”이 아니라 **“에이전트에게 전문 분야 절차를 가르치는 문서 묶음”**이었다. **Scientific Agent Skills**는 하루 **+1,091★**로 GitStock 트렌딩 3위에 올랐고 10/16 기준 **50,381★**(MIT)다([GitStock](https://gitstock.org/trending) · [GitHub](https://github.com/K-Dense-AI/scientific-agent-skills)). 원래 이름은 ‘Claude Scientific Skills’였는데, 특정 모델 전용에서 **개방형 Agent Skills 표준**으로 넓히며 이름을 바꿨다.

## 무엇이 들어 있나 (쉽게)
- **스킬 = 에이전트용 실험 매뉴얼.** 각 스킬은 `SKILL.md` 한 장에 목적·작업 순서·버전을 적고, 필요하면 예제 코드·참고 문서·실행 스크립트·템플릿을 붙인다. 에이전트는 “단일세포 RNA 분석해 줘” 같은 요청을 받으면 해당 매뉴얼을 읽고 **그 분야의 관례와 검증 체크**대로 움직인다.
- **177개 스킬**: 유전체·단일세포, 신약 후보 스크리닝·ADMET, 질량분석, 임상시험·약동학, 현미경·의료영상, 신경과학, 재료·양자, 천문, 지리공간, 실험실 자동화, 논문 작성·피어리뷰·포스터까지.
- **100+ 데이터베이스**: PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, FRED, USPTO 등 — 어떤 엔드포인트를 쓰고 페이지를 어떻게 넘기고 출처를 어떻게 남길지까지 적었다.
- **품질 장치**: 스크립트가 있는 스킬은 `tests/` 아래 테스트 스위트가 따로 있고, 보안 스캔·스킬 테스트가 CI로 돈다. 의료 쪽은 “환자 개별 진단·처방 결정이 아니다” 같은 **사용 경계**를 스킬에 명시했다.
- 같은 팀의 **K-Dense BYOK**: 이 스킬들을 쓰는 데스크톱용 오픈소스 ‘AI 공동 과학자’. 자기 API 키로 40+ 모델 중 선택, 데이터는 내 컴퓨터에.

## 오늘 트렌딩이 말해 주는 것
같은 날 목록엔 **Anthropic 공식 Claude Code 플러그인 디렉터리**(claude-plugins-official, ~3.9만★), 이미 다뤘던 superpowers·ECC·context-mode·caveman 같은 **하네스·토큰 절약 도구**, 그리고 아래 XERJ가 함께 올랐다. 흐름은 뚜렷하다 — 모델 자체보다 **에이전트에 무엇을 ‘장착’하느냐**(스킬·플러그인·검색·메모리)가 인기의 중심이다. 그리고 그 장착물이 코딩을 넘어 **과학·의료·금융 같은 전문 도메인**으로 번지고 있다.

## 왜 중요한가
Agent Skills가 표준이 되면서 “좋은 절차서”는 한 번 쓰면 Cursor·Claude Code·Codex 어디서나 재사용된다. 연구자가 아니어도 시사점은 같다 — 내 업무 노하우(예: 브랜드 리서치 절차, 트레이딩 백테스트 점검표)를 **SKILL.md로 써 두는 것**이 곧 에이전트 생산성이다. 단, 250,000명 사용 같은 수치는 프로젝트 자체 표기다.

출처: [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · [GitStock Trending 2026-10-15](https://gitstock.org/trending) · [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
