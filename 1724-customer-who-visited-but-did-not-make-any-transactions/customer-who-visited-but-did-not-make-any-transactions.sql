# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans
from Visits as v
left join Transactions as T
on v.visit_id= T.visit_id
where T.transaction_id is null
group by customer_id;