---
title: "새로운 각도: 식물의 ‘전기 신호’를 읽는 파운데이션 모델 — Electric Plant ‘Bombadil’, 100종·400만 시간 녹음으로 학습해 물 부족·스트레스를 식물 ‘안쪽’에서 읽는다"
date: 2026-10-26T07:11:00+09:00
category: "AI 모델"
slug: "electric-plant-bombadil"
summary: "미국 스타트업 Electric Plant Company가 10/20 시드 1,120만 달러(Onto Ventures·Climactic 주도)와 함께 식물 전기생리학 파운데이션 모델 ‘Bombadil’을 공개. 줄기·나무껍질 아래 살아 있는 조직에 꽂는 저가 센서 ‘Bud’가 미세 전압을 기록하면, Bombadil이 광합성 효율(광계 II)·잎과 공기 온도차·작물 수분 스트레스 지수(CWSI) 등 7가지 스트레스 지표를 추정한다. 라벨 없이 1,400여 그루·100종의 400만 시간 녹음으로 사전학습했고, 학습 때 못 본 종에도 적용된다고 주장. 센서 값은 ‘수십 달러’(CEO). 창업자는 식물 쇼핑몰 Bloomscape 창업자."
---

## 한줄 요약
농부는 지금까지 식물을 **밖에서** 읽었다 — 흙 수분, 날씨, 잎 색, 위성 사진. Electric Plant는 식물 **안에서 흐르는 전기**를 듣고, 그걸 언어 모델처럼 학습한 AI로 “지금 물이 필요해요”를 읽어 낸다([보도자료](https://www.businesswire.com/news/home/20261020814345/en/Electric-Plant-Company-Launches-From-Stealth-With-%2411.2M-in-Funding-and-a-Foundation-AI-Model-for-Plants-Bombadil)).

## 식물이 전기로 ‘말한다’고?
- 식물 조직에는 상태에 따라 **미세한 전압 변화**가 흐른다. CEO 저스틴 매스트는 “빛이 더 필요할 때 전기 신호가 흐르고, 제어 보드가 그걸 감지해 화분을 빛 쪽으로 움직인” 로봇 화분 연구를 보고 이 분야에 빠졌다고 말했다([TechCrunch, 10/20](https://techcrunch.com/2026/10/20/plants-can-speak-using-electricity-so-this-startup-built-an-ai-model-to-decipher-their-language/)).
- 공동창업자 리 폰 크라우스는 DARPA와 일한 신경과학자. 뇌파를 읽는 AI의 방법론을 식물에 가져왔다.

## 어떻게 동작하나
| 단계 | 내용 |
|---|---|
| 센서 ‘Bud’ | 아이폰을 세로로 접은 정도 크기. 스테인리스 나사가 **형성층(껍질 바로 아래 살아 있는 층)**까지 들어가 미세 전압을 읽는다. 저전력 무선으로 기지국 전송 |
| 밀도 | 정확한 결과에 **에이커당 센서 두어 개**면 된다고(CEO) |
| 모델 ‘Bombadil’ | 클라우드에서 신호 해석 → 7가지 스트레스 지표 추정(광계 II 효율, 잎-공기 온도차, CWSI 등) |
| 학습 | 라벨 없이 **400만 시간**(1,400여 그루·100종) 자기지도 사전학습. 이후 데이터는 700만 시간으로 늘었다고 |
| 일반화 | 학습 때 보지 못한 종에도 지표를 추정한다고 주장(백서 공개) |
| 확장 방식 | 병 감지·개화 시기 예측 같은 새 과제를 **같은 기반 모델 위에 ‘판독기’로 추가** |

- 센서 가격: 기존 장비는 수천 달러인데 **“수십 달러”**(CEO, TechCrunch).
- 효과 주장: 수확량을 늘리면서 **물 사용 20% 이상 절감** 가능(CEO 주장, 고객사 비공개).
- 사업 방식: 직접 농사 서비스를 하지 않고 **이미 식물 관리 사업을 하는 운영사에 기술을 라이선스**. 상업 현장에서 센서 수백 개가 돌고 있다고.

## 왜 ‘새로운 각도’인가
- **파운데이션 모델의 레시피(라벨 없이 대량 사전학습 → 여러 과제에 재사용)가 언어·이미지·DNA를 넘어 ‘생체 전기’로 간다.** 회사는 자사 데이터가 “공개된 인간 뇌활동 녹음을 다 합친 것보다 많다”고 주장한다 — 식물은 수천 개를 동시에, 계속, 현장에서 녹음할 수 있기 때문.
- **새로운 인터페이스**: 투자사 Onto의 표현대로 “사람과 식물 사이의 새 인터페이스”. 당장은 농업·임업 센서지만, 회사는 가정 화분부터 국립공원까지를 말한다. 창업자가 식물 쇼핑몰 Bloomscape 출신이라는 점에서, 언젠가 **‘화분이 말을 거는’ 소비자 제품**도 상상해 볼 수 있다.
- 신중하게 볼 점: 정확도·효과 수치는 회사 주장이고, 고객사는 공개되지 않았다. 시드 단계다.

출처: [Electric Plant 보도자료 (10/20)](https://www.businesswire.com/news/home/20261020814345/en/Electric-Plant-Company-Launches-From-Stealth-With-%2411.2M-in-Funding-and-a-Foundation-AI-Model-for-Plants-Bombadil) · [TechCrunch (10/20)](https://techcrunch.com/2026/10/20/plants-can-speak-using-electricity-so-this-startup-built-an-ai-model-to-decipher-their-language/) · [Bombadil 백서](https://www.electricplant.co/research/bombadil-paper)
