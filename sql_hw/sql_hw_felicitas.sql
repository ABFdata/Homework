-- use sakila 
use sakila;

-- 1a. Display the first and last names of all actors from the table `actor`. 
select first_name, last_name
from actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 
select concat(first_name, ' ', last_name) 
AS 'actor_name' 
from actor;

select * from actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, 
-- "Joe." What is one query would you use to obtain this information?
select actor_id, first_name, last_name
from actor
where first_name = 'Joe';

-- 2b. Find all actors whose last name contain the letters `GEN`:
select first_name, last_name
from actor 
where last_name like '%GEN%';

-- 2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first 
-- name, in that order:
select last_name, first_name
from actor
where last_name like '%LI%';

-- 2d. Using `IN`, display the `country_id` and `country` columns of the 
-- following countries: Afghanistan, Bangladesh, and China:
select country_id, country
from country 
where country = 'Afghanistan' or country = 'Bangladesh' or country = 'China';

-- * 3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. 
-- Hint: you will need to specify the data type.
alter table actor
add middle_name varchar(50) after first_name;

select * from actor;

-- You realize that some of these actors have tremendously long last names. 
-- Change the data type of the `middle_name` column to `blobs`.
alter table actor
change middle_name middle_name blob;
select * from actor;

-- 3c. Now delete the `middle_name` column.
alter table actor
drop column middle_name;

select * from actor;

-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name, count(*) as count
from actor
group by last_name
having count(*)>0;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names 
-- that are shared by at least two actors
select last_name, count(*) as count
from actor
group by last_name
having count(*)>1;

-- Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
select first_name, last_name
from actor
where first_name = 'GROUCHO'; -- and last_name = 'WILLIAMS';

update actor
set first_name = 'HARPO'
where first_name = 'GROUCHO' and last_name = 'WILLIAMS';

select actor_id, first_name, last_name
from actor
where first_name = 'HARPO';

-- 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name 
-- after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. 
-- Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. 
-- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, 
-- HOWEVER! (Hint: update the record using a unique identifier.)

update actor
set first_name = 'GROUCHO'
where actor_id = 172;
-- first_name = 'HARPO' and last_name = 'WILLIAMS';

select actor_id, first_name, last_name
from actor
where first_name = 'GROUCHO';

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
select * from address;

create table address_new (
	address_id smallint(5),
	address varchar(50), 
    address2 varchar(50),
    district varchar(20),
    city_id smallint(5),
    postal_code varchar(10),
    phone varchar(20),
    location geometry,
    last_update timestamp
);

select * from address_new;

-- 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. 
-- Use the tables `staff` and `address`:
-- table staff

select * from staff;

select first_name, last_name, address
from staff 
join address
on staff.address_id = address.address_id;

-- 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. 
-- Use tables `staff` and `payment`. 
select * from payment;

select first_name, last_name, amount, payment_date 
from staff
join payment
on staff.staff_id = payment.staff_id
where payment_date like '2005-08%';

-- 6c. List each film and the number of actors who are listed for that film. 
-- Use tables `film_actor` and `film`. Use inner join.
-- select title, actor_id
-- from film_actor
-- inner join film
-- on film_actor.film_id = film.film_id;

select title, count(*) as actor_count
from film_actor
inner join film
on film_actor.film_id = film.film_id
group by film_actor.film_id;

-- 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

select title -- count(*) as film_count
from film
inner join inventory 
on inventory.film_id = film.film_id;
-- group by inventory_id.film_id
-- where title = 'Hunchback Impossible'


 select title
 from film
 where title = 'Hunchback Impossible';
 




