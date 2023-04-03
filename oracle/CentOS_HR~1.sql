insert into membertbl values ('figure', '����', '��⵵ ������ ������');

select * from membertbl;

update membertbl set memberaddress = '���� ������ ���ﵿ'
where membername='����' ;

select * from membertbl;

Delete from membertbl
where membername='����';

select * from membertbl;

create table deletedmembertbl (
    memberid char(8),
    membername nchar(5),
    memberaddress nchar(20),
    deleteDate date
);

create trigger trg_deletedmembertbl
    after delete
    on membertbl
    for each row
begin
    insert into deletedmembertbl
    values (:old.memberid, :old.membername, :old.memberaddress, SYSDATE());
end ;


select *
from trg_deletedmembertbl;