select * from membertbl where memberaddress like '경기%' ;
select * from membertbl where membername = '지운이';

create view hr.membertbl_view 
as
    select membername, memberaddress
    from hr.membertbl;
    
select * from membertbl_view ;

create procedure hr.myProc as
var1 int;
var2 int;
begin
    select  count(*)  into var1 from hr.membertbl;
    select  count(*)  into var2 from hr.producttbl;
    dbms_output.put_line(var1+var2);
end;
