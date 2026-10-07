---
title: "세컨드 브레인 / PKM: Perplexity pplx-embed-v2-late — PDF·슬라이드를 OCR 없이 ‘페이지 그대로’ 찾는 오픈 임베딩, 0.6B로 9B 인덱스를 검색"
date: 2026-10-08T07:10:00+09:00
category: "세컨드 브레인 / PKM"
slug: "pplx-embed-v2-late-multimodal"
summary: "Perplexity가 10/7 MIT 라이선스 멀티모달 ‘늦은 상호작용(ColBERT)’ 임베딩 0.6B·9B를 Hugging Face에 공개했다. 토큰마다 128차원 벡터를 만들고 MaxSim으로 점수화, 텍스트·이미지·문서 페이지를 OCR 없이 검색. 두 모델이 임베딩 공간을 공유해 작은 모델로 큰 모델 인덱스를 질의할 수 있다. ViDoRe v3 이미지 nDCG@10 62.3%/65.2%(회사 수치)."
---

## 한줄 요약
어제 소개한 Google EmbeddingGemma 2에 이어, 하루 만에 **Perplexity**가 멀티모달 임베딩을 공개했다. **pplx-embed-v2-late** 두 모델(0.6B·9B)은 텍스트·이미지·**PDF나 슬라이드 같은 ‘시각 문서’**를 OCR로 글자를 뽑지 않고 **페이지 자체로** 검색한다. 라이선스는 **MIT**([Perplexity 커뮤니티 공지](https://community.perplexity.ai/t/were-releasing-pplx-embed-v2-late-two-late-interaction-embedding-models-that-retrieve-text-images-and-pages-with-a-shared-embedding-space-for-cross-model-querying/6296), [Hugging Face 모델 카드](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b)).

## ‘늦은 상호작용’이 뭔데? (쉽게)
보통 임베딩은 문서 하나를 **벡터 하나**로 꾹 눌러 담는다. 표·그림·여러 주제가 섞인 페이지는 그 과정에서 디테일이 뭉개진다. 이 모델은 **토큰(조각)마다 128차원 벡터**를 따로 만들고, 질문의 각 조각과 가장 잘 맞는 문서 조각을 찾아 점수를 더하는 **MaxSim** 방식(ColBERT 계열)을 쓴다. 그래서 “3분기 슬라이드의 그 막대그래프” 같은 **세부 검색에 강하다**. 대신 저장 공간은 더 든다.

## 숫자와 특징 (회사 발표)
| 모델 | 활성 파라미터 | 공개 ViDoRe v3 이미지 nDCG@10 | 마크다운 nDCG@10 |
|---|---|---|---|
| 0.6B | 3.4억 | 62.3% | 61.2% |
| 9B | 74억 | 65.2% | 64.7% |
- **공유 임베딩 공간**: 9B로 만든 인덱스를 **0.6B로 질의**할 수 있다. 색인은 한 번 무겁게, 검색은 가볍게.
- Qwen3.5 기반(양방향 어텐션), 내부 18B ColBERT 교사 모델에서 증류.
- Sentence Transformers 6.0+에서 바로 사용. 단, 텍스트와 이미지를 **한 배치에 섞어 넣을 수는 없다**.

## 왜 중요한가 (세컨드 브레인 관점)
내 지식 창고의 상당 부분은 **PDF 보고서, 강의 슬라이드, 스크린샷**이다. 지금까지는 OCR → 텍스트 임베딩을 거치며 표·도표 정보가 사라졌다. 로컬에서 돌릴 수 있는 0.6B(활성 3.4억)급 모델이 ‘페이지 그대로’ 검색을 해 주면, Obsidian 볼트나 개인 아카이브용 **멀티모달 검색 레이어**를 직접 만들 수 있다. EmbeddingGemma 2(단일 벡터, 온디바이스)와 비교하면 — **가볍고 단순한 쪽은 Gemma, 문서 세부 검색은 pplx-late**라는 선택지가 생겼다. 위의 LLM Wiki처럼 ‘임베딩 없는 그래프 검색’ 진영과는 철학이 다르다는 점도 기억해 두자.

출처: [Perplexity 공지](https://community.perplexity.ai/t/were-releasing-pplx-embed-v2-late-two-late-interaction-embedding-models-that-retrieve-text-images-and-pages-with-a-shared-embedding-space-for-cross-model-querying/6296) · [HF: pplx-embed-v2-late-0.6b](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b) · [HF: 9b](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-9b) · [Crypto Briefing 보도](https://cryptobriefing.com/perplexity-pplx-embed-v2-late-multimodal-models/)
