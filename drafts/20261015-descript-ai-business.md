---
title: "AI 비즈니스: Descript — ‘문서처럼 고치는 영상 편집기’가 에이전트 창구로, 미터 두 개(미디어 시간 + AI 크레딧)로 받는 구독"
date: 2026-10-15T07:00:00+09:00
category: "AI 비즈니스"
slug: "descript-ai-business"
summary: "Descript는 녹취록을 고치면 영상이 고쳐지는 편집기에서, AI 공동 편집자 Underlord를 Claude·ChatGPT·Cursor(MCP)와 API로 부르는 ‘영상 작업 백엔드’로 이동 중. 가격은 Free $0, Hobbyist $16·Creator $24·Business $50(연간 결제 기준, 월 결제 $24/$35/$65), Enterprise 별도. 과금 미터는 미디어 시간과 AI 크레딧 두 개이고, API·MCP도 같은 잔고를 쓴다(소진 시 402 에러). 최근 공개 투자는 2022년 OpenAI Startup Fund 주도 Series C $5,000만."
---

## 한줄 요약
**Descript**는 “녹취록을 지우면 영상도 잘린다”는 텍스트 기반 편집으로 팟캐스터·크리에이터 시장을 연 회사다. 2026년 지금 이 회사의 무게중심은 편집 화면보다 **AI 공동 편집자 ‘Underlord’**, 그리고 그 Underlord를 **바깥 AI가 부르게 하는 API·MCP**로 옮겨 가고 있다. 사람이 앱을 열지 않아도 Claude나 ChatGPT가 “이 영상 가져와서 필러 단어 지우고 60초 하이라이트 만들어 게시해”를 대신 시키는 구조다([MCP 안내](https://help.descript.com/api-and-mcp/mcp), [API 안내](https://help.descript.com/api-and-mcp/api)).

## 숫자가 말하는 구조 (공개 가격, 2026-10-15 확인)
- **Free $0**: 월 **60분** 미디어, 720p, 워터마크. 카드 없이 시작.
- **Hobbyist**: 연간 결제 시 **$16**/인·월(월 결제 $24). 월 **10시간** 미디어, **400** AI 크레딧, 1080p 무워터마크, Underlord·Studio Sound·필러 단어 제거, 커스텀 보이스 클론.
- **Creator**: 연간 **$24**(월 $35). **30시간**, **800** 크레딧, 4K, 최대 3인 팀, 최신 모델로 영상 생성, 스톡 라이브러리 무제한, **충전(top-up)** 가능.
- **Business**: 연간 **$50**(월 $65). **40시간**, **1,500** 크레딧, 팀 전체 Brand Studio, 30+ 언어 번역·더빙, 사진/텍스트로 아바타 생성, SLA 우선 지원, 최대 5인.
- **Enterprise 별도**: SSO·SCIM·감사 로그, 학습 제외·보존 기간 설정, 맞춤 MSA, 전담 CSM. SOC 2 Type II.
- **투자**: 2022-11 **Series C $5,000만**(OpenAI Startup Fund 주도, a16z·Redpoint·Spark 참여), 누적 **$1억**. 당시 The Information은 기업가치를 약 **$5.5억**으로 보도([TechCrunch](https://techcrunch.com/2022/11/15/ai-powered-media-editing-app-descript-lands-fresh-cash-from-openai/)). 이후 공개 라운드는 찾지 못했다.

> 참고: 일부 가격 추적 사이트가 10/13 “Free·Business·Enterprise 플랜 삭제”를 기록했지만, 10/15 현재 공식 가격 페이지에는 모두 그대로 있다. 스크래핑 오류로 보고 사실로 다루지 않았다.

## 돈이 흐르는 구조
**1) 미터가 두 개다** — *미디어 시간*은 불러오거나 녹화한 원본 분량(전사 여부와 무관), *AI 크레딧*은 Underlord·Studio Sound·Eye Contact·생성 미디어·아바타 사용량이다. 원본이 긴 팟캐스트 팀은 시간에서, 생성·보정을 많이 쓰는 마케팅 팀은 크레딧에서 상위 플랜으로 밀려 올라간다. 충전은 Creator부터라 “무료→저가 플랜에서 오래 버티기”가 어렵게 설계돼 있다.
**2) API·MCP도 같은 잔고** — 외부 에이전트가 가져오기(import)를 하면 미디어 시간을, Underlord 편집을 시키면 크레딧을 쓴다. 둘 중 하나라도 바닥나면 **HTTP 402(결제 필요)**를 돌려준다. 즉 “에이전트 연동”은 무료 부가기능이 아니라 **사용량을 늘리는 새 유입구**다. MCP는 로그인 기반·**드라이브 하나 단위**로 묶이고, 렌더 파일은 게시(web link) 후 서명 URL로만 받는 등 경계도 분명하다.
**3) 모델은 사서 쓰고, 고르는 건 사용자** — 10/12 릴리스 노트 기준 AI 음성은 **ElevenLabs v4**, 유료 플랜 영상 생성 기본값은 **MiniMax H3 Max Turbo**(무료는 PixVerse V4.5), 모델 선택기엔 Gemini 3.8 Flash가 추가됐고 Enterprise 기본은 Claude Opus 5.5다([릴리스 노트](https://descript.canny.io/changelog/release-roundupoctober-12-2026)). Underlord v2는 영상 하나를 끝까지 편집하는 데 크레딧이 약 **20% 덜 든다**고 회사가 밝혔다([Underlord v2](https://descript.canny.io/changelog/announcingunderlord-v2), 회사 테스트·독립 검증 없음). 비싼 모델을 고를수록 크레딧이 빨리 닳는 구조라, **모델 원가를 사용자 선택으로 넘기는** 방식이다.
**4) 팀 기능이 상위 플랜의 이유** — Brand Studio(공용 템플릿·가드레일), 더빙, 아바타, 비동기 녹화 요청(Enterprise) 같은 “조직이 쓸 때만 필요한” 기능이 Business 이상에 몰려 있다.

## 왜 중요한가
어제 다룬 Clueso가 “제품 화면을 다시 찍어 주는 유지보수”를 판다면, Descript는 **편집이라는 노동 자체를 사용량 미터로 바꿔** 판다. 경쟁자가 생성 모델(아바타·합성 영상)이라면, Descript의 해자는 **원본 녹음·녹화가 이미 쌓여 있는 드라이브**와 텍스트 기반 편집 습관이다. 위험도 분명하다: 핵심 생성 기능을 ElevenLabs·MiniMax·Anthropic 등 **외부 모델에 의존**하므로, 원가가 오르면 크레딧 단가로 전가될 수밖에 없다. ANDRSN 관점에선 “에이전트가 우리 앱을 부르게 하되, **부를 때마다 계량기가 돈다**”는 설계가 가장 배울 점이다.

출처: [Descript Pricing](https://www.descript.com/pricing) · [Descript MCP overview](https://help.descript.com/api-and-mcp/mcp) · [Descript API](https://help.descript.com/api-and-mcp/api) · [Release roundup—Oct 12, 2026](https://descript.canny.io/changelog/release-roundupoctober-12-2026) · [Underlord v2](https://descript.canny.io/changelog/announcingunderlord-v2) · [TechCrunch (2022 Series C)](https://techcrunch.com/2022/11/15/ai-powered-media-editing-app-descript-lands-fresh-cash-from-openai/)
