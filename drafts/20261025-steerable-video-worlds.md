---
title: "AI 콘텐츠: ‘한 번에 뽑기’에서 ‘찍으면서 지시하기’로 — 텐센트 Hy-Nomas는 구간마다 “왼쪽으로 패닝, 이제 문으로” 지시를 받고, Tripo EdenLive는 회색 게임 화면을 실시간 영상으로"
date: 2026-10-25T07:05:00+09:00
category: "AI 콘텐츠"
slug: "steerable-video-worlds"
summary: "이번 주 오픈 영상 모델 두 개가 같은 방향을 가리켰다. 텐센트 Hunyuan의 Hy-Nomas(10/21 가중치 공개)는 영상을 구간 단위로 이어 만들며 구간 사이에 새 텍스트 지시나 카메라 경로를 받는다(720×1280·24fps, 8스텝, RTX 4090 1장용 저메모리 설정). Tripo AI의 EdenLive(10/23)는 코딩 에이전트·게임 엔진이 만든 거친 화면을 RTX 5090 한 장에서 720p·초당 24프레임 이상으로 ‘다시 그려’ 몇 분씩 연속 생성. 둘 다 가중치 공개. 단 Hy-Nomas는 디코더 라이선스가 비상업일 수 있어 상업 사용은 확인 필요."
---

## 한줄 요약
지금까지 AI 영상은 **프롬프트 한 번 → 클립 한 개**였다. 마음에 안 들면 처음부터 다시(리롤). 이번 주 공개된 두 오픈 모델은 **영상이 만들어지는 중간에 지시를 끼워 넣는** 쪽으로 간다 — 감독이 현장에서 말하듯.

## 1. 텐센트 Hy-Nomas — 구간마다 방향을 바꾸는 ‘인터랙티브 월드’
- 한 번에 한 구간씩 이어 생성(자기회귀). **구간 사이에** 자유로운 텍스트 지시(물체 추가·스타일 변경), 시작·끝 시간이 있는 동작 설명, **카메라 경로**를 넣을 수 있다. 앞 구간의 기억(KV 캐시)으로 물체·조명을 유지한다([ReelStack](https://thereelstack.com/lab/tencent-hy-nomas-open-interactive-video-world-model)).
- 사양: 720×1280·24fps, 증류 버전 8스텝, **시네마틱·양팔 로봇** LoRA 2종, 프롬프트 보강기 동봉. 팀원에 따르면 약 80억 파라미터.
- 실행: 표준 설정은 GPU 8장, **RTX 4090 1장**용 저메모리 설정(8비트 압축·CPU 오프로드) 제공. CUDA 13 필요. 웹 데모 있음.
- 주의: 텐센트는 Apache 2.0이라고 표기했지만 **비디오 디코더가 NVIDIA PixelUMM 파인튜닝**이고 그 가중치는 비상업 연구 라이선스라는 지적이 있다 → 고객 작업엔 확인 전 쓰지 말 것([Fervor Creative AI](https://fervorcreativeai.com/briefings/2026-10-24-0514/)). 속도·벤치마크 수치와 기술 보고서는 아직 없다.

## 2. Tripo AI EdenLive — 회색 박스를 실시간 영상으로
- 코딩 에이전트나 게임 엔진이 만든 **거친 화면(2D/3D 장면 또는 참고 영상) + 목표 첫 프레임 + 텍스트**를 받아 디테일한 영상으로 다시 렌더한다. 480p·720p 출력.
- 회사 실험에서 **RTX 5090 한 장에 720p·초당 24프레임 이상**, 몇 분씩 연속 생성([VoxelMatters](https://www.voxelmatters.com/tripo-ai-releases-edenlive-real-time-generative-renderer/)).
- 가중치·실시간 생성 코드·**텍스트→간단한 플레이 가능 게임** 스킬·프런트엔드까지 공개. 배치·움직임·카메라 경로는 그대로 두고 **외형만 바꿔 보는** 프리뷰, 캐릭터·스타일 교체에 쓸 수 있다.
- 5월 공개한 월드 모델 ‘Project Eden’의 일부. “세계 상태의 변화”와 “화면 그리기”를 분리한 설계.

## 왜 중요한가
두 모델 모두 **사람의 입력을 작업의 ‘시작’에서 ‘중간’으로** 옮긴다. 긴 프롬프트로 한 번에 맞히려 애쓰기보다 **짧게 시작하고 자주 지시**하는 습관이 맞는 도구가 늘고 있다.
실무 활용: 프리비즈(사전 시각화)·롱테이크 카메라 무빙, 그리고 **코딩 에이전트가 만든 프로토타입 게임·인터랙션을 ‘완성 화면처럼’** 보여 주는 피치 자료.
ANDRSN 관점: 필름·경험 디자인 시안에서 “구도는 고정, 룩만 5가지”를 빠르게 비교할 수 있다. 단 라이선스 확인이 먼저.

출처: [The ReelStack — Hy-Nomas (10/23)](https://thereelstack.com/lab/tencent-hy-nomas-open-interactive-video-world-model) · [Hy-Nomas GitHub](https://github.com/Tencent-Hunyuan/Hy-Nomas) · [VoxelMatters — EdenLive (10/23)](https://www.voxelmatters.com/tripo-ai-releases-edenlive-real-time-generative-renderer/) · [Fervor Creative AI 브리핑 (10/24)](https://fervorcreativeai.com/briefings/2026-10-24-0514/)
