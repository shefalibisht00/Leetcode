/* Write your T-SQL query statement below */

with cte as(
select id,
    num,
    LAG(num) over(order by id) nxt
from Logs
), cte2 as (
select 
      num,
      SUM(case when num=nxt then 0 else 1 end) over(order by id) as diff
from cte
)
select distinct num as ConsecutiveNums from
(
select num,
        count(1) over(partition by diff) as n
from cte2
) tmp
where n>=3



