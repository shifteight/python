import sys

data = []
for k in range(26):
    a = len(data)
    b = sys.getsizeof(data)
    print('length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
    data.append(None)
