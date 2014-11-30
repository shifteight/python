__author__ = 'kevin'


def factors(n):
    """
    A generator that computes factors
    :param n:
    """
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def fibonacci():
    """
    A generator that computes Fibonacci series
    :param None:
    """
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def print_first_n_fibs(n):
    """
    Print first n fibonacci numbers
    :param n:
    """
    i = iter(fibonacci())
    for j in range(n):
        print(next(i))
