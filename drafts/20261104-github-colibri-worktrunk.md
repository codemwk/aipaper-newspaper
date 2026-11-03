---
title: "GitHub 트렌드: ‘내 컴퓨터에서 744B 모델’ colibri, 에이전트 5~10개를 나란히 굴리는 worktrunk, 49명짜리 ‘게임 스튜디오’ — 11/3 급상승이 말해 주는 것"
date: 2026-11-04T07:08:00+09:00
category: "GitHub 트렌드"
slug: "github-colibri-worktrunk"
summary: "11/3 GitHub 일간 트렌딩 상위권: 1위는 여전히 claude-mem(하루 +1,138★). 새로 볼 만한 건 C로 만든 MoE 추론 엔진 colibri(★약 4.7만, 하루 +803) — 자주 쓰는 전문가는 GPU, 덜 쓰는 건 RAM, 나머지는 SSD에서 불러와 744B GLM-5.2를 상주 메모리 약 9.9GB로 돌린다. 에이전트마다 작업 폴더를 나눠 주는 git worktree 관리 CLI worktrunk(★약 1만), Claude Code를 에이전트 49명·워크플로 72개의 게임 개발 조직으로 만드는 Claude-Code-Game-Studios(하루 +1,181)."
---

## 한줄 요약
오늘의 키워드는 **“있는 장비로, 여러 에이전트를, 조직처럼”**. 큰 모델을 집 PC에서 돌리고, 에이전트 여러 개를 충돌 없이 병렬로 굴리고, 아예 회사 조직도를 에이전트로 짠다([GitStock 11/3 트렌딩](https://gitstock.org/trending/2026-11-03)).

## 1. colibri — “작은 엔진, 거대한 모델”
- **원리**: MoE(전문가 혼합) 모델은 수천억 파라미터라도 토큰마다 일부 ‘전문가’만 쓴다. colibri는 자주 쓰는 전문가는 GPU, 따뜻한 것은 RAM, 차가운 것은 **NVMe SSD에서 필요할 때 스트리밍**한다.
- **체감**: README 예시에서 744B GLM-5.2(int4)를 CPU 스트리밍으로 **상주 메모리 약 9.9GB**에 띄운다. 최소 사양은 RAM 8GB(16GB 권장), 디스크 22GB(가장 작은 모델). GPU는 선택.
- **범위**: 언어 모델 엔진 10종(GLM, Kimi K3, DeepSeek V4 Flash, Qwen3.6 계열 등)과 이미지·결정 모델. 기존 GGUF 파일을 그대로 읽는다. 순수 C, Apache-2.0, ★약 47,200([GitHub](https://github.com/JustVugg/colibri)).
- **주의**: SSD에서 읽는 만큼 **속도는 느리다**. ‘돌아간다’와 ‘쓸 만하게 빠르다’는 다른 문제.

## 2. worktrunk — 에이전트마다 ‘자기 책상’
Claude Code·Codex가 오래 혼자 일할 수 있게 되면서 5~10개를 동시에 돌리는 사람이 늘었다. 같은 폴더에서 돌리면 서로의 변경을 덮어쓴다. git의 worktree가 답인데 명령이 번거롭다. worktrunk는 **브랜치 이름 하나로 작업 폴더를 만들고 오가게** 해 주고, 훅 자동화·빌드 캐시 복사 같은 편의를 얹었다(Rust, ★약 10,400, [GitHub](https://github.com/max-sixty/worktrunk)).

## 3. Claude-Code-Game-Studios — 조직도를 통째로
Claude Code를 **에이전트 49명, 워크플로 스킬 72개**, 실제 게임 스튜디오 위계를 흉내 낸 조율 체계로 바꾼다(MIT, ★약 34,500, 11/3 하루 +1,181, [GitHub](https://github.com/Donchitos/Claude-Code-Game-Studios)).

## 왜 중요한가
지난번 저장하신 **orca·headroom(멀티 에이전트 운영)** 흐름과 같은 줄기다. 관심이 ‘더 똑똑한 에이전트 하나’에서 **‘여럿을 어떻게 나누고 기억시키고 싸게 돌리나’**로 옮겨 갔다 — 1위 claude-mem(세션 간 기억, ★약 11만)까지 포함해서 오늘 상위권이 전부 그 이야기다.
