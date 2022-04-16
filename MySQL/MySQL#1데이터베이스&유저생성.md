# MySQL 뿌시기 Step1 🐧
<img src="./images/mysql.png" width="700px" height="250px" title="MySQL Title" alt="MySQL_Dolphin"></img>

## 1. 데이터베이스 & 유저 만들기

### 데이터베이스 생성하기
- 생성되어있는 데이터베이스 확인
```
mysql>show databases;
```
- 데이터 베이스 생성
```
mysql>create database <데이터베이스명>;
```
- 생성한 데이터베이스 사용
```
mysql>use <데이터베이스명>;
```
- 데이터베이스에 생성되어있는 테이블 조회
```
mysql>show tables;
```
- 데이터베이스 삭제
```
mysql>drop database <데이터베이스명>;
```

### User + Host 생성하기
- User 생성 (<host> : localhost 또는 %(ALL) 또는 IP) 
```
mysql>create user <user-name>@'<host>' identified by '<password>';
```
- 등록 User 확인
```
mysql>use mysql;
mysql>select host, user from user;
```
- 권한 부여
  - host별로 따로 권한부여가 가능, 분리하여 권한 부여
```
mysql>grant all privileges on *.* to '<user-name>'@'<host>;
```
- 특정 DB 권한 부여
```
mysql>grant all privileges on <DB>.* to <user-name>'@'<host>';
```
- 권한 변경 적용
```
mysql>flush privileges;
```
- User 삭제
```
mysql>drop user '<user>'@<host>';
```