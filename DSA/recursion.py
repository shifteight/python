__author__ = 'kevin'


def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return n, 0
    else:
        (a, b) = good_fibonacci(n-1)
        return a+b, a


def linear_sum(S, n):
    """Return the sum of the first n numbers of seq S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        start, stop = start + 1, stop - 1


def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


def power_faster(x, n):
    """Compute x**n using squaring technique."""
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)