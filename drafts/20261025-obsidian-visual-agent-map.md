---
title: "세컨드 브레인 / PKM: Obsidian ‘Visual Agent Map’ — 큰 질문을 ‘주제 지도’로 쪼개고 가지마다 따로 조사, 카드는 전부 내 볼트의 마크다운. “AI는 생각을 대신하지 말고 생각을 도와야”"
date: 2026-10-25T07:10:00+09:00
category: "세컨드 브레인 / PKM"
slug: "obsidian-visual-agent-map"
summary: "Obsidian 커뮤니티에 새 플러그인 Visual Agent Map(VAM)이 소개됐다(Apache-2.0, 무료). 질문 하나를 AI와 함께 다단계 주제 지도로 쪼개되, 제안마다 내가 승인해야 추가된다. 원하는 가지만, 혹은 여러 가지를 백그라운드로 조사하고, 카드마다 ‘교과서’ 같은 노트 스타일을 고른다. 끝까지 맡기는 AIM 모드는 하위 주제를 채운 뒤 출처가 달린 문서로 마무리. API 키 대신 내 Codex CLI·Claude Code 로그인을 쓰고, AI의 수정은 초안으로 와서 승인 전엔 노트가 안 바뀐다. 데스크톱 전용(macOS 확인)."
---

## 한줄 요약
새 주제를 공부할 때 막히는 건 답이 아니라 **‘질문의 모양’을 모른다는 것**이다. 채팅창은 긴 답 하나를 줄 뿐. **Visual Agent Map**은 질문을 **주제 지도**로 펼쳐 놓고, 어느 가지를 더 팔지 내가 고르게 한다([Obsidian 포럼](https://forum.obsidian.md/t/visual-agent-map-turn-a-big-question-into-a-visual-research-map-with-ai-kept-as-markdown/119702)).

## 세 가지 모드
| 모드 | 하는 일 |
|---|---|
| **Visual maps** | 질문 → AI가 다단계 목차 제안 → **하나씩 검토 후 추가**. 가지 하나 또는 여러 개를 백그라운드 조사, 노트 스타일 선택, 비슷한 주제 병합·하위 주제를 부모로 통합 |
| **AIM**(Adaptive Inquiry Map) | 질문과 배경을 주고 첫 질문에 한 번 답하면 끝까지 조사. 지도가 채워지는 걸 보다가 **출처 링크가 달린 문서**로 마무리(MindSearch 등 연구에서 착안) |
| **Coffee Tables** | 덜 익은 아이디어를 가상 AI 손님들과 대화로 굴려 보고, 관찰자 메모를 나중에 다시 보기 |

## 내 볼트를 지키는 설계
- **모든 카드가 일반 마크다운 노트** — 링크·편집·삭제 자유, 플러그인을 지워도 노트는 남는다. AI 없이 수동 지도만 써도 된다.
- **API 키를 저장하지 않는다**: AI 작업은 로컬의 **Codex CLI나 Claude Code 로그인**을 통해 실행(그 구독 한도에서 차감). 텔레메트리 없음.
- **AI 수정은 초안**으로 도착 — 승인 전까지 노트는 그대로.
- 한계: 데스크톱 전용, macOS만 확인(Windows·Linux 미검증). 여러 주제를 동시에 조사하면 한도를 많이 쓰고, 일부 주제는 실패할 수 있다. 제작자도 “출처가 있다고 주장이 참인 건 아니다”라고 명시.

## 왜 중요한가
이번 달 PKM 플러그인들의 공통 기준이 또렷해졌다 — **읽기 우선, 승인 후 쓰기, 결과는 내 마크다운**(Glossa·Paragraph Review·xiaoji와 같은 줄기). VAM은 거기에 **‘탐색의 구조’**를 더했다. LLM Wiki가 “아는 것을 정리”하는 도구라면, VAM은 “모르는 것을 지도로 그리는” 앞단이다. 둘을 이으면 *지도로 탐색 → 확정된 카드만 위키로 승격*하는 흐름이 된다.
설치: 설정 → 커뮤니티 플러그인 → “Visual Agent Map” 검색, 내장 샘플의 5단계 투어부터.

> 지난번 저장하신 Obsidian + 에이전트 기사들(Copilot·LLM Wiki·Glossa)과 이어지는 소식입니다.

출처: [Obsidian 포럼 — Visual Agent Map 소개](https://forum.obsidian.md/t/visual-agent-map-turn-a-big-question-into-a-visual-research-map-with-ai-kept-as-markdown/119702) · [GitHub kevcltsai/visual-agent-map](https://github.com/kevcltsai/visual-agent-map)
