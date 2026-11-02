---
title: "GitHub 트렌드: Floorplan — ‘AI로 만든 내 앱, 어떻게 돌아가는지 모르겠다’는 사람을 위한 지도. Claude·Codex가 코드를 읽고 부품·화면·요청 흐름을 쉬운 말로 그린다. 키 노출·열린 DB 같은 ‘건강검진’도"
date: 2026-11-03T07:08:00+09:00
category: "GitHub 트렌드"
slug: "floorplan-codebase-map"
summary: "10/27 공개된 Floorplan(MIT, ★약 2,200)은 Claude Code·Codex 플러그인으로, 코드베이스를 읽어 부품·파일·웹 요청에 쉬운 이름을 붙인 확대·축소 가능한 인터랙티브 지도를 만든다. 여러 저장소에 걸친 프론트↔백엔드 요청까지 잇고, 코드 속 키·열린 Supabase 테이블·위조 가능한 Stripe 웹훅을 찾는 ‘건강검진’, AI가 방금 바꾼 부분을 보여 주는 ‘최근 작업’을 제공. 같은 주 아키텍처 다이어그램 스킬 stack-diagram, 애니메이션 역설계 스킬 reanimate도 떴다."
---

## 한줄 요약
바이브 코딩으로 앱은 돌아간다. 그런데 “결제하면 무슨 일이 일어나?”, “이거 바꾸면 뭐가 깨져?”엔 **“모르겠다”**가 정직한 답이다. Floorplan은 **아무도 그리지 않은 설계도**를 대신 그려 준다([GitHub](https://github.com/haydenschmitty/floorplan), [라이브 데모](https://haydenschmitty.github.io/floorplan-demo/)).

## 무엇을 보여 주나
- **줌 가능한 앱 지도**: 부품 → 파일 → 엔드포인트까지 내려가며, 화면과 프론트↔백엔드 요청(저장소가 여러 개여도), 외부 서비스 연결을 선으로 잇는다. 모든 요소에 **쉬운 영어 이름**.
- **건강검진**: 코드에 박힌 키, 열려 있는 Supabase 테이블·Firebase 규칙, 위조 가능한 Stripe 웹훅, 아무나 부를 수 있는 엔드포인트.
- **최근 작업**: Claude나 Codex가 방금 무엇을 왜 바꿨는지 지도 위에 표시. PRD에서 설계도를 먼저 그리는 기능도.
- 의존성 0, Node 18+. README가 Archify(문서용 다이어그램), Understand Anything(대형 코드베이스 학습)과의 차이를 표로 정리해 둔 점도 친절하다.

## 같은 주의 ‘보여 주는’ 스킬들
| 프로젝트 | 하는 일 | ★(11/3) |
|---|---|---|
| [stack-diagram](https://github.com/caru-ini/stack-diagram) | 스택을 한 문장으로 말하면 공식 로고가 들어간 아키텍처 다이어그램 | 약 1,100 |
| [reanimate](https://github.com/NiazMorshed2007/reanimate) | 아무 애니메이션이나 프레임 단위로 역설계하고, 복제본이 **똑같이 움직이는지 증명** | 약 930 |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 픽셀아트 효과 244개 + 나만의 효과를 만드는 스킬 | 약 3,400 |

## 왜 중요한가
코딩 에이전트가 코드를 **쓰는** 단계에서, 사람이 그 결과를 **이해하고 검사하는** 단계로 도구의 무게가 옮겨 가고 있다. 특히 Floorplan의 건강검진은 비개발자가 만든 앱에서 실제로 자주 터지는 사고(키 노출, 열린 DB) 목록 그대로라 실용적이다. 단, 지도는 AI가 추론한 결과이므로 **그럴듯한 그림이 틀린 추론을 가릴 수 있다**는 점은 기억하자.
