# Index & Partition 성능 향상 기법

## Index
- Index Scan VS Table Scan (Full Table Search)
- Clustered Index VS Non-Clustered(secondary) Index
- Clustered Index (물리적 데이터 파일(PK)을 이용한 인덱스)
  > PK or Unique index
  > Physica Data File
- Only Reading(Select) Performance (Insert 속도는 느림)
- Fast MySQL Optimizer (8.0부터는 2~3배정도 빨라져 사용이 용이)
- Cardinality
  > Cardinality가 높은 경우가 조회 Cost가 적게 들어간다.
  > Cardinality는 조회 값의 중복도 정도. distinct 값이 많으면, 중복도가 '낮다'
    - ex) 1,2,3,4,5 는 Cardinality가 '높음' / 남자,여자 는 Cardinality가 '낮음'

<pre><code>
SELECT    *
FROM      테이블명
use index (인덱스명)
WHERE     조건
</code></pre>

## B(Balanced)-Tree
- Roots, Branches, Leaves Node
- Node == Page
- 1Page = 16KB(16384)
- Page Splits(50% Threshold(한계), 8KB)
- Leaf Node
    - Clustered Index(PK 인 경우) -> Data(물리적 테이블 데이터)
    - Non-Clusted Index -> RID(행 식별자)
      - RID : '파일그룹번호-데이터페이지번호-데이터페이지오프셋'으로 구성되는 포인팅 정보이다. 
              ex) 1-3-1, 1번 파일그룹의 3번 데이터 페이지의 1번째 데이터가 된다.

## Execution Plan
<pre><code> explan select * from 테이블명 where 조건
</code></pre>
- id : select id
- select_type : SIMPLE, UNION, SUBQUERY, etc
- type : data scan type 
  - const : PK와 같은 Clustered Index, 
  - ALL : Full scan, 
  - ref : Unique하지않은 Index 사용, 
  - range : Index 범위 사용, 
  - index : 특정 Index 사용, 
  - fulltext : fulltext Index 사용, 
  - etc
- possible_keys
- key : Selected key by Optimizer
- key_len : index size
- ref : const, columns
- rows : access row count(statistical estimation 통계적 추정)
- filtered : left rows (statistical estimation 통계적 추정)
- Extra : Using where, Using Index, Using filesort(Non-Clustered Index인 경우), etc

### 인덱스 생성 또는 재구성 후에는 optimize table, analyze table을 해주는게 좋음
  - optimize table 테이블명;
  - analyze table 테이블명;

## Show table로 인덱스 확인
 - show index from 테이블명
Data Size = Rows * Avg_row_length

## Index 정리
 - Clustered 인덱스는 데이터 파일과 직접 연관
 - 데이터 크기가 너무 크면 페이지 분할이 빈번하여 쓰기 성능 절하(Index 컬럼은 필요 컬럼만!)
 - 인덱스는 Cardinality가 높을수록 유리
 - Clustered 인덱스는 읽기 성능은 보조 인덱스보다 빠르지만 쓰기는 느림
 - 페이지 분할은 시스템에 부담이 간다
 - 다중 컬럼 인덱스는 순서를 꼭 고려할것
 - 인덱스는 꼭 필요한 것만
 - 전체 테이블의 10~15%이상을 읽을 경우 보조 인덱스는 사용 안함

## Clustered Index/ Non-Clustered Index 정리
- Clustered Index
  - 물리적으로 테이블의 데이터를 재배열
    - 데이터가 테이블에 삽입되는 순서에 상관없이 인덱스로 생성되어 있는 컬럼을 기준으로 정렬되어 삽입된다.
    - 인덱스 페이지를 **키값과 데이터 페이지의 번호로 구성**하고, 검색하고자하는 데이터의 키 값으로 페이지 번호를 알아내어 데이터를 찾는다.
- Non-Clustered Index
  - 물리적으로 데이터를 배열하지 않은 상태로 데이터 페이지가 구성된다.
  - **인덱스 페이지는 키값과 RID로 구성**된다
    - RID는 '파일그룹번호-데이터페이지번호-데이터페이지오프셋'으로 구성되는 포인팅 정보이다.
    - ex) 1-3-1, 1번 파일그룹의 3번 데이터 페이지의 1번째 데이터
    - 중간 레벨 인덱스 페이지들을 생성하고, 이 인덱스 페이지를 찾기위한 루트 레벨 인덱스 페이지를 생성한다.
    - 검색하고자하는 데이터의 키값을 루트 레벨 인덱스 페이지에서 비교하여 중간 레벨 인덱스 페이지 번호를 찾고, 중간 레벨 인덱스 페이지에서 RID 정보로 실제 데이터의 위치로 이동한다.

