/* Write your T-SQL query statement below */

with cte as (
select  player_id, 
event_date,
        ROW_NUMBER() OVER(partition by player_id ORDER BY event_date) Rn
from activity
) 
select  player_id, event_date as first_login
from cte
where Rn=1