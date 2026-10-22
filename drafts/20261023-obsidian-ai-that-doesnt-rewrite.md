---
title: "세컨드 브레인 / PKM: ‘내 글을 고치지 않는 AI’ — Obsidian에 코멘트만 다는 Automatic Paragraph Review 등장, AI 플러그인 고르는 새 기준 3가지"
date: 2026-10-23T07:09:00+09:00
category: "세컨드 브레인 / PKM"
slug: "obsidian-ai-that-doesnt-rewrite"
summary: "10/22 Obsidian 플러그인 업데이트 흐름(synon Obsidian×AI 데일리, obsidianstats): Automatic Paragraph Review 1.0.1(William Booth, MIT)은 노트를 절대 고치지 않고 이해·논리·사실의 빈틈에 점선 밑줄과 코멘트만 단다. 기존 Codex CLI 로그인을 그대로 써 API 키 불필요, 읽기 전용 샌드박스·셸/웹검색 차단, 보내는 범위는 선택 문단+앞 최대 8,000자(프런트매터·코드·표 제외), Obsidian 1.13.7+ 데스크톱. 같은 방향: Bilingual Reader 1.0.1(원문 그대로 두고 번역은 별도 파일), Selection AI Button 1.3.1(자동 전송 없음). 그 밖에 Vault Intelligence 9.9.1 Anthropic 프리셋, Voxtral Transcribe 1.18.0(Voxtral 3 전환). 고르는 기준: 출력이 본문에 들어가나·전송은 내가 누르나·결과는 어디 저장·동기화되나."
---

## 한줄 요약
지금까지 Obsidian AI 플러그인의 화두는 “AI가 노트를 **얼마나 잘** 고쳐 주나”, 그리고 “AI가 고친 걸 사람이 **승인**하게 하자”였다. 이번 주엔 아예 다른 답이 나왔다: **고치지 않는다.**

## Automatic Paragraph Review 1.0.1
William Booth가 만든 데스크톱용 플러그인(MIT). 내가 쓴 문장 중 **이해·논리·사실의 빈틈**이 보이는 곳에 **점선 밑줄**을 긋고, 마우스를 올리면 코멘트가 뜬다([synon 정리](https://synon.co.jp/article/news/2026-10-22-obsidian-ai-daily), [obsidianstats](https://www.obsidianstats.com/updates)).
- **절대 안 고친다**: 노트를 다시 쓰지도, AI 문장을 Markdown에 넣지도 않는다고 명시. 코멘트는 “확인해 볼 제안”이지 출처 붙은 팩트체크가 아니라고도 적었다.
- **API 키 불필요**: 공식 Codex CLI에 `codex login` 해 두면 그 로그인을 쓴다. 플러그인은 자격 정보를 저장·복사하지 않는다. 검토는 일회용 `codex exec`로 돌고, **셸·웹 검색·연결 앱은 꺼져 있으며 샌드박스는 읽기 전용**. 사용량은 Codex 계정 한도에서 빠진다.
- **보내는 범위**: 고른 문단 + 같은 노트의 바로 앞 **최대 8,000자**. 프런트매터·코드 블록·인용·표는 안 보낸다. 결과는 플러그인 `data.json`에 남아, 플러그인 데이터를 동기화하면 같이 동기화된다.
- **조건**: Obsidian 1.13.7 이상 데스크톱. 확인된 환경은 macOS + Codex CLI 0.163.0뿐, 모바일·읽기 모드 미지원.

## 같은 방향의 플러그인들
- **Bilingual Reader 1.0.1**: 11개 언어 번역, **원문은 그대로** 두고 번역본을 별도 파일로 저장해 분할 화면으로 연다.
- **Selection AI Button 1.3.1**: 선택한 문장을 질문 입력창에 **넣기만** 한다. 자동 전송·시스템 클립보드 사용 없음, 노트를 편집하면 대기 중 작업 취소.
- 그 밖에: **Vault Intelligence 9.9.1**이 Anthropic 프리셋 추가(단, Anthropic은 임베딩을 제공하지 않음), **Voxtral Transcribe 1.18.0**이 Mistral Voxtral 3로 전환하며 볼트 속 이름·용어를 받아쓰기에 반영.

## AI 플러그인 고르는 새 기준 3가지
1. **AI 출력이 본문에 들어가나**, 아니면 별도 파일·별도 화면에 머무나?
2. **전송은 내가 직접 누르나**, 자동으로 나가나?
3. **결과가 어디에 저장되고, 어디로 동기화되나?** (플러그인 데이터 폴더도 동기화 대상인지 확인)

## 왜 중요한가
세컨드 브레인의 가치는 “내가 생각한 흔적”에 있다. AI가 문장을 매끈하게 고칠수록 노트는 깔끔해지지만 **내 생각은 흐려진다.** 코멘트만 다는 AI는 편집자가 아니라 **질문을 던지는 독자** 역할이라, 배우고 쓰는 용도의 볼트에 특히 잘 맞는다. 기존 구독(Codex) 로그인을 재사용하는 방식은 편하지만, 사용량 한도와 전송 범위를 꼭 알고 쓰자.

> 지난번 저장하신 Obsidian Copilot ‘에이전트 편집 검토’ 기사(10/17)와 이어지는 소식입니다 — 이번엔 ‘검토할 편집 자체를 만들지 않는’ 쪽.

출처: [synon — Obsidian×AI 데일리 (10/22)](https://synon.co.jp/article/news/2026-10-22-obsidian-ai-daily) · [obsidianstats — Plugin Updates](https://www.obsidianstats.com/updates)
