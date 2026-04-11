CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks FLOAT
);


INSERT INTO students (name, age, course, marks)
VALUES 
('Shashank', 23, 'Statistics', 85),
('Amit', 22, 'CS', 78),
('Riya', 24, 'Math', 90);

SELECT * FROM students;
SELECT name, marks FROM students;

UPDATE students
SET marks = 88
WHERE name = 'Amit';

DELETE FROM students
WHERE name = 'Riya';

SELECT * FROM students WHERE marks > 80;
SELECT * FROM students WHERE course = 'CS';

SELECT * FROM students ORDER BY marks DESC;
SELECT * FROM students ORDER BY age ASC;

SELECT course, AVG(marks)
FROM students
GROUP BY course;

SELECT COUNT(*) FROM students;
SELECT SUM(marks) FROM students;
SELECT AVG(marks) FROM students;
SELECT MAX(marks) FROM students;
SELECT MIN(marks) FROM students;

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100)
);

INSERT INTO courses (course_name)
VALUES ('Statistics'), ('CS'), ('Math');

SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course = courses.course_name;

SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.course = courses.course_name;

SELECT students.name, courses.course_name
FROM students
RIGHT JOIN courses
ON students.course = courses.course_name;

SELECT course, COUNT(*)
FROM students
GROUP BY course;

SELECT * FROM students;

SELECT name, marks FROM students;

SELECT * FROM students WHERE marks > 80;

SELECT * FROM students WHERE course = 'CS';

SELECT * FROM students ORDER BY marks DESC;

SELECT COUNT(*) FROM students;

SELECT AVG(marks) FROM students;

SELECT MAX(marks) FROM students;

SELECT MIN(marks) FROM students;

SELECT SUM(marks) FROM students;

SELECT course, AVG(marks)
FROM students
GROUP BY course;

SELECT course, COUNT(*)
FROM students
GROUP BY course;

SELECT course, COUNT(*)
FROM students
GROUP BY course
HAVING COUNT(*) > 1;

SELECT * FROM students
WHERE marks BETWEEN 70 AND 90;

SELECT * FROM students
WHERE name LIKE 'S%';

SELECT * FROM students
WHERE course != 'CS';


SELECT s.name, c.course_name
FROM students s
INNER JOIN courses c
ON s.course = c.course_name;

SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c
ON s.course = c.course_name;

SELECT s.name, c.course_name
FROM students s
RIGHT JOIN courses c
ON s.course = c.course_name;

SELECT MAX(marks)
FROM students
WHERE marks < (SELECT MAX(marks) FROM students);

SELECT * FROM students
WHERE marks > (SELECT AVG(marks) FROM students);

DELETE FROM students
WHERE id NOT IN (
    SELECT MIN(id)
    FROM students
    GROUP BY name
);

SELECT name, marks,
RANK() OVER (ORDER BY marks DESC) AS rank
FROM students;

SELECT * FROM students
ORDER BY marks DESC
LIMIT 2;