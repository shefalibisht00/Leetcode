with filtered_data as (
select id, 
       visit_date, 
       people, 
       LAG(id,1) OVER(order by id) as prevID_1, 
       LAG(id,2) OVER(order by id) as prevID_2,
       LEAD(id,1) OVER(order by id) as nextID_1, 
       LEAD(id,2) OVER(order by id) as nextID_2
from Stadium 
where people>=100
), ordered_filtered_data as (
select *, 
       CASE WHEN id+1=nextID_1 AND id+2 = nextID_2 then 'Y' 
            WHEN id-1=prevID_1 AND id-2 = prevID_2 then 'Y' 
            WHEN id-1 = prevID_1 and id+1=nextID_1 then 'Y'
            ELSE 'N' END as flag
from filtered_data
)
select id, visit_date, people from ordered_filtered_data where flag = 'Y'