---
title: "Grok Voice Transcribe 2.0 — 정확도 2배 주장, 가격은 그대로 $0.10/$0.20"
date: 2026-09-20T07:26:00+09:00
category: "AI Content Gen"
slug: "grok-voice-transcribe-20"
summary: "xAI(SpaceXAI) 공식. STT 2.0이 1.0 대비 실환경 정확도 대폭 개선(단기 다국어 명령 WER 20.6%→6.8%). Artificial Analysis 스트리밍 32모델 정확도 1위 주장. 배치 $0.10·스트리밍 $0.20/오디오시. Loom→Cursor 워크플로 사례."
---

## 한줄 요약
[xAI 발표](https://x.ai/news/grok-voice-transcribe-2)에서 **Grok Voice Transcribe 2.0**이 나왔다. 요금은 1.0과 동일하고, 정확도·다국어·실전화 오디오를 전면에 내세웠다.

## 지금 뭐가 뜨나
- **가격 동결**: 배치 **$0.10/오디오시**, 스트리밍 **$0.20/오디오시**. 화자분리·워드 타임스탬프·키텀 바이어싱 포함.
- **정확도 메시지**: 사내 평가에서 1.0 대비 “약 2배 정확”, 단기 다국어 보이스 커맨드 WER **20.6% → 6.8%**. Artificial Analysis 스트리밍 보드에서 **32모델 중 정확도 1위**라고 인용.
- **기능**: 자동 언어 감지·중도 언어 전환, 최대 8채널, 필러 제거, 스마트 턴 디텍션(보이스 에이전트용).
- **현장 사례**: Atlassian Loom이 영상 STT를 2.0으로 교체. “Loom 녹음 → 트랜스크립트 → Cursor가 코드 반영” 루프를 SVP 코멘트로 강조.
- 곧 STT API 기본값이 2.0으로 바뀌고 1.0은 수주 내 deprecate. 고정이 필요하면 `grok-voice-transcribe-1.0` 핀.

## 왜 중요한가
콘텐츠·고객지원·에이전트 파이프라인에서 **STT는 ‘싼 전처리’가 아니라 병목**이다. 가격을 올리지 않고 품질만 올리는 쪽은, 트랜스크립트→에이전트 코딩·위키 인제스트 같은 **다운스트림 AI** 단가를 바로 낮춘다.

## 기억할 것
- [Introducing Grok Voice Transcribe 2.0](https://x.ai/news/grok-voice-transcribe-2)
