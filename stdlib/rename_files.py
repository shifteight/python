from string import Template
import time, os.path

photo_files = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photo_files):
    base, ext = os.path.splitext(filename)
    new_name = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, new_name))