create table userTBL
( userID CHAR(8) NOT NULL PRIMARY KEY,
  userName NVARCHAR2(10) NOT NULL,
  birthYear NUMBER(4) NOT NULL,
  addr NCHAR(2) NOT NULL,
  mobile1 CHAR(3),
  mobile2 CHAR(8),
  height NUMBER(3),
  mDate DATE
);

select * 
from userTBL;

INSERT INTO userTBL VALUES('LSG', '�̽±�', 1987, '����', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES('KBS', '�����', 1979, '�泲', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES('KKH', '���ȣ', 1971, '����', '019', '3333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES('JYP', '������', 1950, '���', '011', '4444444', 166, '2009-4-4');
INSERT INTO userTBL VALUES('SSK', '���ð�', 1979, '����', NULL, NULL, 186, '2013-12-12');
INSERT INTO userTBL VALUES('LJB', '�����', 1963, '����', '016', '6666666', 182, '2009-9-9');
INSERT INTO userTBL VALUES('YJS', '������', 1969, '�泲', NULL, NULL, 170, '2005-5-5');
INSERT INTO userTBL VALUES('EJW', '������', 1972, '���', '011', '8888888', 174, '2014-3-3');
INSERT INTO userTBL VALUES('JKW', '������', 1965, '���', '018', '9999999', 172, '2010-10-10');
INSERT INTO userTBL VALUES('BBK', '�ٺ�Ŵ', 1973, '����', '010', '0000000', 176, '2013-5-5');

COMMIT;
SELECT * FROM userTBL;