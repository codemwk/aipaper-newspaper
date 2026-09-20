---
title: "Qwen-MM-Plugins — Video2Note·Skill Creator로 ‘영상→노트·스킬’"
date: 2026-09-21T07:06:00+09:00
category: "GitHub"
slug: "qwen-mm-plugins-video2note"
summary: "QwenLM/Qwen-MM-Plugins(오픈소스). Omni-Flash와 짝. Video2Note는 튜토리얼→도해 PDF, Omni Skill Creator는 시연 영상→검증된 Skill.md. Codex·Claude Code·Qwen Code·Gemini CLI 등 하네스에 설치."
---

## 한줄 요약
[Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins)는 Qwen3.8-Omni-Flash 발표와 함께 공개·강조된 **멀티모달 에이전트 플러그인 묶음**이다. 모델만 바꾸는 게 아니라 **영상 지식을 노트·스킬 파일로 굳히는** 쪽이 실무 신호다.

## 지금 뭐가 뜨나
- `omni-video2note`: 긴 튜토리얼을 핵심 프레임+텍스트 **PDF 노트**로. 재개·검수 루프.
- `omni-skill-creator`: 화면 녹화·전문가 시연 → 재사용 **Agent Skill.md**(프레임·클립·오디오 동봉 가능).
- 기타: `core`/`api` 인식·OCR, `omni-chatcut`(MV·해설·번역), `omni-memory`(장편 AV 인물·사건 메모리).
- 설치: 공식 `install.sh` 또는 에이전트에게 리포 URL을 주고 플러그인 선택. Claude Code·Codex·Gemini CLI·OpenClaw 등 지원 표기.

## 왜 중요한가
GitHub 트렌드를 “별 많은 레포”가 아니라 **에이전트가 남기는 산출물 포맷**으로 보면, Skill.md·PDF 노트는 세컨드브레인·팀 SOP와 바로 맞물린다. “한 번 본 영상”을 **다음 에이전트가 호출 가능한 자산**으로 바꾼다.

## 기억할 것
- [GitHub Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) · [Video2Note 허브](https://qwenlm.github.io/qwen-mm-plugins-hub/plugins/omni-video2note/)
