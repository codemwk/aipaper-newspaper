---
title: "AI 콘텐츠: 오픈소스 100일 만에 ‘파생 모델 1,472개’ — MiniMax H3 패밀리 공개, 5초 영상 8초 생성·초당 0.025달러부터, HeyGen·Suno·Pika가 만든 H3 변종까지 한 API로"
date: 2026-11-27T07:25:00+09:00
category: "AI 콘텐츠"
slug: "minimax-h3-family"
summary: "MiniMax가 11/26 영상·이미지 모델 라인업 ‘H3 패밀리’를 발표했다. 고급 상업용 H3(2K, 초당 0.08달러~), 대량 생산용 H3-Highspeed(5초 영상 평균 11초), 최저가 H3-Lite(초당 0.025달러), 참조 이미지 16장까지 받는 H3-Image, 4K 이미지를 10초 안에 뽑는 H3-Image Highspeed다. H3를 오픈소스로 푼 지 100일 동안 파생 모델 1,472개, 다운로드 1억 4,800만 회가 나왔다고 회사는 밝혔다."
---

## 한줄 요약
모델 하나를 오픈소스로 풀고, 남들이 그 위에 만든 변종까지 **자기 플랫폼 API로 모아 파는** 전략. 영상 생성의 가격과 속도도 한 단계 내려왔다([TechPlugged, 11/26](https://techplugged.com/minimax-h3-family-video-image-models/)).

## 라인업과 가격 (회사 발표)
| 모델 | 용도 | 해상도 | 시작 가격 |
| --- | --- | --- | --- |
| H3 | 고급 상업 작업, 부분 편집 | 2K / 768P | 초당 0.08달러 |
| H3-Highspeed | 일상·대량 생산, 최대 30초 | 768P / 480P | 초당 0.04달러 |
| H3-Lite | 최저가 | 768P / 480P | 초당 0.025달러 |
| H3-Image | 참조 이미지 16장 | — | 출력 100만 토큰당 3.80달러 |
| H3-Image Highspeed | 4K 이미지 10초 이내 | 4K | 100만 토큰당 7.60달러 |

- **H3:** 막연한 분위기·감정 묘사를 해석하고, 사람·옷·물건 교체나 화면 일부만 조명 바꾸기 같은 **부분 편집**을 지원.
- **H3-Highspeed:** 5초 클립 평균 약 11초, 15초 클립도 1분 이내.
- **H3-Lite:** 일부 하드웨어에서 768P 5초 클립을 약 8초에, 영상 비용 약 0.20달러.

## 파트너가 만든 H3 변종 (일부)
- **fal H3 Max:** 768P 5초를 3초 안에, Turbo는 그 두 배 속도.
- **HeyGen Video 1:** 최대 30초, 화면·대사·효과음을 한 번에.
- **Suno H3 Move:** 노래에 입 모양을 맞춘 뮤직비디오.
- **Creatify Boreal-H3:** 이커머스 광고 특화. **Pika H3 Flex:** 6단계 생성 + 카메라·동작·효과음 제어.
- **LightX2V H3 Turbo:** 4~8단계 생성, **로컬 실행 가능**. **Akatz Character Swap:** 장면은 두고 인물만 교체.
- 파생 모델 전부를 **MiniMax Open Platform API**에서 부를 수 있다고 밝혔다.

## 왜 중요한가
- 숏폼·광고를 대량으로 만드는 입장에선 **초당 0.025~0.04달러**와 “5초 영상 10초 안팎”이 의미 있는 기준선이다. 실험 비용이 사실상 몇 센트 단위로 내려왔다.
- 오픈소스 → 파생 생태계 → 자사 API로 회수하는 구조는 **‘오픈 모델로 돈 버는 법’**의 한 답이다.
- 주의: 속도·가격·파생 모델 수·“오픈소스 중 지시 이행 최고” 등은 모두 MiniMax 발표이며 독립 검증 전이다. 세부 요금은 플랫폼 문서를 확인해야 한다.

출처: [TechPlugged — MiniMax launches H3 Family](https://techplugged.com/minimax-h3-family-video-image-models/) · [ZICQ 보도](https://zicq.com/articles/n-a080835b1836496764d52fc9463a3e28-MiniMax-Launches-the-H3-Family-for-Video.html)
