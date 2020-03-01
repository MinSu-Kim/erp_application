select user(), database ()

select * from title;

delete from title where title_no=6;

select * from employee;
delete from employee where emp_no = 1004


select emp_no, emp_name, title, manager, salary, dept, hire_date, gender, if (pic is not null, 1, 0) as pic from employee;