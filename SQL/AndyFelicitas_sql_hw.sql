-- use sakila 
use sakila;

-- 1a. Display the first and last names of all actors from the table `actor`. 
SELECT 
    first_name, last_name
FROM
    actor;
    

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 
SELECT 
    CONCAT(first_name, ' ', last_name) AS 'actor_name'
FROM
    actor;
    
SELECT 
    *
FROM
    actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, 
-- "Joe." What is one query would you use to obtain this information?
SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    first_name = 'Joe';
    
select * from actor;


-- 2b. Find all actors whose last name contain the letters `GEN`:
SELECT 
    first_name, last_name
FROM
    actor
WHERE
    last_name LIKE '%GEN%';
    
select first_name, last_name
from actor
where last_name like '%GEN%';

-- 2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first 
-- name, in that order:
SELECT 
    last_name, first_name
FROM
    actor
WHERE
    last_name LIKE '%LI%';
    

-- 2d. Using `IN`, display the `country_id` and `country` columns of the 
-- following countries: Afghanistan, Bangladesh, and China:
SELECT 
    country_id, country
FROM
    country
WHERE
    country = 'Afghanistan'
        OR country = 'Bangladesh'
        OR country = 'China';
        
# other way to query
select country_id, country
from country
where country in ('Afghanistan', 'Bangladesh', 'China');

-- * 3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. 
-- Hint: you will need to specify the data type.
alter table actor
add middle_name varchar(50) after first_name;

SELECT 
    *
FROM
    actor;

-- You realize that some of these actors have tremendously long last names. 
-- Change the data type of the `middle_name` column to `blobs`.
alter table actor
change middle_name middle_name blob;
SELECT 
    *
FROM
    actor;

-- 3c. Now delete the `middle_name` column.
alter table actor
drop column middle_name;

SELECT 
    *
FROM
    actor;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT 
    last_name, COUNT(*) AS count
FROM
    actor
GROUP BY last_name
HAVING COUNT(*) > 0;

# new entry
select last_name, count(*) as count
from actor
group by last_name
having count > 0
order by count DESC;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names 
-- that are shared by at least two actors
SELECT 
    last_name, COUNT(*) AS count
FROM
    actor
GROUP BY last_name
HAVING COUNT(*) > 1;

select last_name, count(*) as count
from actor
group by last_name
having count > 1
order by count desc;


-- Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
SELECT 
    first_name, last_name
FROM
    actor
WHERE
    first_name = 'GROUCHO';-- and last_name = 'WILLIAMS';

UPDATE actor 
SET 
    first_name = 'HARPO'
WHERE
    first_name = 'GROUCHO'
        AND last_name = 'WILLIAMS';

SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    first_name = 'HARPO';

-- 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name 
-- after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. 
-- Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. 
-- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, 
-- HOWEVER! (Hint: update the record using a unique identifier.)

UPDATE actor 
SET 
    first_name = 'GROUCHO'
WHERE
    actor_id = 172;
-- first_name = 'HARPO' and last_name = 'WILLIAMS';

SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    first_name = 'GROUCHO';

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
SELECT 
    *
FROM
    address;

CREATE TABLE address_new (
    address_id SMALLINT(5),
    address VARCHAR(50),
    address2 VARCHAR(50),
    district VARCHAR(20),
    city_id SMALLINT(5),
    postal_code VARCHAR(10),
    phone VARCHAR(20),
    location GEOMETRY,
    last_update TIMESTAMP
);

SELECT 
    *
FROM
    address_new;

-- 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. 
-- Use the tables `staff` and `address`:
-- table staff

SELECT 
    *
FROM
    staff;

SELECT 
    first_name, last_name, address
FROM
    staff
        JOIN
    address ON staff.address_id = address.address_id;
    


-- 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. 
-- Use tables `staff` and `payment`. 
SELECT 
    *
FROM
    payment;

SELECT 
    first_name, last_name, SUM(amount) AS 'total'
FROM
    staff
        JOIN
    payment ON staff.staff_id = payment.staff_id
WHERE
    payment_date LIKE '2005-08%'
GROUP BY staff.staff_id;


select first_name, last_name, sum(amount) as 'Total'
from staff
join payment on staff.staff_id = payment.staff_id
where payment_date like '2005-08%'
group by staff.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. 
-- Use tables `film_actor` and `film`. Use inner join.
-- select title, actor_id
-- from film_actor
-- inner join film
-- on film_actor.film_id = film.film_id;

SELECT 
    title, COUNT(*) AS actor_count
FROM
    film_actor
        INNER JOIN
    film ON film_actor.film_id = film.film_id
GROUP BY film_actor.film_id;

-- 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
-- this displays how many 'Hunchback Impossible' are found in the column title
SELECT 
    title
FROM
    film
        INNER JOIN
    inventory ON inventory.film_id = film.film_id
WHERE
    title = 'Hunchback Impossible';

-- this counts the copies of 'Hunchback Impossible'
SELECT 
    COUNT(*) AS hunchback_copies
FROM
    film
        INNER JOIN
    inventory ON inventory.film_id = film.film_id
