---
title: "AI 도구: 구글 Gmail MCP, 에이전트가 ‘메일 보내기’까지 — 단, 서버가 직접 사용자에게 ‘보낼까요?’를 묻는 연결에서만. 승인 창을 못 띄우는 앱엔 보내기 버튼 자체가 없다"
date: 2026-11-28T07:45:00+09:00
category: "AI 도구"
slug: "gmail-mcp-send-approval"
summary: "11/24 정식 출시된 Google Workspace의 Gmail MCP 서버는 처음엔 검색·읽기·초안·라벨·휴지통만 됐고 ‘보내기’가 없었다(해커뉴스 화제). 11/27(UTC) 갱신된 공식 문서에는 send_message·reply·forward가 올라왔는데, MCP ‘폼 엘리시테이션’으로 사용자 승인 창을 띄울 수 있는 기본 엔드포인트(/mcp/v1)에서만 제공된다. 승인 UI를 못 그리는 앱용 대체 엔드포인트(/mcp/v1self)엔 보내기 도구가 아예 없다."
---

## 한줄 요약
에이전트에게 “메일 보내기”를 열어 주되, **최종 확인은 서버가 직접 사람에게** 받는다. 앱이 승인을 건너뛰지 못하게 설계했다([AI SI Daily, 11/27](https://aisidaily.com/daily/ai-daily-2026-11-27/)).

## 무엇이 바뀌었나
- **11/24 GA 시점:** 메시지·스레드 검색과 읽기, 초안 만들기·가져오기, 라벨 관리, 휴지통·스팸 이동. 보내기 언급 없음 → 해커뉴스 “구글 MCP의 Gmail은 메일을 못 보낸다” 글이 367점.
- **11/27 문서:** 도구 목록에 `send_message`, `reply`, `forward`. **기본 엔드포인트 `/mcp/v1` 전용**.
- **폼 엘리시테이션이란:** 에이전트가 보내기를 호출하면 서버가 “입력 필요” 응답과 함께 **승인 양식**을 돌려주고, MCP 앱이 그 창을 사용자에게 보여 준 뒤 같은 호출을 승인 정보와 함께 다시 보낸다. Claude Desktop·Google Antigravity처럼 이를 지원하는 앱은 별도 코드 없이 된다([Google 개발자 문서, 11/27 갱신](https://developers.google.com/workspace/guides/mcp-elicitation)).
- 이 승인은 메일 전송뿐 아니라 **캘린더 일정 수정, 파일 수정·삭제, 일부 데이터 읽기**에도 쓰이며, Workspace 관리자 정책과 함께 작동한다. OAuth 토큰에는 `gmail.send` 권한이 있어야 한다.

## 왜 중요한가
- 지금까지 에이전트의 “위험한 행동 전 확인”은 **각 앱(호스트)이 알아서** 하는 영역이었다. 구글은 그 확인을 **서비스 쪽 서버로 끌어올렸다**. 앱이 확인을 생략하도록 만들어져 있어도 보내기는 안 된다.
- 브로커 MCP(MT5의 ‘거래 허용/확인 요청/금지’, NordFX의 읽기 전용)에서 본 것과 같은 패턴이 메일로 왔다. **읽기는 넓게, 쓰기·보내기는 사람 확인 뒤**가 업계 기본값으로 굳고 있다.
- 주의: 보내기 도구 추가는 문서 갱신으로 확인된 것이고, 별도 출시 공지는 없다. 엔드포인트·권한 구조는 바뀔 수 있으니 연결 전 공식 문서를 확인할 것.

출처: [Google — 폼 엘리시테이션](https://developers.google.com/workspace/guides/mcp-elicitation) · [Workspace MCP 도구 목록](https://developers.google.com/workspace/guides/mcp-server-tools) · [AI SI Daily](https://aisidaily.com/daily/ai-daily-2026-11-27/)
