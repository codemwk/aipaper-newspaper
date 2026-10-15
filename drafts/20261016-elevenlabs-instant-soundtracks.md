---
title: "AI 콘텐츠: ElevenLabs ‘Instant Soundtracks’ — 영상을 올리면 음악을 깔고, 효과음 자리를 스스로 찾아 타임라인에 박는다"
date: 2026-10-16T07:04:00+09:00
category: "AI 콘텐츠"
slug: "elevenlabs-instant-soundtracks"
summary: "ElevenLabs(10/15) ElevenCreative 업데이트: 업로드한 영상에 오리지널 배경음악 + 장면 큐에 맞춘 효과음을 생성해 타임라인에 자동 배치. 효과음은 별도 레이어로 편집, 원본 오디오를 레퍼런스로(장르·BPM·악기) 새 스코어 생성, 장면별 무드 전환, 숏폼 컷 타이밍 개선. API 새 파라미터 add_sfx·separate_tracks(음악/SFX 분리 ZIP)·use_audio_as_reference, 요청당 영상 10개·합계 200MB·10분."
---

## 한줄 요약
숏폼 편집에서 가장 귀찮은 작업 중 하나는 **“로고 나올 때 ‘휙’ 소리 넣기”** 같은 효과음 타이밍 맞추기다. ElevenLabs가 2026-10-15 **Instant Soundtracks**를 내놨다. 영상을 올리면 모델이 **배경음악을 작곡**하고, 화면을 보며 **효과음이 필요한 순간을 찾아** 해당 타임스탬프에 자동으로 배치한다([ElevenLabs 블로그](https://elevenlabs.io/blog/introducing-instant-soundtracks)).

## 무엇이 되나
- **음악 + 효과음 동시 생성**: 스코어를 깔고, 영상 속 동작·전환·화면 이벤트를 분석해 효과음을 타임라인에 맞춘다.
- **편집 가능한 레이어**: Music Video Editor에서 효과음은 음악과 **별도 레이어**. 효과음 추가·타이밍 조정·음악 교체를 처음부터 다시 만들지 않고 할 수 있다.
- **원본 오디오를 레퍼런스로**: 영상에 이미 있는 소리의 장르·크레센도·BPM·악기 구성을 분석해 “분위기가 닮은” 새 음악을 만든다.
- **장면별 무드 전환**: 빠른 장면엔 EDM·R&B, 느리고 친밀한 장면엔 어쿠스틱 기타로 넘어가는 식. 숏폼의 컷·전환 타이밍도 더 촘촘해졌다고 한다.

## 어디서, 어떻게
- ElevenCreative의 Music Video Editor, 광고용 **Creative Engine**, **ElevenMusic** 플랫폼에서 즉시 사용.
- **ElevenCreative Studio API** 새 파라미터: `add_sfx`, `separate_tracks`, `use_audio_as_reference`. `separate_tracks=true`면 음악·효과음을 **분리 파일 ZIP**으로 돌려줘 자체 파이프라인에서 믹싱할 수 있다.
- 한 요청에 영상 최대 **10개**, 합계 **200MB·10분**.
- 가격(크레딧 소모량)은 이번 발표에 따로 나오지 않았다.

## 왜 중요한가
영상 생성 모델은 대부분 “오디오 포함”을 내세우지만, 실제 마케팅 팀은 **이미 찍은 영상**에 소리를 입히는 일이 훨씬 많다. ElevenLabs는 생성보다 **후반 작업(사운드 디자인)**을 자동화하는 쪽으로 들어왔고, 분리 트랙 API로 다른 편집 도구의 ‘부품’이 되려 한다. ANDRSN처럼 film·sound를 함께 다루는 스튜디오라면, 초안 단계 사운드 스케치를 몇 초 만에 뽑고 사람이 다듬는 흐름을 시험해 볼 만하다.

출처: [ElevenLabs — Introducing Instant Soundtracks](https://elevenlabs.io/blog/introducing-instant-soundtracks)
