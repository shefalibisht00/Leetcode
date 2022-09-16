CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        
        select ISNULL(
        (select salary
        from
        (
            select salary,
                   dense_rank() over(order by salary desc) rn
            from Employee
            group by salary
        ) as tmp
        where tmp.rn=@N
        ), null)
        
       
    );
END