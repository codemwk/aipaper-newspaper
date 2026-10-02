---
title: "디자인/UI·UX: Framer Agent — Rotate·Perspective·Depth를 프롬프트로, 레이어는 캔버스에서 편집 가능"
date: 2026-10-03T07:01:00+09:00
category: "디자인/UI·UX"
slug: "framer-agent-3d-transforms"
summary: "Framer(2026-09-01). Agent가 Rotate X/Y/Z·Perspective·Depth·Origin·Backface 등 3D Transform을 지원. 결과는 편집 가능한 Frames/Effects. Skills(09-22)와 쌓이면 ‘지침+공간 모션’ 루프."
---

## 한줄 요약
[Framer](https://www.framer.com/blog/teaching-the-framer-agent-to-design-in-3d/)(2026-09-01, Jurre Houtkamp 등)가 Agent에 **네이티브 3D Transform**을 열었다. Rotate X/Y/Z, Perspective, Depth, Origin, Backface 등을 프롬프트로 조합하고, 출력은 **선택·리사이즈·스프링 조정이 되는 캔버스 레이어**로 남는다([Updates](https://www.framer.com/updates/agent-3d-transforms)). 어제·그저께 Skills·Figma Weave와 겹치지 않는 축: **공간 모션을 에이전트가 쌓고, 디자이너가 광학 무게를 다듬는** 루프.

## 무엇이 바뀌나
- **프롬프트 → 구조**: 납작한 마크를 3축 회전·마스크·이펙트가 엮인 루프 애니메이션으로 확장. 손편집으로는 연결 프레임이 폭증하는 작업을 Agent가 초안.
- **캔버스 우선권**: CSS 한 줄 회전과 달리, 투영된 결과에서도 핸들·중첩·이펙트 선택이 따라가야 한다. Framer는 2024 3D Transforms 위에 Agent를 얹었다고 설명한다.
- **Skills와 결합**: 09-22 Skills가 브랜드·CMS 규칙을 담고, 3D는 **표현 레이어**를 담당. `/skills` + 3D 프롬프트가 같은 프로젝트에 공존.

## 왜 중요한가 (AiPaper·퍼스널 OS)
“생성 후 검은 박스”가 아니라 **에이전트 산출물이 디자인 시스템의 편집 가능 객체**가 되는지가 UI 도구의 분기점이다. 대시보드·랜딩 모션을 외주 GPU 영상이 아니라 **유지보수 가능한 레이어**로 두려면 Framer 쪽 실험이 바로 참고 사례다.

## 기억할 것
- [Blog](https://www.framer.com/blog/teaching-the-framer-agent-to-design-in-3d/) · [Updates](https://www.framer.com/updates/agent-3d-transforms)
