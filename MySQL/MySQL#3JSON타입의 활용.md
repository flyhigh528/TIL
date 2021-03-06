# MySQL λΏμκΈ° Step3 π§
<img src="./images/mysql.png" width="700px" height="250px" title="MySQL Title" alt="MySQL_Dolphin"></img>

# JSON Type νμ©νκΈ°!
## πππ JSON Type πππ
- JSONκ° νμ©λκΈ° μ’μ κ²½μ°!
  - λΉ λ₯Έ μ‘°νλ³΄λ€ λ°μ΄ν°μ μ μ₯μ μ€μ μ λλ λ°μ΄ν°
  - λ³νκ° μμΌλ©΄μ μ ννλμ§ μμΌλ©°, λ€μν νμμ λ³νκ° μκ΅¬λλ λ°μ΄ν°
  - μ΄νλ¦¬μΌμ΄μμ ν΅ν λ°μ΄ν°λ₯Ό μ²λ¦¬νκ³  DBμλ λ¨μ μ μ₯μ΄ μκ΅¬λλ λ°μ΄ν°
  - μ§μμ μΈ λ°μ΄ν°μ νμμ λ³νκ° κ°λ₯ν λ°μ΄ν°
- JSON νμ΄λΈ μμ± & μλ ₯ μμ 
```
-- JSON Typeμ info μ»¬λΌμ΄ μλ users νμ΄λΈ μμ±
CREATE TABLE users ( 
    id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(64) NOT NULL,    
    info JSON
);   

-- users νμ΄λΈμ λ°μ΄ν° μλ ₯, JSONμ Keyκ°κ³Ό Dataκ° μλ ₯
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
- JSON λ°μ΄ν° Select
  - JSON λ°μ΄ν°μ μλ Keyλ **path μ°μ°μ(->)**λ‘ μ½μ μ μλ€.
```
-- JSON Typeμ infoμμ nameκ³Ό age ν€κ°μ λ°μ΄ν°λ₯Ό μ‘°ν
select id, email, info -> '$.name' , info -> '$.age' from users;
```
- JSON λ°μ΄ν° Update
```
update users set info = JSON_SET(info, '$.age', 1) where id=1;
```

### MySQL JSON Path ννμ
MySQLμ JSON λ°μ΄ν°λ₯Ό μ²λ¦¬νλ μΏΌλ¦¬λ₯Ό μ½κ² μ¬μ©νκΈ° μν **JSON path ννμ(expressions)**λ₯Ό μ κ³΅νλ€.
- path μ°μ°μ(->) λ JSON_EXTRACT()μ λμΌνλ€. μλλ λ μΏΌλ¦¬λ λμΌν μ‘°ν μ‘°κ±΄μ΄λ€.
```
SELECT * FROM users WHERE info->'$.name' = 'yundream';

SELECT * FROM users WHERE json_extract(info, '$.name') = 'yundream';

-- "(μλ°μ΄ν)λ₯Ό λΊ κ²°κ³Όκ° μ‘°ν
SELECT * FROM users WHERE info->>'$.name' = 'yundream';

