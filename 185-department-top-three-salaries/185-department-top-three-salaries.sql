/* Write your T-SQL query statement below */

with Emp_Dpt as (
select dpt.name as department, emp.name as employee, emp.salary,
    DENSE_RANK() OVER(partition by dpt.name order by emp.salary desc) as Rn
from Employee emp
join Department dpt
    on emp.departmentId = dpt.id
)
select department, employee, salary 
from Emp_Dpt
    where Rn<=3
order by department, salary desc