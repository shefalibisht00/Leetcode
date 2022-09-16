/* Write your T-SQL query statement below */

with cte as (
    select id,
    visit_date,
    people,
    (id - row_number() over(order by visit_date asc)) as diff
    from Stadium where people>=100
)
select id,
    visit_date,
    people
from (
select id,
    visit_date,
    people,
    count(*) over(partition by diff) as numOfRows
from cte
) tmp where numOfRows>=3


