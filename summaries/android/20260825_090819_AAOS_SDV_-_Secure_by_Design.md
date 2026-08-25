# AAOS SDV - Secure by Design

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/aaos-sdv-secure-by-design.html
- **요약 일시**: 2026-08-25 09:08:19

---

## 🔑 핵심 요약
- **AAOS SDV**(Android Automotive OS for Software Defined Vehicle)는 가상화 기반 도메인 격리와 "deny-by-default" 정책으로 보안을 설계 단계부터 내재화
- **APEX** 패키지를 통한 불변 스토리지·암호화 무결성·원자적 롤백으로 소프트웨어 무결성을 보장
- **DICE**(Device Identifier Composition Engine) 기반 TLS로 VM 간 제로트러스트 인증 구현

---

## 📣 주요 발표 내용

### 기반: 도메인 격리
- **Cuttlefish** 가상화 기술로 클러스터·인포테인먼트 등 논리 도메인을 독립 VM으로 분리
- **Microdroid** 기반 상속으로 기존 Android 보안 기능(UID 격리, `SELinux` deny-by-default) 그대로 활용
- `SELinux` + POSIX capabilities로 최소 권한 원칙 적용 — 누락 설정은 과도한 권한 대신 접근 차단

### 소프트웨어 무결성: APEX 4대 원칙
| 원칙 | 메커니즘 | 효과 |
|------|---------|------|
| 불변 스토리지 | `apex_payload.img`를 `MS_RDONLY` 루프백 마운트 | root 권한으로도 실행 중 코드 수정 불가 |
| 암호화 무결성 | `dm-verity` + Merkle Tree (4KB 블록 단위) | 블록 변조 즉시 감지·실행 중단 |
| 엄격한 격리 | `/apex` 하위 전용 파티션·전용 linker namespace | 비권한 데몬의 라이브러리 접근 표면 최소화 |
| 원자적 복구 | Active/Backup 이중 버퍼 롤백 (`apexd` 관리) | 업데이트 실패 시 `/system` 파티션으로 즉시 복구 |

### 메모리 안전성
- 신규 컴포넌트는 **Rust**를 주 언어로 채택 — 메모리 안전성 취약점 클래스 예방
- 파트너사 서비스 개발에도 Rust 채택 권장

### 분산 신뢰: DICE 기반 TLS
- **UDS**(Unique Device Secret)는 제조 시 생성, 1단계 부트로더만 접근 가능
- 각 펌웨어 레이어 해시를 체인으로 연결해 **CDI**(Compound Device Identifier) 도출
- VM 간 통신 시 소프트웨어 상태까지 동시 검증 — IP 주소만 믿는 기존 신뢰 모델 대체

---

## 💡 개발자 포인트

- **서비스 레벨 권한** (특정 VM 내 리소스 접근)과 **VM 레벨 권한** (cross-VM 통신 경계) 이중 구조로 업데이트 유연성과 보안을 균형 유지
- 비보안 민감 서비스는 APEX 업데이트만으로 배포 가능, VM 전체 재배포 불필요

> **Breaking**: 보안 민감 신호(security-sensitive signals)를 새 VM에 추가하려면 메시 내 **모든 VM의 VM-레벨 권한**을 동시에 갱신해야 함 — 시스템 전체 업데이트 필요

- APEX 서명 검증은 부팅마다 수행 — 서명 없는 패키지는 실행 불가
- `dm-verity` 해시 불일치 시 커널이 즉시 실행을 중단하므로, 파티션 이미지 빌드 파이프라인에서 무결성 검증 필수

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 블로그 게시일 | 2026년 8월 24일 |
| 대상 플랫폼 | AAOS SDV (Software Defined Vehicle) |
| 참고 문서 | [AAOS SDV Overview page](https://source.android.com/docs/automotive/sdv) |

