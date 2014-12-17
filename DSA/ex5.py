__author__ = 'kevin'


def test_list_size(n):
    import sys
    data = list(range(6))
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


def summation(data):
    """Calculate the sum of elements in an n*n data array.
    For comparison to comprehension syntax method with built-in sum function.
    """
    s = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            s += data[row][col]
    return s

# testing:
# In ipython:
# data = [[1,2,3], [2,3,4], [3,4,5]]
# %timeit(summation(data))
# %timeit(sum(sum(row) for row in data))


def shuffle1(numbers):
    """An implementation of shuffle function alike that in random module.
    Using method like C-1.20, but with randrange().
    """
    from random import randrange
    n = len(numbers)
    for i in range(n-1, 1, -1):
        j = randrange(i-1)
        numbers[i], numbers[j] = numbers[j], numbers[i]