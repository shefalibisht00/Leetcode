/* Write your T-SQL query statement below */


select name from customer
where COALESCE(referee_id,'') != 2
