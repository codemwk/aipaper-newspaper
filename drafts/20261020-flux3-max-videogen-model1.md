---
title: "AI 콘텐츠: 10초 영상을 11초 만에 — fal·BFL ‘FLUX 3 Max’(1080p 초당 $0.0725, 할인가), 같은 날 VideoGen은 프롬프트 한 줄로 ‘최대 10분’ 다중 컷 영상 모델 예고"
date: 2026-10-20T07:04:00+09:00
category: "AI 콘텐츠"
slug: "flux3-max-videogen-model1"
summary: "10/19 fal이 Black Forest Labs와 함께 후속 학습한 영상 모델 FLUX 3 Max 출시: 10초 영상 생성 10.95초(Seedance 2.5는 277.8초, 원조 FLUX 3는 126.4초), Artificial Analysis 영상 아레나 예비 평가 1,139점(FLUX 3 대비 +50). 텍스트·이미지·키프레임→영상, 5~20초, 720p/1080p, 끝 장면 이미지 지정, 오디오 생성 기본 켜짐. 가격(11/7까지 75% 할인) 720p 초당 $0.0425·1080p $0.0725, 이후 $0.17·$0.29. 같은 날 YC 출신 VideoGen은 ‘Model 1’ 공개 — 대본·대사·컷을 스스로 계획해 최대 10분짜리 다중 컷 영상, 회사 주장 품질은 Seedance 2.5의 약 80%·가격은 절반 이하(검증 전), 파트너 한정 출시와 $100만 크레딧 지원."
---

## 한줄 요약
AI 영상의 두 가지 병목은 **기다림**과 **길이**다. 2026-10-19 하루에 두 회사가 각각 하나씩을 겨냥했다. **FLUX 3 Max**는 10초 영상을 **약 11초**에 만들고, **VideoGen Model 1**은 프롬프트 하나로 **최대 10분**짜리 이야기 영상을 만들겠다고 한다.

## ① FLUX 3 Max — “생성 대기 시간이 사라진다”
이미지 모델 FLUX로 유명한 Black Forest Labs(BFL)의 FLUX 3를, 추론 플랫폼 **fal**의 연구팀이 후속 학습·강화학습·추론 최적화로 다시 다듬은 모델이다([fal 보도자료](https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html)).
- **속도**: 10초 영상 **10.95초**. 같은 품질 점수의 Seedance 2.5는 277.8초, 원조 FLUX 3는 126.4초(fal 자체 측정).
- **품질**: Artificial Analysis 영상 아레나 **예비** 평가에서 이미지→영상 1,139점, FLUX 3보다 50점 높다. 표가 더 쌓이면 바뀔 수 있다고 fal도 명시했다.
- **기능**: 텍스트→영상, 이미지→영상, 여러 키프레임→영상. **5~20초**(1초 단위), 720p 기본·1080p 업스케일, 비율 21:9~9:16, **끝 장면 이미지** 지정, 오디오 생성 기본 켜짐, ‘생각 수준’ low/high.

| 해상도 | 할인가(11/7까지, 75%↓) | 정가 |
|---|---|---|
| 720p | 초당 $0.0425 | 초당 $0.17 |
| 1080p | 초당 $0.0725 | 초당 $0.29 |

10초 1080p 클립 하나가 할인가로 약 **$0.73**, 정가로 **$2.90**이다([fal 모델 페이지](https://fal.ai/models/blackforestlabs/flux-3-max/image-to-video)).

## ② VideoGen Model 1 — “한 편을 통째로”
샌프란시스코 스타트업 **VideoGen**(YC 2024 여름)이 첫 자체 모델을 공개했다([AI Affairs](https://www.aiaffairs.com/technology/videogen-model-1-ten-minute-ai-video-one-prompt/)).
- 내장된 **‘생각 하네스’**가 대본·대사·컷·호흡을 먼저 짜고, 컷과 컷 사이에 인물·장소·이야기 정보를 넘겨 **최대 10분**의 다중 컷 영상을 만든다. 실사·애니·시네마틱 버전을 따로 학습해 요청마다 골라 쓴다.
- CEO 안톤 쾨니히 주장: 품질은 Seedance 2.5의 **약 80%**, 가격은 비슷한 모델의 **절반 이하**. 공식 벤치마크·가격·외부 검증은 **아직 없다**. AI Affairs도 모델을 직접 써 보지 못했다.
- 10/19부터 **비공개 파트너 한정** 출시, 영화인·스튜디오·학생에게 **$100만 무료 크레딧** 신청을 받는다(작품성·배포 계획·VideoGen 크레딧 표기 의사 심사). 마케팅용 버전도 학습 중.

## 왜 중요한가
생성 시간이 영상 길이보다 짧아지면 영상 작업은 ‘주문하고 기다리기’에서 **‘보면서 고치기’**로 바뀐다. 시안을 열 번 돌려 보는 비용이 커피 한 잔 값이 되는 셈이다. 반면 10분짜리 한 방 생성은 아직 회사 주장 단계다 — 실제로 쓸 만한지는 **컷 사이 인물 일관성**이 드러나는 공개 결과물을 보고 판단하자. 브랜드 필름 관점에선 지금 당장은 **짧은 고품질 컷을 빠르게 뽑아 사람이 엮는** 쪽이 현실적이다.

출처: [fal — FLUX 3 Max 출시 (PR Newswire, 10/19)](https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html) · [fal 모델 페이지 — 가격·옵션](https://fal.ai/models/blackforestlabs/flux-3-max/image-to-video) · [AI Affairs — VideoGen Model 1 (10/19)](https://www.aiaffairs.com/technology/videogen-model-1-ten-minute-ai-video-one-prompt/)
