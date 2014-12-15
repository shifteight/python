__author__ = 'kevin'


def insertion_sort(A):
    """Sort list of comparable elements into non-decreasing order."""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur


a = [2, 4, 5, 1, 3]
insertion_sort(a)
print(a)