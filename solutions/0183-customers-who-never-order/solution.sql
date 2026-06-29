# Write your MySQL query statement below
select name as Customers from Customers where id not in
(select Customers.id from Customers 
join Orders
on Customers.id=Orders.customerId);
