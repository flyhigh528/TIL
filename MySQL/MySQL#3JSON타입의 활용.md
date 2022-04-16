# MySQL 뿌시기 Step3 🐧
<img src="./images/mysql.png" width="700px" height="250px" title="MySQL Title" alt="MySQL_Dolphin"></img>

# JSON Type 활용하기!
## 🌟🌟🌟 JSON Type 🌟🌟🌟
- JSON가 활용되기 좋은 경우!
  - 빠른 조회보다 데이터의 저장에 중점을 두는 데이터
  - 변화가 없으면서 정형화되지 않으며, 다양한 형식의 변화가 요구되는 데이터
  - 어플리케이션을 통한 데이터를 처리하고 DB에는 단순 저장이 요구되는 데이터
  - 지속적인 데이터의 형식에 변화가 가능한 데이터
- JSON 테이블 생성 & 입력 예제
```
-- JSON Type의 info 컬럼이 있는 users 테이블 생성
CREATE TABLE users ( 
    id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(64) NOT NULL,    
    info JSON
);   

-- users 테이블에 데이터 입력, JSON은 Key값과 Data값 입력
insert into users (email, info) values
('1@naver.com', '{ 
    "name": "1",
    "age":37,
    "address1":"suwon",
    "address2":"yongtong",
    "tel":"010-000-0001"  
}'),
('2@naver.com', '{ 
    "name": "12",
    "age":37,
    "address1":"suwon",
    "address2":"yongtong",
    "tel":"010-000-3"  
}');
```
- JSON 데이터 Select
  - JSON 데이터에 있는 Key는 **path 연산자(->)**로 읽을 수 있다.
```
-- JSON Type의 info에서 name과 age 키값의 데이터를 조회
select id, email, info -> '$.name' , info -> '$.age' from users;
```
- JSON 데이터 Update
```
update users set info = JSON_SET(info, '$.age', 1) where id=1;
```

### MySQL JSON Path 표현식
MySQL은 JSON 데이터를 처리하는 쿼리를 쉽게 사용하기 위한 **JSON path 표현식(expressions)**를 제공한다.
- path 연산자(->) 는 JSON_EXTRACT()와 동일하다. 아래는 두 쿼리는 동일한 조회 조건이다.
```
SELECT * FROM users WHERE info->'$.name' = 'yundream';

SELECT * FROM users WHERE json_extract(info, '$.name') = 'yundream';

-- "(쌍따옴표)를 뺀 결과값 조회
SELECT * FROM users WHERE info->>'$.name' = 'yundream';

SELECT * FROM users WHERE json_unquote(json_extract(info, '$.name')) = 'yundream';
```
#
## JSON 함수들 8.0기준 (https://dev.mysql.com/doc/refman/8.0/en/json-function-reference.html)
| 함수명 | 설명 | 예제 |
| :----: |  :----: | ----------------------------|
|JSON_VALID() |JSON 데이터의 유효성 검사| |
|JSON_PRETTY() |들여쓰기를 포함해 보기 좋게 JSON 데이터 출력| |
|JSON_OBJECT() |문자열 형태가 아닌 key, value 쌍으로 JSON 데이터 만들기| |
|JSON_ARRAY() | JSON 데이터를 배열(Array) 형태로 작성 및 변환| |
|JSON_EXTRACT() | 인라인 패스(->)와 같이 특정 값만 뽑아 추출| |
|JSON_VALUE() |특정 값 추출, 출력 타입 정의 가능|| |
|JSON_QUOTE() | 특정 값 추출시 값의 좌우에 큰따옴표 붙여서 출력| |
|JSON_UNQUOTE() | 특정 값 추출시 값의 좌우에 출력되는 큰따옴표 제거| |
|JSON_LENGTH() | JSON 데이터의 키 개수| |
|JSON_DEPTH() | JSON 데이터의 깊이(계층)| |
|JSON_KEYS() | JSON 데이터의 key들만 추출| |
|JSON_TYPE() | JSON 데이터의 데이터 타입 출력| |
|JSON_SEARCH() |특정값으로 JSON 패스(위치) 검색| select<br> json_search(info, 'one', 'kaka'),<br> info -> "$.ame[0].first"<br> from users;|
|JSON_CONTAINS() |JSON 데이터에 특정 값의 존재 여부 확인| |
|JSON_REPLACE() |JSON 데이터의 값 부분 변경| |
|JSON_INSERT() | JSON 데이터에 특정 key, value 쌍을 추가| |
|JSON_SET() |JSON 데이터에서 특정 key에 해당되는 값만 변경| |
|JSON_REMOVE() |JSON 데이터의 특정 key, value 제거| |
|JSON_MERGE() |기존 JSON 데이터에 값 추가, MySQL 8에서 deprecated됨| |
|JSON_MERGE_PRESERVE() | JSON 데이터 특정 위치의 값 변경(기존 값 유지)| |
|JSON_MERGE_PATCH() | JSON 데이터 특정 위치의 값 변경(기존 값 대치)| |
|JSON_TABLE() | JSON 데이터를 테이블 형태로 정의| |
|JSON_ARRAYAGG() |전체 JSON 데이터를 취합(통합)하여 배열로 출력| |
|JSON_OBJECTAGG() | JSON 데이터를 취합(통합)하여 Object 형태로 출력| |
|JSON_STORAGE_SIZE() | JSON 데이터가 차지하는 데이터 크기| |
|JSON_STORAGE_FREE() | JSON 데이터 컬럼의 여유공간, JSON 데이터 있으면 항상 0| |

## JSON_TABLE
```
select * from 
  json_table(' [{"last": "aa", "first": "bb", "age": "xx"}, {"last": "cc", "first": "dd", "age":5}]',
  '$[*]'
  columns(
		j_last varchar(10) path '$.last',
        j_first varchar(10) path '$.first',
        -- empty일 때 0, error일 때 -1로 대체 출력
        j_age int path '$.age' default '0' on empty default '-1' on error,
        -- age에 값이 있는경우 1, 없는경우 0 출력
        j_age_exists tinyint exists path '$.age'
    )
  ) a;

-- 일반 테이블과 JOIN이 가능
select * from 
  json_table(' [{"id":1,"last": "aa", "first": "bb", "age": "xx"}, {"id":2,"last": "cc", "first": "dd", "age":5}]',
  '$[*]'
  columns(
		j_id int path '$.id',
		j_last varchar(10) path '$.last',
        j_first varchar(10) path '$.first',
        -- empty일 때 0, error일 때 -1로 대체 출력
        j_age int path '$.age' default '0' on empty default '-1' on error,
        -- age에 값이 있는경우 1, 없는경우 0 출력
        j_age_exists tinyint exists path '$.age'
    )
  ) j
	inner join users u on j.id = u.id;
```

## JSON의 INDEX 사용!
1. 테이블 생성 시, JSON 컬럼의 Key에 대해서 색인을 생성
```
CREATE TABLE users (
    id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(64) NOT NULL,
    info JSON,                                          
    -- info_name은 info컬럼의 name에 접근
    info_name VARCHAR(10) GENERATED ALWAYS AS (info->'$.name')
);                 
```
2. Index 생성
```
CREATE INDEX `name_idx` ON users(name_virtual);
```

### 이러한 방법을 이용하면 JSON형식의 Key를 조건으로 사용하는 경우에도 Index 참조가 가능하다.
   

자세한 Type별 설명은 [MySQL Manual](https://dev.mysql.com/doc/refman/8.0/en/data-types.html) 참조!