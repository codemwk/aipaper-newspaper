---
title: "AI 콘텐츠: ElevenLabs Hosted MCP — 로컬 설치 없이 OAuth로 보이스 에이전트 관리"
date: 2026-09-28T07:05:00+09:00
category: "AI 콘텐츠"
slug: "elevenlabs-hosted-mcp"
summary: "ElevenLabs hosted MCP(api.elevenlabs.io/v1/mcp). Claude Connectors 디렉터리·OAuth. 에이전트 생성·프롬프트·보이스·전사·TTS 링크. EU/IN/SG 레지던시 URL. 로컬 MCP는 호스티드로 이전."
---

## 한줄 요약
[ElevenLabs Hosted MCP](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)는 보이스·Conversational AI 워크스페이스를 **원격 MCP**로 노출한다. Claude Desktop Connectors에서 ElevenLabs를 고르고 OAuth하면, API 키를 클라이언트에 복사하지 않고 **에이전트 CRUD·대화 검토·TTS 샘플**을 자연어로 돌린다. 로컬 오픈소스 MCP([소개 글](https://elevenlabs.io/blog/introducing-elevenlabs-mcp))는 호스티드가 후속으로 정리되는 흐름이다.

## 할 수 있는 것 (공식 문서)
- 에이전트 생성·복제·삭제, 시스템 프롬프트·보이스·언어·첫 메시지 수정.
- 최근 대화·전체 트랜스크립트·토픽 탐색, 위젯·공유 링크, 지식베이스 크기.
- 변경 전 **예상 LLM 사용·비용** 추정, 텍스트→스피치 다운로드 링크.
- **레지던시**: 기본 `https://api.elevenlabs.io/v1/mcp` / EU·India·Singapore는 별도 URL+해당 환경 계정으로 OAuth.
- **이중 권한**: ElevenLabs OAuth 스코프 + 클라이언트 쪽 툴별 승인/자동실행. 삭제는 destructive — 승인 게이트 권장.

## 왜 중요한가
콘텐츠·고객지원·내레이션 파이프라인에서 “보이스 API 키를 `.env`에 심기” 대신 **커넥터·스코프**로 옮기는 신호다. AiPaper형 오디오 브리핑·에이전트 콜을 붙일 때, 보안·레지던시·툴 승인 UX를 함께 설계해야 한다.

## 기억할 것
- [Hosted MCP docs](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp) · [GitHub elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)
