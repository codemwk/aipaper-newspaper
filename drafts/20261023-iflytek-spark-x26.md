---
title: "AI 모델: iFlytek Spark X2.6 — 2,930억 파라미터 MoE·100만 토큰 문맥을 ‘중국산 칩으로만’ 학습했다는 주장, 노트북용 4B는 Apache 2.0 공개"
date: 2026-10-23T07:07:00+09:00
category: "AI 모델"
slug: "iflytek-spark-x26"
summary: "iFlytek이 10/22 베이징 ‘1024 개발자 축제’에서 Spark X2.6 발표: 293B 총 파라미터·토큰당 30B 활성 MoE, 100만 토큰 문맥, 코딩·에이전트 작업 겨냥, 국산 1만 장 규모 추론 클러스터에 배포. 회사는 ‘전부 국산 컴퓨팅으로 학습’ 주장(독립 검증 없음). API 한시 40% 할인가: 입력 0.9위안·캐시 0.08위안·출력 3.6위안/100만 토큰. 온디바이스 Spark-X2.6-4B는 Apache 2.0으로 Hugging Face·Ollama 공개 — 생각 수준 none/low/high 조절, 자체 발표 기준 SWE Verified 62.8(이전 41.6)·BFCL-V4 71.8. Ollama로 바로 실행 가능."
---

## 한줄 요약
중국 음성 AI 강자 **iFlytek(커다쉰페이)** 이 10/22 새 대형 모델 **Spark X2.6**를 발표했다. 숫자보다 메시지가 크다 — “**엔비디아 없이, 중국산 칩만으로 학습했다**”([Global Times](https://www.globaltimes.cn/page/202610/1372798.shtml), [DigIntoAI](https://digintoai.com/en/articles/iflytek-spark-x2-6)).

## 큰 모델: Spark X2.6
- **구조**: 293B 총 파라미터, 토큰마다 30B만 쓰는 MoE(전문가 혼합) — ‘큰 지식, 적은 계산’.
- **문맥**: **100만 토큰** (책 여러 권, 큰 코드베이스를 한 번에).
- **용도**: 코딩과 에이전트(여러 단계 작업). 국산 1만 장 규모 추론 클러스터에 배포.
- **국산 학습 주장**: 회장 류칭펑은 “장기 과제 학습의 효율 병목을 국산 칩에서 처음 돌파했다”고 했다. 독립 검증은 아직 없다.
- **가격**(한시 40% 할인, 종료일 미표기, 100만 토큰당): 입력 **0.9위안**, 캐시 적중 0.08위안, 출력 **3.6위안**.

## 작은 모델: Spark-X2.6-4B (바로 써 볼 수 있는 쪽)
- **Apache 2.0** 공개 — Hugging Face, ModelScope, **Ollama**(`ollama run SparkLLM/Spark-X2.6-4B`).
- 기존 4B와 같은 구조에 후처리 학습만 강화. **생각 수준 none/low/high**를 골라 속도·비용을 조절.
- 팀이 발표한 점수(생각=high): SWE Verified **62.8**(이전 41.6), BFCL-V4 71.8(이전 65.1), MCP-Atlas 62.4. RTX 4090과 Mac M5 Pro에서의 속도표도 함께 냈다([SparkLLM, dev.to](https://dev.to/sparkllm/spark-x26-4b-stronger-on-device-agents-coding-and-controllable-thinking-2fh)). 모두 자체 측정이다.

## 왜 중요한가
- 미국의 칩 수출 규제 속에서 중국 모델 업체들은 **‘국산 칩으로도 학습까지 된다’** 를 증명하려 경쟁 중이다(같은 날 화웨이 Ascend 910C로 DeepSeek-V4-Pro 후처리 학습을 마쳤다는 현지 보도도 나왔다). 성공한다면 중국 모델 가격 하락 압력은 더 커진다.
- 개인 사용자에겐 4B 모델이 실용적이다. 로컬 에이전트·코딩 보조를 **노트북에서 무료로** 시험해 볼 선택지가 하나 늘었다.

출처: [Global Times (10/22)](https://www.globaltimes.cn/page/202610/1372798.shtml) · [DigIntoAI (10/22)](https://digintoai.com/en/articles/iflytek-spark-x2-6) · [SparkLLM — Spark-X2.6-4B (dev.to)](https://dev.to/sparkllm/spark-x26-4b-stronger-on-device-agents-coding-and-controllable-thinking-2fh)
