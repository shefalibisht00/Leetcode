/* Write your T-SQL query statement below */

with cte as (
select customer_number
,dense_rank() over(order by count(1) desc) rn
from Orders
group by customer_number
)
select customer_number from cte where rn=1

