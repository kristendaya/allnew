DECLARE
	inum 	NUMBER (3);
	hap		NUMBER (5) ;
	
BEGIN
		inum :=1;
		hap :=0;
		WHILE inum <= 100
		LOOP	
				hap := hap + inum;
				inum := inum +1 ;
		END LOOP;
		dbms_output.put_line('합계 : ' || hap) ;
END ;
