"""
SMAP 측정결과 내용을 SQLITE3에 importing
"""

#1. sqlite3 db파일 정의(생성)
import sqlite3

# 1.1 sqlite3 파일 생성
conn = sqlite3.connect('sqlite.db')


# 2. excel 파일 읽어오기
import pandas as pd

# 보통 pandas에서 데이터를 저장하는 객체를 df (dataframe)
df = pd.read_excel('전사 일일 측정 결과장(0925~1005).xlsx', sheet_name='SMAP시나리오통계 Rawdata(0916)')

# 앞에 5줄 보자
df.head()

# 컬럼 수 확인
print("컬럼 수 : ", len(df.columns))

# df 컬럼을 list형태로 저장한다.
col_names = df.columns
print(col_names)


# 정규표현식을 이용해서 '숫자.공백' 으로 이루어진 문자열을 검색 후 삭제한다.
# list comprehension
import re

col_names_step1 = [re.sub('[0-9]+.\s','',i ) for i in col_names]
print(col_names_step1)

# df이 컬럼명을 숫자제거한 컬럼명으로 변경한다.
df.columns = col_names_step1
print(df.columns)

# 기본, GPS라는 단어가 들어간 컬럼명만 추출한다.
wanted_col = [i for i in col_names_step1 if '기본:' in i or 'GPS:' in i ]
print(wanted_col)
len(wanted_col)

# 원본 df에서 wanted_col명만 추출하여 별도로 df2에 저장한다.
df2 = df[wanted_col]

# 컬럼 전체가 비어있는 대상은 제외한다.

df3 = df2.dropna(axis=1, how='all')
df3.columns

# ': ' 을 포함하는 컬럼명을 '_' 로 변경하고자한다.
rename_col = [i.replace(': ', '_') for i in df3.columns if '기본:' in i or 'GPS:' in i ]
df3.columns = rename_col


# raw라는 테이블을 없으면 만들고(append), 테이블이 있으면 기존내용 밑에 추가한다.(단, 컬럼수가 동일하거나 엑셀안에 있는 컬럼명이 같아야 한다.)
# 컬럼수가 50개컬럼만 우선 가져오자
df3.to_sql('raw', if_exists='replace', index=False, con= conn)

