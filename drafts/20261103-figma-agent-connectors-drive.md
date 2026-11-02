---
title: "디자인: Figma 에이전트·Make에 Google Drive 연결, ‘커넥터’는 무료 Starter 플랜까지 — 리서치 문서·스프레드시트·이미지를 그대로 디자인 맥락으로. 단, ‘쓰기’ 권한은 기본 꺼짐"
date: 2026-11-03T07:06:00+09:00
category: "디자인/UI·UX"
slug: "figma-agent-connectors-drive"
summary: "Figma가 11/2(한국 11/2 저녁) Google Drive 커넥터를 Figma 에이전트와 Make에 추가하고, 커넥터 기능을 Starter 포함 전 플랜에 열었다. 드라이브의 리서치·데이터·이미지를 프롬프트 맥락으로 쓰고, 결정 요약이나 에셋을 새 드라이브 파일로 만들 수 있다. 검증 커넥터는 Notion·Linear·GitHub·Granola·zeroheight·Mobbin 등 20여 개. 외부로 ‘쓰는’ 도구는 기본 비활성, 도구마다 ‘실행 전 묻기/항상 실행/실행 안 함’ 선택, Figma도 프롬프트 인젝션을 경고."
---

## 한줄 요약
디자인 에이전트가 **캔버스 밖의 자료**를 직접 읽기 시작했다. 인터뷰 노트, 설문 스프레드시트, 브랜드 이미지 폴더가 프롬프트 한 줄로 디자인 맥락이 된다([Figma 포럼 공지](https://forum.figma.com/product-updates-3/connect-google-drive-to-the-figma-agent-and-make-59533), [Figma 도움말](https://help.figma.com/hc/en-us/articles/35440096186007-Use-verified-partner-MCP-connectors-with-the-Figma-agent-and-Figma-Make)).

## 무엇이 바뀌었나
- **Google Drive 커넥터**: 드라이브 파일(문서·시트·이미지 등)을 읽어 리서치 요약, 실제 데이터 반영, 에셋을 캔버스로 가져와 편집. 반대로 **결정 요약·에셋을 새 드라이브 파일로 생성**도 가능.
- **커넥터 전 플랜 개방**: 무료 Starter에서도 프롬프트 박스의 ‘+’ 메뉴 → 커넥터에서 추가. (직접 만드는 커스텀 MCP 커넥터는 유료 플랜)
- 검증 커넥터 목록: Amplitude, Asana, Atlassian, Box, Contentsquare, Dovetail, Google Drive, Granola, GitHub, Hex, Linear, Mobbin, Notion, Slack, Sprig, Zapier, zeroheight 등.

## 꼭 봐야 할 설정 한 가지
| 설정 | 의미 | 추천 상황 |
|---|---|---|
| Ask to run | 매번 허락받고 실행 | 기본값으로 두기 좋음 |
| Always run | 묻지 않고 실행 | 믿을 수 있는 소스·읽기 도구만 |
| Never run | 아예 안 씀 | 필요 없는 도구 — 에이전트 속도도 빨라짐 |

- 외부로 **쓰는 도구는 기본 비활성**이다. 켜는 순간 에이전트가 Slack 메시지 발송, Jira 이슈 생성 같은 일을 할 수 있다.
- Figma 도움말 스스로 “외부 소스에서 맥락을 가져올 땐 **프롬프트 인젝션**을 경계하라”고 적었다. 누군가 공유 드라이브 문서에 숨긴 지시문이 에이전트를 움직일 수 있다는 뜻.
- ‘Always run’ 상태에선 16MB를 넘는 응답(대략 5~6MB 이상 이미지)은 내려받기가 실패할 수 있다 — 그럴 땐 ‘Ask to run’으로 바꿔 다시.

## 왜 중요한가
지난 몇 주 Figma의 흐름(에이전트 정식 출시, 코드 레이어·Specs, 라이브러리 가이드라인)은 **디자인 시스템을 에이전트에게 가르치는 일**이었다. 이번엔 **리서치·데이터를 에이전트에게 먹이는 일**이다. 디자이너의 일이 ‘시안 그리기’에서 **‘에이전트가 볼 맥락과 권한을 설계하기’**로 넓어지고 있다.
