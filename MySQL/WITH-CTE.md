# WITH - CTE (Common Table Expression)
- MySQL 8.0 이상부터 지원, 메모리에 임시 결과 셋으로 올려놓고 재사용
- 순서에 의한 절차적으로 작성하여, 작성하기 쉽고 읽기 쉽다
- CTE 종류
  - Common Table Expressions (기본 CTE)
    - 순차적 쿼리 작성 가능
    - 예제) 부서 별 평균 salary가 가장 높은 부서와 가장 낮은 부서를 구하고 평균 급여 차액을 구하시오
<pre><code> WITH AvgSal AS (
    select d.dname, avg(e.salary) avgsal
      from Dept d inner join Emp e on d.id = e.dept
     group by d.id
     
  ),
  MaxAvgSal AS (
    select * from AvgSal order by avgsal desc limit 1
  ),
  MinAvgSal AS (
    select * from AvgSal order by avgsal limit 1
  ),
  SumUp AS (
    select '최고' as gb, m1.* from MaxAvgSal m1
    UNION
    select '최저' as gb, m2.* from MinAvgSal m2
  )
select gb, dname, format(avgsal * 10000,0) from SumUp
UNION
select '', '평균급여차액', format( (max(avgsal) - min(avgsal)) * 10000, 0) from SumUp;
</code></pre>

  - Recursive Common Table Expressions (재귀 CTE) **실무에서 많이사용함!!!**
    - 스스로 추가적인 Row를 생성 가능
    - 예제) 피보나치 수열 출력
<pre><code> WITH RECURSIVE fibonacci (n, fib_n, next_fib_n) AS
(
    select 1, 0, 1  -- 초기값 세팅
    UNION ALL
    select n + 1, next_fib_n, fib_n + next_fib_n
      from fibonacci where n < 10 -- 10개까지 출력
)
select * from fibonacci;
</code></pre>

  - 예제) 부서 트리 계층구조 출력
<pre><code>  WITH RECURSIVE CteDept(id, pid, pname, dname, d, h) AS 
(
    select id, pid, cast('' as char(31)), dname, 0, cast(id as char(10)) from Dept where pid = 0
    UNION ALL
    select d.id, d.pid, cte.dname, d.dname, d + 1, concat(cte.h, '-', d.id) from Dept d inner join CteDept cte on d.pid = cte.id
)
select /*+ SET_VAR(cte_max_recursion_depth = 5) */ d, dname from CteDept order by h;
</code></pre>

  ## - **재귀 CTE 실행횟수 제한하기 ( 꼭 주의해야함! )**
    - SET SESSION cte_max_recursion_depth = 20;      -- 재귀 실행을 20회로 제한
    - SET SESSION cte_max_recursion_depth = 1000000; -- 재귀 실행을 1M로 제한
    - SET max_execution_time = 1000;                 -- 최대 실행을 1000번까지로 제한(디폴트)

