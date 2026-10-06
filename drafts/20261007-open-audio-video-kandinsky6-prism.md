---
title: "AI 콘텐츠: ‘소리까지 같이 만드는’ 오픈 영상 모델 둘 — Kandinsky 6.0 Video(16GB GPU)와 Tencent·Fudan Prism(네이티브 2K)"
date: 2026-10-07T07:04:00+09:00
category: "AI 콘텐츠"
slug: "open-audio-video-kandinsky6-prism"
summary: "10/6 하루에 MIT 라이선스 오디오-비디오 동시 생성 모델 두 개가 공개. Kandinsky 6.0 Video는 Lite 3B·Pro 29B, 5초+44kHz 립싱크, 16GB 프리셋. Prism은 720p~2K 네이티브, 약 8.5초, 80GB GPU 필요. 그동안 Veo 3.1·Sora 2 같은 폐쇄형이 독점하던 영역."
---

## 한줄 요약
대사·효과음·배경음악을 **영상과 한 번에** 만드는 ‘오디오-비디오 동시 생성’은 그동안 Veo 3.1, Sora 2 같은 **폐쇄형 모델의 영역**이었다. 10월 6일 하루에 이걸 **MIT 라이선스로 통째로 공개**한 모델이 두 개 나왔다.

## 1) Kandinsky 6.0 Video — “집 GPU로 돌려 보는” 쪽
- **Lite(3B)·Pro(29B)** 두 가지. 텍스트→영상+소리, 이미지→영상+소리 모두 지원.
- **5초 클립 + 44kHz 오디오(립싱크 포함)**, 내장 업스케일러로 **1080p**까지.
- 구조: 기존 Kandinsky 5.0 영상 스트림에 **새로 학습한 오디오 스트림**을 붙이고 양방향 크로스어텐션으로 박자를 맞춘다.
- 성능(자체 보고서): 오픈 모델 LTX 2.5를 VABench 대부분 항목에서 앞서고, Veo 3.1 Fast와는 항목별로 승패를 나눴다. 화질은 MiniMax H3·Seedance 2.0에 뒤지지만 **음성 품질은 경쟁권**.
- 메모리: 블록 오프로드로 Pro 최대 메모리를 72.8→21.7GiB까지 낮췄고 **16GB 프리셋**도 있다. 대신 증류 안 한 Pro로 풀HD를 뽑으면 H100에서 약 402초.
- 코드·가중치·Diffusers 통합 공개, ComfyUI 노드·HF Space 제공([AICoder](https://aicoder.com/news/news-20261006-kandinsky-6-video-open-audio-video-29b-mit), [논문 arXiv 2610.05608](https://paperswithcode.co/paper/2610.05608)).

## 2) Prism — “처음부터 2K로” 그리는 쪽
- **Fudan대·Tencent Hunyuan(+저장대)** 공동. 작게 만들고 키우는 대신 **720p·1080p·2K(2560×1440)를 네이티브**로 생성.
- 기본 길이 **205프레임(24fps 약 8.5초)**. 프롬프트를 ‘그림용’과 ‘소리용’으로 나누고 음악·효과음 태그를 쓴다.
- 비결: 입이 움직이거나 북을 치는 등 **소리와 화면이 강하게 엮인 구역에만 촘촘한 어텐션**, 배경은 성기게 — 학습 속도 2.5배.
- 대신 무겁다: 720p도 **80GB GPU 1장+CPU 오프로드**, 1080p·2K는 80GB GPU 4장 이상. 체크포인트 하나가 약 65GB, 아직 ComfyUI 노드·호스팅 API 없음([ArtRealm](https://artrealmai.com/article/prism-tencent-hunyuan-native-2k-video-audio), [GitHub](https://github.com/Tencent-Hunyuan/Prism)).

## 왜 중요한가
MIT 라이선스는 **상업적 사용·파인튜닝·자체 서비스화**가 자유롭다는 뜻이다. 쇼츠·광고 제작 파이프라인을 직접 꾸리는 팀은 “소리는 ElevenLabs, 영상은 따로” 하던 이음새를 줄일 수 있다. 개인은 **Kandinsky Lite/16GB 프리셋**으로 먼저 실험하고, 2K 품질이 필요하면 Prism을 클라우드 GPU로 시간 단위로 빌리는 게 현실적이다.

## 체크포인트
- 모든 품질 비교는 **개발팀 자체 평가**. 5~8초 길이 제한은 여전하다.
