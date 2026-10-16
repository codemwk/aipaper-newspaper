---
title: "디자인/UI·UX: ‘Figma·Canva를 직접 만든다’는 오픈소스 둘 — Rust로 짠 FigCraft(명령 400개를 에이전트·CLI와 공유), 설치형 Canva 대안 Doory"
date: 2026-10-17T07:07:00+09:00
category: "디자인/UI·UX"
slug: "figcraft-doory-open-design-tools"
summary: "이번 주 GitHub 신규 레포 상위권에 디자인 툴 둘. storytold/figcraft(10/9 생성, ~2K★): Figma 클린룸 재구현, 순수 Rust 네이티브, 오토레이아웃·컴포넌트·변수·프로토타입·Dev Mode, 400+ 명령 레지스트리를 UI·CLI·JSON·MCP가 공유, .fig는 ‘최선 노력’, 자체 추정 ‘Figma 대체 49%’. 모체 ArtCraft는 주간 +2.2만★. shaongitbd/doory(10/10 생성, ~1.4K★): 브라우저 디자인 에디터, 유료 플랜 없음, Docker 자가 호스팅, 템플릿 10개."
---

## 한줄 요약
10/11 본지가 다룬 Photoshop 클린룸 PhotoCraft의 ‘형제’가 나왔다. 같은 ArtCraft 커뮤니티의 **FigCraft**는 **Figma를 Rust로 다시 짠** 데스크톱 앱이고, 비슷한 시기에 등장한 **Doory**는 “오픈소스 Canva 대안”을 내걸었다. 둘 다 이번 주 GitHub 신규 레포 상위 10위 안에 들었다([Shareuhack 주간](https://www.shareuhack.com/zh-TW/posts/github-trending-weekly-2026-10-16)).

## FigCraft — 에이전트가 ‘클릭’할 수 있는 Figma
- **무엇**: 프레임, 오토레이아웃, 컴포넌트와 변형(variants), 벡터 네트워크, 스타일·변수(라이트/다크 모드), 프로토타입, **Dev Mode(컴포넌트 속성이 React props가 되는 코드)**까지 갖춘 인터페이스 디자인 툴. macOS·Windows·Linux·FreeBSD·웹([GitHub](https://github.com/storytold/figcraft)).
- **에이전트 설계**: 모든 메뉴·도구·제스처가 **400개 이상 명령이 담긴 하나의 레지스트리**를 호출한다. UI·CLI·JSON 제어 채널·**MCP 서버**가 같은 명령을 쓰므로, 사람이 클릭할 수 있는 건 스크립트와 AI 에이전트도 할 수 있다. 창 없이 렌더·내보내기·명령 스크립트 실행도 가능.
- **내 파일은 내 디스크에**: `.figcraft` 파일은 로컬 아카이브, 계정·텔레메트리 없음. SVG·PNG·PDF 입출력, Figma REST API JSON은 열리고 **.fig 파일은 ‘최선 노력’** 수준.
- **솔직한 현황표**: 스스로 **“Figma를 실무에서 대체하기까지 약 49%”**라고 적었다. 멀티플레이어는 첫 프리뷰(계정·팀·클라우드 없음), 플러그인은 Figma 것이 아닌 자체 WebAssembly, 실제 Figma 문서와의 대조 검증은 아직. 라이선스 MIT/Apache-2.0, early alpha.
- **모체 ArtCraft**는 GitStock 기준 이번 주 **+22,319★**(총 약 3.05만)으로 주간 2위권이었다([GitStock](https://gitstock.org/trending/weekly/2026-10-16)).

## Doory — 가입 없이 쓰는 설치형 Canva
- **무엇**: 포스터·소셜 포스트·스토리·슬라이드·청첩장·이력서·썸네일·명함을 만드는 **브라우저 에디터**. PNG·JPG·SVG·PDF·MP4·WebM·GIF로 내보내기([GitHub](https://github.com/shaongitbd/doory)).
- **기능**: 아이콘 약 2만 5천 개, 브라우저 안에서 도는 배경 제거, 등장·퇴장 애니메이션 27종·페이지 전환 16종, CC0 음악 24개·효과음 88개, 발표 모드, 보기·댓글·편집 공유 링크와 **실시간 공동 편집**, 버전 기록, **브랜드 킷**.
- **조건**: 유료 플랜 없음, 계정 없이 시작, Docker로 자기 서버에 설치. 다만 템플릿은 **10개**뿐인 “젊은 프로젝트”라고 스스로 밝혔고, GitHub상 라이선스 표기가 표준 식별자로 잡히지 않아(NOASSERTION) 상업 이용 전 확인이 필요하다.

## 왜 중요한가
코딩 에이전트 덕에 “잘 알려진 앱의 UI를 다시 만드는 비용”이 급락했다는 신호가 한 달 새 세 번째다. 디자이너에게 실질적인 의미는 두 가지다. ① **에이전트 친화성**: FigCraft처럼 모든 동작이 명령으로 노출되면, 에이전트가 디자인 파일을 직접 고치는 자동화(배너 수백 장 리사이즈, 다크모드 변형 생성)가 플러그인 없이 된다. ② **소유권**: 클라우드 계정 없이 로컬 파일과 자가 호스팅으로 작업하는 선택지. 단, 둘 다 알파 단계라 **클라이언트 납품용 메인 툴로 쓰기엔 이르다** — 실험용·사내 도구용으로 먼저 만져볼 것.

출처: [storytold/figcraft](https://github.com/storytold/figcraft) · [shaongitbd/doory](https://github.com/shaongitbd/doory) · [GitStock 주간 트렌딩 10/16](https://gitstock.org/trending/weekly/2026-10-16) · [Shareuhack GitHub 주간 10/16](https://www.shareuhack.com/zh-TW/posts/github-trending-weekly-2026-10-16)