WHERE
    title = 'Hunchback Impossible'
HAVING (hunchback_copies >= 1);

-- 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. 
-- List the customers alphabetically by last name:
-- sum the purchase amount for each person 
SELECT 
    first_name, last_name, SUM(amount)
FROM
    customer
        JOIN
    payment ON customer.customer_id = payment.customer_id
GROUP BY first_name , last_name
ORDER BY last_name ASC;

--  7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
-- films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles 
-- of movies starting with the letters `K` and `Q` whose language is English. 

SELECT 
    title, name
FROM
    film AS f
        JOIN
    language AS l ON f.language_id = l.language_id
WHERE
    title LIKE 'K%' OR title LIKE 'Q%';

-- 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

SELECT 
    first_name, last_name, actor_id
FROM
    actor
WHERE
    actor_id IN ((SELECT 
            actor_id
        FROM
            film_actor
        WHERE
            film_id IN (SELECT 
                    film_id
                FROM
                    film
                WHERE
                    title = 'Alone Trip')));

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses 
-- of all Canadian customers. Use joins to retrieve this information.

SELECT 
    first_name, last_name, email, country
FROM
    customer AS c
        INNER JOIN
    address AS a ON c.address_id = a.address_id
        INNER JOIN
    city AS ci ON a.city_id = ci.city_id
        INNER JOIN
    country AS co ON ci.country_id = co.country_id
WHERE
    co.country = 'Canada';

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as famiy films.

SELECT 
    *
FROM
    category;-- category_id, name(category)
SELECT 
    *
FROM
    film;-- film_id, title
SELECT 
    *
FROM
    film_category;-- film_id, category_id

SELECT 
    title, name AS category
FROM
    film AS f
        INNER JOIN
    film_category AS fc ON f.film_id = fc.film_id
        INNER JOIN
    category AS c ON fc.category_id = c.category_id
WHERE
    c.name = 'Family';

-- 7e. Display the most frequently rented movies in descending order.

SELECT 
    f.title AS 'Movie', COUNT(r.rental_date) AS 'Times Rented'
FROM
    film AS f
        JOIN
    inventory AS i ON i.film_id = f.film_id
        JOIN
    rental AS r ON r.inventory_id = i.inventory_id
GROUP BY f.title
ORDER BY COUNT(r.rental_date) DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT 
    *
FROM
    store;-- store_id, address_id
SELECT 
    *
FROM
    film;-- rental_duration * -- rental_rate
SELECT 
    *
FROM
    inventory;-- inventory_id, film_id, store_id
SELECT 
    *
FROM
    payment;-- staff_id, amount
SELECT 
    *
FROM
    staff;-- staff_id, store_id

SELECT 
    store_id, SUM(amount) AS store_total
FROM
    payment AS p
        JOIN
    staff AS s ON p.staff_id = s.staff_id
GROUP BY p.staff_id
ORDER BY store_total DESC;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT 
    *
FROM
    store;-- store_id, address_id
SELECT 
    *
FROM
    city;-- city_id, city, country_id
SELECT 
    *
FROM
    address;-- address_id, city_id
SELECT 
    *
FROM
    country;-- has country_id, country

SELECT 
    store_id, city, country
FROM
    store AS s
        INNER JOIN
    address AS a ON s.address_id = a.address_id
        INNER JOIN
    city AS c ON a.city_id = c.city_id
        INNER JOIN
    country AS co ON c.country_id = co.country_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT 
    *
FROM
    category;-- category_id, name(genre)
SELECT 
    *
FROM
    film_category;-- category_id, film_id 
SELECT 
    *
FROM
    inventory;-- inventory_id, film_id
SELECT 
    *
FROM
    payment;-- payment_id, customer_id, staff_id, rental_id, amount
SELECT 
    *
FROM
    rental;-- rental_id, inventory_id, customer_id, staff_id

SELECT 
    name, SUM(amount) AS gross_revenue
FROM
    category AS c
        INNER JOIN
    film_category AS fc ON c.category_id = fc.category_id
        INNER JOIN
    inventory AS i ON fc.film_id = i.film_id
        INNER JOIN
    rental AS r ON i.inventory_id = r.inventory_id
        INNER JOIN
    payment AS p ON r.rental_id = p.rental_id
GROUP BY name
ORDER BY gross_revenue DESC
LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. 
-- If you haven't solved 7h, you can substitute another query to create a view.

CREATE TABLE top_five (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    name VARCHAR(30),
    gross_revenue DECIMAL(10 , 2 ),
    PRIMARY KEY (id)
);

insert into top_five (name, gross_revenue)
values ('Sports', 5314.21), ('Sci-Fi', 4756.98), ('Animation', 4656.30), ('Drama', 4587.39), ('Comedy', 4383.58);

SELECT 
    *
FROM
    top_five;

-- create view
CREATE VIEW view_top_five AS
    SELECT 
        name, gross_revenue
    FROM
        top_five;


-- 8b. How would you display the view that you created in 8a?
-- display view --
SELECT 
    *
FROM
    view_top_five;


-- 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it. 
drop view view_top_five;