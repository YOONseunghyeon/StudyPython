#Oracle_data
#cx_oracle 설치 : pip install cx_oracle
from sqlite3 import DatabaseError
from unittest import result
import cx_Oracle as ora
#dse = data source explorer , localhost- 내컴퓨터
#makedsn ('호스트명/ip주소', portnumber, '서비스명')
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
#connect(user, password, dsn, encoding)    utf-8을 넣어야 한글로 나옴
conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')

# DB접속이 성공하면 Connection 부터 cursor() 메서드를 호출하여 객체를 가져옴
cur = conn.cursor()  # 실행결과 데이터를 담을 메모리 객체
try:
    for row in cur.execute('SELECT * FROM emp'):
        print(row)     #-----데이터 모두 출력
    # cur.execute('SELECT COUNT(*) FROM emp')  #count 데이터 수세기 (13,)
    # result = cur.fetchone()   #한줄로 나옴
    # print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 15번라인 확인요 : {e}')
finally:
    cur.close() #커서 부터 먼저 닫고 
    conn.close() # 그다음 DB 접속 닫아야함