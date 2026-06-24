# Stop extracting data: Run serverless Python natively in BigQuery!

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=qOLRUiEgeEw
- **요약 일시**: 2026-06-24 09:06:02

---

## 🔑 핵심 요약
- **BigQuery 관리형 Python UDF**가 **정식 출시(GA)** — 데이터 추출 없이 워런지 내부에서 Python 실행
- **데이터 이동 제로, 인프라 관리 제로** — 별도 VM·네트워크 전송 없이 서버리스 컴퓨트에서 바로 실행
- 표준 SQL 안에서 `BeautifulSoup` 등 외부 라이브러리를 임포트해 수백만 행에 즉시 적용 가능

---

## 📣 주요 발표 내용
- **관리형 Python UDF(User-Defined Function)** 가 **GA(General Availability)** 단계로 전환
- BigQuery의 **서버리스 컴퓨트 엔진** 내부에서 커스텀 Python 코드를 네이티브 실행
- 표준 **SQL** 구문 안에서 Python UDF를 정의하고, `BeautifulSoup` 같은 표준 라이브러리를 그대로 임포트
- **Hugging Face** 에 보안 연결해 모델 설정(config)을 가져오고, **warm container** 에 캐싱하여 인메모리로 빠르게 처리
- 데이터 정제·수학 연산 같은 가벼운 스크립트를 위해 더 이상 GB 단위 데이터를 외부로 추출할 필요 없음

---

## 💡 개발자 포인트
- 기존에 데이터를 외부 VM으로 빼서 처리하던 파이프라인을 **BigQuery 내부 UDF로 대체** 가능 → 네트워크 지연·보안 리스크·VM 관리 부담 제거
- SQL 쿼리 흐름 안에 Python 로직을 직접 녹일 수 있어 **ETL 단계 단순화**

> **보안/성능 팁:** Hugging Face 등 외부 모델 연동 시 모델 설정을 `warm container`에 캐싱하면 반복 호출에서 인메모리 처리로 속도가 크게 향상됩니다.

- 실습은 영상 고정 댓글(pinned comment)의 **code lab** 링크에서 단계별로 진행 가능

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
| ---- | ---- |
| BigQuery 관리형 Python UDF | **GA (정식 출시)** |

