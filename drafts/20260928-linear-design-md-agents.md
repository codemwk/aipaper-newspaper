---
title: "Design: Linear DESIGN.md — 코딩 에이전트가 읽는 ‘바이올렛·키보드’ 디자인 계약"
date: 2026-09-28T07:02:00+09:00
category: "Design/UI·UX"
slug: "linear-design-md-agents"
summary: "DesignMD Directory의 Linear DESIGN.md. linear.app에서 추출한 색·타이포·스페이싱 토큰을 Cursor·Claude Code·Codex가 따르는 단일 소스. Inter Variable, 4/8/12/16px 스케일, 딥 바이올렛·모노스페이스 미학."
---

## 한줄 요약
[DesignMD Directory — Linear DESIGN.md](https://designmd.directory/p/linear-design-md)는 Linear 사이트에서 뽑은 **에이전트용 디자인 계약서**다. “예쁜 UI 만들어 줘” 대신 **색·폰트·간격·라디우스를 파일로 고정**하고, Cursor·Claude Code·Codex가 그 파일을 읽게 한다. 어제 Figma 플러그인·Code Connect와 다른 축은 **캔버스가 아니라 레포 루트의 DESIGN.md**다.

## 무엇이 들어있나
- **팔레트**: Primary `#e4f222`, Secondary/브랜드 `#5e6ad2`, 딥 배경 `#08090a`·패널 `#0f1011` 등 추출 토큰 표.
- **타이포**: Inter Variable 기준 Display~Caption 스케일, 모노스페이스 표본.
- **레이아웃**: space-1~16(4–64px), radius-sm~full, 그림자 단계.
- **사용법**: 레포에 DESIGN.md(또는 `.cursor/rules`)를 두고 “임의 Tailwind 금지·토큰만” 규칙을 심음. DesignMD는 Google Stitch 등에도 같은 포맷을 권한다.

## 왜 중요한가
UI UX Pro Max가 “스타일·안티패턴을 생성”한다면, DESIGN.md는 **이미 존재하는 브랜드를 에이전트 입력으로 고정**한다. 퍼스널 OS·대시보드 UI를 여러 에이전트에 맡길 때, 시각 일관성의 병목은 모델이 아니라 **읽을 계약 파일의 유무**다.

## 기억할 것
- [designmd.directory/p/linear-design-md](https://designmd.directory/p/linear-design-md) · [linear.app](https://linear.app)
