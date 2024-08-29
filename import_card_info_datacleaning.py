"""
django console에서 실행 시키기 위한 코드
"""

import pandas as pd
from auth_ons.models import User
from apps.models import Card
import datetime

df = pd.read_excel(r'C:\Users\user\PycharmProjects\DataPortal\utils\격려금 지급 대상자.xlsx',
                   sheet_name='소급대상')


df['년도'] = df['년도'].apply(lambda x: x.replace('년', ''))

for idx, itm in df.iterrows():
    print(f"N{itm['사번']}")  # f-string
    auth = User.objects.filter(username=f'N{itm["사번"]}')

    if auth.exists():
        Card.objects.create(
            author=auth.first(),
            card_name=itm['자격증명'],
            card_level=itm['수준'],
            card_year=itm['년도'],
            card_money=itm['지급액'],
        )
