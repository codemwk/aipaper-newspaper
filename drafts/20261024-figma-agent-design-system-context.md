---
title: "디자인/UI·UX: Figma가 직접 쓴 ‘에이전트에게 디자인 시스템 가르치는 법’ — 라이브러리·가이드라인·예시·스킬 4단 구조"
date: 2026-10-24T07:02:00+09:00
category: "디자인/UI·UX"
slug: "figma-agent-design-system-context"
summary: "Figma가 10/22 블로그에서 Figma 에이전트에게 디자인 시스템을 ‘제대로’ 쓰게 하는 방법을 정리. ① 게시된 라이브러리 연결(승인된 컴포넌트·토큰 사용) ② 가이드라인 파일 첨부(규칙·예외·피해야 할 실수 — 라이브러리 켜면 자동 적용) ③ 예시(Examples 페이지나 _example 접미사) ④ 반복 작업은 /design-system-audit 같은 스킬로. 단 가이드라인은 새 화면을 만들 때 더 잘 지켜지고 기존 화면 수정 땐 아직 덜 일관적이라고 Figma가 인정."
---

## 한줄 요약
“AI가 만든 화면은 우리 제품처럼 안 보인다”는 불만에 Figma가 내놓은 답은 모델이 아니라 **문맥(context) 정리법**이다. PM Wayne Lin이 10/22 쓴 가이드는 에이전트에게 줄 정보를 네 층으로 나눈다([Figma 블로그](https://www.figma.com/blog/how-to-put-your-design-system-to-work-with-the-figma-agent/)).

## 4단 구조
| 층 | 무엇 | 언제 쓰나 |
|---|---|---|
| **라이브러리** | 게시된 컴포넌트·토큰·변수 | 기본 재료. 연결하면 에이전트가 ‘승인된’ 부품만 고른다 |
| **가이드라인** | 라이브러리에 붙이는 지시 파일 | 늘 지켜야 할 규칙·예외·실수와 대안, 비슷한 컴포넌트 중 고르는 기준 |
| **예시** | `Examples` 페이지 또는 이름 끝 `_example` | “말보다 보여 주기” — 팀이 부품을 실제로 어떻게 조합하는지 |
| **스킬** | `/`로 부르는 반복 절차 | 예: `/design-system-audit`(분리된 인스턴스·하드코딩 값·접근성 누락 점검) |

예를 들면 “결제 화면의 ‘주문하기’는 항상 Primary 버튼, ‘뒤로’는 Secondary”를 가이드라인에 한 번 써 두면, 매번 프롬프트에 반복할 필요가 없다.

## 실무 팁 (원문에서)
- 컴포넌트 이름을 **의미 있게**(`Card/OrderSummary/Default`처럼), 속성·변형(variant)을 정의해 둘수록 에이전트가 잘 고른다
- 같은 실수를 반복하면 → 프롬프트를 고칠 게 아니라 **가이드라인·라이브러리·예시를 고칠 신호**
- `Examples`·`_example`은 **대소문자 구분**, 컴포넌트 세트는 부모에 붙일 것
- 솔직한 한계: 가이드라인은 **새로 만들 때** 잘 적용되고, **기존 화면 편집** 땐 아직 일관성이 떨어진다

## 왜 중요한가
이번 달 Webflow의 DESIGN.md, Char의 design.md, Figma Specs까지 — 흐름은 하나다. **디자인 시스템이 ‘사람이 읽는 문서’에서 ‘에이전트가 읽는 계약서’로** 바뀌고 있다. 좋은 시스템의 기준에 “에이전트가 헷갈리지 않는가”가 새로 붙었다.

> 지난번 저장하신 Figma Agent·DESIGN.md 류 기사들과 이어지는 소식입니다 — 이번엔 Figma가 직접 낸 ‘운영 매뉴얼’.

출처: [Figma 블로그 — How to put your design system to work with the Figma agent (10/22)](https://www.figma.com/blog/how-to-put-your-design-system-to-work-with-the-figma-agent/)
