---
title: "GitHub 트렌드: 영상을 ‘글’로 바꾸는 스킬들 — 샷 단위로 역설계하는 rea-video, 영상을 React로 쓰는 raea, 그리고 제인스트리트의 ‘소크라테스식 과외’ 스킬"
date: 2026-11-13T07:08:00+09:00
category: "GitHub 트렌드"
slug: "github-video-skills-socratic-tutor"
summary: "Upstar의 에이전트 스킬 주간 순위(11/6~11/12) 상위권: 퀀트 회사 제인스트리트의 agent_skills(+7.7천 별, 소크라테스식 튜터 스킬 1개), 영상을 샷 단위로 ‘실사·AI·코드 중 무엇인지’ 판정하고 VIDEO.md로 정리하는 rea-video(+5.2천), 영상·모션그래픽·3D를 React/TypeScript로 써서 내 GPU로 렌더링하는 raea(+1.9천)."
---

## 한줄 요약
이번 주 GitHub ‘에이전트 스킬’ 순위의 공통점은 **영상과 학습**이다. 사람이 감으로 하던 일을 **에이전트가 읽을 수 있는 문서 형식**으로 바꾸는 저장소들이 빠르게 올라왔다([Upstar 에이전트 스킬 순위](https://upstar.dev/t/agent-skills)).

## rea-video — “이 영상 어떻게 만들었지?”에 답하는 스킬 (+5.2천 별)
- 영상을 **샷 단위로 쪼개서** 각 샷이 직접 찍은 건지, AI로 생성한 건지, 코드로 만든 건지 판정하고 **다시 만드는 방법**까지 정리한다([GitHub](https://github.com/JuneYaooo/rea-video), Apache 2.0).
- 결과물은 두 가지다. 사람이 읽는 **리포트**(HTML/PDF)와 AI가 읽는 **VIDEO.md**. VIDEO.md는 층으로 나뉜 공개 형식이라, AI가 질문에 필요한 층만 읽어서 토큰을 아낀다.
- 사용법은 Claude Code나 Codex에 “이 저장소 설치하고 이 영상 분석해 줘”라고 말하는 게 전부다. ffmpeg와 Python만 있으면 된다. Gemini 같은 영상 모델을 연결하면 판정이 더 정확해지고, 샷마다 역설계한 프롬프트도 만들어 준다.
- README 예시: 폰으로 찍은 틱톡 광고와 그걸 AI로 리메이크한 영상을 비교해 “왼쪽은 전부 실사, 세트 1개·카메라 2대 / 오른쪽은 전부 AI, 3번의 생성으로 8샷”이라고 판정했다.

## raea — 영상을 ‘코드’로 쓰고 내 GPU로 렌더링 (+1.9천 별)
- 영상, 모션그래픽, 3D, 게임을 **AI가 이미 잘 쓰는 React/TypeScript**로 작성하고 내 GPU로 렌더링한다. Rust·Bevy 기반이다([GitHub](https://github.com/shinyobjectz/raea)).
- 설치하면 Claude Code 스킬 폴더에 raea 스킬이 추가돼서, 에이전트가 쓰고, 렌더링하고, **품질 기준 검사(`raea check`)**까지 할 수 있다. 애플 실리콘 맥에서 90프레임을 약 1초에 렌더링한다고 한다.
- v0.1.1이 첫 정식 릴리스이고, 라이선스는 FSL-1.1-ALv2(일정 기간 뒤 Apache 2.0으로 전환되는 소스 공개형)다. 아직 다듬어지지 않은 부분이 많다고 스스로 밝혔다.

## janestreet/agent_skills — 퀀트 회사가 공개한 과외 선생 (+7.7천 별)
- 아직 스킬은 **socratic-tutor** 하나뿐이다. 진단 테스트로 시작해 0~5레벨 스킬 맵을 만들고, **한 번에 질문 하나씩**, 간격 반복 복습, 최종 평가까지 진행하는 엄격한 튜터다([GitHub](https://github.com/janestreet/agent_skills), MIT).
- 일반 챗봇에서도 SKILL.md 내용을 붙여 넣기만 하면 쓸 수 있다.

## 왜 중요한가
영상 레퍼런스 분석은 그동안 감각의 영역이었다. 이제 **레퍼런스 → VIDEO.md(분석) → raea·생성 모델(재제작)**이라는 흐름이 문서와 코드로 이어지기 시작했다. 지난번 저장하신 OpenMontage·ArtCraft처럼 ‘에이전트용 크리에이티브 스튜디오’ 흐름의 연장선이다. 다만 남의 광고를 샷 단위로 복제하는 건 저작권 문제가 생길 수 있다. **분석은 학습용으로, 제작은 내 소재로** 하는 게 안전하다.
