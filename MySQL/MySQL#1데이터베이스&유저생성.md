# MySQL ๋ฟ์๊ธฐ Step1 ๐ง
<img src="./images/mysql.png" width="700px" height="250px" title="MySQL Title" alt="MySQL_Dolphin"></img>

## 1. ๋ฐ์ดํฐ๋ฒ ์ด์ค & ์ ์  ๋ง๋ค๊ธฐ

### ๋ฐ์ดํฐ๋ฒ ์ด์ค ์์ฑํ๊ธฐ
- ์์ฑ๋์ด์๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค ํ์ธ
```
mysql>show databases;
```
- ๋ฐ์ดํฐ ๋ฒ ์ด์ค ์์ฑ
```
mysql>create database <๋ฐ์ดํฐ๋ฒ ์ด์ค๋ช>;
```
- ์์ฑํ ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ฌ์ฉ
```
mysql>use <๋ฐ์ดํฐ๋ฒ ์ด์ค๋ช>;
```
- ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์์ฑ๋์ด์๋ ํ์ด๋ธ ์กฐํ
```
mysql>show tables;
```
- ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ญ์ 
```
mysql>drop database <๋ฐ์ดํฐ๋ฒ ์ด์ค๋ช>;
```

### User + Host ์์ฑํ๊ธฐ
- User ์์ฑ (<host> : localhost ๋๋ %(ALL) ๋๋ IP) 
```
mysql>create user <user-name>@'<host>' identified by '<password>';
```
- ๋ฑ๋ก User ํ์ธ
```
mysql>use mysql;
mysql>select host, user from user;
```
- ๊ถํ ๋ถ์ฌ
  - host๋ณ๋ก ๋ฐ๋ก ๊ถํ๋ถ์ฌ๊ฐ ๊ฐ๋ฅ, ๋ถ๋ฆฌํ์ฌ ๊ถํ ๋ถ์ฌ
```
mysql>grant all privileges on *.* to '<user-name>'@'<host>;
```
- ํน์  DB ๊ถํ ๋ถ์ฌ
```
mysql>grant all privileges on <DB>.* to <user-name>'@'<host>';
```
- ๊ถํ ๋ณ๊ฒฝ ์ ์ฉ
```
mysql>flush privileges;
```
- User ์ญ์ 
```
mysql>drop user '<user>'@<host>';
```