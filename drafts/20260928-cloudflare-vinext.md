---
title: "GitHub: Cloudflare vinext — Next.js API를 Vite로 다시 쓰고 Workers에 한 방에"
date: 2026-09-28T07:07:00+09:00
category: "GitHub"
slug: "cloudflare-vinext"
summary: "cloudflare/vinext(MIT, ★~8.8k). Next.js API 표면을 Vite 플러그인으로 재구현. Workers 우선 배포. 블로그: 1인+AI·약 $1,100 토큰·1주. 벤치 빌드 ~4x, 클라이언트 gzip ~57%↓(방향성). Agent Skill로 마이그레이션."
---

## 한줄 요약
[cloudflare/vinext](https://github.com/cloudflare/vinext)는 Next.js의 **빌드 산출물을 개조(OpenNext)**하는 대신, **라우팅·RSC·Server Actions 등 API 표면을 Vite 위에 다시 구현**한다. [Cloudflare 블로그](https://blog.cloudflare.com/vinext/)는 엔지니어 1명+AI로 약 1주·토큰비 **~$1,100**에 프로토타입이 나왔다고 적는다. 쉬운 말로: “Next를 Cloudflare에 맞게 깎지 말고, Next처럼 쓰는 Vite 앱을 만든다.”

## 무엇이 되나 / 주의
- **됨**: App·Pages Router, RSC, Server Actions, 미들웨어, ISR, `next/link`·`image`·`navigation` 등. `vinext deploy`→Workers. `npx skills add cloudflare/vinext` 후 “migrate to vinext”.
- **실험적**: README·블로그 모두 production 전면 대체가 아님을 명시. Cache Components/PPR·일부 네이티브 모듈 등 갭. `vinext check`로 호환성 점검.
- **벤치(블로그, 33라우트 픽스처)**: Vite 8/Rolldown 빌드 평균이 Next 16 Turbopack 대비 **~4.4× 빠름**, 클라이언트 gzip **~57% 작음** — 방향성 수치, 서빙 성능 아님.

## 왜 중요한가
에이전트 시대의 “프레임워크 재작성” 레퍼런스다. 스펙·테스트·기반 툴(Vite)이 있으면 **중간 추상화 레이어를 AI가 채워** 배포 락인을 흔든다. Next 앱을 Workers·엣지로 옮기려는 팀에게는 OpenNext 대안 후보. 스타 스냅샷(2026-09-28 `gh`): **~8,858★**.

## 기억할 것
- [github.com/cloudflare/vinext](https://github.com/cloudflare/vinext) · [blog.cloudflare.com/vinext](https://blog.cloudflare.com/vinext/) · [vinext.dev](https://vinext.dev)
