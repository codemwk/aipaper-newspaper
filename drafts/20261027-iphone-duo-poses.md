---
title: "디자인/UI·UX: 아이폰에 ‘접는 선’이 생겼다 — iPhone Duo가 디자이너에게 던진 숙제는 화면 크기가 아니라 ‘자세(pose)’. 반쯤 접어 세우면 위는 보는 칸, 아래는 조작하는 칸"
date: 2026-10-27T07:05:00+09:00
category: "디자인/UI·UX"
slug: "iphone-duo-poses"
summary: "애플 첫 폴더블 iPhone Duo가 10/23 출시(한국 포함 1차 국가). 안쪽 화면은 iPhone 18 Pro Max보다 50% 크고, 바깥·안쪽 화면 비율이 같아 앱이 비례 확대된다. 표준 SwiftUI·UIKit 부품으로 만든 앱은 자동으로 조작 버튼을 옆으로 옮기고, 여러 단으로 펼치고, 반쯤 접히면 버튼을 접는 선에서 비켜 놓는다. 새 힌지 API는 화면 각도를, ‘예약 영역’ API는 접는 선·카메라 위치를 알려 준다. Figma도 10/23 iPhone Duo 프레임 프리셋 추가."
---

## 한줄 요약
iPhone Duo는 “화면이 커진 아이폰”이 아니라 **“여러 자세로 쓰는 아이폰”**이다. 책상 위에 반쯤 접어 세우면 노트북처럼 **위는 보는 칸, 아래는 조작하는 칸**이 된다. 디자이너에게 새로 생긴 변수는 해상도가 아니라 **힌지 각도**다([Apple 뉴스룸](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/)).

## 앱이 화면을 나누는 방식 (실제 사례)
- **MLB**: 반쯤 접어 세우면 위에는 중계, 테이블에 닿은 아래쪽엔 실시간 기록. “중계와 박스스코어 중 고를 필요가 없다.”
- **Prime Video**: 반쯤 접으면 위는 영상, 아래는 출연진·부가정보(X-Ray).
- **NYT Cooking**: 주방 조리대에 세워 두고 단계·타이머·영상을 함께.
- **Detail**(영상·팟캐스트 편집): 영상과 자막 원고를 나란히. 새 **Core AI** 프레임워크로 자막·군말 제거·음질 개선을 **기기 안에서** 처리.
- **한국 앱**: 카카오톡(여러 대화방 목록 + 한 대화), 웹툰·네이버 시리즈(큰 화면 읽기), 카카오페이지(책처럼 펼친 Split View), BAND.

## 디자이너가 알아야 할 새 규칙
| 무엇 | 내용 |
|---|---|
| 같은 화면 비율 | 바깥·안쪽 화면 비율이 같아, 펼치면 앱이 **비례 확대**되며 이어진다 |
| 표준 부품의 자동 적응 | 버튼을 손 닿는 옆으로, 안쪽 화면에선 여러 단으로, 반쯤 접히면 **접는 선에서 버튼을 비켜 놓는다** |
| 배치·예약 영역 API | 접는 선 기준으로 내용을 나누거나 끝까지 채우는 맞춤 레이아웃 |
| 힌지 API | 열고 닫는 **각도**에 반응 (닫힘·반쯤 열림·완전 열림 + 연속 각도) |
| 씬 액세서리 | 두 화면에 동시에 표시 — 예: 촬영당하는 사람 쪽 바깥 화면에 프롬프터 |
| 테스트 | Xcode 27.1 Device Hub에서 가상 Duo를 열고·접고·돌려 보기 |
- ‘Made for iPhone Duo’ 배지: 최적화 앱은 App Store에 배지가 붙는다. 업계 보도(MacRumors)에 따르면 iOS 27.1 SDK로 빌드해야 최적화로 인정되며, 구형 앱은 가운데에 여백을 두고 뜬다.
- **Figma**는 10/23 iPhone Duo·iPhone 18 프레임 프리셋을 디자인·프로토타입·Make 미리보기·코드 레이어 전반에 추가했다([Figma 릴리스 노트](https://www.figma.com/release-notes/)).

## 왜 중요한가
- **디자인 시스템의 배당금.** 표준 부품으로 만든 팀은 새 기기에 거의 공짜로 맞춰지고, 전부 손으로 그린 팀은 화면 한가운데 접는 선을 떠안는다. 컴포넌트 규칙을 지키는 것이 곧 ‘미래 기기 대응’이다.
- **‘자세’라는 새 어휘.** 손에 든 폰, 펼친 태블릿, 반쯤 세운 노트북형 — 같은 앱이 세 가지 물건이 된다. 와이어프레임에 화면 크기뿐 아니라 **자세별 상태**를 그려야 한다.
- **AI는 조용히, 기기 안에서.** 이번 출시에서 AI는 챗봇이 아니라 편집 앱 안에서 군말을 지우는 기능으로 등장했다. 새 화면에 가장 잘 맞는 AI는 화면을 더 쓰기 쉽게 만드는 AI라는 점을 보여 준다.
- 가격: 미국 1,999달러부터. 한국은 10/23 1차 출시국에 포함.

출처: [Apple 뉴스룸 — 개발자 앱 경험 (10/22)](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/) · [Apple Developer — Strike a pose with adaptive layouts](https://developer.apple.com/videos/play/tech-talks/111463/) · [Apple Developer — Leverage multiple displays and scenes](https://developer.apple.com/videos/play/tech-talks/111464/) · [Figma 릴리스 노트 (10/23)](https://www.figma.com/release-notes/)
