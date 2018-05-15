create database suppliers;

use suppliers;

create table suppliers_table
(
 supplier_id int primary key,
 supplier_name varchar(30),
 city varchar(30),
 state varchar(30),
 total_spent decimal (8,2)
);

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('100', 'Shop of Epiphany', 'Augusta', 'Georgia', '220500.00');

select * from suppliers_table;

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('200', 'Instant Assemblers', 'Valdez', 'Alaska', '37000.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('300', 'Time Manufactures', 'Redwood City', 'California', '90500.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('400', 'Roadhouse Inc.', 'New York City', 'New York', '78150.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('500', 'Smiths & Berries', 'Portland', 'Oregon', '114600.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('600', 'Wesson LLC', 'Yuma', 'Alaska', '32000.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('700', 'ICF Foods', 'Orlando', 'Caliornia', '78700.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('800', 'Cheffmens Inc.', 'Toledo', 'Georgia', '187500.00');

insert into suppliers_table (supplier_id, supplier_name, city, state, total_spent)
values ('900', 'Samwoods Drinks.', 'Portland', 'Georgia', '17800.00');

select * from suppliers_table;

# Question 1 query suppliers that work in Georgia or California
select supplier_name, state
from suppliers_table
where state = 'Georgia'
or state = 'California';

# Question 2 query suppliers with the characters "wo" and the character "I" or 'i' in their name
select * 
from suppliers_table
where supplier_name like '%wo%'
and (supplier_name like '%I%' or supplier_name like '%i');

# Question 3 query suppliers on which a min 37,00 and max 80,000 was spent
select supplier_name, total_spent
from suppliers_table
where total_spent >= 37000.00
and total_spent <= 80000.00;

# Question 4 query supplier names and state where they belong in Georgia or Alaska
# supplier id is 100 or greater than 600
# Amount spent is less than 100,000 or amount spent is 220,000
select supplier_name, state, supplier_id, total_spent
from suppliers_table
where state in ('Georgia', 'Alaska')
and (supplier_id = 100 or supplier_id > 600)
and total_spent < 100000.00 or total_spent = 200000.00;

select * from suppliers_table
order by total_spent;

# Question 5 - True or False: The Keywords such as Select and Where must always be captialized
# FALSE

# Question 6 - True or False: The database works on first processing the filtering condition and then processes the from condition
# FALSE

# Question 7 - True or False: Having just the filter condition shown below in a SQL query will return all of the records from the table
# WHERE 1 = 1
# TRUE - Explanation: A 1=1 in a filter condition will always evaluate to true. If there are no other filter conditions in a SQL query, all records will be returned. 1=1 will always evaluate to true. 

# Question 8 - True or False: Null can not be compared using an equal sign
# TRUE - is null or is not null

# Question 9 True or False: The order by clause is processed before the FROM clause in a SQL statement and it's used to sort the columns
# FALSE - It's processed after the from clause and is one of the last clauses processed by the database engine.
