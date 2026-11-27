---
title: "세컨드 브레인: AI 비서의 ‘기억’을 내 볼트 파일로 — Obsidian Copilot 4.1 ‘Teammates’, 재무·가족·공부 담당 AI 팀원을 마크다운으로. 같은 주, 2,100만 명의 챗봇 대화가 경매에 오른다"
date: 2026-11-28T07:40:00+09:00
category: "세컨드 브레인"
slug: "obsidian-copilot-teammates"
summary: "Obsidian에서 가장 많이 설치된 AI 플러그인 Copilot이 4.1에서 ‘Copilot Teammates’를 냈다. 역할별 AI 팀원의 지시문과 장기 기억을 전부 볼트 안 마크다운 파일로 저장해, 모델·에이전트·앱을 바꿔도 그대로 가져간다. @로 팀원을 불러 서로 의견을 묻게 할 수도 있다. 완전 로컬 대안으로는 모든 수정을 diff 승인으로만 쓰는 Local Vault Agent도 있다. 같은 주 미국 40여 개 주 법무장관은 파산한 Character.AI가 2,100만 계정의 대화 기록을 12/1 경매에 부치는 것을 막아 달라고 법원에 요청했다."
---

## 한줄 요약
“내 AI 비서가 몇 달간 배운 것”은 **누구 서버에 있나?** Copilot의 답은 “당신 볼트의 파일”이다([Obsidian Copilot v4.1.0 릴리스, 11/21](https://github.com/logancyang/obsidian-copilot/releases/tag/4.1.0)).

## Copilot Teammates — 무엇이 되나
- **팀원 = 볼트 파일:** 각 팀원의 지시문과 장기 기억이 **마크다운 파일**. 모델·에이전트·앱을 바꿔도, 파일을 읽는 다른 앱과도 **같은 팀을 공유**.
- **역할 분리:** 재무, 가족, 학습처럼 삶의 영역별로 팀원을 만들고 각자 지시문·기억·범위를 따로 둔다.
- **@로 협업:** 가족 여행을 짜다가 @재무 팀원을 불러 현금 흐름을 확인하는 식.
- **대화로 만들고 가르치기:** 필요한 팀원을 설명하면 Copilot이 초안을 만들고, 함께 일하며 가르친 걸 기억한다.
- 현재 **Supporter 등급용**. 블랙프라이데이로 Supporter와 연간 Plus 첫해 20% 할인(12/6까지). Copilot은 약 280만 다운로드, v4부터 Claude Code·Codex·OpenCode를 볼트 안에서 돌리는 에이전트 호스트(에이전트 모드는 데스크톱 전용)([9to5stuff 가이드, 11/26](https://9to5stuff.com/best-obsidian-ai-plugins/)).

## 완전 로컬을 원하면 — Local Vault Agent
- Ollama 기반, **아무것도 기기 밖으로 나가지 않는다**. 노트를 검색·읽고, 주제를 모아 인용 달린 새 노트를 쓰고, 수정은 **항상 diff를 보여 주고 승인받은 뒤** 쓴다. 승인한 변경은 이력과 되돌리기가 남는다. MIT·무료·계정 불필요([커뮤니티 플러그인 페이지](https://community.obsidian.md/plugins/local-vault-agent)).

## 같은 주의 반대 사례 — Character.AI 대화 경매
- 파산한 Character.AI가 플랫폼과 **미국 2,100만+ 계정(미성년 210만+)의 대화 기록**, IP 주소·메타데이터를 **12/1 경매**에 부치려 하자, 캘리포니아 등 40여 개 주 법무장관이 파산 법원에 차단을 요청했다. 회사 개인정보 방침엔 “개인정보를 금전 대가로 팔지 않는다”고 적혀 있었다([캘리포니아 법무부](https://oag.ca.gov/news/press-releases/attorney-general-bonta-opposes-asset-sale-characterai-amid-child-safety-concerns), [TechCrunch, 11/25](https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/)).

## 왜 중요한가
- 지난번 저장하신 **Obsidian Copilot·claude-mem 기사와 이어지는 소식**이다. 기억 신선도 문제에 이어 이번엔 **기억의 소유권**. 회사가 사라지면 서버 속 기억은 자산으로 팔릴 수 있지만, 볼트 파일은 내 디스크에 남는다.
- 여러 전문 봇을 쓰는 지금 구조와 Teammates의 “역할별 팀원 + @ 호출”은 거의 같은 그림이다. 봇별 지시문·기억을 **LLM Wiki/볼트의 마크다운으로 백업**해 두면 앱을 옮겨도 잃지 않는다.
- 주의: Teammates는 유료 Supporter 기능이고, 파일로 저장돼도 클라우드 모델을 쓰면 대화 내용은 그 모델 제공자에게 간다.

출처: [Copilot 4.1.0](https://github.com/logancyang/obsidian-copilot/releases/tag/4.1.0) · [Local Vault Agent](https://community.obsidian.md/plugins/local-vault-agent) · [CA 법무부](https://oag.ca.gov/news/press-releases/attorney-general-bonta-opposes-asset-sale-characterai-amid-child-safety-concerns) · [TechCrunch](https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/)
