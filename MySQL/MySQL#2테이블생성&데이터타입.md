# MySQL 뿌시기 Step2 🐧
<img src="./images/mysql.png" width="700px" height="250px" title="MySQL Title" alt="MySQL_Dolphin"></img>

# 1. 테이블생성 & DataType

## 테이블 생성 기본 문법
```CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [partition_options]

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [partition_options]
    [IGNORE | REPLACE]
    [AS] query_expression

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    { LIKE old_tbl_name | (LIKE old_tbl_name) }

create_definition: {
    col_name column_definition
  | {INDEX | KEY} [index_name] [index_type] (key_part,...)
      [index_option] ...
  | {FULLTEXT | SPATIAL} [INDEX | KEY] [index_name] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] PRIMARY KEY
      [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
      [index_name] [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] FOREIGN KEY
      [index_name] (col_name,...)
      reference_definition
  | check_constraint_definition
}

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT {literal | (expr)} ]
      [VISIBLE | INVISIBLE]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
      [SECONDARY_ENGINE_ATTRIBUTE [=] 'string']
      [STORAGE {DISK | MEMORY}]
      [reference_definition]
      [check_constraint_definition]
  | data_type
      [COLLATE collation_name]
      [GENERATED ALWAYS] AS (expr)
      [VIRTUAL | STORED] [NOT NULL | NULL]
      [VISIBLE | INVISIBLE]
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [reference_definition]
      [check_constraint_definition]
}

data_type:
    (see Chapter 11, Data Types)

key_part: {col_name [(length)] | (expr)} [ASC | DESC]

index_type:
    USING {BTREE | HASH}

index_option: {
    KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'
  | {VISIBLE | INVISIBLE}
  |ENGINE_ATTRIBUTE [=] 'string'
  |SECONDARY_ENGINE_ATTRIBUTE [=] 'string'
}

check_constraint_definition:
    [CONSTRAINT [symbol]] CHECK (expr) [[NOT] ENFORCED]

reference_definition:
    REFERENCES tbl_name (key_part,...)
      [MATCH FULL | MATCH PARTIAL | MATCH SIMPLE]
      [ON DELETE reference_option]
      [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT

table_options:
    table_option [[,] table_option] ...

table_option: {
    AUTOEXTEND_SIZE [=] value
  | AUTO_INCREMENT [=] value
  | AVG_ROW_LENGTH [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | CHECKSUM [=] {0 | 1}
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB' | 'LZ4' | 'NONE'}
  | CONNECTION [=] 'connect_string'
  | {DATA | INDEX} DIRECTORY [=] 'absolute path to directory'
  | DELAY_KEY_WRITE [=] {0 | 1}
  | ENCRYPTION [=] {'Y' | 'N'}
  | ENGINE [=] engine_name
  | ENGINE_ATTRIBUTE [=] 'string'
  | INSERT_METHOD [=] { NO | FIRST | LAST }
  | KEY_BLOCK_SIZE [=] value
  | MAX_ROWS [=] value
  | MIN_ROWS [=] value
  | PACK_KEYS [=] {0 | 1 | DEFAULT}
  | PASSWORD [=] 'string'
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | SECONDARY_ENGINE_ATTRIBUTE [=] 'string'
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value
  | TABLESPACE tablespace_name [STORAGE {DISK | MEMORY}]
  | UNION [=] (tbl_name[,tbl_name]...)
}

partition_options:
    PARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list)
        | RANGE{(expr) | COLUMNS(column_list)}
        | LIST{(expr) | COLUMNS(column_list)} }
    [PARTITIONS num]
    [SUBPARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list) }
      [SUBPARTITIONS num]
    ]
    [(partition_definition [, partition_definition] ...)]

partition_definition:
    PARTITION partition_name
        [VALUES
            {LESS THAN {(expr | value_list) | MAXVALUE}
            |
            IN (value_list)}]
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string' ]
        [DATA DIRECTORY [=] 'data_dir']
        [INDEX DIRECTORY [=] 'index_dir']
        [MAX_ROWS [=] max_number_of_rows]
        [MIN_ROWS [=] min_number_of_rows]
        [TABLESPACE [=] tablespace_name]
        [(subpartition_definition [, subpartition_definition] ...)]

subpartition_definition:
    SUBPARTITION logical_name
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string' ]
        [DATA DIRECTORY [=] 'data_dir']
        [INDEX DIRECTORY [=] 'index_dir']
        [MAX_ROWS [=] max_number_of_rows]
        [MIN_ROWS [=] min_number_of_rows]
        [TABLESPACE [=] tablespace_name]

query_expression:
    SELECT ...   (Some valid select or union statement)
```
#
## Data Type
### Integer Type 숫자형

