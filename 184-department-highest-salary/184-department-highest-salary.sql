/* Write your T-SQL query statement below */

with Emp_Dpt as (
select dpt.name as department, emp.name as employee, emp.salary
from Employee emp
join Department dpt
    on emp.departmentId = dpt.id
), highestSalaryDept as (
select department, max(salary) as salary
from Emp_Dpt
group by department
)
select dpt.department, emp.employee, dpt.salary
from highestSalaryDept dpt 
join Emp_Dpt emp
on emp.salary = dpt.salary and emp.department = dpt.department
