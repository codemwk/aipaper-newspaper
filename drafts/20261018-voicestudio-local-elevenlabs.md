---
title: "GitHub 트렌드: VoiceStudio(~7.3만★, 주간 +1.5만) — ‘내 컴퓨터에서 도는 ElevenLabs 대안’, 음성 복제·목소리 디자인·영상 더빙·받아쓰기를 646개 언어로, 에이전트용 MCP까지"
date: 2026-10-18T07:09:00+09:00
category: "GitHub 트렌드"
slug: "voicestudio-local-elevenlabs"
summary: "debpalash/VoiceStudio(AGPL-3.0, ~7.3만★): 10/11~17 GitHub Python 주간 1위(+14,708★). 완전 로컬 음성 스튜디오 — 음성 복제, 설명으로 목소리 디자인, 타이밍 맞춘 영상 더빙, 플로팅 받아쓰기 위젯, 전사, 오디오북·배치 작업, 레시피·감시 폴더 자동화. 기본 엔진 k2-fsa/OmniVoice, 다른 엔진 선택 가능. 로컬 API·MCP로 에이전트 연동. NVIDIA(CUDA)·Apple Silicon(MPS)·CPU 지원, macOS·Windows·Linux·Docker. 원격 서비스는 선택, 사용 통계는 동의 시만."
---

## 한줄 요약
같은 주 OpenAI는 “글로 목소리를 만드는” 기능을 클라우드 API로 냈다. 반대편에선 **모든 걸 내 컴퓨터에서 돌리는** 오픈소스가 급상승했다. **VoiceStudio**는 이번 주(10/11~17) GitHub Python 주간 트렌딩 1위로 별 **+14,708개**, 누적 약 **7.3만 개**다([AgentPress 주간 정리](https://b.cmkk.fun/content/qGRQkxtEzMph) · [GitHub](https://github.com/debpalash/VoiceStudio)).

## 무엇을 할 수 있나
README는 스스로를 **“오픈소스, 완전 로컬 ElevenLabs 대안”**이라 부른다. 기능은 세 묶음이다.
- **만들기**: 깨끗한 녹음 한 개로 **음성 복제**, 또는 말로 설명해 **목소리 디자인**. 화면 위에 떠 있는 위젯으로 **받아쓰기**.
- **제작**: 영상에 **타이밍을 맞춘 더빙**, 이야기·**오디오북**·배치 작업.
- **연결**: **로컬 API와 MCP** — Claude Code·Codex 같은 에이전트가 VoiceStudio를 도구로 불러 쓸 수 있다. 재사용 ‘레시피’와 **감시 폴더**(폴더에 원고를 넣으면 자동 처리) 지원.
- 언어 **646개**. 기본 엔진은 오픈소스 **OmniVoice(k2-fsa)**, 다른 엔진으로 바꿀 수 있다.

## 어디서 돌아가나
NVIDIA GPU(Windows·Linux, CUDA 가속), **Apple Silicon(Metal 가속)**, 전용 GPU가 없어도 CPU로 느리지만 사용 가능(약 5GB 여유 공간). macOS·Windows·Linux 앱과 Docker 제공. 인텔 맥은 화면만 쓰고 원격 백엔드에 연결해야 한다. 원격 서비스는 선택 사항이고, 사용 통계는 동의해야 수집된다고 밝힌다. 라이선스는 **AGPL-3.0** — 이걸 고쳐 서비스로 외부에 제공하면 소스 공개 의무가 생길 수 있으니 상업 이용 전 확인이 필요하다.

## 왜 중요한가
음성은 AI 콘텐츠 중 **비용과 개인정보 부담이 가장 큰 영역**이다. 유튜브 내레이션·팟캐스트·사내 교육 영상 더빙을 매달 클라우드 요금으로 내던 작업을, 이제 맥북 한 대로 돌릴 수 있는 수준의 도구가 반년 만에 7만 개 넘는 별을 받았다. 다만 **음성 복제는 본인 또는 명시적 동의를 받은 목소리에만** 써야 한다. 설치는 공식 Releases 페이지나 README의 공식 경로로만 하자 — 인기 레포 주변엔 가짜 ‘간편 설치’ 명령이 돈다는 경고가 최근 여러 프로젝트에서 나왔다.

출처: [GitHub debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) · [AgentPress — GitHub Trending 주간(10/11~17)](https://b.cmkk.fun/content/qGRQkxtEzMph)
