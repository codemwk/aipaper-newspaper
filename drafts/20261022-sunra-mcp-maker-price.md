---
title: "AI 콘텐츠: Sunra MCP — Claude·ChatGPT 대화창에서 Seedance·Veo·Kling·Nano Banana를 부르고, 값은 ‘모델 제작사 API 가격’ 그대로라는 약속"
date: 2026-10-22T07:06:00+09:00
category: "AI 콘텐츠"
slug: "sunra-mcp-maker-price"
summary: "크리에이티브 플랫폼 Sunra가 Sunra MCP 출시: Claude·ChatGPT엔 커넥터(mcp.sunra.ai, 브라우저 로그인), Claude Code·Codex·Cursor·Antigravity 등엔 CLI 설치로 이미지·영상·음성·3D 모델 호출. 규칙: 제작사가 API 가격을 공개한 모델은 그 가격 그대로(1크레딧=$0.01). 예: Seedance 2.5 720p·오디오 초당 $0.2311(ByteDance 가격). Basic 월 $12(1,200크레딧)는 제작사 가격과 동일, Pro($29~99)·Creator($125~2,051)와 연간 결제는 크레딧 단가 최저 $0.0037까지. 41개 설정 비교표에서 Basic 기준 동률이 많고 일부는 경쟁사가 더 쌈(Replicate GPT Image 2는 39%↓ 등). SNS의 ‘초당 $0.039부터’는 설정·요금제 근거 불명(LHC 지적). 생성 전 비용 추정·확인, 프롬프트는 각 모델 제작사로 전달."
---

## 한줄 요약
영상 모델 가격표를 탭 하나에 띄워 놓고 다른 탭에서 생성하던 사람을 겨냥한 제품이다. **Sunra MCP**는 쓰던 AI 비서 안에서 생성 모델을 부르게 하고, 가격은 **“모델을 만든 회사의 API 가격 그대로”** 받겠다고 했다([Sunra 공식 발표](https://sunra.ai/blog/introducing-sunra-mcp)).

## 어떻게 붙나
- **Claude·ChatGPT**: 커넥터/플러그인에 `mcp.sunra.ai`를 추가하고 브라우저로 로그인 — API 키가 필요 없다.
- **Claude Code·Codex·Cursor·Antigravity 등**: 설정 프롬프트로 Sunra CLI를 설치·로그인.
- 카탈로그: Seedance 2.5부터 Veo 3.1, Kling 3.0, Nano Banana Pro, 3D용 Meshy까지. 비서가 **생성 전 비용을 추정**하고, 자동 확인을 켜지 않으면 **사용자가 확인해야** 과금된다([LHC](https://www.lhc.media/en/media/ai-watch/access-to-ai-models-at-no-extra-cost-sunra-mcps-calculation)).

## 가격 구조
1크레딧 = $0.01 기준으로 제작사 가격을 그대로 크레딧으로 환산한다(제작사가 가격을 바꾸면 따라 바꿈).
| 요금제 | 월 가격 | 월 크레딧 | 크레딧당(월/연 결제) |
|---|---|---|---|
| Basic | $12 | 1,200 | $0.0100 / $0.0075 |
| Pro | $29~99 | 3,500~12,000 | 약 $0.0082 / $0.0049 |
| Creator | $125~2,051 | 17,000~280,000 | 약 $0.0073 / $0.0037 |

예: **Seedance 2.5(720p, 오디오)** 는 ByteDance API 가격 **초당 $0.2311** → 약 23크레딧. Basic에선 그대로, Creator 연간 결제면 같은 크레딧이 훨씬 싸진다.

## 솔직한 비교표, 그리고 빈칸
- Sunra는 41개 모델 설정을 Runway·Higgsfield·Krea·Pika·fal·Replicate 등 9곳과 비교하며 **지는 곳도 표시**했다: GPT Image 2는 Replicate가 39% 쌈, Kling 3.0 Pro는 Magnific이 46% 쌈(오디오 포함 여부 불명) 등. Creator 연간 결제 기준으론 41개 중 37개에서 더 싸다고 주장(모든 크레딧을 다 쓴다는 가정).
- 반면 SNS에 돈 “Seedance 2.5 **초당 $0.039부터**” 같은 문구는 어떤 설정·요금제 기준인지 설명이 없다(LHC 지적). 예산은 **공식 표**로 잡을 것.
- 남은 크레딧은 이월되지 않는다. Sunra는 프롬프트로 자체 모델을 학습하지 않는다지만, 데이터는 **선택한 모델의 제작사**(OpenAI·Google·ByteDance·Kuaishou 등)로 간다.
- Midjourney·Suno는 카탈로그에 있지만 공개 API 가격이 없어 비교에서 빠졌다.

## 왜 중요한가
생성 AI 앱의 수익은 대개 **크레딧 마진**에서 나왔다. ‘제작사 가격 그대로’는 그 마진을 포기하고 **구독(크레딧 선구매)과 편의성**으로 버티겠다는 선언이다. 그리고 생성이 **대화 속 한 단계**가 되면, “샷 리스트 짜기 → 샷별 영상 생성 → 4번 샷만 다시”를 한 창에서 할 수 있다. 테스트 팁: 이미 만든 샷 하나를 같은 프롬프트로 돌려 **초당 비용·대기 시간·결과**를 비교하고, 10개 생성 후 청구액을 공시 단가와 대조해 볼 것([Unhindered](https://unhindered.ai/news/sunra-mcp-seedance-2-5-inside-claude-chatgpt-from-0-039-per-second)).

출처: [Sunra — Introducing Sunra MCP](https://sunra.ai/blog/introducing-sunra-mcp) · [LHC — Sunra MCP’s calculation](https://www.lhc.media/en/media/ai-watch/access-to-ai-models-at-no-extra-cost-sunra-mcps-calculation) · [Unhindered (10/21)](https://unhindered.ai/news/sunra-mcp-seedance-2-5-inside-claude-chatgpt-from-0-039-per-second)
