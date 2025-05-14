CREATE DATABASE StudentRecordsDB;
USE StudentRecordsDB;
CREATE TABLE Students(
Student_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name varchar(50),
age int not null,
class_id int not null,
total_score int not null
);
insert into Students (first_name, last_name, age, class_id, total_score)
values
('Sakshi','singh',20,101,92),('Saumya','singh',17,102,99),('Harsh','Rajput',16,103,95),
('Khushi','singh',20,104,94),('Rohit','raj',19,105,93);

select * from  students;

select avg(total_score) as average_score from Students;
update Students
set total_score = 90
where student_id = 105;
update Students
set age = age + 1
where class_id = 104;
