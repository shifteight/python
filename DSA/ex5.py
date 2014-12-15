__author__ = 'kevin'


def test_list_size(n):
    import sys
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)