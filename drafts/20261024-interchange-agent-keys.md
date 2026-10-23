---
title: "AI 트레이딩: 증권 인프라 회사 Interchange, 에이전트 전용 ‘열쇠’를 만들었다 — 문서만/읽기만/읽기·쓰기 3단계, 60초짜리 토큰, 재시도는 같은 주문 ID로"
date: 2026-10-24T07:07:00+09:00
category: "AI 트레이딩"
slug: "interchange-agent-keys"
summary: "증권 계좌·주문 API 플랫폼 Interchange가 10/22 MCP 서버와 Agent Auth 공개(우선 샌드박스). 에이전트는 문서 검색 도구 + ‘조회(query)’·‘명령(command)’ 두 API 도구로 계좌 개설·입금·주문까지. Agent Key는 Docs Only / Read Only / Read & Write 중 하나로 만들 때 고정 — 리서치용 키를 매매용으로 넓힐 수 없다. 연결은 브라우저 승인, 키를 만든 사람만 승인 가능, 키 보관(archive) 즉시 차단. 호출마다 60초짜리 토큰으로 바꿔 누가·어떤 클라이언트로·무엇을 했는지 기록. 명령 도구는 스스로 재시도하지 않고, 타임아웃이 ‘두 번째 매매’가 되지 않도록 같은 ID 재사용을 지시."
---

## 한줄 요약
IBKR·Walt·Coinbase가 “에이전트가 매매해도 된다”는 **문**을 열었다면, Interchange는 그 문의 **자물쇠와 출입 기록부**를 공개했다. 증권 계좌·주문 API를 다른 금융사에 제공하는 회사가 10/22 **MCP 서버 + Agent Auth**를 냈다([Interchange 블로그](https://www.interchange.com/blog/introducing-interchange-mcp-and-agent-auth)).

## 에이전트가 할 수 있는 일 (샌드박스)
- **문서 도구**: 모든 가이드·API 패키지 색인, 전문 검색, 스키마 원문 읽기
- **API 도구 단 두 개**: 읽는 건 전부 **query**, 상태를 바꾸는 건 전부 **command**. 처음부터 읽기·쓰기를 분리해 설계해서 가능했다고
- 계좌 개설 → 입금 → 주문까지 샌드박스에서 실행

## 안전장치 설계 (핵심)
| 장치 | 내용 |
|---|---|
| **3단계 키** | Docs Only / Read Only / Read & Write — **생성 시 고정**, 리서치용 키를 매매용으로 넓힐 수 없음. 엔드포인트 단위 세분화는 다음 버전 |
| **사람 승인** | 브라우저에서 로그인·프로그램·키를 골라 승인. **키를 만든 사람만** 승인 가능, 한 프로그램에만 |
| **즉시 차단** | 키를 archive하면 갱신 토큰이 바로 폐기 |
| **60초 토큰** | 에이전트 토큰은 API에 직접 닿지 않음. 호출마다 키·승인자·클라이언트 이름이 박힌 60초짜리 토큰으로 교환, 모든 행동에 기록 |
| **중복 주문 방지** | command 도구는 **스스로 재시도하지 않음**. 행동 전 ID를 만들고, 재시도 땐 같은 ID, 타임아웃 뒤엔 상태부터 확인 — “타임아웃이 두 번째 매매가 되면 안 된다” |

## 어떻게 봐야 하나
이번 주 흐름을 한 줄로: **IBKR**은 ‘별도 칸(AI Partition)’, **Walt**는 ‘출금 불가·실행 기본 OFF’, **Interchange**는 ‘키 등급 고정·호출별 기록’. 같은 날 Coinbase는 공식 X 계정에서 “에이전트가 문자 그대로 대신 매매한다”며 MCP 연결을 홍보했다([Outposts 정리](https://outposts.io/project/coinbase/article/coinbase-pitches-ai-agent-trading-via-its-connector-cmvfcsz6n000l06jq71hhf9z3)). 마케팅은 빨라지고, 기록·권한 설계는 이제 막 표준이 생기는 중이다.
개인 MT5 자동매매에 옮겨 쓸 만한 교훈: **① 분석용·주문용 계정/키를 아예 분리 ② 주문엔 고유 ID를 붙여 재시도 중복 방지 ③ 에이전트가 한 모든 호출을 로그로**.

> 지난번 저장하신 MT5 에이전트 매매 안전장치(RiskGate, 권한 분리) 기사와 이어지는 소식입니다.

출처: [Interchange — Introducing the Interchange MCP server and Agent Auth (10/22)](https://www.interchange.com/blog/introducing-interchange-mcp-and-agent-auth) · [Outposts — Coinbase agent trading (10/22)](https://outposts.io/project/coinbase/article/coinbase-pitches-ai-agent-trading-via-its-connector-cmvfcsz6n000l06jq71hhf9z3)
