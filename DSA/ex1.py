__author__ = 'kevin'

# exercises for chapter 1

def is_multiple(n, m):
    """
    return true if n is a multiple of m
    :param n:
    :param m:
    :return:
    """
    if n % m == 0:
        return True
    else:
        return False


def is_even(k):
    if k == 0:
        return True
    else:
        return not is_even(k - 1)


def minmax(data):
    """
    return min and max value of the sequence data
    :param data:
    :return:
    """
    minimum = maximum = data[0]
    n = len(data)
    for i in range(1, n):
        if data[i] <= minimum:
            minimum = data[i]
        elif data[i] >= maximum:
            maximum = data[i]

    return minimum, maximum


def sum_of_squares(n):
    """
    return sum of squares of all the positive integers smaller than n
    :param n:
    :return:
    """
    return sum(k * k for k in range(1, n))  # using generator comprehension


def my_choice(data):
    """
    return a random element from a non-empty sequence `data`, using randrange function
    from random module.
    :param data:
    :return:
    """
    import random
    return data[random.randrange(len(data))]


def reverse_list(numbers):
    """
    reverse a list of integers (in place).
    :param numbers:
    :return: numbers with reversed order
    """
    n = len(numbers)
    for i in range((n + 1) // 2):
        numbers[i], numbers[-(i + 1)] = numbers[-(i + 1)], numbers[i]
    return numbers


def check_odd_product(numbers):
    """
    determine if there is a distinct pair of numbers in the sequence
    whose product is odd.
    :param numbers: a sequence of integers
    :return: boolean
    """
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] * numbers[j] % 2 != 0:
                return True
    return False


def check_odd_product_simple(numbers):
    """
    determine if there is a distinct pair of numbers in the sequence
    whose product is odd.
    suffice to check if there are more than 1 odd numbers.
    :param numbers: a sequence of integers
    :return: boolean
    """
    n = len(numbers)
    j = 0
    for i in range(n):
        if numbers[i] % 2 != 0:
            j += 1

    if j > 1:
        return True

    return False


def is_distinct(numbers):
    """
    determine if all the numbers are different from each other.
    suffice to to check if the set of those numbers does not have
    a smaller length.
    :param numbers: a sequence (list or tuple) of numbers
    :return:
    """
    unique_numbers = set(numbers)
    return len(numbers) == len(unique_numbers)


# Some exercises

# C-1.18
# [k * (k + 1) for k in range(10)]

# C-1.19
# [chr(k) for k in range(97,123)]

# C-1.20
# TODO!

# C-1.21
# TODO!

# C-1.22
# dot product of two arrays of length n
def dot_product(a, b):
    """
    return the dot product of array a and b
    :param a: int array of length n
    :param b: int array of length n
    :return: dot product of a and b
    """
    n = len(a)
    c = []
    for i in range(n):
        c.append(a[i] * b[i])
    return c