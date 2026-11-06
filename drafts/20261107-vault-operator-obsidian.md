---
title: "세컨드 브레인: Vault Operator — Obsidian 안에서 승인 게이트·원클릭 Undo로 도는 에이전트 하네스"
date: 2026-11-07T07:09:00+09:00
category: "세컨드 브레인"
slug: "vault-operator-obsidian"
summary: "pssah4/vault-operator(약 263★)는 Obsidian 커뮤니티 플러그인형 에이전트다. 계획→검색→읽기→쓰기 루프에 쓰기 승인, 변경 Undo, BYOK, MCP·스킬을 얹었다. Inline AI 채팅, 다중 탭, PDF 출처 블록, 웹 클리핑(로컬 이미지)까지. 어제 vault-loop 안전 패턴과 맞물리는 ‘앱 안 하네스’다."
---

## 한줄 요약
채팅봇이 답을 주면, Vault Operator는 **루프를 돈다** — 행동 선택 → vault 실행 → 결과 피드백 → 완료까지. 모든 쓰기는 보이고, **승인 필요**, 변경은 **한 번에 Undo**. 무료·오픈소스·로컬 우선, 클라우드·ChatGPT/Copilot 구독·Ollama/LM Studio 모두([GitHub](https://github.com/pssah4/vault-operator), [문서](https://pssah4.github.io/vault-operator)).

## 눈에 띄는 기능
- **Inline AI**(v3.0+): 선택 구간 Cmd/Ctrl+Shift+I. Lookup·Rewrite·Translate·Summarize·액션 아이템 — 사이드바와 같은 스킬/MCP/메모리.
- **다중 채팅 탭**(v3.3.1): 긴 작업과 새 작업을 병렬, 중단 후 이력 재개.
- **출처**: PDF 드롭 → 주장마다 원문 단락 링크. URL → Markdown 아카이브 + 이미지 로컬화(v3.3.6).
- **Connectors/MCP**: 외부 클라이언트가 Streamable HTTP로 vault 도구를 쓰도록 문서화.

## 왜 중요한가
지난 [11/6] kepano/obsidian-skills·vault-loop가 “스킬·안전 루프”였다면, Vault Operator는 **Obsidian UI 안에 심은 풀 하네스**다. reader-signal의 Obsidian Copilot·claude-mem·LLM Wiki 줄기와 맞닿는다. “플러그인 하나가 VS Code+Copilot을 대체할 수 있나”를 실험하는 사용자 인용도 README에 쌓여 있다.

## 주의
커뮤니티 플러그인(비공식). 스타 263은 headroom·impeccable급 바이럴은 아니다 — 성숙도·권한 모델을 vault 백업 후 시험할 것. 웹·MCP를 열면 유출면이 넓어진다.
