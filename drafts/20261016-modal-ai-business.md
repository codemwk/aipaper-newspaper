---
title: "AI 비즈니스: Modal — ‘GPU 초 단위 과금’으로 연 매출 런레이트 $10억, 에이전트 샌드박스만 $3억… Series D $7.5억·기업가치 $157.5억"
date: 2026-10-16T07:00:00+09:00
category: "AI 비즈니스"
slug: "modal-ai-business"
summary: "Modal(10/14)이 Accel 주도 $7.5억 Series D(포스트머니 $157.5억)와 연환산 런레이트 $10억 돌파를 발표. 5월 Series C($46.5억) 이후 사용량 3배, 전년 대비 15배+. 돈은 ‘쓴 만큼 초 단위’로 번다: H100 초당 $0.001097(시간당 약 $3.95), B200 $0.001736, CPU 코어·초 $0.0000131. 요금제는 Starter $0+컴퓨트(월 $30 포함)·Team 월 $250+컴퓨트(월 $100 포함)·Enterprise 맞춤. 2023년 출시한 Sandboxes가 단독 $3억 런레이트."
---

## 한줄 요약
**Modal**은 AI 앱을 만드는 회사들이 “GPU를 사거나 예약하지 않고” 코드를 돌리게 해 주는 서버리스 클라우드다. 2026-10-14 창업자 Erik Bernhardsson은 **연환산 런레이트(ARR) $10억 돌파**와 **$7.5억 Series D(포스트머니 $157.5억, Accel 주도·Kleiner Perkins 신규 참여)**를 발표했다([Modal 블로그](https://modal.com/blog/1-billion-annualized-run-rate-series-d)). 불과 5개월 전 Series C 때 기업가치는 $46.5억이었다([TFN](https://techfundingnews.com/modal-becomes-latest-decacorn-after-750m-raise-to-build-cloud-infrastructure-for-ai-agents/)).

## 누구에게 무엇을 파나
- **Functions**: 코드를 쓰면 Modal이 실행. 이미지 생성, Suno의 음악, SGLang·vLLM 기반 LLM 추론, 모델 학습에 쓰인다.
- **Sandboxes (2023 출시)**: LLM이 *직접 쓴 코드*를 고객 시스템과 격리해 돌리는 상자. 백그라운드 에이전트, 강화학습, 바이브코딩 플랫폼이 주 고객. 누적 **약 30억 개** 생성, **동시 100만 개**까지 확장, 이 제품만 **$3억 런레이트**(전체의 3분의 1 가까이).
- 고객 예시(회사 발표): DoorDash, Cognition, Ramp, Linear, Hebbia(백그라운드 에이전트), Runway(영상 생성), Physical Intelligence·1X(로봇 학습). TypeSafe AI의 Jev는 출시 첫 3일에 Modal에서 **1조 토큰**을 처리했다고 한다.
- 최근 추가: 데코레이터 하나로 RDMA 연결 클러스터를 받는 멀티노드 학습, RL·후학습 제품, Modal servers(HTTP 서버), Sandboxes의 가상머신 GA. 어제(10/15) 공개된 Meta Muse Spark Open의 호스팅 파트너 명단에도 들어 있다.

## 돈이 흐르는 구조 (공개 가격, 2026-10-16 확인)
- **초 단위 종량제**: B300 **$0.001972/초**, B200 **$0.001736/초**, H200 **$0.001261/초**, H100 **$0.001097/초**(시간당 약 $3.95), A100 80GB $0.000694/초, L4 $0.000222/초. CPU는 물리 코어·초당 **$0.0000131**, 메모리 GiB·초당 $0.00000222([가격](https://modal.com/pricing)).
- **샌드박스는 별도 단가**: CPU 코어·초 $0.00003942, 메모리 GiB·초 $0.00000667 — 일반 함수 CPU보다 약 3배 비싸다. “에이전트용 격리”가 프리미엄 상품이라는 뜻.
- **요금제**: Starter **$0 + 컴퓨트**(월 $30 포함, 3명), Team **월 $250 + 컴퓨트**(월 $100 포함, 인원 무제한, GPU 동시 50개), Enterprise 맞춤(HIPAA·SSO·감사 로그, AWS/GCP 마켓플레이스 약정 소진).
- **가산 요금**: 리전 지정 시 기본가의 1.15~1.75배, 선점 불가(non-preemptible) 실행은 3배. 9/1부터 Shared Endpoints는 토큰 단위로 첫 요청부터 과금.
- **회사 논리**: “예약 GPU는 쉬는 시간에도 돈을 낸다.” 컨테이너가 1~2초에 뜨고 내려가니, 들쭉날쭉한 트래픽에선 시간당 단가가 비싸 보여도 총액이 싸다는 주장이다.

## 왜 중요한가
지금까지 다룬 AI 비즈니스 사례가 대부분 **AI를 쓰는 앱**이었다면, Modal은 그 앱들이 **매초 내는 통행료**를 받는다. 특히 Sandboxes 숫자는 “에이전트가 코드를 쓰고 실행하는 일”이 이미 독립된 수억 달러 시장이 됐다는 증거다. 위험도 분명하다: TFN 분석대로 기업가치는 런레이트의 약 16배이고, Baseten·Together AI·Fireworks가 같은 추론 시장에서 비슷한 속도로 자금을 모으고 있으며, 대형 클라우드나 모델 회사가 자체 샌드박스를 만들면 프리미엄이 깎일 수 있다. ANDRSN 관점의 교훈은 하나 — **원가(GPU)를 소유하지 않고, ‘쉬는 시간 0원’이라는 가격 설계 자체를 브랜드로 만든 회사**라는 점이다.

출처: [Modal — $1B ARR & Series D](https://modal.com/blog/1-billion-annualized-run-rate-series-d) · [Modal Pricing](https://modal.com/pricing) · [Tech Funding News](https://techfundingnews.com/modal-becomes-latest-decacorn-after-750m-raise-to-build-cloud-infrastructure-for-ai-agents/) · [Accel — Our Investment in Modal](https://www.accel.com/news/our-investment-in-modal)