SELECT * FROM users WHERE json_unquote(json_extract(info, '$.name')) = 'yundream';
```
#
## JSON ν¨μλ€ 8.0κΈ°μ€ (https://dev.mysql.com/doc/refman/8.0/en/json-function-reference.html)
| ν¨μλͺ | μ€λͺ | μμ  |
| :----: |  :----: | ----------------------------|
|JSON_VALID() |JSON λ°μ΄ν°μ μ ν¨μ± κ²μ¬| |
|JSON_PRETTY() |λ€μ¬μ°κΈ°λ₯Ό ν¬ν¨ν΄ λ³΄κΈ° μ’κ² JSON λ°μ΄ν° μΆλ ₯| |
|JSON_OBJECT() |λ¬Έμμ΄ ννκ° μλ key, value μμΌλ‘ JSON λ°μ΄ν° λ§λ€κΈ°| |
|JSON_ARRAY() | JSON λ°μ΄ν°λ₯Ό λ°°μ΄(Array) ννλ‘ μμ± λ° λ³ν| |
|JSON_EXTRACT() | μΈλΌμΈ ν¨μ€(->)μ κ°μ΄ νΉμ  κ°λ§ λ½μ μΆμΆ| |
|JSON_VALUE() |νΉμ  κ° μΆμΆ, μΆλ ₯ νμ μ μ κ°λ₯|| |
|JSON_QUOTE() | νΉμ  κ° μΆμΆμ κ°μ μ’μ°μ ν°λ°μ΄ν λΆμ¬μ μΆλ ₯| |
|JSON_UNQUOTE() | νΉμ  κ° μΆμΆμ κ°μ μ’μ°μ μΆλ ₯λλ ν°λ°μ΄ν μ κ±°| |
|JSON_LENGTH() | JSON λ°μ΄ν°μ ν€ κ°μ| |
|JSON_DEPTH() | JSON λ°μ΄ν°μ κΉμ΄(κ³μΈ΅)| |
|JSON_KEYS() | JSON λ°μ΄ν°μ keyλ€λ§ μΆμΆ| |
|JSON_TYPE() | JSON λ°μ΄ν°μ λ°μ΄ν° νμ μΆλ ₯| |
|JSON_SEARCH() |νΉμ κ°μΌλ‘ JSON ν¨μ€(μμΉ) κ²μ| select<br> json_search(info, 'one', 'kaka'),<br> info -> "$.ame[0].first"<br> from users;|
|JSON_CONTAINS() |JSON λ°μ΄ν°μ νΉμ  κ°μ μ‘΄μ¬ μ¬λΆ νμΈ| |
|JSON_REPLACE() |JSON λ°μ΄ν°μ κ° λΆλΆ λ³κ²½| |
|JSON_INSERT() | JSON λ°μ΄ν°μ νΉμ  key, value μμ μΆκ°| |
|JSON_SET() |JSON λ°μ΄ν°μμ νΉμ  keyμ ν΄λΉλλ κ°λ§ λ³κ²½| |
|JSON_REMOVE() |JSON λ°μ΄ν°μ νΉμ  key, value μ κ±°| |
|JSON_MERGE() |κΈ°μ‘΄ JSON λ°μ΄ν°μ κ° μΆκ°, MySQL 8μμ deprecatedλ¨| |
|JSON_MERGE_PRESERVE() | JSON λ°μ΄ν° νΉμ  μμΉμ κ° λ³κ²½(κΈ°μ‘΄ κ° μ μ§)| |
|JSON_MERGE_PATCH() | JSON λ°μ΄ν° νΉμ  μμΉμ κ° λ³κ²½(κΈ°μ‘΄ κ° λμΉ)| |
|JSON_TABLE() | JSON λ°μ΄ν°λ₯Ό νμ΄λΈ ννλ‘ μ μ| |
|JSON_ARRAYAGG() |μ μ²΄ JSON λ°μ΄ν°λ₯Ό μ·¨ν©(ν΅ν©)νμ¬ λ°°μ΄λ‘ μΆλ ₯| |
|JSON_OBJECTAGG() | JSON λ°μ΄ν°λ₯Ό μ·¨ν©(ν΅ν©)νμ¬ Object ννλ‘ μΆλ ₯| |
|JSON_STORAGE_SIZE() | JSON λ°μ΄ν°κ° μ°¨μ§νλ λ°μ΄ν° ν¬κΈ°| |
|JSON_STORAGE_FREE() | JSON λ°μ΄ν° μ»¬λΌμ μ¬μ κ³΅κ°, JSON λ°μ΄ν° μμΌλ©΄ ν­μ 0| |

## JSON_TABLE
```
select * from 
  json_table(' [{"last": "aa", "first": "bb", "age": "xx"}, {"last": "cc", "first": "dd", "age":5}]',
  '$[*]'
  columns(
		j_last varchar(10) path '$.last',
        j_first varchar(10) path '$.first',
        -- emptyμΌ λ 0, errorμΌ λ -1λ‘ λμ²΄ μΆλ ₯
        j_age int path '$.age' default '0' on empty default '-1' on error,
        -- ageμ κ°μ΄ μλκ²½μ° 1, μλκ²½μ° 0 μΆλ ₯
        j_age_exists tinyint exists path '$.age'
    )
  ) a;

-- μΌλ° νμ΄λΈκ³Ό JOINμ΄ κ°λ₯
select * from 
  json_table(' [{"id":1,"last": "aa", "first": "bb", "age": "xx"}, {"id":2,"last": "cc", "first": "dd", "age":5}]',
  '$[*]'
  columns(
		j_id int path '$.id',
		j_last varchar(10) path '$.last',
        j_first varchar(10) path '$.first',
        -- emptyμΌ λ 0, errorμΌ λ -1λ‘ λμ²΄ μΆλ ₯
        j_age int path '$.age' default '0' on empty default '-1' on error,
        -- ageμ κ°μ΄ μλκ²½μ° 1, μλκ²½μ° 0 μΆλ ₯
        j_age_exists tinyint exists path '$.age'
    )
  ) j
	inner join users u on j.id = u.id;
```

## JSONμ INDEX μ¬μ©!
1. νμ΄λΈ μμ± μ, JSON μ»¬λΌμ Keyμ λν΄μ μμΈμ μμ±
```
CREATE TABLE users (
    id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(64) NOT NULL,
    info JSON,                                          
    -- info_nameμ infoμ»¬λΌμ nameμ μ κ·Ό
    info_name VARCHAR(10) GENERATED ALWAYS AS (info->'$.name')
);                 
```
2. Index μμ±
```
CREATE INDEX `name_idx` ON users(name_virtual);
```

### μ΄λ¬ν λ°©λ²μ μ΄μ©νλ©΄ JSONνμμ Keyλ₯Ό μ‘°κ±΄μΌλ‘ μ¬μ©νλ κ²½μ°μλ Index μ°Έμ‘°κ° κ°λ₯νλ€.
   

μμΈν Typeλ³ μ€λͺμ [MySQL Manual](https://dev.mysql.com/doc/refman/8.0/en/data-types.html) μ°Έμ‘°!