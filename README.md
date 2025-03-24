# 🏠 Airbnb 스타일 숙소 예약 백엔드 API 구현

## 📌 프로젝트 개요
> Django와 Django REST Framework(DRF)를 활용하여 숙소 등록, 예약, 리뷰, 인증 등 **Airbnb와 유사한 백엔드 시스템**을 구현한 프로젝트입니다.  
> 사용자 인증부터 숙소 관리, 편의시설 등록, 예약 생성 및 리뷰 기능까지 **RESTful API 아키텍처 기반**으로 구축했습니다.

## ⚙️ 사용 기술
- Python 3.11, Django 5.1.4
- Django REST Framework (DRF)
- SQLite3 (개발용)
- JWT 인증 (pyjwt)
- Git & GitHub
- Postman (테스트)

## 🧩 주요 기능

| 기능 | 설명 |
|------|------|
| 사용자 인증 | 회원가입, 로그인/로그아웃, JWT 기반 인증 |
| 사용자 정보 | 프로필 조회 및 수정, 비밀번호 변경 |
| 숙소 관리 | 숙소 등록, 수정, 삭제, 리스트/상세 조회 |
| 편의시설 | 다대다 연결, 숙소와 연동 가능 |
| 카테고리 | 숙소 타입 분류 (`Room`과 연결됨) |
| 예약 | 미래 예약 리스트, 숙소 예약 생성 |
| 리뷰 | 숙소 리뷰 등록/조회 (페이지네이션 적용) |
| 사진 업로드 | 숙소별 이미지 업로드 지원 |
| 위시리스트 | 찜한 숙소 저장 및 삭제 (선택 구현) |

## 📁 ERD & 모델 구조 요약 (간단)

- **User**
  - `username`, `name`, `email`, `avatar`, `is_host`, `gender` 등
- **Room**
  - `owner` (User FK), `name`, `price`, `category`, `amenities`, `photos`
- **Amenity**
  - `name`, `description`
- **Booking**
  - `user`, `room`, `check_in`, `check_out`
- **Review**
  - `user`, `room`, `payload`, `rating`

## 🔐 인증 및 권한 처리
- Django 기본 인증 + JWT 토큰 인증 구현
- 로그인된 사용자만 예약/리뷰 작성 가능
- 숙소 소유자만 수정/삭제 가능 (`is_owner` 확인)
- `IsAuthenticatedOrReadOnly`, `PermissionDenied` 등 DRF 권한 시스템 사용


## 🔍 테스트 방식
- Postman / Thunder Client를 통해 CRUD 기능 직접 테스트
- 인증/비인증 상태에 따른 접근 권한 확인

## 💡 느낀 점
- 사용자 인증과 권한 처리를 통해 **보안적인 흐름을 실감**하며 학습할 수 있었고,  
- Django REST Framework의 구조적인 API 설계 방식에 대한 감을 키울 수 있었습니다.  
- 프론트엔드를 사용하지 않고도 **API 단독 프로젝트로 기능 중심 백엔드 개발을 경험**할 수 있었습니다.


## ✅ 선택적으로 추가하면 좋은 것
- `Docker`로 개발 환경 구성
- `pytest` 기반 단위 테스트 추가
- `Render`나 `Railway`로 백엔드 배포
- API문서 자동화
- CI/CD (예: GitHub Actions) 구성
