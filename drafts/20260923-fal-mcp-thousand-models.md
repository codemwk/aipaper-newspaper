---
title: "fal MCP — 대화 한 턴으로 이미지·비디오·TTS 1,000+ 모델을 호출"
date: 2026-09-23T07:07:00+09:00
category: "AI 콘텐츠"
slug: "fal-mcp-thousand-models"
summary: "fal.ai 호스팅 MCP(mcp.fal.ai). search_models·run_model·submit_job 등 9툴. Claude/Cursor에 Bearer 키만. SDK 없이 생성·큐·가격 조회. MCP 서버 자체는 무료, 모델 실행만 과금. 어제 H3 Max ‘속도 모델’과 다른 ‘카탈로그 접속’ 각도."
---

## 한줄 요약
[fal MCP Server](https://blog.fal.ai/connect-your-ai-to-1-000-models-with-the-fal-mcp-server/)는 AI 어시스턴트가 **fal 카탈로그 1,000+ 모델**을 검색·실행·체인하게 한다. “코드를 짜서 fal을 호출”이 아니라 **대화가 곧 fal 호출**이다. 엔드포인트: `https://mcp.fal.ai/mcp`.

## 무엇이 다른가
- **9툴**: 발견(`search_models`, `get_model_schema`, `get_pricing`, `search_docs`) · 실행(`run_model`, `submit_job`, `check_job`) · 유틸(`upload_file`, `recommend_model`).
- **세팅**: Claude Code `claude mcp add --transport http fal-ai https://mcp.fal.ai/mcp --header "Authorization: Bearer $FAL_KEY"`. Cursor/Desktop도 URL+헤더 JSON.
- **과금**: MCP 서버는 무료. **모델 실행만** 표준 fal 요금. 키는 요청마다 헤더로만 전달·저장하지 않는다고 명시.
- **어제와 구분**: 9/22 [fal H3 Max](https://fal.ai/learn/devs/introducing-h3-max-by-fal)는 **특정 비디오 모델의 속도·티어 가격**. 오늘은 **카탈로그 전체를 에이전트 도구로 여는 접속층**.

## 왜 중요한가
콘텐츠 파이프가 “모델 고르기 → SDK → 큐 폴링”에서 **한 문장 오케스트레이션**으로 내려온다. 태그라인·제품컷·보이스오버를 한 대화에서 체인하는 예시가 공식 블로그에 있다. 퍼스널 미디어·광고 A/B에 바로 붙는 인프라다.

## 기억할 것
- [fal 블로그](https://blog.fal.ai/connect-your-ai-to-1-000-models-with-the-fal-mcp-server/) · [fal.ai/mcp](https://fal.ai/mcp)
