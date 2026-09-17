---
title: "NeoMME — 문서 페이지를 OCR 없이 검색하는 단일 타워 멀티모달 인코더"
date: 2026-09-18T07:45:00+09:00
category: "GitHub"
slug: "neomme-visual-document-rag"
summary: "2026-09-03 HF 블로그. H Company NeoMME 260M·800M. 텍스트+이미지 패치를 한 Transformer. NeoMME-Retriever는 ColPali식 페이지 이미지 검색. Apache 2.0, Transformers 지원."
---

## 한줄 요약
[Hugging Face 블로그](https://huggingface.co/blog/Hcompany/neomme)(**2026-09-03**)에서 H Company는 **NeoMME**(260M·800M)를 공개했다. 별도 비전 타워·인과 LM 없이, **하나의 양방향 Transformer**가 텍스트 토큰과 원시 이미지 패치를 같이 처리한다.

## 무엇이 바뀌었나
- 사전학습: 마스크드 이산 확산 텍스트 디노이저. 멀티모달 예제에서는 이미지는 보이고 텍스트를 가려 **이미지에 근거한 복원**을 강제.
- **NeoMME-Retriever**: ColPali처럼 PDF 페이지를 **스크린샷 이미지**로 인덱싱. OCR 파이프라인 우회. 한 번의 forward로 **dense + late-interaction** 임베딩.
- ViDoRe v3 등에서 260M이 800M 미만 급 중 상위권, 800M은 비슷한 크기 경쟁 모델과 근접(블로그 표). L40S에서 2048² 기준 260M이 초당 약 **51 페이지** 인코딩(ColModernVBERT 대비 약 2× 주장).
- late-interaction 저장을 pooling+양자화로 페이지당 ~1.5MB → **6KB**(255×)까지 줄이면서 nDCG@10의 95%+ 유지하는 설정을 제시.
- **Apache 2.0**, Transformers 네이티브. 비주얼 RAG 데모 스페이스 링크 제공.

## 왜 중요한가
세컨드 브레인·리서치 볼트 사용자는 “마크다운만 RAG”에 막히기 쉽다. 표·차트·레이아웃이 있는 **보고서 PDF**를 페이지 그림 그대로 찾게 하면, LLM Wiki·옵시디언 인제스트 앞단이 달라진다. 코드 덤프 없이 기억할 문장: **문서를 글자로만 읽지 말고, 페이지 사진으로 검색한다**.

## 기억할 것
- [NeoMME 블로그](https://huggingface.co/blog/Hcompany/neomme) · 컬렉션 `Hcompany/NeoMME` · arXiv [2609.01657](https://arxiv.org/abs/2609.01657)
