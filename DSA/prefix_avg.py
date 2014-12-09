__author__ = 'kevin'

# Calculate prefix averages of a sequence of numbers.

def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    With running time: O(n^2)
    """
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    With running time: O(n^2)
    """
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j + 1)
    return A

def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    With running time: O(n)
    """
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

if __name__ == '__main__':
    x = range(10000)
    # In ipython: %timeit prefix_average2(x)