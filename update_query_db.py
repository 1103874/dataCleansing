"""
SQLITE3 DB안에서 QUERY로 조회하기
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite.db')

# 일자의 유니크한 값만 추출
print(pd.read_sql('select distinct 기본_CDATE, `기본_CALL TYPE` from raw order by 기본_CDATE',con = conn ))

# `기본_CALL TYPE`이 HTTP -> FTP 변경 요청.
# SQL QUERY를 전송하기 위해서는 커서는 반드시 선언
cursor = conn.cursor()

'''
#주의사항 : 될 수 있으면 UPDATE는 하지 않는다.
이유는 같은걸 한 번 복사해 놓고, 값 덮어쓰고, 기존걸 삭제하는 절차를 수행하여 시간지연 발생.
'''
cursor.execute('update raw set `기본_CALL TYPE` = "FTP" where `기본_CALL TYPE` = "HTTP"')
conn.commit() # 전송한 query문 실행을 승인
# conn.rollback() # 전송한 쿼리문 실행을 취소

print(pd.read_sql('select distinct 기본_CDATE, `기본_CALL TYPE` from raw order by 기본_CDATE',con = conn ))

