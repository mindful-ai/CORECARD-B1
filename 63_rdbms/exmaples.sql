Use newdb2;



/* Creating roles */
CREATE ROLE manager;
GRANT insert, update, delete TO manager;
GRANT manager TO root;
REVOKE insert FROM manager;
DROP ROLE manager;

/* Creating indeces */
select * from employees limit 10;
create index nameindex on employees(first_name, last_name);
/* Indexes are used to retrieve data from the database more quickly than otherwise. 
The users cannot see the indexes, they are just used to speed up searches/queries. */



/* Creating views */
CREATE VIEW my_new_view AS
SELECT location_id, department_name, country_name, job_title
FROM departments, countries, jobs;

/* WHERE Price > (SELECT AVG(Price) FROM Products); */

select * from my_new_view;

CREATE OR REPLACE VIEW my_new_view AS
SELECT location_id, department_name, country_name, job_title, region_name
FROM departments, countries, jobs, regions;

select * from my_new_view;

drop view my_new_view;

/* Creating triggers: The CREATE TRIGGER statement allows you to create a new trigger 
that is fired automatically whenever an event such as INSERT, DELETE, or UPDATE occurs against a table. */

CREATE TABLE account (acct_num INT, amount DECIMAL(10,2));
CREATE TRIGGER ins_sum BEFORE INSERT ON account
FOR EACH ROW SET @sum = @sum + NEW.amount;


select * from account;

SET @sum = 0;
INSERT INTO account VALUES(137,14.98),(141,1937.50),(97,-100.00);

SELECT @sum AS 'Total amount inserted';

/* Transaction Control Language */
use newdb;
select * from customers;
commit;
start transaction;
savepoint firstsavepoint;
update customers set salary = '7000' where id = 8;
select * from customers;
rollback to firstsavepoint;
select * from customers;
commit;



