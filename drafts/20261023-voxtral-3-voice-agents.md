---
title: "AI 콘텐츠: Mistral Voxtral 3 — 받아쓰기 분당 $0.0035, 음성 합성 100만 자당 $13, ‘듣고-생각하고-말하는’ 음성 에이전트를 통화 한 턴 1초 안에"
date: 2026-10-23T07:06:00+09:00
category: "AI 콘텐츠"
slug: "voxtral-3-voice-agents"
summary: "Mistral이 10/20 Voxtral 3(공개 프리뷰) 발표: 받아쓰기 Voxtral Small/Mini Transcribe 3(50개+ 언어, 화자 분리, 키워드로 정확도 높이는 context biasing, 말 끝 감지), 실시간 Mini Transcribe Realtime 3(500ms 미만), 음성 합성 Voxtral Mini TTS 3(35개+ 언어·50개+ 방언, 감정·속도·강조 지시, 한국어 프리셋 포함). LiveKit 기반 음성 에이전트 SDK — 각 턴 1초 미만, 끼어들면 멈춤, SIP 전화·WebRTC. Pro Voice는 30분 음성으로 화자 특성 재현. 가격: Mini 받아쓰기 $0.0035/분, 실시간 $0.008/분, Small $0.0040/분, TTS $13/100만 자, 음성 에이전트 API $0.04~0.08/분. EU 호스팅 또는 자체 서버 배포. 성능 비교는 Mistral 자체 평가 포함."
---

## 한줄 요약
Mistral이 음성 제품군 **Voxtral 3**를 냈다. 받아쓰기(STT)·음성 합성(TTS) 모델에 더해, 이를 하나로 엮는 **음성 에이전트 SDK**까지 묶었다. 콜센터·예약 봇·핸즈프리 비서를 겨냥한다([Mistral 발표, 10/20](https://mistral.ai/news/voxtral-3/), [변경 로그](https://docs.mistral.ai/resources/changelogs)).

## 구성
| 모델 | 하는 일 | 가격 |
|---|---|---|
| Voxtral Mini Transcribe 3 (4B) | 일괄 받아쓰기 | **$0.0035/분** |
| Voxtral Small Transcribe 3 | 고정밀 받아쓰기·화자 분리 | $0.0040/분 |
| Voxtral Mini Transcribe Realtime 3 | 실시간(500ms 미만) | $0.008/분 |
| Voxtral Mini TTS 3 | 음성 합성 | **$13 / 100만 자** |
| 음성 에이전트 API | 듣기+추론(Mistral Small 4)+말하기 | $0.04/분(큰 모델 $0.08) |

## 눈여겨볼 기능
- **context biasing**: 전문 용어·사람 이름 목록을 주면 받아쓰기가 그 단어를 더 잘 잡는다(미세조정 불필요).
- **말 끝 감지**: 소리와 의미를 함께 보고 상대가 말을 끝냈는지 판단 → 덜 끊고 빨리 답한다.
- **TTS 감정 지시**: `emotion`·`pacing`·`emphasis` 값으로 톤 조절, 특이한 이름은 발음 기호 힌트로 교정. 음성 프리셋 18개 언어에 **한국어 포함**.
- **Pro Voice**: 약 **30분 음성**으로 화자의 말투·감정 폭까지 재현(전문용). 
- **에이전트 SDK**(LiveKit 기반): 듣기·생각·말하기가 서로를 기다리지 않는 스트리밍 구조로 **턴당 1초 미만**, 사용자가 끼어들면 바로 멈춘다. 전화(SIP)·브라우저(WebRTC) 지원.
- **배포**: Mistral의 EU 호스팅 API 또는 자체 서버. 음성 보관 여부를 직접 통제.

성능은 Whisper·ElevenLabs Scribe v2·Gemini 3.5 Transcribe보다 낫다고 주장하지만, TTS 비교 상당수는 **Mistral 내부 평가**(심사 모델 사용)라 참고만 하자.

## 왜 중요한가
음성은 가격이 빨리 무너지는 분야다. 1시간 받아쓰기가 약 **$0.21**이면, 회의 녹음·팟캐스트 자막·음성 메모 정리를 “비용 걱정 없이 전부 돌리는” 구간에 들어선다. 실제로 Obsidian 플러그인 **Voxtral Transcribe 1.18.0**이 바로 Voxtral 3로 옮겨 가며 볼트 안의 이름·용어를 받아쓰기에 반영하기 시작했다([synon Obsidian×AI 데일리 10/22](https://synon.co.jp/article/news/2026-10-22-obsidian-ai-daily)).

> 지난번 저장하신 VoiceStudio(로컬 음성 스튜디오)·Fish Audio Drama 3와 이어지는 소식입니다 — 로컬 무료 vs 초저가 API, 선택지가 하나 더 생겼습니다.

출처: [Mistral — Voxtral 3 (10/20)](https://mistral.ai/news/voxtral-3/) · [Mistral Docs Changelog](https://docs.mistral.ai/resources/changelogs) · [synon Obsidian×AI 데일리 (10/22)](https://synon.co.jp/article/news/2026-10-22-obsidian-ai-daily)
