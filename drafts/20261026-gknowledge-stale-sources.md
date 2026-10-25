---
title: "세컨드 브레인 / PKM: gknowledge — 카파시 ‘LLM 위키’를 리눅스 데스크톱 앱으로. 모델 없이도 돌고, ‘원본 파일이 바뀐 페이지’를 찾아 주는 stale_sources 도구까지"
date: 2026-10-26T07:10:00+09:00
category: "세컨드 브레인 / PKM"
slug: "gknowledge-stale-sources"
summary: "카파시의 ‘LLM Wiki’ 아이디어(AI가 원문을 매번 다시 읽지 말고, 원문으로 위키를 만들어 계속 관리하게 하라)를 GNOME 네이티브 앱으로 만든 오픈소스 gknowledge가 v0.3.0(10/19)을 냈다. 문서를 넣으면 출처 요약 페이지와 인물·개념 페이지를 [[위키링크]]로 엮고, 답변엔 번호 인용이 붙는다. 결과물은 Obsidian에서 바로 열리는 마크다운 폴더. 모델 없이 도는 오프라인 엔진, 로컬 모델·ChatGPT 계정 로그인 선택, MCP 서버 제공. 새 버전은 ‘수집 후 원본이 바뀐 문서’를 감지해 표시·재수집하고 MCP로 stale_sources를 노출한다. 아직 별 24개의 작은 프로젝트(MIT)."
---

> 지난번 저장하신 Obsidian + 에이전트 기억 기사들(LLM Wiki·ai-memory·enquire-mcp ‘신선도’)과 이어지는 소식입니다 — 이번엔 ‘위키가 낡았는지’를 도구가 직접 알려 줍니다.

## 한줄 요약
LLM 위키의 가장 큰 약점은 **원본이 바뀌어도 위키는 그대로**라는 것. gknowledge는 그 낡음(drift)을 추적하는 기능을 넣었다([개발자 dev.to 글](https://dev.to/francescobianco/i-turned-karpathys-llm-wiki-into-a-native-gnome-app-and-it-works-offline-130c)).

## 무엇을 하나 (30초 요약)
1. 마크다운·텍스트·PDF·HTML 문서를 넣는다(논문·노트·명세 등).
2. 문서마다 **요약 페이지**, 그 안의 사람·시스템·개념마다 **개별 페이지**를 만들고 `[[위키링크]]`로 엮는다. 모든 페이지는 출처를 기록.
3. 질문하면 위키에서 답하고, **클릭되는 번호 인용**을 단다.
- 결과는 YAML 머리말이 붙은 **평범한 마크다운 폴더** → Obsidian으로 열고, grep하고, git에 넣을 수 있다. 동기화 서비스·잠금 없음.

## 다른 LLM 위키와 다른 점
| 특징 | 내용 |
|---|---|
| 네이티브 앱 | GTK 4 + Libadwaita. Electron·웹뷰 없음, GNOME 테마 따름 |
| 모델 없이도 동작 | 내장 오프라인 엔진이 수집하고 ‘발췌’로 답함. 모델을 붙이면 진짜 종합 |
| 두뇌 선택 | Ollama·LM Studio·OpenAI 호환 주소, 또는 **ChatGPT 계정 로그인**(내 Plus/Pro 플랜에서 사용량 차감) |
| 스텁 페이지 억제 | 내용 없는 한 줄 페이지를 안 만들고 중복 병합(‘RAG’ = ‘retrieval augmented generation’). 예시 논문 6편에서 114쪽 → 64쪽 |
| 에이전트 연결 | MCP 서버 — Claude Code·Codex·Cursor가 같은 위키를 검색·읽기·질문·자료 추가 |

## v0.3.0(10/19)의 핵심: ‘낡은 원본’ 추적
- 사용자 댓글(“에이전트로 문서를 점검해 보니 잡힌 건 환각이 아니라 **원본이 바뀌어 낡아 버린 문서**였다”)을 받아들여 추가된 기능.
- 수집 후 **원본 파일이 바뀌면 감지 → 표시 → 갱신·재수집** 가능. MCP로 `stale_sources` 도구를 노출해, 에이전트가 “지금 낡은 출처가 뭐지?”를 물어볼 수 있다([릴리스 v0.3.0](https://github.com/openapi/gknowledge/releases)).
- 같은 버전에서 **Flatpak**(GNOME 51 런타임, PDF 지원)으로도 배포 — 우분투 외 배포판 사용자도 설치 가능.

## 왜 볼 만한가
- 세컨드 브레인에서 **‘얼마나 많이 아느냐’보다 ‘아는 게 아직 맞느냐’**가 중요해지는 흐름. 위키 페이지가 출처를 기록하니, 출처가 바뀌면 그 페이지를 의심하라고 알려 줄 수 있다 — 단순하지만 대부분의 PKM 도구에 없는 기능.
- Obsidian 사용자에게 바로 쓸 아이디어: 에이전트가 만든 노트 머리말에 `source:`(원본 경로)와 `ingested:`(수집 날짜)를 남겨 두면, 나중에 “원본 수정일 > 수집일”인 노트를 찾는 것만으로 같은 효과를 낼 수 있다.
- 한계: 별 24개, v0.3의 초기 프로젝트이고 리눅스(GNOME) 전용. 로드맵의 ‘린트(모순·고아·낡은 페이지 찾기)’와 그래프 보기는 아직 예정.

출처: [dev.to — I turned Karpathy's LLM Wiki into a native GNOME app (10/13, 댓글 10/19–21)](https://dev.to/francescobianco/i-turned-karpathys-llm-wiki-into-a-native-gnome-app-and-it-works-offline-130c) · [openapi/gknowledge](https://github.com/openapi/gknowledge) · [gknowledge-mcp (PyPI)](https://pypi.org/project/gknowledge-mcp/) · [카파시 LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
