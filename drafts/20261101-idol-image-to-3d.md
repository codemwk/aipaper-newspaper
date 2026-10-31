---
title: "AI 콘텐츠: Sperid Idol — 사진 한 장 → 최대 100만 개 3D 가우시안. 소비 GPU 7.2GB, 2초대"
date: 2026-11-01T07:08:00+09:00
category: "AI 콘텐츠 생성"
slug: "idol-image-to-3d"
summary: "Sperid Labs가 10/31 Idol을 오픈소스로 공개했다. 객체 사진·렌더 한 장에서 배경 제거 후 표준 3DGS .ply(최대 1,048,576 가우시안)를 만든다. 피크 VRAM 약 7.2GB, 최적화 시 2초 미만 가능. Apache-2.0. DINOv3·FLUX.2 VAE 게이트 수락 필요."
---

## 한줄 요약
멀티뷰 촬영 없이 **한 장으로 뒷면까지 채운 스플랫**을 뽑는 오픈 가중치 파이프라인이다([Hugging Face](https://huggingface.co/speridlabs/Idol)).

## 스펙
| 항목 | 내용 |
|---|---|
| 출력 | `.ply` + 전처리 입력 PNG + 예측 카메라 JSON |
| 모드 | `synthetic`(렌더/생성 이미지) / `real`(사진, 여백 더 큼) |
| 가우시안 수 | 기본 262,144 — 최대 **1,048,576**(32 배수) |
| 메모리 | 피크 **~7.2GB** VRAM |
| 라이선스 | 가중치·SDK 쪽 Apache-2.0 표기 |

의존: 게이트된 `facebook/dinov3-…`, `black-forest-labs/FLUX.2-dev`(VAE만). `hf auth login` 후 첫 실행 시 약 3GB 가중치 다운로드.

## 벤치(팀 표)
동일 설정(50스텝·262K)에서 Idol이 TripoSplat·TRELLIS 대비 신규 시점 DINOv2/CLIP·선명도에서 앞선다고 보고. LGM은 PSNR은 높지만 블러(팀 주석). H100 요청 시간 Idol 6.8s vs TripoSplat 9.9s. RTX 4090 약 19s.

## 왜 중요한가
- 크리에이티브·제품 팀이 ‘이미지 → 실시간 3D 자산’을 **로컬·표준 포맷**으로 가져갈 수 있다. 다만 인코더 게이트·단일 뷰 환각(없는 뒷면)은 검수 대상.
