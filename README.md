## Wash Korea Project

[데모 영상](https://drive.google.com/file/d/1BbsvlZo2QaIZrlAps9iEAxLlXMc7TCYO/view?usp=sharing)
[웹 사이트](링크 추가 예정)

### [팀명] : Wash Korea(워시 코리아)

- 러쉬코리아(https://lush.co.kr/) 클론 프로젝트
- 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 클론했습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며, 위 데모 영상에서 보이는 부분은 모두 백앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.

### 프로젝트 선정이유

- 기본적인 커머스 사이트에 필요한 핵심 기능들을 구현해 볼 수 있어서 선택하게 되었습니다.

### 개발 인원 및 기간

- 개발기간 : 2021/11/1 ~ 2021/11/12
- 개발 인원 : 프론트엔드 3명, 백엔드 2명
- 팀원 : 권은경, 박보라, 석예주, 이수경, 허규빈
- [프론드 github 링크](https://github.com/wecode-bootcamp-korea/26-1st-WASH-Korea-frontend)
- [백 github 링크](https://github.com/wecode-bootcamp-korea/26-1st-WASH-Korea-backend)

<br>

## 적용 기술 및 구현 기능

### 적용 기술

> - Front-End : JavaScript, React.js, sass, react-modal
> - Back-End : Django, Python, MySQL, jwt, bcrypt, AWS(EC2, RDS)
> - Common : Git, Github, Slack, Trello, dbdiagram, postman

### Modeling
![](https://images.velog.io/images/gyuls/post/294fcef4-a36b-4b16-b465-5979ace9d49f/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7,%202021-11-14%2022-00-41.png)

### 구현 기능

#### 권은경
> 로그인 & 회원가입
- bcrypt 활용 패스워드 암호화
- JWT 활용 인증/인가 기능

> 제품 상세페이지
- 제품 상세페이지 조회 api

> 리뷰
- 리뷰 CRUD API

#### 허규빈
> 카테고리 & 제품 리스트 페이지
- 카테고리 & 정렬 제품리스트 api
- 검색된 제품리스트

> 장바구니
- 장바구니 CRUD API

<br>

## Reference

- 이 프로젝트는 [러쉬](https://lush.co.kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
