SELECT c.clubname, c.roomno, s.stdname, s.addr
	FROM stdtbl s
		INNER JOIN STDCLUBTBL SC 
			ON sc.stdname = s.STDNAME 
		INNER JOIN CLUBTBL c 
			ON sc.clubname = c.CLUBNAME 
		ORDER BY c.CLUBNAME ;
		
SELECT * FROM stdtbl;

--핸드폰번호없는애들 
SELECT username, concat(mobile1, mobile2 ) AS "전화번호" FROM usertbl u
	 WHERE username IN (
	 	SELECT username FROM usertbl WHERE mobile1 IS NULL 
	 );
	 
	
	
