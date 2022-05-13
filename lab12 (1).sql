.read data.sql
-- Lab 12

-- Q2
CREATE TABLE obedience as
-- REPLACE THIS LINE
SELECT seven, gerald
from students;


-- Q3
CREATE TABLE blue_dog as
-- REPLACE THIS LINE
SELECT color, pet from students where color = "blue" and pet = "dog";


-- Q4
CREATE TABLE smallest_int as
-- REPLACE THIS LINE
SELECT time, smallest FROM students WHERE smallest >3 ORDER BY smallest LIMIT 20;


-- Q5
CREATE TABLE sevens as
-- REPLACE THIS LINE
SELECT seven FROM students s, checkboxes c where s.time = c.time AND s.number=7 AND c.'7'='True';;


-- Q6
CREATE TABLE matchmaker as
-- REPLACE THIS LINE
SELECT s1.pet, s1.song, s1.color, s2.color from students s1, students s2 WHERE s1.pet = s2.pet and s1.song = s2.song and s1.time!=s2.time and s1.time<s2.time;


-- Q7
CREATE TABLE smallest_int_count as
-- REPLACE THIS LINE
SELECT smallest, count(*) from students group by smallest having smallest>=1;


