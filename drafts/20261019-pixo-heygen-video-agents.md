---
title: "AI 콘텐츠: 노래 박자에 맞춰 컷을 자르는 Pixo, 에이전트가 직접 부르는 HeyGen Video 1 — 이번 주 AI 영상은 ‘예쁜 클립’보다 ‘편집과 배치(batch)’"
date: 2026-10-19T07:05:00+09:00
category: "AI 콘텐츠"
slug: "pixo-heygen-video-agents"
summary: "① Pixo(10/17): 뮤직비디오 에이전트에 ‘비트 인식 편집’ — 박자에 맞춰 컷을 나누되 가사 구절 사이를 우선, 리드·백업·애드리브 보컬을 캐릭터에 배정해 립싱크(끌 수도 있음). 곡 구간·가사·가수를 분석해 스토리보드 → Seedance·Kling·Veo·Hailuo 등으로 생성 → 타임라인 조립, 16:9·9:16·3:4·1:1, 480p~4K. 무료 200크레딧, Basic 월 $9.90(연)·Pro $39.90(연, 4K). ② HeyGen Video 1(10/16): 원격 MCP 서버에 탑재 — Claude·Cursor·Codex에서 OAuth 로그인만으로 5~15초 클립(대사·환경음·효과음 한 번에) 생성, HeyGen 크레딧 차감(무료 플랜 월 3개). MiniMax H3 기반 미세조정, OpenRouter 기준 768p 초당 $0.03(HeyGen 표기)."
---

## 한줄 요약
AI 영상 경쟁의 초점이 바뀌고 있다. 한 컷을 얼마나 그럴듯하게 뽑느냐에서, **여러 컷을 음악·이야기에 맞게 이어 붙이는 편집**과 **에이전트가 대량으로 돌리는 배치 생산**으로. 이번 주 나온 두 업데이트가 그 두 방향을 대표한다.

## ① Pixo — 노래를 넣으면 ‘연출된’ 뮤직비디오
2025년 창업한 **Pixo**가 2026-10-17 뮤직비디오 에이전트에 세 가지를 더했다([Derivative Works 정리](https://cite.io/blog/pixo-adds-beat-aware-music-video-editing/)).
- **비트 인식 편집**: 음악의 박자를 기준으로 컷 경계를 정하되, **가사 구절 사이의 빈 곳**을 우선한다. 노래 한 줄 중간에서 화면이 끊기지 않게.
- **가수 구분·듀엣**: 리드 보컬, 백업 보컬, 애드리브를 구분해 화면 속 캐릭터에 배정하고, 시간 맞춘 지시로 **립싱크**를 만든다. 내러티브 영상이라면 립싱크를 끌 수 있다.
- **곡 단위 연출**: 곡의 구간·가사·타이밍을 분석해 **스토리보드**를 만들고, 각 샷이 맡은 음악 구간과 길이를 그대로 들고 생성 단계로 간다. 공연자·의상·장소 레퍼런스를 전 장면에 재사용하고, 마음에 안 드는 샷만 바꿀 수 있다([Pixo](https://pixo.video/ai-music-video-generator)).
- **사양**: 오디오 WAV·MP3·OGG·M4A 20MB까지, 16:9·9:16·3:4·1:1, 해상도 480p~4K(생성 모델에 따라). SLOP TV에 따르면 생성은 Seedance·Kling·Veo·Hailuo 등으로 한다.
- **가격**(SLOP TV, 10/18 확인): 무료 200크레딧, **Basic 월 $9.90(연 결제)·월 결제 $19.90**(1080p 상한), **Pro 월 $39.90(연 결제)**로 4K.
- **주의**: Pixo 자체 가이드도 오디오 교체 후 입 모양이 완벽하지 않을 수 있으니 보컬 클로즈업은 확인하고 필요하면 컷어웨이를 쓰라고 권한다.

## ② HeyGen Video 1 — 에이전트가 부르는 영상 모델
HeyGen은 2026-10-16 범용 영상 모델 **HeyGen Video 1**을 자사 **원격 MCP 서버**에 올렸다([SLOP TV, 10/18](https://sloptvnews.com/ai-video-tools-october-picks/)).
- **무엇**: 9/30 출시된 HeyGen의 첫 범용 영상 모델(아바타 제품이 아님). **MiniMax H3를 기반으로 미세조정**했다. 텍스트·이미지·레퍼런스로 **5~15초** 클립을 만들고 **대사·환경음·효과음을 한 번의 호출**에 같이 생성한다. 480p·768p·2K, 21:9부터 9:16까지([neurocartel 정리](https://neurocartel.com/en/blog/heygen-video-1-mcp)).
- **연결**: Claude·Claude Code·Cursor 등에서 `https://mcp.heygen.com/mcp/v1/`을 추가하고 **OAuth로 한 번 로그인** — API 키가 필요 없다. 비용은 기존 HeyGen 크레딧에서 빠지고, **무료 플랜(월 3개)**을 포함한 모든 플랜에서 된다([HeyGen MCP 문서](https://developers.heygen.com/mcp/overview)).
- **가격**: HeyGen이 밝힌 768p 정가는 **초당 $0.03**(비교: Veo 3.1 $0.40, HeyGen 표기). OpenRouter에서는 10월 말까지 할인이 걸려 있어 날짜별로 확인 필요. 10초 클립 1,000개면 정가로 약 $300.
- **약점**: HeyGen 프롬프트 노트는 긴 화면 텍스트, 머리카락 같은 부드러운 움직임, 손 클로즈업을 가장 불안정한 영역으로 꼽는다. 15초가 상한이라 긴 장면은 이어 붙여야 한다.

## 왜 중요한가
두 업데이트를 합치면 1인 제작 파이프라인이 보인다: **에이전트가 대본·샷 리스트를 짜고(MCP로 HeyGen 같은 모델을 직접 호출), 편집 도구가 음악에 맞춰 조립한다.** ANDRSN 관점에서 브랜드 필름·사운드 작업을 한다면, 이제 비교 기준은 “어느 모델이 예쁜가”보다 **① 초당 단가 ② 같은 인물·제품을 컷마다 유지하는 레퍼런스 기능 ③ 음악·대사와의 싱크**다.

출처: [Derivative Works — Pixo 비트 인식 편집 (10/17)](https://cite.io/blog/pixo-adds-beat-aware-music-video-editing/) · [Pixo 뮤직비디오 생성기](https://pixo.video/ai-music-video-generator) · [SLOP TV — 이번 주 AI 영상 도구 5종 (10/18)](https://sloptvnews.com/ai-video-tools-october-picks/) · [neurocartel — HeyGen Video 1 MCP·가격 (10/17)](https://neurocartel.com/en/blog/heygen-video-1-mcp) · [HeyGen MCP 문서](https://developers.heygen.com/mcp/overview)
