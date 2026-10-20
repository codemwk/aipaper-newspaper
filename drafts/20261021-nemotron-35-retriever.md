---
title: "AI 모델: NVIDIA Nemotron 3.5 검색 모델 공개 — PDF 페이지를 ‘사진째로’ 찾는 임베딩(1B·8B)과 재정렬 8B, 한국어 포함·상업 이용 가능"
date: 2026-10-21T07:07:00+09:00
category: "AI 모델"
slug: "nemotron-35-retriever"
summary: "NVIDIA가 10/20 Hugging Face에 Nemotron 3.5 Retriever 공개. Embed-1B(1.55B): 문서 페이지를 이미지·텍스트·둘 다로 임베딩, 질문은 텍스트, 표·차트·인포그래픽 페이지 지원, 2,048차원(512·1,024로 잘라 써도 됨), 컨텍스트 32,768토큰, 텍스트 34개·이미지 18개 언어 평가(한국어 포함). 8B 교사 모델에서 증류, 기존 Nemotron-3-Embed-1B와 같은 텍스트 임베딩 공간 유지. ViDoRe V3(이미지+텍스트) 58.82로 Qwen3-VL-Embedding-8B(57.03)보다 높다고 모델 카드에 표기. Rerank-8B(8.38B, 32K)는 텍스트·페이지 이미지 재정렬. OpenMDW-1.1 라이선스로 상업 이용 가능, NVIDIA GPU(Ampere·Hopper·Blackwell)용."
---

## 한줄 요약
‘내 문서에 묻는 AI(RAG)’가 자주 틀리는 이유 중 하나는 **PDF를 글자로만 읽기** 때문이다. 표, 차트, 슬라이드는 텍스트로 뽑으면 의미가 깨진다. 2026-10-20 NVIDIA가 공개한 **Nemotron 3.5 Retriever**는 문서 페이지를 **이미지째로** 이해해 찾는 오픈 모델이다([Hugging Face 모델 카드](https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16)).

## 구성
| 모델 | 크기 | 역할 |
|---|---|---|
| Nemotron-3.5-Embed-1B | 1.55B | 페이지(이미지·텍스트·둘 다)를 벡터로 — 1차 검색 |
| Nemotron-3.5-Embed-8B | 8B급 | 더 정확한 임베딩(1B의 교사 모델) |
| Nemotron-3.5-Rerank-8B | 8.38B | 찾은 후보를 다시 정렬 — 2차 정밀 검색 |

## Embed-1B의 특징
- **입력**: 질문은 텍스트, 문서는 **페이지 이미지·텍스트·둘을 합친 것** 모두 가능. 표·차트·인포그래픽이 있는 페이지를 지원한다.
- **출력**: 2,048차원 벡터. 앞부분만 잘라 **1,024·512차원**으로 써도 검색이 유지된다(저장 공간 절약).
- **언어**: 텍스트 검색 34개, 이미지 검색 18개 언어로 평가 — 둘 다 **한국어 포함**.
- **호환성**: 기존 Nemotron-3-Embed-1B와 **같은 텍스트 임베딩 공간**을 공유해, 이미 텍스트로 색인해 둔 자료에 이미지 검색을 얹기 쉽다.
- **성능(모델 카드 기준)**: 시각 문서 검색 벤치마크 ViDoRe V3(이미지+텍스트)에서 **58.82**, 크기가 훨씬 큰 Qwen3-VL-Embedding-8B는 57.03. 다국어 이미지 검색 MIRACL-VISION에서 68.93.
- **라이선스**: OpenMDW-1.1, **상업·비상업 이용 가능**. NVIDIA GPU(Ampere·Hopper·Blackwell)에서 Transformers·Sentence Transformers·vLLM으로 실행.

## 왜 중요한가
세컨드 브레인에 쌓이는 건 깔끔한 마크다운만이 아니다. 스캔한 계약서, 강의 슬라이드, 차트가 든 리서치 PDF, 화면 캡처가 훨씬 많다. ‘페이지를 사진처럼 기억하는’ 임베딩은 이런 자료를 **OCR 없이** 검색 대상으로 만든다. 1B라는 작은 크기에 512차원 절삭까지 되니 개인 서버나 소규모 팀에서도 현실적이다. 
한계: 모델 카드 스스로 “항상 정확한 문서를 찾는다는 보장은 없다”고 적었다. 성능 수치는 NVIDIA 자체 평가이며, 공식 예제는 CUDA GPU를 전제로 한다(맥 단독 실행은 별도 확인 필요).

출처: [Hugging Face — Nemotron-3.5-Embed-1B 모델 카드 (10/20)](https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16) · [Hugging Face — Nemotron-3.5-Rerank-8B](https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16) · [Nemotron 3.5 Retriever 컬렉션](https://huggingface.co/collections/nvidia/nemotron-35-retriever)
