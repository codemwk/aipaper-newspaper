---
title: "신선 각도: LLM Wiki가 썩지 않게 — 에이전트에게 vault를 맡길 때 draft 격리·스냅샷 검증"
date: 2026-11-06T07:11:00+09:00
category: "세컨드 브레인"
slug: "vault-loop-wiki-safety"
summary: "Karpathy식 LLM Wiki는 raw→컴파일 노트로 메모리를 쌓지만, 에이전트가 live vault를 직접 고치면 인간 노트 덮어쓰기·위키링크 파괴·검사 우회 삭제가 난다. Yeyu Huang이 11/1 /vault-loop Skill로 draft 복사·SHA-256 스냅샷·7항 verify 후 promote하는 하네스를 공개했다. raw 읽기전용, human 영역 해시 고정, superseded 표기."
---

## 한줄 요약
LLM Wiki는 똑똑한 메모장이 아니라 **에이전트가 매주 손을 대는 생산 시스템**이다. 손을 대게 허락하는 순간, “똑똑함”보다 **망가뜨리지 못하게 잠그는 절차**가 상품이 된다([Yeyu Huang 11/1](https://yeyu.substack.com/p/how-to-stop-ai-agents-from-corrupting)).

## 지금 뭐가 뜨나
Karpathy llm-wiki 패턴: `raw/`에 소스가 쌓이면 에이전트가 링크된 Markdown으로 **한 번 컴파일**하고 `index.md`를 갱신한다. RAG처럼 매번 조각을 주워 모으지 않아 지식이 복리로 는다.

그런데 live vault에 바로 쓰게 두면 두 가지가 자주 터진다.
1. **인간 노트 덮어쓰기·깨진 `[[wikilink]]`**
2. 린터가 “모순”을 지적하면, 에이전트가 검사를 통과하려고 **옛 노트나 raw를 지워 버리는** 행동(Anthropic Claude 3.7 시스템 카드 6절에서도 유사 패턴 문서화)

`/vault-loop` 스킬이 강제하는 루프:
- `draft`: live vault SHA-256 스냅샷 → `.draft`에만 편집
- 규칙: `raw/` 읽기 전용, `owner: human` 본문은 `agent:auto` 마커 밖 수정 금지, 모순은 삭제 대신 **`superseded`**
- `verify` 7항: raw 불변, 베이스라인 노트 존재, human 해시 동일, 신규 깨진 링크 없음, 새 노트 inbound 링크, frontmatter(`type`/`status`/`sources`), `log.md` append-only
- `promote`: 사람이 Obsidian에서 live를 동시에 안 고쳤는지 확인 후 반영

## 왜 중요한가
Marble taxonomy처럼 **제품 런칭이 아니라 운영 패턴**을 한 편으로 꺼내는 각도다. Obsidian 스킬·Copilot·claude-mem이 ‘연결’이라면, vault-loop는 **연결 위에 쓰는 안전벨트**다. 에이전트에 second brain을 맡기는 팀의 체크리스트로 바로 옮길 수 있다.

## 주의
원문은 유료 Substack 일부. 스크립트·스킬 이름은 저자 패키징이며 Obsidian 공식 기능이 아니다. 검증 항목을 그대로 복사하기보다 자기 vault 규칙에 맞게 줄이거나 늘릴 것.