## Sargable(Search ARGument ABLE) Query
 - where, order by, group by 등에는 가능한 index가 걸린컬럼 사용
 - where 절에 함수, 연산, Like(앞부분 %)는 Not Sargable
 - between, like, 대소비교(<,> 등)는 범위가 크면 Not Sargable
 - or 연산자는 필터링의 반대개념(row를 늘리는)이므로 Not Sargable
 - offset이 길어지면 Not Sargable
   - ex) select * from 테이블명 order by 컬럼명 limit 10 offset 200;
   - 200개 이후의 값 10개를 출력해야하므로 offset값이 커지면 결국 전체 스캔과 다를게 없음.
 - 범위보다는 in  절을 사용하는게 좋고, in보다는 exists가 좋다
 - 꼭 필요한 경우가 아니라면 서브쿼리보다는 Join 사용


## Fulltext Index
- fulltext index default 제외단어 조회
<pre><code> select * from information_schema.inoodb_ft_default_stopword;
</code></pre>
- fulltext index 설정 조회
<pre><code> show variable like 'innodb_ft%';
</code></pre>
- 원하는 Stop Word 설정(한글)
<pre><code> /ect/my.cnf 파일의 옵션 변경
inoodb_ft_min_token_size=2
innodb_ft_server_stopword_table=데이터베이스명/테이블명
</code></pre>
- fulltext index 사용
<pre><code> select * from 테이블명 where match(인덱스컬럼1, 인덱스컬럼2) against('조건값'))
</code></pre>

- Search Expression 
    - "*" :  같은경우 
    - "+" : 조건을 추가하는 경우 
      - ex) ('조선* +중기*' IN BOLEAN MODE) : 조선~ 문자열이 있으면서 중기~ 문자열이 있는 데이터
    - "-" : 제외조건 추가 하는 경우
      - ex) ('조선* -후기*' IN BOLEAN MODE) : 조선~ 문자열이 있으면서 후기~ 문자열이 있는 데이터는 제외

## Partition
- 8,192개까지 가능
- FK 지정 불가
- PK를 지정할 경우 PK가 Partition Key
- Partition Types
  - Range : 컬럼 1개를 기준으로 범위조건(less than)을 이용해 파티셔닝 (INT형)
   <pre><code> partition by RANGE (컬럼1) (
                   Partition 조건명1 VALUES THAN (숫자조건),
                   partition 조건명2 values less then MAXVALUE
                 );</pre></code> 
  - List : IN 조건을 이용하여 파티셔닝 (INT형)
   <pre><code> partition by LIST (컬럼1) (
                   Partition 조건명1 VALUES IN (조건1, 조건2, ...),
                   Partition 조건명2 VALUES IN (조건3, 조건4, ...)
                 );</pre></code> 
  - Range Column : 여러 컬럼을 기준으로 잡아 범위조건으로 파티셔닝 (string, date, datetime 가능)
   <pre><code> partition by range columns (컬럼1,컬럼2) (
                   Partition 조건명 VALUES LESS THAN (조건1, 조건2),
                   Partition 조건명 VALUES LESS THAN (조건3, 조건4)
                 );</pre></code> 
  - List Column : 여러 컬럼을 기준으로 잡아 IN 조건으로 파티셔닝 (string, date, datetime 가능)
   <pre><code> partition by List columns (컬럼1,컬럼2) (
                   Partition 조건명 VALUES IN (조건1, 조건2),
                   Partition 조건명 VALUES IN (조건3, 조건4)
                 );</pre></code> 
  - Hash : 해시 함수를 이용해 데이터를 고르게 분포되도록 하기 위해 사용
   <pre><code> PARTITION BY HASH(컬럼명)
               PARTITIONS 나눌갯수;</pre></code> 
  - Key : 지정된 키 컬럼을 기준으로 파티셔닝, 여러 컬럼 기준으로 파티셔닝이 가능
   <pre><code> PARTITION BY HASH(컬럼명)
               PARTITIONS 나눌갯수;</pre></code> 

- 등록 Partition 조회
<pre><code> select * from information_schema.partitions
where table_name='테이블명';
</code></pre>
- Partition 수정
<pre><code> alter table 테이블명 REORGANIZE Partition 변경조건명(ex : p3) INTO (
  partition p3 values less than (새로운 조건)
  partition p4 values less than MAXVALUE
);
optimize table 테이블명;
</code></pre>
- Partition 삭제
<pre><code> alter table 테이블명 DROP Partition 조건명;
optimize table 테이블명;
</code></pre>

- Partition 사용의 유용한 Case
  - 이력성 데이터의 경우, 일정 기간이 지나면 백업 장치에 옮긴 뒤 DB에서는 삭제한다. 이런 경우 파티션 테이블이 데이터 삭제 주기와 일치하면 해당 파티션만 삭제하면 되므로 관리가 수월하다(삭제 속도도 빠름)