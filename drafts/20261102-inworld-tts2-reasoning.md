---
title: "AI 콘텐츠: Inworld TTS-2 ‘Reasoning’ — 말하기 전에 스스로 연기 노트를 쓰는 음성 모델. 감정 태그 대신 상황 설명 600자"
date: 2026-11-02T07:03:00+09:00
category: "AI 콘텐츠"
slug: "inworld-tts2-reasoning"
summary: "Inworld가 10/28 Realtime TTS-2에 Reasoning을 추가했다. 대사와 상황(최대 600자, 읽히지도 과금되지도 않음)을 주면 내부 언어모델이 ‘따뜻하게, 웃음 섞어’ 같은 연기 지시를 쓰고 그대로 읽는다. 지시문은 응답으로 돌려준다. 같은 모델 ID·같은 가격, 짧은 문장 생성 약 13%↑. 실시간 양방향(duplex)은 아직."
---

## 한줄 요약
“I can't believe you did that.”은 깜짝 파티에서도, 배신 고백 뒤에도 나오는 말이다. Inworld TTS-2는 이제 **상황을 읽고 어떻게 말할지 먼저 정한 뒤** 읽는다([Inworld 블로그](https://inworld.ai/blog/realtime-tts-2-reasoning-speed-consistency), [ArtRealmAI 정리](https://artrealmai.com/article/inworld-realtime-tts-2-reasoning-context-steered-delivery)).

## 무엇이 바뀌었나
- **Reasoning(옵트인)**: 요청 하나에 필드 하나(`REASONING_ON`). 내부의 작은 언어모델이 대사+상황으로 자유 형식 연기 지시를 쓰고, TTS-2가 그대로 연기.
- **상황 필드**: 최대 600자. 음성으로 읽히지 않고 과금도 안 됨. 이전 대사는 별도 필드로 넘겨 대화 흐름 반영.
- **투명성**: 모델이 고른 지시가 응답에 `reasoningInstruction`으로 돌아온다. 사람이 직접 단 태그·지시는 항상 우선.
- **업데이트된 TTS-2**: 짧은 발화 약 **13%**, 중간 길이 약 **9%** 빠른 생성. 클론 음색 유사도↑, 긴 세션 음색 흔들림↓, 긴 문장 단어 누락·어말 /p/ /t/ /k/ 탈락 수정.

## 어디까지 되나
| 지원 | 아직(곧) |
|---|---|
| 일반 합성·스트리밍·비동기(오디오북) | WebSocket 스트리밍 |
| 동반자 음성 메시지, 생성형 스토리·수업, 사전 생성 게임 대사 | Duplex(Realtime API 포함), 배치 |

가격은 그대로 — 온디맨드 100만 자당 25달러(ArtRealmAI 인용 가격표). 외부 Cekura 벤치(TTS-2 Flash 첫 소리 중앙값 46ms 등)는 **이번 업데이트·Reasoning 이전** 측정이다.

## 왜 중요한가
- 지금까지는 LLM이 대사마다 `[happy]` 같은 태그를 고르도록 프롬프트 규칙을 유지해야 했다. 이제 **‘장면 설명’만 넘기면 연출은 음성 모델이** 맡는다. 오디오북·숏폼 내레이션 제작에선 태깅 노동이 빠진다.
- 팁: 돌아온 지시문을 로그로 남겨 두면, 이상하게 읽힌 줄은 태그가 아니라 **상황 설명을 고치면** 된다.
