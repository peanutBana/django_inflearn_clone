
# Django Inflearn Clone

## 장고 기능을 익히기 위한 인프런 사이트 클론코딩 입니다.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/93357028/188320546-d2f55cf8-ae02-453b-bcc6-d18042c95031.png">

## 목차
1.  [들어가며](#open)
    - [프로젝트 소개](#introduce)
    - [프로젝트 기능](#function)
    - [사용 기술](#used_tech)
        - [백엔트](#backend)
        - [프론트 엔드](#frontend)

2. [구조 및 설계](#structure) 
    - [프로젝트 구조](#project_structure)
    - [DB 설계](#DB_map)
    - [API 설계](#API_map)

3. [개발 내용](#dev_log)

4. [마치며](#close)
   - [프로젝트 보완사항](#fix)
   - [후기](#epil)

## 들어가며
### 1.프로젝트 소개
장고라는 웹 프레임워크를 사용하여 기본적인 로그인/아웃 기능, 회원가입 기능, 강의 CRUD 기능을 익히기 위해 시작된 프로젝트 입니다. 강의를 여러번 보며 다른 기능도 추가할 예정입니다!

### 2.프로젝트 기능
프로젝트의 주요 기능

- 홈 - 좌측 상단 홈버튼, 우측 상단에 강의 리스트보기, 로그인/아웃,강의 만들기(로그인 시), 회원가입 버튼, 강의 리스트
- 사용자 - 회원가입 및 로그인, 강의 CRUD
- 댓글 - CRUD 기능
# Django Inflearn Clone

## 장고 기능을 익히기 위한 인프런 사이트 클론코딩 입니다.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/93357028/188320546-d2f55cf8-ae02-453b-bcc6-d18042c95031.png">

## 목차
1.  [들어가며](#open)
    - [프로젝트 소개](#introduce)
    - [프로젝트 기능](#function)
    - [사용 기술](#used_tech)
        - [백엔트](#backend)
        - [프론트 엔드](#frontend)

2. [구조 및 설계](#structure) 
    - [프로젝트 구조](#project_structure)
    - [DB 설계](#DB_map)
    - [API 설계](#API_map)

3. [개발 내용](#dev_log)

4. [마치며](#close)
   - [프로젝트 보완사항](#fix)
   - [후기](#epil)

## 들어가며
### 1. 프로젝트 소개
장고라는 웹 프레임워크를 사용하여 기본적인 로그인/아웃 기능, 회원가입 기능, 강의 CRUD 기능을 익히기 위해 시작된 프로젝트 입니다. 강의를 여러번 보며 다른 기능도 추가할 예정입니다!

### 2. 프로젝트 기능
프로젝트의 주요 기능

- 홈 - 좌측 상단 홈버튼, 우측 상단에 강의 리스트보기, 로그인/아웃,강의 만들기(로그인 시), 회원가입 버튼, 강의 리스트
- 사용자 - 회원가입 및 로그인, 강의 CRUD
- 댓글 - CRUD 기능

### 3. 사용 기술
#### 백엔드

- Python3
- Django 4.0.5
- Ckeditor

IDE

- Visual Studio Code

DataBase

- Sqlite 3

#### 프론트엔드
- HTML/CSS
- JavaScript
- jQuery 3.6.0
- Bootstrap 3.3.2

### 4.실행화면

<details>
<summary>강의 관련</summary>
<div markdown="1">

---
1. 강의리스트 전체 목록
<img src="https://user-images.githubusercontent.com/93357028/188324913-80762936-487b-4031-b101-5980e2151963.png">
  
---
2. 강의 상세 조회
<img src="https://user-images.githubusercontent.com/93357028/188476775-c2a48b83-1157-4902-b3f2-245e936090e7.png">
강의 상세 내용 

---
3. 강의 만들기
<img src="https://user-images.githubusercontent.com/93357028/188477355-2c7e9c37-29f1-4d44-9f37-b3846d6b1499.png">
새로운 강의 작성 후 메인 화면으로 redirect 한다.

---
4. 내가 만든 강의 조회
<img src="https://user-images.githubusercontent.com/93357028/188477690-b64aa2fc-c51c-40fc-ab48-bba49791092b.png">
로그인 한 사용자가 작성한 강의만 조회 가능하다.

</div>
</details>

<details>
<summary>회원 관련</summary>
<div markdown="1">

---
1. 회원가입 화면
<img src="https://user-images.githubusercontent.com/93357028/188484430-c9e55962-d7d5-4c68-b047-5d40aef768da.png">
회원가입 완료 후 메인화면으로 redirct

---
2. 로그인 화면
<img src="https://user-images.githubusercontent.com/93357028/188484852-4e430861-0750-43ef-b3dd-bfedf335e36e.png">
</div>
</details>

<details>
<summary>댓글 관련</summary>
<div markdown="1">

---
1. 댓글 작성 화면
<img src="https://user-images.githubusercontent.com/93357028/188486142-5272edce-5bf8-4613-9e92-2b722b1ecd0a.png">
댓글 제출버튼, 동영상강의 링크, 댓글 내용(스타일 개선 예정) 및 삭제버튼(admin계정)

</div>
</details>

## 구조 및 설계
### 1. 프로젝트 구조 

<details>
<summary>프로젝트 구조 보기</summary>
<div markdown="1">

<img src="https://user-images.githubusercontent.com/93357028/188486985-608d81c7-8c2f-4230-bb10-3da325436215.png">

</div>
</details>

### 2. DB 설계

<details>
<summary>DB 설계 보기</summary>
<div markdown="1">
<img width="437" alt="image" src="https://user-images.githubusercontent.com/93357028/188488922-196e1a3d-af16-4d97-a2cd-514521cf6c6b.png">
<img width="619" alt="image" src="https://user-images.githubusercontent.com/93357028/188488782-29b5e238-490f-402c-b0ad-2e3b0259c7d0.png">
</div>
</details>

### 3. API 설계

<details>
<summary>API 설계 보기</summary>
<div markdown="1">

</div>
</details>

