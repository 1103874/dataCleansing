"""
SQLITE3 DB안에서 QUERY로 조회하기
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite.db')

# 일자의 유니크한 값만 추출
print(pd.read_sql('select distinct 기본_CDATE from raw order by 기본_CDATE',con = conn ))

# 20221001 일자 데이터는 삭제할 것
cursor = conn.cursor()

cursor.execute('delete from raw where 기본_CDATE = "20221001"')
conn.commit() # 전송한 query문 실행을 승인
conn.rollback() # 전송한 쿼리문 실행을 취소

# 일자의 유니크한 값만 추출
print(pd.read_sql('select distinct 기본_CDATE from raw order by 기본_CDATE',con = conn ))