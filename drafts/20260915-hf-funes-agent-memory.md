---
title: "세컨드 브레인 — Hugging Face funes, ‘내가 소유하는’ 코딩 에이전트 기억"
date: 2026-09-15T07:45:00+09:00
category: "Second Brain"
slug: "hf-funes-agent-memory"
summary: "2026-09-03 HF 블로그. funes가 Claude Code·Codex·pi·Hermes 세션을 로컬 인덱싱. recall/get으로 원문+출처. 기본 로컬, 선택적으로 내가 소유한 HF 데이터셋으로 동기화. LLM Wiki·Obsidian 캐시와 같은 ‘파일에 두는 기억’ 줄기."
---

## 한줄 요약
[Hugging Face 블로그 — funes(2026-09-03)](https://huggingface.co/blog/funes)는 코딩 에이전트가 남긴 세션 트레이스를 **검색 가능한 내 기억**으로 바꾸는 도구다. Claude Code·Codex·pi·Hermes를 한 저장소에 인덱싱하고, 에이전트가 스스로 `recall`/`get`을 쓴다.

## 어떻게 동작하나
`curl …/install.sh | sh` 후 `funes add claude`(또는 codex/pi/hermes). 첫 인덱스·도구 주입·턴 완료 시 증분 인덱싱이 붙는다. 검색은 로컬 임베딩+BM25+크로스엔코더 리랭크+최근성. **결과는 요약이 아니라 원문 구절 + 에이전트·시각·세션·턴 출처**. 기본은 완전 로컬(Lance). `funes add codex org/funes-memory`처럼 바인딩하면 **내가 소유한(기본 private) HF 데이터셋**으로 따라다닌다. 푸시 전 시크릿 스캔. `funes ask`는 설치 없이 한 질문만 던지는 읽기 전용 모드.

## 왜 중요한가 (LLM Wiki와 맞닿는 지점)
어제 Obsidian 캐시·LLM Wiki 줄기와 같다. **컨텍스트를 프롬프트에 붙이지 말고, 소유 가능한 파일/데이터셋 그래프에 둔다.** Claude→Codex로 에이전트를 바꿔도 결정이 이어지고, 팀·OSS는 “검색 가능한 CLAUDE.md 역사”를 공개할 수 있다. 벤치에서는 recall이 핸드오프·컴팩션보다 싸다는 사내 측정이 소개됐지만, 커뮤니티 재현(hit@1 등)은 반감기 설정에 민감하다는 댓글도 있다.

## 기억할 것
- 레포: [github.com/huggingface/funes](https://github.com/huggingface/funes)
- 원칙: 기억은 **서비스 계정이 아니라 데이터셋**. LLM Wiki/Obsidian 인덱스의 코딩-에이전트 버전.
