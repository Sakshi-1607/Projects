CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50),
    email VARCHAR(100)
);

