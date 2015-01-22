import hashlib
import sys

file_name = sys.argv[1]
read_file = file(file_name)
the_hash = hashlib.md5()
for line in read_file.readlines():
    the_hash.update(line)
print the_hash.hexdigest()
