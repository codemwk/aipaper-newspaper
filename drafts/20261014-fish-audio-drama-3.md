---
title: "AI 콘텐츠: Fish Audio Drama 3 — ‘배우에게 디렉션하듯’ 대괄호로 연기 지시하는 TTS, 83개 언어·오픈웨이트, API 한시 $10/100만 자"
date: 2026-10-14T07:04:00+09:00
category: "AI 콘텐츠"
slug: "fish-audio-drama-3"
summary: "Fish Audio(10/13) Drama 3: [목이 메어] 같은 자연어 디렉션을 문장 중간에도 반영. Artificial Analysis 발음 견고성 93.2%(S2.1 Pro 88.1%). 35B MoE(활성 ~3B). 오픈웨이트(연매출 $50만 미만 상업 무료). API는 11/12까지 $10/100만 자(정가 $50). 실존 인물 무단 음성 복제 금지."
---

## 한줄 요약
TTS는 이미 “잘 읽는” 단계를 지났다. 이제 경쟁은 **“연기를 디렉팅할 수 있느냐”**다. Fish Audio가 10/13 공개한 **Drama 3**는 `[barely holding it together, forcing a smile]`처럼 **배우에게 하듯 대괄호로 지시**하면 그 지점부터 톤을 바꾼다([Fish Audio 블로그](https://fish.audio/blog/fish-audio-drama-3/)).

## 무엇이 새로운가
- **문장 중간 디렉션**: 속삭임·웃음·숨소리를 적은 자리에서 정확히 바꾸고, 짝 태그로 **특정 단어만** 강조. 디렉션 언어는 대사 언어와 달라도 된다(예: 한국어 지시 + 영어 대사). **83개 언어**.
- **발음 정확도**: Artificial Analysis ‘Pronunciation Robustness’에서 **93.2%**(이전 S2.1 Pro 88.1%) — 브랜드·지명·기술 용어 95.9%, 코드·경로·이메일 86.3%.
- **학습 방식**: “받아쓰기 쉬운가·레퍼런스와 닮았나” 대신 **사람이 선호한 테이크**를 예측하는 단일 보상 모델로 RL. 웃음·속삭임이 감점되지 않게 한 것이 핵심.
- **구조**: 35B MoE(토큰당 활성 약 3B, Qwen3.5-35B-A3B 기반), 하이브리드 어텐션, 새 codebook-MTP 디코더. H200 1장에서 단일 스트림 271fps(S2 177fps).
- **다음**: 테이크 비교형 ‘인터랙티브 편집’, 한 단어만 바꿔 끼우는 **오디오 인페인팅**은 초대제 테스트 중.

## 가격·라이선스
- API `model: drama-3`, 기존 S2.1 Pro와 같은 엔드포인트. **11/12까지 $10/100만 자**(정가 $50, 80% 할인), 신규 크리에이터 플랜 50% 할인.
- **오픈웨이트**(Hugging Face): Fish Audio Community License v1.0 — 연구·비상업 무료, **연매출 $50만 미만이면 상업 사용 무료**. 그 이상이거나 TTS·클로닝 API로 재판매하면 별도 라이선스. **동의 없는 실존 인물 음성 복제 금지**. (fish-speech 저장소 ~3.3만★, 10/14)

## 왜 중요한가
오디오북·오디오 드라마·게임 대사·숏폼처럼 **“한 번 렌더하고 보관하는” 대사**에서, 재생성 없이 **연출만 고치는** 워크플로가 열린다. 작은 스튜디오에겐 상업 무료 구간이 실질적이다. 다만 테이크 편차가 있어 “여러 번 뽑아 고르라”는 게 회사 권고다.

출처: [Fish Audio — Drama 3](https://fish.audio/blog/fish-audio-drama-3/) · [GitHub fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)
