CREATE DATABASE unidb;
USE unidb;

CREATE TABLE students (
id INT PRIMARY KEY,
name varchar(50) NOT NULL,
department VARCHAR(15) NOT NULL);

CREATE TABLE courses (
course_id VARCHAR(20) PRIMARY KEY,
name varchar(50) NOT NULL,
credit SMALLINT NOT NULL);

CREATE TABLE result(
std_id INT NOT NULL,
course_id VARCHAR(20) NOT NULL,
mark_type VARCHAR(20) NOT NULL,
marks SMALLINT NOT NULL,
FOREIGN KEY (std_id) REFERENCES students(id),
FOREIGN KEY (course_id) REFERENCES courses(course_id),
PRIMARY KEY (std_id, course_id, mark_type));

INSERT INTO students VALUES
( '1937463', 'Harper Lee', 'CSE'),
( '1937464', 'Garcia Marquez', 'CSE'),
( '1937465', 'Forster, E.M.', 'CSE'),
( '1937466', 'Ralph Ellison', 'CSE');

INSERT INTO courses VALUES
( 'CSE-401', 'Object Oriented programming', 3),
( 'CSE-403', 'Data Structure', 2),
( 'CSE-407', 'Unix programming', 2);

INSERT INTO result VALUES
( '1937463', 'CSE-401','Internal Exam' ,15),
( '1937463', 'CSE-401','Mid Term Exam' ,20),
( '1937463', 'CSE-401','Final Exam', 35),
( '1937464', 'CSE-403','Internal Exam' ,17),
( '1937464', 'CSE-403','Mid Term Exam' ,15),
( '1937464', 'CSE-403','Final Exam', 30),
( '1937465', 'CSE-401','Internal Exam' ,18),
( '1937465', 'CSE-401','Mid Term Exam' ,23),
( '1937465', 'CSE-401','Final Exam', 38),
( '1937466', 'CSE-407','Internal Exam' ,20),
( '1937466', 'CSE-407','Mid Term Exam' ,22),
( '1937466', 'CSE-407','Final Exam', 40);


select * from result;

SELECT result.std_id, result.course_id,
MAX(CASE WHEN result.mark_type = "Internal Exam" THEN result.marks END) "Internal Exam",
MAX(CASE WHEN result.mark_type = "Mid Term Exam" THEN result.marks END) "Mid Term Exam",
MAX(CASE WHEN result.mark_type = "Final Exam" THEN result.marks END) "Final Exam"
FROM result
GROUP BY result.std_id, result.course_id
ORDER BY result.std_id, result.course_id ASC;

SELECT result.std_id,result.course_id,
MAX(CASE WHEN result.mark_type = "Internal Exam" THEN result.marks END) "Internal Exam",
MAX(CASE WHEN result.mark_type = "Mid Term Exam" THEN result.marks END) "Mid Term Exam",
MAX(CASE WHEN result.mark_type = "Final Exam" THEN result.marks END) "Final Exam",
SUM( result.marks) as Total
FROM result
GROUP BY result.std_id, result.course_id
ORDER BY result.std_id, result.course_id ASC;

/* MySQL doesn't have a pivot function, alternatively in other platforms:

SELECT * FROM   
(
    SELECT 
        category_name, 
        product_id
    FROM 
        production.products p
        INNER JOIN production.categories c 
            ON c.category_id = p.category_id
) t 
PIVOT(
    COUNT(product_id) 
    FOR category_name IN (
        [Children Bicycles], 
        [Comfort Bicycles], 
        [Cruisers Bicycles], 
        [Cyclocross Bicycles], 
        [Electric Bikes], 
        [Mountain Bikes], 
        [Road Bikes])
) AS pivot_table;

can be executed for pivoting */


show databases;
use newdbr;
show tables;