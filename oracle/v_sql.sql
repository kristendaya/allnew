DECLARE 
	v_sql varchar2 (100) ;
	v_height usertbl.height%TYPE;
	
BEGIN -- "" 밑에 얘네가 다 ㅎ스프링
	v_sql := 'select height from usertbl where userid = ''EJW''';  
	EXECUTE IMMEDIATE v_sql INTO v_height ;
	dbms_output.put_line('키:' || v_height ) ;
END;
