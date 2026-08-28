# What "real-time voice AI" actually means

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=RsmKGpJ1we4
- **요약 일시**: 2026-08-28 09:08:08

---

## 🔑 핵심 요약
- 대부분의 음성 AI는 **STT → LLM → TTS** 세 시스템을 이어붙인 구조로, "진짜 실시간"이 아님
- **Real-time voice agent**는 오디오를 입력받아 오디오로 출력하는 단일 라이브 세션으로 동작
- 핵심 차별점은 **Barge-in**: 말하는 도중 끊어도 AI가 즉시 멈추는 자연스러운 대화 경험

---

## 📣 주요 발표 내용
- 기존 음성 AI의 한계 명확화: `speech-to-text` → `LLM` → `text-to-speech` 파이프라인 방식은 순서대로 "차례를 넘기는" 구조
- **Barge-in**(끼어들기): 사용자가 AI의 발화 중간에 말을 걸면 AI가 즉시 응답 중단 — 실사람처럼 대화 가능
- **Gemini Live**를 활용한 real-time voice agent 구현 사례 소개

---

## 💡 개발자 포인트
- 오디오 입출력이 동일한 라이브 세션에서 처리되어야 진짜 실시간 — 단순 파이프라인 연결로는 구현 불가
- Barge-in 지원 여부가 "음성 봇"과 "자연스러운 대화 에이전트"를 나누는 기준

> **Barge-in**이 없으면, 사용자가 말을 걸어도 AI가 현재 발화를 끝낼 때까지 무시됨 — UX에 치명적

- **Gemini Live** API를 활용하면 audio-in / audio-out 라이브 세션 구성 가능

---

## 📅 버전 / 출시 일정
해당 없음
