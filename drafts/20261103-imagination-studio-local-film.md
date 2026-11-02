---
title: "AI 콘텐츠: Imagination Studio — 기획·콘티·이미지·소리 있는 영상·목소리·음악을 ‘내 컴퓨터 한 대’에서. 구독·클라우드 없는 오픈소스 AI 영화 스튜디오(Mac·DGX Spark)"
date: 2026-11-03T07:03:00+09:00
category: "AI 콘텐츠"
slug: "imagination-studio-local-film"
summary: "개발자 keys(drowzeys)와 Wasserman Productions의 Sam Wasserman이 만든 Imagination Studio가 11/2 주목받았다. Apache-2.0 오픈소스로, 영화 기획(Slate 워크플로)부터 Qwen-Image-2.1·FLUX3-K 이미지, MiniMax H3/FastH3 소리 동기 영상, Fish Audio Drama 3 다화자 음성, MiniMax Music 3 노래까지 로컬에서 돌린다. 5초 864×480 클립 렌더에 DGX Spark 73초, M5 Ultra Mac 66초. 메모리에 따라 기능이 잠기고 풀린다."
---

## 한줄 요약
지금까지 로컬 AI 영상 제작은 모델 서버 여러 개, 파이썬 파이프라인 여러 개를 붙이는 일이었다. Imagination Studio는 그걸 **앱 하나·작업 대기열 하나·라이브러리 하나**로 묶었다([Hermes AI News](https://hermes-ai.net/news/imagination-studio-packs-video-voice-and-image-generation-into-one-local-app/), [GitHub](https://github.com/drowzeys/Imagination-Studio-by-keys-Wasserman)).

## 작업 공간 8개
| 영역 | 하는 일 |
|---|---|
| Story | 캐스팅·로케이션·룩북·샷 프롬프트까지 ‘영화 크루처럼’ 기획(Wasserman Slate 워크플로) |
| Image | Qwen-Image-2.1, FLUX3-K, MOSS-Image. 캐릭터 5방향 턴어라운드 |
| Video | MiniMax H3 / FastH3로 **최대 15초, 소리 동기** 영상 |
| Previs | 참고 영상에서 포즈 골격·깊이·윤곽·카메라 움직임 설명 추출 |
| Sound | Fish Audio Drama 3(한 테이크 최대 16명, [whispering] 같은 연기 지시, 음성 복제), MiniMax Music 3(최대 5분 보컬 포함) |
| Edit | 업스케일, SAM 3.1로 인물 지우기 |
| Agent room | Claude Code·Codex·Gemini·Grok 등 외부 에이전트, 로컬 모델 연결 |
| Studio Vaults | 생성물·LoRA 보관함 |

## 실제로 얼마나 빠른가
- FastH3 5초 864×480 클립: **DGX Spark 73초, M5 Ultra Mac 66초**(제작자 수치). DGX Spark 최대 8대까지 묶을 수 있고, Tailscale+QR로 폰에서 원격 조작.
- 설치 프로그램이 메모리·디스크를 먼저 재고, **통합 메모리 용량에 따라 쓸 수 있는 기능이 열린다**. 큰 영상·편집 모델은 OS와 메모리를 나눠 써야 해서다.
- 핵심 생성은 구독·클라우드 추론·생성 API 키 없이 로컬. 단, 에이전트 연동을 켜면 클라우드를 쓸 수 있다.

## 왜 중요한가
- 영상·음성·음악 AI가 각각 좋아진 다음 단계는 **‘파이프라인의 통합’**이다. 지난주 다룬 Genspark Media Studio가 클라우드 쪽 답이라면, 이건 **로컬·오픈소스 쪽 답**이다. 원본 소재가 밖으로 나가지 않는다는 점이 광고·영화 사전 시각화 현장에서 의미가 있다.
- 다만 ‘개인 개발자+제작사’ 프로젝트(10월 초 생성, ★약 500)라 안정성은 미지수. 모델별 라이선스(특히 상업 이용)는 각 모델 조건을 따로 확인해야 한다.
