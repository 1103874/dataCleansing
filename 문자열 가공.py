import pandas as pd
import pymssql

df = ''

# apply 함수 : 데이터프레임의 각 행에 함수를 적용하는 방법
# apply함수, df['컬럼명'] : 해당 컬럼에 함수를 적용
# lambda 함수 : 한줄로 함수를 정의하는 방법
df['DeptName'].apply(lambda x: x) # 예시
df['DeptName'].apply(lambda x: x + '부서') # 예시

# apply와 lambda함수의 조합
# apply함수, df[['컬럼명1', '컬럼명2']] : 해당 컬럼들에 함수를 적용
df[['DeptName','PartyTeamName']].apply(lambda x: x['DeptName'], axis=1) # axis 0 : 행방향, axis 1 : 열방향
df[['DeptName','PartyTeamName']].apply(lambda x: x['DeptName'] + x['PartyTeamName'], axis=1) # axis 0 : 행방향, axis 1 : 열방향
df[['DeptName','PartyTeamName']].apply(lambda x: x['PartyTeamName'].replace(x['DeptName'],''), axis=1) # axis 0 : 행방향, axis 1 : 열방향
df['PartyTeamName'] = df[['DeptName','PartyTeamName']].apply(lambda x: x['PartyTeamName'].replace(x['DeptName'],'').strip(), axis=1) # axis 0 : 행방향, axis 1 : 열방향, strip : 공백 제거

#############################################

# region명 추출
df['region'] = df['PartyTeamName'].apply(lambda x : x.split(' ')[0])
# 팀명에서는 그 사람의 본인 소속 조직이다. region은 그의 상위 조직이 된다.