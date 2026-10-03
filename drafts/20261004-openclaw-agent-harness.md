---
title: "GitHub 트렌드: openclaw — ‘모델이 아니라 하네스’가 트렌딩 정상, 셀프호스트 퍼스널 에이전트"
date: 2026-10-04T07:08:00+09:00
category: "GitHub 트렌드"
slug: "openclaw-agent-harness"
summary: "github.com/openclaw/openclaw(~391k★ 조회 시점). 로컬 퍼스널 AI 어시스턴트·게이트웨이·채널·스킬·메모리. top10.dev: 트렌딩 상위가 모델이 아닌 하네스 레이어라는 신호."
---

## 한줄 요약
[openclaw/openclaw](https://github.com/openclaw/openclaw)는 “Any OS. Any Platform. The lobster way.”를 내건 **셀프호스트 퍼스널 AI 어시스턴트**다. 조회 시점 GitHub 별 **약 39만+**. [top10.dev 정리](https://top10.dev/story/two-of-githubs-top-three-trends-are-agent-harnesses-not-models-2017)대로, 주간 트렌딩 상단을 **모델 체크포인트가 아니라 하네스**(스킬·메모리·보안 정책·툴 라우팅·채널)가 차지하는 패턴이 뚜렷하다. 가치는 특정 LLM 벤더에 묶이지 않는 **실행·정책 레이어**.

## 실무로 보면
- **Gateway**: 세션·툴·이벤트·메신저 채널의 컨트롤 플레인. 에이전트 하네스는 준비된 턴을 실행하는 저수준 executor.
- **워크스페이스**: 로컬 파일·브라우저·셸·메모리를 한곳에 — “채팅창 너머 실제로 하는 AI”.
- **선택 기준**: 별 수보다 **채널 allowlist·샌드박스·스킬 설치 경로**를 README에서 먼저 확인할 것(대규모 스타 레포는 공급망·권한 면 점검 필수).

## 왜 중요한가
어제 OpenHarness/ohmo에 이어, 생태계 메시지가 동일하다: **모델을 갈아끼우는 비용 < 하네스를 다시 짜는 비용**. 코딩 에이전트·퍼스널 OS 모두 “portable wrapper”가 패키지 생태계처럼 굳는 중.

## 기억할 것
- [openclaw/openclaw](https://github.com/openclaw/openclaw) · [top10.dev harness trend](https://top10.dev/story/two-of-githubs-top-three-trends-are-agent-harnesses-not-models-2017)
