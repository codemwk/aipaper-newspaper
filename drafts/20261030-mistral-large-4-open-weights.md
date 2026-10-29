---
title: "AI 모델: Mistral Large 4 ‘Le Chonk’ 가중치 공개 — 1조 파라미터 오픈웨이트, 입력 $0.70·출력 $2.10. 단, ‘모델을 서비스로 파는’ 회사는 별도 라이선스"
date: 2026-10-30T07:03:00+09:00
category: "AI 모델"
slug: "mistral-large-4-open-weights"
summary: "Mistral이 10/29 Mistral Large 4(별칭 Le Chonk)의 개선판 가중치를 Hugging Face에 공개했다. 이달 초 프리뷰 이후 강화학습을 더 돌려 코딩·방어적 사이버보안·추론 효율을 끌어올렸다고 설명. 추론 모드 3단계, vLLM·SGLang으로 자체 배포 가능. 가격 입력 $0.70·캐시 입력 $0.07·출력 $2.10(100만 토큰당). 라이선스는 수정 MIT 계열이지만 MaaS 사업자는 별도 상업 라이선스 필요."
---

## 한줄 요약
10/7 기사에서 다룬 Mistral Large 4 프리뷰가 약속대로 **가중치까지 공개**됐다. 프리뷰보다 개선된 버전이고, 누구나 내려받아 자기 서버에서 돌릴 수 있다([Mistral 발표](https://mistral.ai/news/mistral-large-4-oss/)).

## 무엇이 바뀌었나 (회사 설명)
- 프리뷰 이후 받은 피드백으로 **강화학습을 더 확장** → 코딩·방어적 보안 작업에서 큰 개선, “아직 포화 신호가 없다”.
- **추론 효율 개선**: 같은 성능을 더 적은 추론 비용으로.
- **추론 모드 3단계**로 비용과 성능을 골라 쓴다.
- The Verge에 따르면 Mistral은 “코딩 최강 오픈웨이트 모델”이라고 주장하고, 악의적인 사이버 요청은 다른 오픈 모델보다 더 잘 거절한다고 밝혔다([The Verge](https://www.theverge.com/ai-artificial-intelligence/1022184/mistral-ai-has-officially-released-its-large-4-le-chonk-model)). 순위·벤치마크 수치는 회사 주장이라 여기선 옮기지 않는다.

## 쓰는 방법과 값
| 경로 | 내용 |
|---|---|
| 바로 써보기 | Mistral Studio, Mistral API, OpenRouter, Vibe Code(자기 저장소에서 기능 구현·버그 수정) |
| 직접 배포 | Hugging Face 가중치 + vLLM / SGLang, NVIDIA NeMo AutoModel로 미세조정, TensorRT LLM으로 서빙 |
| API 가격(100만 토큰) | 입력 **$0.70** · 캐시 입력 **$0.07** · 출력 **$2.10** |

## 라이선스에서 꼭 볼 한 줄
‘Mistral Ecosystem Open-Weight’ 라이선스(수정 MIT): 사용·수정·미세조정·상업화 모두 자유. **단 하나, 모델을 API 서비스(MaaS)로 파는 회사는 Mistral에 별도 상업 라이선스를 받아야 한다.** 자기 제품 안에 넣어 쓰는 건 괜찮고, “이 모델을 그대로 재판매”는 막은 구조다.

## 왜 중요한가
- **1조 파라미터급을 내려받는 시대.** 개인 PC용은 아니지만, 데이터를 밖으로 못 내보내는 기업·기관에는 현실적인 선택지가 하나 늘었다.
- **오픈웨이트의 수익 모델이 정리되는 중.** “무료로 풀되, 우리 경쟁자가 될 클라우드 재판매만 막는다” — 오픈 모델 회사들이 점점 이 선을 긋는다.
