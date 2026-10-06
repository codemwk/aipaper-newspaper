---
title: "GitHub 트렌드: REA — “저 앱의 저 기능, 어떻게 만든 거지?”를 에이전트가 바이너리까지 파고드는 MCP (~8.9K★, 오늘 상승 1위)"
date: 2026-10-07T07:09:00+09:00
category: "GitHub 트렌드"
slug: "rea-reverse-engineer-agents"
summary: "morluto/rea는 네이티브 바이너리·JS/Electron 앱·.NET·웹사이트를 하나의 MCP로 분석해 ‘근거·한계·모르는 것’을 붙여 보고한다. Hopper·Ghidra·IDA를 엔진으로 쓰고, 정적 JS 분석은 Node만 있으면 된다. AttentionVC 일간 트렌딩 1위. 라이선스·약관 확인은 필수."
---

## 한줄 요약
**REA(Reverse Engineer Anything)**는 “다른 앱에서 본 기능이 어떻게 동작하는지, **소스 코드 없이** 바이너리 수준까지 알아내 달라”를 코딩 에이전트에게 시키게 해 주는 오픈소스(MIT) 도구다. 10월 7일 기준 별 약 **8.9천 개**, AttentionVC 일간 트렌딩 **상승폭 1위**다([GitHub](https://github.com/morluto/rea), [AttentionVC](https://github.attentionvc.ai/trending/repos)).

## 무엇을 하나 (쉽게)
- **하나의 MCP로 여러 대상**: 네이티브 실행 파일, JavaScript·Electron 앱(ASAR 포함), .NET 어셈블리, 웹사이트. 실험적으로 안드로이드 APK(JADX), 펌웨어(Binwalk·Unblob)도.
- **분석 엔진은 빌려 쓴다**: 이미 쓰던 **Hopper·Ghidra(12.1.4)·IDA Pro**를 연결. Electron 앱 같은 **정적 JS 분석은 Node만** 있으면 된다.
- **보고 형식**: 결론마다 **근거(Evidence)·복원한 구조 그래프·한계·모르는 것**을 함께 낸다. “디컴파일 결과는 원본 소스가 아닌 의사코드”라고 스스로 밝힌다.
- **로컬 실행**: 분석은 대상의 **임시 복사본**에서 돌고, 세션이 끝나면 지운다. 앱을 실행하지 않는 정적 분석이 기본.
- **에이전트 지원**: Claude Code·Codex·Cursor·Gemini CLI·OpenCode·GitHub Copilot CLI 등. `npx rea-agents setup`은 바꿀 설정을 **먼저 보여 주고 백업한 뒤** 승인을 받는다.

## 왜 뜨나
최근 트렌딩의 공통 흐름은 **“코딩 에이전트에 전문가 한 명을 붙인다”**다 — 영상 스튜디오(OpenMontage), CAD(text-to-cad), 게임 모딩(universal-modder)에 이어 이번엔 **리버스 엔지니어**. 제품 팀 입장에선 “경쟁 앱이 이 애니메이션·오프라인 동기화를 어떻게 구현했나”를 에이전트가 근거와 함께 설명해 주는 **리서치 도구**가 된다. 보안 쪽에선 의심스러운 바이너리·확장 프로그램 점검에도 쓰인다.

## 체크포인트 (중요)
- 상용 소프트웨어의 리버스 엔지니어링은 **EULA·서비스 약관·지역 법률**에 따라 금지될 수 있다. 내 앱, 상호운용성, 보안 점검처럼 **권한이 있는 대상**에 쓰고, 분석 결과를 그대로 베끼는 건 피하자.
- Hopper 데모 모드는 기능 제한이 있고, Windows 지원은 실험 단계.
