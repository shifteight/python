__author__ = 'kevin'


import sys
import os

if len(sys.argv) < 3:
    print "You need to specify two directories:"
    print sys.argv[0], "<dir1> <dir2>"
    sys.exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

print "Comparing:"
print directory1
print directory2

for directory in [directory1, directory2]:
    if not os.access(directory, os.F_OK):
        print directory, "isn't a valid directory!"
        sys.exit()

    print "Directory", directory
    for item in os.walk(directory):
        print item
    print