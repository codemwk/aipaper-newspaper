---
title: "AI 비즈니스: Mach9 — 도로 스캔을 ‘설계 도면’으로 바꿔 주는 AI CAD, 좌석이 아니라 ‘마일·에이커당’ 받는다. 하드웨어를 접고 3,400만 달러 시리즈 A"
date: 2026-10-25T07:00:00+09:00
category: "AI 비즈니스"
slug: "mach9-ai-business"
summary: "미국 스타트업 Mach9이 10/21 시리즈 A 3,400만 달러(First Round·Bessemer 공동 주도, 누적 4,900만 달러)를 유치. 라이다(LiDAR)로 찍은 도로·전봇대·전선 스캔에서 연석·차선·표지판을 AI가 센티미터 단위로 그려 초안 도면을 만들고, 면허 있는 측량사가 검토·서명한다. ‘최대 10배 빠르게, 비용 5분의 1’(회사 주장). 50개 주 2,500개 이상 프로젝트, 10만 마일 이상. 요금은 사용량 기반 — 측량한 도로 1마일·1에이커당. 소프트웨어 예산이 아니라 ‘프로젝트 인건비 예산’을 가져가는 구조. 매출·기업가치는 비공개."
---

## 한줄 요약
도로를 레이저로 스캔하는 건 이제 하루면 되는데, 그걸 **엔지니어가 쓸 도면**으로 옮기는 건 아직 사람이 점 하나하나 따라 그린다. Mach9은 그 ‘따라 그리기’를 AI로 대신하고, **그린 거리(마일)만큼 돈을 받는다**. 10/21 시리즈 A 3,400만 달러를 발표했다([Mach9 보도자료](https://mach9.ai/news/34-million-series-a)).

## 누구에게 무엇을 파나
- **고객**: 토목 엔지니어링·측량 회사(WSP, HNTB, NV5)와 주 교통국(Caltrans, 미네소타 DOT, 메릴랜드 도로청), 전력·통신 회사.
- **제품**: 클라우드 CAD ‘Digital Surveyor’. 고객이 가진 장비로 찍은 3D 스캔을 올리면 AI가 **연석·표지판·전봇대·차선·전선**을 센티미터 정확도로 그린 초안을 만든다. 측량사는 꼭짓점을 고치고 품질을 점검한 뒤 **자기 이름으로 서명**한다 — 이 업계는 면허와 법적 책임이 걸려 있어서 ‘사람이 최종 확인’이 필수다([TechCrunch](https://techcrunch.com/2026/10/21/mach9-raises-34m-after-pivoting-to-ai-cad-software/)).
- **써 보는 느낌**: 사용자가 몇 개를 그리면 다음 것을 예측해 제안하고, 탭 키로 받아들이는 방식 — 코딩 AI의 자동완성과 같은 구조([xyHt](https://www.xyht.com/lidarimaging/between-the-scanner-and-the-deliverable-how-mach9-is-building-the-missing-layer-in-geospatial-production/)).

## 돈 버는 구조: “소프트웨어 좌석”이 아니라 “측량한 거리”
- 요금은 **사용량 기반 — 도로 1마일, 면적 1에이커당**. 약정 규모에 따라 단가가 달라지고, 클라우드 전용(사내 설치 없음)이다(xyHt, [Bessemer](https://www.bvp.com/news/mach9-bringing-civil-engineering-into-the-ai-era)).
- Bessemer의 투자 논리: 엔지니어링 회사도 발주처에 **마일·면적 단위로 청구**한다. Mach9 단가가 그 청구 방식과 같으니 프로젝트마다 이익이 바로 보이고, 돈은 작은 IT 예산이 아니라 **훨씬 큰 프로젝트 인건비 예산**에서 나온다.
- 반대로 오토데스크·벤틀리 같은 기존 강자는 **좌석 라이선스**로 팔기 때문에, 작업을 자동화할수록 자기 매출이 줄어드는 구조라 적극적으로 나서기 어렵다는 게 투자사의 해석이다.

## 숫자
| 항목 | 내용 |
|---|---|
| 이번 투자 | 시리즈 A $3,400만 (First Round·Bessemer 공동 주도, Prudence·Quiet Capital) / 누적 $4,900만 |
| 사용 실적 | 50개 주 2,500개+ 프로젝트, 10만 마일+ |
| 고객 수 | 비공개 베타 고객 약 100곳(TechCrunch) |
| 속도·비용 | “최대 10배 빠르게, 5분의 1 비용”(회사 주장). 기존 방식은 1마일에 약 1주 |
| 고객 사례 | Pennoni “같은 인원으로 50% 더 많은 일” |
| 매출·기업가치 | 비공개 |

## 피벗 이야기
2021년 카네기멜런 로보틱스 출신들이 **차량용 스캐너(하드웨어)**로 시작했다. 그런데 고객 회사 측량 책임자가 스캔 데이터를 오토캐드에 넣고 나무·인도·연석을 하나씩 손으로 그리는 걸 보고, 다른 고객은 “스캐너는 이미 4대 있다, 필요한 건 자동화”라고 잘라 말했다. 2022년 말 하드웨어를 접고 소프트웨어로 갈아탔다.

## 왜 중요한가
- **‘AI가 사람 일을 줄인다’가 아니라 ‘사람이 모자란 곳을 메운다’**: 미국 측량사 면허는 2011~2025년 24% 줄었고, 도로·전력망·광통신 재건 예산(인프라법 1.2조 달러)은 넘친다.
- **가격을 고객의 청구 단위에 맞춘 것**이 핵심이다. ‘AI 기능 추가 요금’이 아니라 ‘고객이 이미 돈을 받는 단위’로 값을 매기면 ROI 설득이 필요 없다.
- ANDRSN 관점: 이 회사의 메시지는 “AI CAD”보다 **“검토하고 서명하는 건 당신”**이다. 책임이 무거운 업계일수록 브랜드는 ‘자동화’가 아니라 **‘전문가의 이름을 지켜 주는 도구’**를 약속해야 먹힌다.

출처: [Mach9 보도자료 (10/21)](https://mach9.ai/news/34-million-series-a) · [TechCrunch (10/21)](https://techcrunch.com/2026/10/21/mach9-raises-34m-after-pivoting-to-ai-cad-software/) · [Bessemer 투자 메모 (10/21)](https://www.bvp.com/news/mach9-bringing-civil-engineering-into-the-ai-era) · [xyHt 인터뷰 (3/19)](https://www.xyht.com/lidarimaging/between-the-scanner-and-the-deliverable-how-mach9-is-building-the-missing-layer-in-geospatial-production/)
