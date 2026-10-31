---
title: "세컨드 브레인: Basic Memory 1.0 — 프로젝트 위키·라이브 노트·문서 수입·에이전트(베타). MCP 도구 12개로 토큰 49%↓"
date: 2026-11-01T07:09:00+09:00
category: "세컨드 브레인/PKM"
slug: "basic-memory-1-0"
summary: "Basic Memory가 10월 클라우드 1.0과 오픈코어 v0.24를 묶었다. 프로젝트마다 wiki(index/log, OKF), Comark 라이브 보드·차트, PDF·Word·PPT·CSV→노트, 스케줄·폴더 감시 에이전트(베타), 검토 큐. MCP bm_* 12도구가 동일 작업에 토큰 49%·호출 19% 감소(팀 측정). Cloud $19 / Pro $99 / Business $249."
---

## 한줄 요약
지난번 저장하신 LLM Wiki·Obsidian 에이전트 관심과 이어지는 소식이다. Basic Memory는 **마크다운을 유지한 채** 위키·에이전트·MCP를 한 제품으로 묶었다([블로그](https://basicmemory.com/blog/basic-memory-1-0)).

## 1.0에서 눈에 띄는 것
- **Wiki**: 폴더별 페이지 + `index.md`/`log.md` 자동 갱신, `bm okf export`.
- **Live notes**: 체크리스트가 칸반으로, 표가 차트로 — 데이터는 여전히 마크다운.
- **문서 → 노트**: PDF·Word·PPT·CSV 추출본을 검색 가능하게.
- **Agents(베타)**: 지시가 적힌 노트가 스케줄·폴더 이벤트·수동으로 실행. 변경은 **리뷰 큐**(diff 승인/취소). 할 일 없으면 스킵·비용 0.
- **MCP 12**: `bm_read`/`bm_write`/`bm_search`/`bm_schema` 등. v0.24 대비 토큰−49%·호출−19%(동일 작업, 팀 발표).

## 요금(Cloud)
| | Cloud | Pro | Business |
|---|---|---|---|
| 월 | **$19** | **$99** | **$249** |
| 멤버 | 2 | 5 | 25 |
| | 사용량 크레딧·지출 한도 |

오픈코어(`basic-memory`)는 MCP·CLI·검색 엔진. v0.24는 POSIX식 cat/grep/ls와 **리비전 잠금 쓰기**(에이전트 충돌 방지).

## 왜 중요한가
- ‘위키를 사람이 쓰고 에이전트가 읽만 하는’ 단계에서, **에이전트가 써도 사람이 게이트**하는 패턴이 제품 기본값이 되고 있다. 도구 이름 변경은 브레이킹 — 마이그레이션 가이드 필수.
