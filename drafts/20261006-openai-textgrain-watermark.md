---
title: "AI 모델: OpenAI textGrain — ChatGPT·Codex 텍스트에 ‘보이지 않는 워터마크’, EU부터·API는 옵트인"
date: 2026-10-06T07:04:00+09:00
category: "AI 모델"
slug: "openai-textgrain-watermark"
summary: "10/5 OpenAI: 단어 선택을 미세하게 기울여 통계 신호를 심는 textGrain. EU AI Act 투명성 의무(8/2 발효)에 맞춰 EU의 ChatGPT·Codex에 수주 내 적용, API는 전 세계 옵트인(기본 OFF). 400토큰 기준 탐지 ~95%(FPR 1%), 단어 10% 동의어 치환 시 92%→66%. 탐지기는 승인 연구기관만."
---

## 한줄 요약
OpenAI가 10월 5일 텍스트 워터마크 기술 **textGrain**을 공개했다. 문장에 기호를 넣는 게 아니라, 둘 다 자연스러운 단어 후보 중 **비밀 키에 따라 한쪽을 살짝 더 고르게** 해서 긴 글 전체에 통계적 패턴을 남긴다. 복사·붙여넣기해도 따라간다([TechCrunch](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/)).

## 어디에, 어떻게
- **EU만 자동 적용**: 8월 2일 발효된 EU AI Act 투명성 규정 때문. 앞으로 몇 주 동안 EU의 **ChatGPT·Codex 전 요금제**에 순차 적용. 전 세계 기본값으로 만들진 않았다.
- **API는 옵트인(기본 OFF)**: 전 세계 API 고객이 오늘부터 일부 모델에 켤 수 있다. 프로젝트·조직 단위 설정이라 요청 코드를 바꿀 필요가 없다([The New Stack](https://thenewstack.io/openai-api-text-watermarking/)).
- **Anthropic과 대비**: Claude는 8월 발표대로 **모델 레벨에서 전 세계 적용**(API 포함, 옵트아웃 언급 없음). OpenAI는 “고객이 의무와 경험에 맞게 선택”하는 쪽.

## 얼마나 잡히고, 얼마나 쉽게 지워지나
- 탐지율(오탐 1% 기준): 200토큰 약 80%, 400토큰 약 95%. 수학·번역·짧은 글·**코드**는 선택지가 적어 더 어렵다.
- 400토큰 글에서 단어 10%를 동의어로 바꾸면 92%→66%, 25% 바꾸면 **17%**.
- Astra 모델로 DeepSWE·Terminal-Bench 등을 돌려 보니 워터마크 ON/OFF 성능 차이는 의미 없었다고 한다.
- **탐지기는 공개하지 않는다** — 승인된 연구·전문 기관에만 먼저. OpenAI 스스로 “워터마크가 없다고 사람이 썼다는 증거는 아니다”, “있어도 사람이 얼마나 편집·판단했는지는 알 수 없다”고 못 박았다. 기술은 오픈소스화 예정.

## 왜 중요한가
AI가 쓴 글을 **나중에 기계가 식별할 수 있는 시대**가 규제와 함께 시작됐다. 콘텐츠를 AI로 만들어 배포하는 사람(뉴스레터·블로그·마케팅)에게 실무 포인트는 셋: (1) EU 사용자를 상대하면 출처 표기 정책을 미리 정할 것, (2) API로 서비스를 만든다면 **켤지 말지가 이제 제품 결정**, (3) 워터마크는 ‘부정행위 탐지기’가 아니므로 이걸로 사람을 판정하는 도구는 경계할 것.

## 기억할 것
- 이미지·오디오는 이미 C2PA·SynthID 적용 중, 텍스트가 마지막 퍼즐.
- [TechCrunch 10/5](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/) · [The New Stack 10/5](https://thenewstack.io/openai-api-text-watermarking/) · [9to5Mac](https://9to5mac.com/2026/10/05/openai-details-new-text-watermarking-system-for-chatgpt-codex-and-the-api/)
