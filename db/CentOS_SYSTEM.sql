CREATE TABLE HR.indextbl
as
    select first_name, last_name, hire_date
    from hr.employees;
    
select * from HR.indextbl;  

create index idx_indextbl_firstname on HR.indextbl(FIRST_name);

select * from HR.indextbl where first_name='Jack';

select * from hr.employees where first_name='Jack';