---
title: "AI 모델: Anthropic Cyber Verification Program 3단 — Defense·Red Team·Specialized, Glasswing 129K 취약점 경험을 ‘검증된 방어자’에게 연다"
date: 2026-10-12T07:03:00+09:00
category: "AI 모델"
slug: "anthropic-cyber-verification-tiers"
summary: "10/6 Anthropic이 CVP를 확장. Project Glasswing과 통합해 Defense / Red Team / Specialized 3티어. Opus·Sonnet 5.5·Mythos 5.1 포함. CyScenarioBench에서 Defense는 50회 중 46 차단, Red Team은 차단 0·34/50 성공. Glasswing 파트너가 4–7월 검증 취약점 ≥129K(고위험 ≥33K) 주장."
---

## 한줄 요약
Anthropic은 **2026-10-06** [Cyber Verification Program 확장](https://www.anthropic.com/news/cyber-verification-program)을 발표했다. 일반 모델의 **보수적 사이버 차단**은 유지한 채, 검증된 보안 조직에 **티어별 완화**를 준다. Glasswing(핵심 소프트웨어 방어)과 기존 CVP를 **하나로 합쳤다**.

## 티어가 나누는 것
- **Defense Access**: SOC·IR, 악성코드 리버싱, **소유·유지 시스템**의 취약점 분석. 기업·비영리·대학·정부·중소 보안펌·OSS 유지자·실적 있는 개인 연구자. “며칠 내” 심사 목표.
- **Red Team Access**: 위 + **승인된** 펜테스트·레드팀. 조직만(개인 불가). 랜섬·물리 피해·고위험 안전시스템 펜테스트는 여전히 실시간 차단. 심사 “몇 주”, 대기 중엔 Defense로 등록.
- **Specialized Access**: 차단 최소. 항공·전력·통신·은행 간 이체·정부 행정 등 **생명·시장에 영향** 가능한 안전시스템 테스트. **미 정부와 심층 심사**. 기존 Glasswing 멤버는 이 티어로 이전·재승인 불필요(현재 모델 기준).
- **공통**: Opus 5.5·Sonnet 5.5·Mythos 5.1 및 이후 신모델. Claude Platform·Vertex·Foundry. Bedrock은 EFS 대상만. **데이터 보관 의무**(오남용 모니터링). 올가을 EFS(제로 리텐션+가드레일) 예고.

## 숫자가 말하는 검증
- **CyScenarioBench**(Opus 5.5, 10과제×5시도): CVP 없음 → 첫 프롬프트에서 전원 차단 / Defense → **46/50** 차단·4 성공 / Red Team → **차단 0**, **34/50** 성공(=가드레일 없음과 동일 67.6%).
- **Glasswing 임팩트**(회사 설문·부분 데이터): 2026-04~07 파트너 **검증 취약점 ≥129,000**, Anthropic OSS 스캔 **+5,500**(4~10월). 이 중 **고·치명 ≥33,000**. “Mythos 없이 같으려면 수개월~수년” 파트너 발언. **하한·과소집계**라고 스스로 적었다.

## 왜 중요한가
어제 Cyber Mission·Usage Policy와 겹쳐 읽히지만, 오늘은 **“누구에겐 열고 누구엔 막을지”를 제품 티어로 만든 날**이다. 듀얼유즈를 전부 막으면 방어자가 손해를 보고, 전부 열면 공격면이 커진다. CVP는 그 중간을 **KYC식 검증 + 차등 분류기**로 판다. 국내 팀이면 Defense  qualifying 여부·데이터 보관 의무·EFS 일정을 먼저 봐야 한다.

출처: [Expanding the Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program)
