---
title: "AI 콘텐츠: Amazon Polly 생성형 음성 엔진 교체 — 숫자·이메일·주소를 덜 틀리게 읽고, 새 목소리 14개 중 한국어 남성 ‘Hyunduk’, 서울 리전에서 바로"
date: 2026-10-21T07:05:00+09:00
category: "AI 콘텐츠"
slug: "amazon-polly-generative-voices"
summary: "AWS가 10/20 Amazon Polly Generative 엔진의 모델을 교체(기존 API 그대로 쓰는 ‘드롭인’ 업그레이드): 더 자연스럽고 정확한 발화, 낮은 지연. 숫자·이메일 주소·도로명 주소 같은 까다로운 텍스트 읽기 개선, SSML 태그 계속 지원, 저지연 스트리밍 API. 9개 로케일에 새 목소리 14개(한국어 Hyunduk, 미국 영어 Kenneth·Nate, 힌디 Kiara·Arjun 등)와 힌디어·핀란드어 신규. 서울·도쿄 등 11개 리전과 GovCloud 제공. 콜센터·챗봇·실시간 음성 에이전트·뉴스·교육·접근성 용도."
---

## 한줄 요약
AI 음성 경쟁이 ElevenLabs·OpenAI의 ‘목소리 디자인’ 쪽으로 쏠린 사이, AWS는 **기업 시스템이 이미 쓰고 있는 TTS**를 조용히 바꿨다. 2026-10-20 **Amazon Polly Generative** 엔진 뒤의 모델이 새것으로 교체됐다([AWS](https://aws.amazon.com/about-aws/whats-new/2026/10/polly-generative/)).

## 무엇이 바뀌었나
- **드롭인 업그레이드**: 코드를 바꾸지 않아도 Generative 음성이 더 자연스럽고 정확해진다. 지연도 낮다.
- **까다로운 텍스트**: **숫자, 이메일 주소, 도로명 주소**처럼 TTS가 자주 틀리는 부분을 더 믿을 만하게 읽도록 설계 — 발음 보정에 드는 손이 줄어든다.
- **기존 통제 유지**: SSML 태그로 속도·강세 등을 그대로 조정. **저지연 스트리밍 API**로 콜센터, 챗봇, LLM 기반 실시간 음성 에이전트에 붙이기 쉽다.

## 새 목소리
9개 로케일에 **14개**: 한국어 **Hyunduk**, 미국 영어 Kenneth·Nate, 호주 영어 Russell·Curtis, 힌디어/인도 영어 Kiara·Arjun, 독일어 Tina, 미국 스페인어 Carlos, 브라질 포르투갈어 Leo·Carolina, 핀란드어 Suvi 등. **힌디어·핀란드어**는 Generative 엔진에 처음 들어왔다. 
제공 리전: 미국 동부·서부, 프랑크푸르트·취리히·런던, 시드니·**서울**·싱가포르·도쿄, 캐나다, 그리고 공공용 GovCloud(미 서부).

## 왜 중요한가
화려한 데모보다 **‘이메일 주소를 제대로 읽는가’**가 실제 서비스의 품질을 가른다. 주문번호·전화번호·주소를 읽어야 하는 고객 응대 음성 에이전트라면 이번 교체가 체감될 가능성이 크다. 한국어 남성 생성형 목소리가 서울 리전에 추가된 것도 국내 서비스에는 실용적인 소식이다. 다만 AWS 발표는 품질 수치를 내놓지 않았으니, 기존 문장 세트로 **업그레이드 전후를 직접 비교**해 보는 게 좋다.

출처: [AWS What's New — Polly Generative engine upgraded (10/20)](https://aws.amazon.com/about-aws/whats-new/2026/10/polly-generative/)
