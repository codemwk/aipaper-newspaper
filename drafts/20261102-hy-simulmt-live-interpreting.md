---
title: "AI 콘텐츠: Tencent Hy-SimulMT — 말하는 동안 통역하고 목소리까지 복제하는 오픈 동시통역 모델(중↔영)"
date: 2026-11-02T07:04:00+09:00
category: "AI 콘텐츠"
slug: "hy-simulmt-live-interpreting"
summary: "Tencent Hunyuan이 10/26 중국어↔영어 실시간 동시통역 모델 Hy-SimulMT(30B-A3B, Apache-2.0)를 공개했다. 오디오가 들어오는 대로 번역 텍스트·음성을 내고 화자 음색을 복제한다(TTS 서비스 별도 필요). RealSI 장문 평가 StreamLAAL 약 3초로 비교군 최저. 6분짜리 실녹음 18개로 CATTI 자격 통역사와 비교했지만 소규모 자체 평가."
---

## 한줄 요약
회의·강연·인터뷰를 **“다 듣고 번역”이 아니라 “들으면서 번역”**하는 오픈 모델이다. 번역문과 함께 원래 화자의 목소리 특징을 살린 음성도 낸다([Hugging Face 모델 카드](https://huggingface.co/tencent/Hy-SimulMT-30B-A3B), [GitHub](https://github.com/Tencent-Hunyuan/Hy-SimulMT)).

## 핵심
- **방향**: 중국어↔영어 양방향 음성→음성. 번역만 내는 판 / 원문+번역(Interleave) 판, 각각 FP8·GGUF 제공.
- **지연**: RealSI 장문 오디오에서 StreamLAAL 약 **3초** — 비교한 시스템 중 최저. GEMBA 품질은 비교한 오픈 모델 전부, 상용 API 5개 중 4개보다 높았다고 회사가 밝힘.
- **단문 벤치**: RealSI-Sentence 84.7로 표 안 최고. FLEURS 90.3(Gemini3.5-LiveTranslate 92.4보다 낮음).
- **사람과 비교**: 2026년 9월 이후 올라온 약 6분 길이 실녹음 18개(10개 분야)를 CATTI 1·2급 통역사 6명과 비교, “품질 대등, 응답은 종종 더 빠름”. 회사 스스로 **소규모 평가**라고 단서를 달았다.

## 쓰려면
- vLLM ≥0.31 기반 SimulInfer(웹 페이지·파일 업로드·WebSocket). 음성 출력·음색 복제는 **별도 TTS 서비스 설정 필요**.
- BF16 가중치만 약 57GiB — H200 한 장급. llama.cpp 지원은 PR 제출 단계(미병합).
- 써 보기만 하려면 Hy Translate 앱.

## 왜 중요한가
- 콘텐츠 제작 쪽에선 **라이브 방송·웨비나 다국어 송출**의 비용 구조가 바뀐다. “말하면서 고쳐 말하는” 방식(먼저 말하고 나중에 정정)이 통역사의 자기 수정과 비슷하다는 현업 평가도 붙었다.
- 다만 공개된 언어쌍은 중↔영뿐이고, 고위험(법·의료) 현장은 여전히 사람 통역 영역이라고 Tencent도 명시했다.
