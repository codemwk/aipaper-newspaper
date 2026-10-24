---
title: "AI 콘텐츠: Block ‘Dessa’ — 글자 없이 ‘사람 말소리’만으로 학습한 음성 모델, 듣는 동시에 말하고 웃고 머뭇거린다. 맥북에서 돌지만 아직 공개는 안 했다"
date: 2026-10-25T07:04:00+09:00
category: "AI 콘텐츠"
slug: "block-dessa-speech-only"
summary: "잭 도시의 Block이 10/23 연구용 음성 모델 Dessa를 공개. 텍스트 데이터나 기존 언어 모델 없이 사람의 대화 음성만으로 처음부터 학습했고, 말하면서 동시에 듣는 ‘풀 듀플렉스’ 방식. 웃음·쉼·울먹임 같은 감정이 태그 없이 모델 안에 있다고 주장. 학습은 NVIDIA GB200 NVL72 랙 하나, 실행은 M4 Max 맥북프로 이상에서 로컬로. 일반 공개는 없고 AI 안전 연구자에게만 먼저 테스트를 요청. ‘음성의 GPT-3 순간’이라는 연구자 주장과 ‘어색하고 섬뜩하다’는 평가가 공존."
---

## 한줄 요약
대부분의 음성 AI는 **말 → 글자 → 생각 → 글자 → 말**로 돈다. Block의 **Dessa**는 중간에 글자가 없다. 사람 대화 **음성만으로** 처음부터 학습해서, 듣는 동시에 말하고(풀 듀플렉스), 웃고, 쉬고, 피곤한 얘기를 할 땐 피곤한 목소리가 된다([TechCrunch](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/)).

## 무엇이 다른가
| 항목 | 기존 음성 에이전트 | Dessa |
|---|---|---|
| 파이프라인 | 받아쓰기 → LLM → TTS | 음성 → 음성 (텍스트 없음) |
| 감정 | ElevenLabs v4·Fish Audio Drama 3처럼 **태그**로 지정 | 모델 안에 내장(회사 주장, 태그 여부는 불분명) |
| 지식 | LLM에서 가져옴 | 대화 데이터에서 나온 것뿐 |
| 실행 | 대부분 클라우드 | **M4 Max 맥북프로 이상에서 로컬** |
| 학습 자원 | — | NVIDIA GB200 NVL72 **랙 1개** |

Block의 주장: “지금 음성 AI는 그냥 별로다. 목소리를 글자로 바꾸면서 글자가 담지 못하는 정보를 엄청나게 버린다. 세계 최강의 AI도 당신이 어떤 기분인지 듣지 못한다.”

## 반응과 한계
- 연구자 Ragavan Thurairatnam: “음성의 GPT-3 순간.” 반면 The Verge는 샘플 대화가 **“어색한 새 친구 같다”**고, 일부는 섬뜩하다고 평했다([The Verge](https://www.theverge.com/ai-artificial-intelligence/1017906/jack-dorsey-block-dessa-ai-voice-speech)).
- **일반 공개 없음**. 먼저 AI 안전 연구자에게 테스트를 요청했다 — 사람처럼 들리는 음성이 **사기·사칭**에 쓰일 위험을 먼저 보겠다는 뜻으로 읽힌다.
- 텍스트를 안 거치니 **사실 지식·도구 호출**은 약할 수밖에 없다. 정보형 비서보다 ‘대화 상대’ 쪽.

## 왜 중요한가
Block은 결제·소상공인 회사다. Square는 이미 음성 AI로 주문을 받는다. **기기에서 도는 자체 음성 모델**이 있으면 매장 주문·고객 응대를 훨씬 싸게 돌릴 수 있다. 음성이 ‘빌려 쓰는 API’에서 **‘직접 소유하는 제품층’**이 되는 흐름.
콘텐츠 제작자에게: 내레이션·오디오 드라마에서 ‘감정 태그 붙이기’ 노동이 언젠가 사라질 수 있다는 신호. 다만 지금은 데모뿐이다.

출처: [TechCrunch (10/24)](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/) · [The Verge](https://www.theverge.com/ai-artificial-intelligence/1017906/jack-dorsey-block-dessa-ai-voice-speech) · [Block — Dessa](https://block.xyz/dessa) · [The Decoder](https://the-decoder.com/blocks-new-ai-model-dessa-was-trained-entirely-on-human-speech-to-catch-emotions-text-based-models-miss/)
