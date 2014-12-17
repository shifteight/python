__author__ = 'kevin'


def test_list_size(n):
    import sys
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)


def find_repeat(ints):
    """Find the only integer that is repeated in an array of size n>=2
       containing integers 1 to n-1 .
    """
    res = ints[0]
    for j in range(1, len(ints)):
        res ^= ints[j]
    for i in range(1, len(ints)):
        res ^= i

    return res
