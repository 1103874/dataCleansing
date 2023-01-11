import pandas as pd
from srview.models import SRreview
from auth_ons.models import User

df = pd.read_excel(r"C:\Users\user\PycharmProjects\DataPortal\srview\utils\230109_'22년전사SR내역_오션등록용_T인병렬님.xlsx",
                   sheet_name='수상자리스트_전사포상_작업', skiprows=3)

for idx, itm in df.iterrows():
    # print(f"{itm['수여자']} SR" )

    SRreview.objects.create(
        region=itm['담당'],
        team=itm['팀'],
        dt=itm['월'],
        type=f"{itm['수여자']} SR",
        title=itm['내용'],
        description=itm['세부내용'],
        author=User.objects.filter(first_name='성기범').get()
    )