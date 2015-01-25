import os

from os.path import join, getsize

for root, dirs, files in os.walk('/home/kevin/work/python'):
    print root, "consumes",
    print sum([getsize(join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"
    if '.git' in dirs:
        dirs.remove('.git')  # don't visit git directories
