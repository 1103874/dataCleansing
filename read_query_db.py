"""
SQLITE3 DB안에서 QUERY로 조회하기
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite.db')

# 쿼리를 PANDAS를 통해서 실행하여 Dataframe으로 저장한다..
query_df = pd.read_sql('select 기본_STIME, 기본_CDATE from raw limit 10',con = conn )
print(query_df)


