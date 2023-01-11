import pathlib
from django.core.files import File
from dtApp.models import SRreview

filelist = pathlib.Path(r"C:\Users\user\PycharmProjects\DataPortal\srview\utils\230109_'22년SR사례_PDF변환파일").glob('**/*')
for file in filelist:

    seq_num = int(file.name.split('_')[0])+3
    print(seq_num, file.name)

    # SRreview.objects.filter(pk=seq_num).save(file.name, File(open(file.name, 'r')))
    SRreview.objects.filter(pk=seq_num).update(file_upload=f'{file.name}')

