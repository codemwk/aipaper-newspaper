---
title: "AI 콘텐츠: OpenAI ‘글로 목소리 만들기’ 정식 출시 — “차분하고 안심되는 성인 목소리” 한 줄이면 브랜드 음성, 생성은 무료, 한국어 새 음성 ‘Noeul’"
date: 2026-10-18T07:05:00+09:00
category: "AI 콘텐츠"
slug: "openai-prompt-to-voice"
summary: "OpenAI API(10/16): prompt-to-voice 전 고객 정식 출시 — 텍스트 설명으로 목소리를 만들어 저장, GPT-Live 세션에서 재사용. API와 음성 Playground 지원. 생성 무료, 말할 때만 일반 GPT-Live 세션 요금. GPT-Live 전용(TTS·Realtime·Chat Completions 불가). 녹음 기반 음성 복제는 별도·동의 요건. 새 GPT-Live 음성 9종(독일어 3, 프랑스어 2, 힌디어 1, 일본어 2, 한국어 Noeul). 10/15엔 GPT-Live에 Decisions API 네이티브 연동."
---

## 한줄 요약
브랜드 전용 목소리를 만들려면 성우를 섭외하고 녹음하고 라이선스를 맺어야 했다. 2026-10-16부터 OpenAI API 고객은 **목소리를 글로 설명하는 것만으로** 새 음성을 만들 수 있다. 예를 들면 “차분하고 안심되는 성인 목소리, 고객 지원용” 같은 한 줄이다([OpenAI 커스텀 음성 가이드](https://developers.openai.com/api/docs/guides/custom-voices) · [Ahead of the Bot 정리](https://aheadofthebot.com/news/2026-10-16-openai-prompt-to-voice/)).

## 어떻게 쓰나 (코드 없이)
1. API 또는 **음성 Playground**에서 이름과 설명을 넣어 ‘프롬프트형 음성’을 만든다.
2. 돌려받은 음성 ID를 저장해 두고, 실시간 대화 모델 **GPT-Live** 세션에서 그 목소리로 말하게 한다.
3. **만드는 건 무료**, 실제로 말할 때(Playground에서 들어 보는 것 포함)만 일반 GPT-Live 세션 요금이 붙는다.

## 꼭 알아야 할 경계선
- **GPT-Live 전용**이다. 일반 TTS(문장 읽기) API, Realtime API, Chat Completions에선 쓸 수 없다. 내레이션 파일을 대량으로 뽑는 용도라면 아직 맞지 않는다.
- **실제 사람 목소리를 녹음해 복제하는 기능**은 별개이며, 자격 제한과 동의 요건이 따로 있다.

## 새 음성 9종 — 한국어 ‘Noeul’ 포함
같은 날 GPT-Live 기본 음성도 9개 늘었다: 독일어 Nuri·Juni·Flitz, 프랑스어 Brise·Sillage, 힌디어 Nira, 일본어 Harema·Shida, 그리고 **한국어 Noeul**. 하루 전(10/15)에는 GPT-Live가 사용자가 말하는 도중에도 판단 API(Decisions)를 바로 호출할 수 있게 됐다 — 말이 끝나기 전에 앱이 움직일 수 있다는 뜻이다(MUVO 정리).

## 왜 중요한가
음성 AI의 경쟁 축이 “누가 더 자연스럽나”에서 **“누가 더 빨리 ‘우리 브랜드 목소리’를 갖게 해 주나”**로 옮겨 가고 있다. 녹음 없이 설명만으로 목소리를 만들면 실존 인물 목소리 도용 위험은 줄고, 브랜드는 성격(나이대·온도·말 속도)을 **문장으로 정의한 ‘보이스 가이드’**를 그대로 제품에 꽂을 수 있다. ANDRSN 같은 브랜드 스튜디오라면 로고·컬러처럼 **‘브랜드 보이스 프롬프트’를 브랜드 시스템의 한 항목**으로 납품하는 시대가 온 셈이다. 반대로 로컬에서 같은 일을 하고 싶다면 이번 주 GitHub에서 급상승한 오픈소스 VoiceStudio(별도 기사)가 대안이 된다.

출처: [OpenAI — Custom voices 가이드](https://developers.openai.com/api/docs/guides/custom-voices) · [OpenAI API Changelog](https://developers.openai.com/api/docs/changelog) · [Ahead of the Bot (10/16)](https://aheadofthebot.com/news/2026-10-16-openai-prompt-to-voice/) · [MUVO 10/17 정리](https://muvoai.com/reports/daily-ai-news-updates-2026-10-17/)