| 타입 | 저장용량 (Bytes) |	Signed 최소값 |	Unsigned 최소값 | Signed 최대값 | Unsigned 최대값 |
| :----: | :----: | :----: | :----: | :----: | ----------------------------|
|TINYINT |	1 |	-128 |	0 |	127 |	255 |
|SMALLINT |	2 |	-32768 |	0 |	32767 |	65535 |
|MEDIUMINT |	3 |	-8388608 |	0 |	8388607 |	16777215 |
|INT |	4 |	-2147483648 |	0 |	2147483647 |	4294967295 |
|BIGINT |	8 |	-2<sup>63</sup> |	0 |	2<sup>63</sup> -1 |	2<sup>64</sup>-1 |

#
### String Type 문자형
  
| 타입 | 최소길이 | 최대길이 | 정의 |
| :----: | :----: | :----: | ----------------------------|
|CHAR(n) | 0 | 255 |- 고정 길이 데이터 타입<br>- 지정된 길이보다 짧은 데이터 입력 시 나머지는 공백으로 채워짐<br> - 검색시, PAD_CHAR_TO_FULL_LENGTH 모드를 설정하지 않으면 공백은 제거됨 |
|VACHAR(n)| 0| 65,535 | - 가변 길이 데이터 타입<br>- 지정된 길이보다 짧은 데이터 입력시 공백으로 채우지 않음<br>- 저장시 1-byte 혹은 2-byte 길이 Prefix 데이터를 저장. 이 Prefix 데이터는 값의 바이트 수에 대한 정보를 담는다.	|
|TINYTEXT(n) | 0 | 255 |- 문자열 데이터 타입(최대 255 byte)<br>- TINYBLOB와 같은 길이값을 저장 가능(단 차이점은 저장 될때 nonbinary string으로 저장) |
|TEXT(n) | 0 | 65,535 |	- 문자열 데이터 타입(최대 65,535 byte)<br>- BLOB와 같은 길이값을 저장 가능(단 차이점은 저장 될때 nonbinary string으로 저장)	 |
| MEDIUMTEXT(n) | 0 | 16,777,215 | - 문자열 데이터 타입(최대 16,777,215 byte)<br>- MEDIRMBLOB와 같은 길이값을 저장 가능(단 차이점은 저장 될때 nonbinary string으로 저장) |
|LONGTEXT(n) | 0 | 4,294,967,295 | - 문자열 데이터 타입(최대 4,294,967,295 byte)<br>- LONGBLOB와 같은 길이값을 저장 가능(단 차이점은 저장 될때 nonbinary string으로 저장)	|

#
### Date and Time Data Type

| 타입 | 길이 | 형식 | 길이 |  정의 |
| :----: | :----: | :----: | :----: | ----------------------------|
|DATE | 3 byte |	0000-00-00 (YYYY-MM-DD) | 1000-01-01 ~ 9999-12-31 |  날짜(년도, 월, 일) 형태의 기간 표현 데이터	|
|TIME |	3 byte |	00:00:00 | . |시간(시, 분, 초) 형태의 기간 표현 데이터 |
|DATETIME | 8 byte | 0000-00-00 00:00:00 (YYYY-MM-DD hh:mm:ss) | 1000-01-01 00:00:00.000000 ~ 9999-12-31 23:59:59.999999 | 날짜와 시간 형태의 기간 표현 데이터	|
|TIMESTAMP | 4 byte	| Integer | . | 날짜와 시간 형태의 기간 표현 데이터 타입 시스템 변경 시 자동으로 그 날짜와 시간이 저장 |
|YEAR | 1 byte | 0000 | . | 년도 표현 데이터 타입 | 

#
### Binary and BLOB Data Type
| 타입 | 길이 | 정의 |
| :----: |  :----: | ----------------------------|
| BINARY(n) & BYTE(n) | 최대 255 byte | CHAR 형태의 이진 데이터 타입 |
| VARBINARY(n) | 최대 65,535 byte | VARCHAR 형태의 이진 데이터 타입 |
| TINYBLOB(n) | 최대 255 byte | 이진 데이터 타입 | 
| BLOB(n) | 최대 65,535 byte | 이진 데이터 타입	|
| MEDIUMBLOB(n)	| 최대 16,777,215 byte | 이진 데이터 타입 |
| LONGBLOB(n) | 최대 4,294,967,295 byte | 이진 데이터 타입	|