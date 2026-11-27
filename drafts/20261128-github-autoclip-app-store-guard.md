---
title: "GitHub 이번 주: ‘유료 숏폼 클리핑을 내 컴퓨터에서 공짜로’ AutoClip, 앱 심사 거절 사유를 미리 잡아 주는 App Store Compliance 플레이북 — 코딩 에이전트가 바로 부르는 MCP·스킬로"
date: 2026-11-28T07:35:00+09:00
category: "GitHub 트렌드"
slug: "github-autoclip-app-store-guard"
summary: "11/21~27 GitHub 급상승 목록에서 처음 다루는 두 저장소. AutoClip(주간 별 +5,449개, 총 약 1만 7,500개)은 팟캐스트·인터뷰·게임 방송 다시보기를 숏폼 클립으로 자르고 자막·커버·제목까지 만드는 MIT 무료 데스크톱 앱으로, 자르기·렌더링은 내 컴퓨터에서 하고 MCP로 에이전트가 직접 부를 수 있다. App Store Compliance(주간 별 +5,109개)는 iOS·안드로이드 앱의 심사 거절 위험을 제출 전에 스캔하는 플레이북 + 코딩 에이전트용 스킬이다."
---

## 한줄 요약
이번 주 급상승의 공통점은 **“에이전트에게 실무 도구를 쥐여 준다”**. 영상 편집과 앱 심사 대비라는, 사람이 제일 귀찮아하는 일을 노렸다([Trend 11/27 주간 목록](https://trend.ondo.sh/github/2026-11-27/en.html)).

## AutoClip — ‘오픈소스 OpusClip 대안’
- **무엇:** 링크·영상 파일·**라이브 방송 다시보기**를 넣으면 하이라이트를 찾고, 말하는 사람을 따라 9:16으로 리프레이밍하고, 자막을 입히고, 커버·제목·게시 문구까지 만든다. TikTok·Shorts·Reels·YouTube·더우인·샤오훙수·빌리빌리용.
- **v1.6 신기능:** OBS·Twitch·YouTube·Kick·Discord·로컬 녹화 6개 다시보기 소스, 방송 종료 후 OBS 자동 캡처, 8초 이상 게임 하이라이트 감지, 13개 언어 UI(한국어 포함).
- **로컬 우선:** 자르기·렌더링은 내 컴퓨터. 클라우드 분석 시 **자막 텍스트만**, 비전 모델엔 샘플 프레임만 보낸다. Ollama·LM Studio + Whisper로 **완전 오프라인**도 가능.
- **에이전트 연결:** MCP 서버(`autoclip-mcp`)와 에이전트 스킬 제공 → Claude Code·Cursor·Codex가 “이 인터뷰에서 숏폼 10개 뽑아” 같은 작업을 직접 수행.
- 회사 측정: 자막 있는 1시간 43분 인터뷰 → **7.5분에 클립 10개**, LLM 비용 약 0.09위안. 무료·MIT, 1인 유지보수([AutoClip README](https://github.com/zhouxiaoka/autoclip)).

## App Store Compliance — 제출 전 ‘거절 사유’ 스캐너
- **무엇:** 앱 폴더를 지정해 스크립트 한 번 돌리면 애플 App Store·Google Play **거절 위험**을 찾아 파일·줄 번호와 함께 보여 준다. 치명적 문제가 있으면 `BLOCKED.`로 시작하는 판정과 수정 방법을 낸다. 앱 코드는 바꾸지 않는다.
- 이미 거절당했다면 **이의 제기(appeal) 플레이북**, 개발자가 아니면 **체크리스트**부터. Claude Code·Codex·Cursor·Grok 등에 스킬로 설치해 **제출할 때마다 자동 점검**.
- 스스로 “스캔이 증명할 수 있는 것과 사람이 봐야 하는 것”을 구분하며 **승인을 보장하지 않는다**고 명시.
- 라이선스 주의: 8/27 이후 버전은 MIT가 아니라 **OpenRoots Agent License 2.3**(연 매출 2천만 달러 이하 무료, AI 학습 금지)([README](https://github.com/mjmirza/app-store-compliance)).

## 왜 중요한가
- AutoClip은 오늘 AI 비즈니스로 다룬 CutAI(월 50달러 구독)와 정반대 모델이다. **같은 ‘귀찮은 편집’ 문제를 무료 + 내 GPU + 내 에이전트로** 푼다. 유료 앱의 가격 방어가 어디까지 가능한지 보여 주는 비교 대상.
- 여러 봇으로 앱을 만드는 환경이라면, 심사 거절 체크를 **에이전트 작업의 마지막 관문**으로 붙여 두는 것만으로 왕복 시간을 줄일 수 있다.
- 주의: 별 수는 수집 시점 스냅숏이다. AutoClip 서명되지 않은 설치본은 macOS 보안 해제가 필요하고, 다운로드한 영상의 저작권은 원저작자에게 있다.

출처: [Trend 11/27](https://trend.ondo.sh/github/2026-11-27/en.html) · [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) · [mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance) · [AI SI Daily 11/27](https://aisidaily.com/daily/ai-daily-2026-11-27/)
