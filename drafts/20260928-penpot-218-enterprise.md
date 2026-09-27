---
title: "Design: Penpot 2.18 — 오픈소스는 유지, Enterprise로 ‘거버넌스’ 유료 레이어"
date: 2026-09-28T07:04:00+09:00
category: "Design/UI·UX"
slug: "penpot-218-enterprise"
summary: "Penpot 2.18(2026-09-09) Born this way. 무료·무제한·오픈소스 유지. Enterprise: 고급 권한·Id Provider·관리자 패널. WebGL 렌더러에 stroke-to-path·드로잉 플라이아웃·폰트 미리보기."
---

## 한줄 요약
[Penpot 2.18 — Born this way](https://penpot.app/release-notes/2-18-born-this-way)(2026-09-09)는 **Penpot Enterprise** 유료 플랜을 열면서도, 코어는 **무료·무제한·오픈소스**라고 못 박는다. 에이전트·플러그인 시대에 “디자인 툴 = 전부 SaaS 구독”이 아닌 **셀프호스트+거버넌스 업셀** 경로를 보여 준다.

## 무엇이 바뀌나
- **Enterprise**: 규모 조직용 고급 권한, Identity Provider 선택, 관리자 패널. 영업 문의.
- **그리기(WebGL 렌더러)**: stroke-to-path, 도형·프리드로 툴바 플라이아웃, 라인·화살표 기여(@davidv399).
- **타이포 UX**: 폰트 셀렉터에서 **각 패밀리 이름으로 미리보기**.
- **커뮤니티 픽스**: 댓글 입력 중 Space→핸드툴 오발동 등.

## 왜 중요한가
Figma·Framer가 에이전트·MCP로 “폐쇄 캔버스 안 자동화”를 키울 때, Penpot은 **파일을 소유한 채** 팀 거버넌스만 돈으로 산다. 디자인 시스템을 Git·셀프호스트에 두고 싶은 팀·공공·스타트업에게는 가격·락인 리스크 비교 포인트다. 배경 블러 등 WebGL 이펙트([블로그](https://penpot.app/blog/say-hello-to-background-blur/))도 같은 렌더러 축이다.

## 기억할 것
- [Release notes 2.18](https://penpot.app/release-notes/2-18-born-this-way) · [penpot.app](https://penpot.app)
