---
title: "GLM-5.3-FlashX — 같은 가중치, 2.5배 요금으로 ‘대기열 앞자리’를 판다"
date: 2026-09-20T07:20:00+09:00
category: "AI Models"
slug: "glm-53-flashx-speed-tier"
summary: "2026-09-18 Z.ai API. FlashX는 GLM-5.3-Flash와 동일 가중치(320B-A18B MoE·1M 컨텍스트)·동일 지능. 서빙만 가속(벤더 peak ~200 tok/s). 리스트 $0.37/$1.25 per 1M in/out = Flash의 2.5×. 독립 벤치 미공개."
---

## 한줄 요약
[OrcaRouter 분석](https://www.orcarouter.ai/blog/glm-5-3-flashx-release)(2026-09-19)과 Z.ai 롤아웃에 따르면 **GLM-5.3-FlashX**는 새 모델이 아니라 **같은 Flash 가중치의 고속 호스팅 티어**다. 지능 점수는 그대로, **가격·지연**만 바뀐다.

## 지금 뭐가 뜨나
- **동일**: MIT 오픈웨이트 Flash와 같은 MoE·1M 컨텍스트·멀티모달. FlashX 전용 벤치마크는 없다(평가할 새 가중치가 없음).
- **차이**: 벤더가 말하는 peak **~200 tok/s** vs Artificial Analysis가 Flash API에서 잰 **~98 tok/s**. 200은 광고성 peak로 읽는 게 맞다.
- **가격(리스트)**: FlashX **$0.37 / $1.25** per 1M in/out (캐시 입력 $0.075). Flash **$0.15 / $0.50**의 **2.5배**. 국내가도 ¥2/¥7 vs ¥0.8/¥2.8로 같은 배수.
- **언제 살까**: 에이전트 루프·인라인 완성처럼 **사람이 다음 토큰을 기다리는** 작업. 배치·오프라인은 Flash/자체 호스팅이 합리.
- Vercel AI Gateway 등에도 `glm-5.3-flashx` 문자열이 올라오기 시작.

## 왜 중요한가
오픈웨이트로 싸게 풀어 둔 뒤, **속도만 유료 SKU**로 분리하는 실험이다. “모델 이름”이 아니라 **서빙 SLA를 상품**으로 파는 시대의 신호.

## 기억할 것
- [OrcaRouter FlashX](https://www.orcarouter.ai/blog/glm-5-3-flashx-release) · 모델 id `glm-5.3-flashx`
