---
title: "GitHub 트렌드: DeepSeek Harness(~245K★) 주변에 ‘생태계’가 붙기 시작 — claude-mem 13.34가 DSH·Pi 전용 기억 플러그인을 냈다"
date: 2026-10-07T07:08:00+09:00
category: "GitHub 트렌드"
slug: "deepseek-harness-claude-mem"
summary: "8/13 생성된 deepseek-ai/deepseek-harness는 ‘모든 것이 플러그인’ 구조의 MIT 에이전트 하네스로 별 약 24.5만 개. 10/6(미국 시간) 세션 기억 도구 claude-mem(~97K★) v13.34.0이 DeepSeek Harness·Pi 네이티브 통합을 추가하고, v13.34.2에선 프롬프트 캐시를 깨던 버그를 고쳤다."
---

## 한줄 요약
요즘 GitHub 상위권은 모델이 아니라 **‘하네스’**(모델을 감싸 도구·기억·권한·UI를 붙이는 실행 틀)가 차지한다. 그중 **DeepSeek Harness**가 별 **약 24.5만 개**까지 올라섰고, 이번 주엔 다른 인기 프로젝트가 **DSH 전용 플러그인**을 내기 시작했다. 하네스가 “앱”에서 **“플랫폼”**으로 넘어가는 신호다.

## DeepSeek Harness는 뭔가
- DeepSeek가 만든 **오픈소스(MIT) 에이전트 하네스**. 레포는 8월 13일 생성, 현재 전 세계 **퍼블릭 프리뷰**([GitHub](https://github.com/deepseek-ai/deepseek-harness), [소개 페이지](https://www.deepseek.com/en/harness/)).
- 설계 철학은 **“Everything is a Plugin”**(Cordis 프레임워크 기반): 모델·도구·스킬·세션·샌드박스·저장소·에이전트 루프·스케줄·**UI까지** 전부 갈아 끼울 수 있는 부품이다.
- **Creator mode**: 채팅으로 “뽀모도로 타이머 플러그인 만들어 줘” 하면 에이전트가 플러그인 코드를 쓰고 설치·검증까지 한다.
- 공식 실험 플러그인: 에이전트 팀, 자동 승인 리뷰, 예약 작업(“매주 금요일 17시 주간 보고서”), 음성 입력. 데스크톱 앱 또는 `npx`로 웹 UI.

## claude-mem 13.34 — “기억”이 하네스를 따라간다
**claude-mem**(~97K★)은 에이전트가 세션 중 한 일을 압축해 저장했다가 다음 세션에 필요한 것만 다시 넣어 주는 **장기 기억** 도구다.
- **v13.34.0**(10/6 UTC): **DeepSeek Harness·Pi 네이티브 통합**. `npx claude-mem install --ide dsh` 한 줄로 설치되고, 첫 턴 전에 작업 맥락을 주입하며 `mem_search`·`mem_timeline`·`mem_get_observations`·`mem_save`·`mem_context` 도구를 준다([릴리스](https://github.com/thedotmack/claude-mem/releases/tag/v13.34.0)).
- 세심한 기본값: 새로 켠 감시는 **기존 대화 기록 끝에서 시작** — 설치하자마자 과거 세션 전부를 몰래 빨아들이지 않는다. 비공개 프롬프트·제외 프로젝트는 캡처 안 함.
- **v13.34.2**: v13.29.0부터 이전 대화를 줄이려 메시지를 고쳐 쓰던 동작 때문에 OpenRouter·Gemini 등에서 **프롬프트 캐시 재사용이 깨지던** 문제를 수정했다. 다만 비용 절감 폭은 “측정 안 했다”고 명시.

## 왜 중요한가
같은 주간 트렌딩엔 ECC(~27.4만★), superpowers(~29.6만★), hermes-agent(~25.2만★)가 나란히 있다([AttentionVC](https://github.attentionvc.ai/trending/repos)). 하네스가 여러 개로 갈라질수록 **기억·스킬처럼 “어느 하네스에서든 따라오는 층”**의 가치가 커진다. 세컨드 브레인 관점에서도 핵심은 같다 — **도구를 바꿔도 기억은 내 것으로 남아야** 한다.

## 체크포인트
- 별 개수는 화제성 지표이지 품질 보증이 아니다. DSH는 아직 **프리뷰**, claude-mem의 DSH 통합은 worker 런타임에서만 동작.
