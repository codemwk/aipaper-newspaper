---
title: "디자인/UI·UX: PhotoCraft — Rust로 다시 쓴 Photoshop 클린룸이 4.1만★, 커밋에 Claude Opus 5.5 공동저자"
date: 2026-10-11T07:08:00+09:00
category: "디자인/UI·UX"
slug: "photocraft-adobe-clone-rust"
summary: "storytold/photocraft(~41.5K★)는 ArtCraft 계열의 오픈소스 이미지 편집기. 순수 Rust, 레이어·마스크·조정 레이어·PSD, early alpha. 공개 커밋에 Claude Opus 5.5 Co-Authored-By가 반복. Adobe 대체가 아니라 ‘에이전트가 UI 복제 속도를 바꾼다’는 신호."
---

## 한줄 요약
**[storytold/photocraft](https://github.com/storytold/photocraft)**가 “순수 Rust로 다시 구현한 Photoshop급 데스크”를 내걸고 **약 4.15만★**(2026-10-11)를 모았다. README는 **early alpha**, MIT/Apache-2.0, macOS·Windows·Linux·FreeBSD·Web. ArtCraft([getartcraft.com](https://getartcraft.com/apps/photocraft)) 브랜드 아래 배포.

## 제품이 말하는 범위
- 레이어·마스크·조정 레이어·레이어 스타일·타입·벡터·브러시, **실제 PSD**.
- **오프라인·오픈소스** — 클라우드 SaaS Firefly와 반대 축.
- 상태 배지가 **early alpha**: 프로 파이프라인 대체가 아니라 **실험·학습·프로토타입** 구간으로 읽는 게 맞다.

## AI가 찍힌 흔적
최근 공개 커밋 메시지에 **`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`**가 반복된다(예: Place/리사이즈·마퀴 힌팅 수정). 2차 블로그가 주장하는 “전체 커밋의 N%” 같은 **집계치는 이 판에서 재집계하지 않았다** — 확인 가능한 사실은 **에이전트 공동저자 트레일러가 히스토리에 남는다**는 점이다.

## 왜 중요한가
디자인 툴 경쟁이 Firefly 크레딧·Figma 에이전트만의 이야기가 아니다. **UI 패리티를 에이전트가 며칠~몇 주 단위로 흉내 내는** 비용 곡선이 열리면, Adobe·Figma의 해자는 “픽셀 기능”보다 **워크플로·파일 호환·팀 권한·법적 안전** 쪽으로 이동한다. 스튜디오 입장에선 “클론 스타 수”보다 **프로덕션에 쓸 수 있는 깊이**를 보는 체크리스트가 필요하다.

출처: [storytold/photocraft](https://github.com/storytold/photocraft) · [PhotoCraft on ArtCraft](https://getartcraft.com/apps/photocraft)
