---
title: "GitHub Hot: Alibaba OpenCodeReview — 결정론 파이프라인 + LLM 에이전트 리뷰"
date: 2026-09-25T07:08:00+09:00
category: "GitHub Hot"
slug: "alibaba-open-code-review"
summary: "alibaba/open-code-review(~40.7k★). 하이브리드 코드리뷰: 결정론 규칙(NPE·스레드·XSS·SQLi 등) + LLM 라인 코멘트. Claude Code·Codex·Cursor 등. OpenAI/Anthropic 호환."
---

## 한줄 요약
[alibaba/open-code-review](https://github.com/alibaba/open-code-review)는 알리바바 스케일에서 검증했다는 **하이브리드 코드 리뷰 도구**다. 결정론 파이프라인으로 확실한 버그 클래스를 잡고, LLM 에이전트가 **라인 단위 코멘트**를 단다(~40.7k★).

## 무엇이 다른가
- **규칙셋**: NPE, 스레드 세이프티, XSS, SQL injection 등 다국어 내장 규칙.
- **에이전트 호환**: Claude Code, Codex, Cursor, Kimi Code 등(README 배지).
- **모델**: OpenAI·Anthropic 호환 API.
- **메시지**: “빠르고 정확한 리뷰” — 순수 LLM 리뷰의 환각·누락을 **결정론 층**으로 보완하는 설계.

## 왜 중요한가
GitHub 트렌딩이 ‘스킬 카탈로그’에 치우친 주에, **프로덕션 리뷰 하네스**가 주간 스타를 끌어모은다. “에이전트가 코드를 쓴다” 다음 병목은 **누가 리뷰하느냐**다.

## 기억할 것
- [GitHub](https://github.com/alibaba/open-code-review) · [open-codereview.ai](https://open-codereview.ai)
