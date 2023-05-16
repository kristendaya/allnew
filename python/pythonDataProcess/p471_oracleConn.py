import cx_Oracle

# cx_Oracle.init_oracle_client(lib_dir="C:\OracleXE\instantclient_19_18")
cx_Oracle.init_oracle_client(lib_dir="/usr/local/OracleXE/instantclient_19_19")

conn = None #접속객체
cur = None #커서 객체

#sql 실행할수있는 객체
try:
    loginfo = 'hr/1234@192.168.1.152:1521/xe'
    # loginfo = 'hr/1234@192.168.1.10:1521/xe'
    conn=cx_Oracle.connect(loginfo)
    print(type(conn))

    cur=conn.cursor()
    print(type(cur))


    sql='select power(2,10) from dual'
    cur.execute(sql)

#dual이 하는 역할 : 메소드를 여러개 갖고있는데 그중에 하나가 파워임. 얘가 연산을 할수있는애임. 듀얼이가~
#듀얼이라는 테이블이 있음.(가상테이블이 수없이만음ㅎㅇㅁ)
    for item in cur:
        print(item)
        

except Exception as err:
    print(err)

finally:
    if cur !=None:
        cur.close()

    if conn !=None:
        conn.close()

print('finished')