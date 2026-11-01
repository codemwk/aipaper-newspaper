---
title: "GitHub 트렌드: DeepSeek dsh-superagent — ‘세션 하나에 사람 하나’를 깨는 라우터·워커 코딩 에이전트. 공개 이틀 만에 ★7천"
date: 2026-11-02T07:05:00+09:00
category: "GitHub 트렌드"
slug: "deepseek-dsh-superagent"
summary: "DeepSeek Harness 팀이 10/31 MIT 연구 프로토타입 dsh-superagent를 공개했다. GitHub(선택적으로 Feishu)를 듣다가 허가된 사람의 요청을 ‘티켓’으로 만들고, 티켓마다 격리된 워커 세션이 작업해 PR로 돌려준다. 자발적 작업은 기본 observe(기록만). 시뮬레이션 p95 15.7분 vs 단일 세션 29.5분. 실제 코드 품질은 측정 안 함."
---

## 한줄 요약
지난번 저장하신 DeepSeek Harness·메신저→PR 워크플로(LYIO) 관심과 이어지는 소식이다. DeepSeek는 **병목은 모델이 아니라 사람의 주의력**이라고 보고, 한 사람이 세션 3~5개를 쫓아다니는 구조를 바꾸려 한다([GitHub](https://github.com/deepseek-ai/dsh-superagent-prototype/), [MarkTechPost](https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/)).

## 어떻게 일하나 (코드 없이)
1. **라우터**(상시 실행): GitHub 이슈·PR 댓글, 선택적으로 Feishu 채팅을 듣는다.
2. 허가된 사람이 부르면 **티켓**을 연다. 티켓엔 “왜 진행해도 되는가”를 적은 변경 불가 위임장(Mandate)이 붙는다.
3. 티켓마다 **격리된 워커 세션·디렉터리**가 작업 → 결과는 원래 대화로, 대개 **PR**로 돌아온다.
4. 이후 PR 댓글은 다시 멘션하지 않아도 해당 워커로 전달.
5. 원칙: 한 번 확인하고, 작업 중엔 조용히, **결과·질문·실패**일 때만 말한다. 로컬 웹 패널엔 사람이 봐야 할 것만.

## 안전장치와 한계
- 자발적 작업은 `off` / `observe`(기본, 하려던 일만 기록) / `auto` 3단계.
- 내 PC에서 OS 사용자 권한 그대로 돈다 → **격리 환경 권장**. Node 22.19+, git, tmux, GitHub CLI 필요.
- 성능: 메시지 약 300개(진짜 요청 약 20개) 시뮬레이션에서 p95 **15.7분 vs 29.5분**(단일 세션+서브에이전트). 단, 합성 메시지·모의 도구 기준이고 **실제 코딩 품질은 측정하지 않았다**.

## 왜 중요한가
- Copilot·Claude Code Action이 ‘불러야 오는 비서’라면, 이건 **팀 채팅방에 상주하는 동료** 모델이다. 메신저→티켓→PR 흐름을 오픈소스로 뜯어볼 수 있는 첫 레퍼런스 중 하나.
- 생성 10/31, 11/2 기준 ★약 7,000. 연구 프로토타입이니 운영 투입보다 **설계 문서(라우터/워커, 위임장, observe 모드)**를 내 하네스에 빌려오는 용도가 현실적이다.
