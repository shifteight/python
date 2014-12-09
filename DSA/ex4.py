__author__ = 'kevin'


def min_max(seq):
    """Return minimum and maximum (as a pair) of a sequence in a recursive way."""
    if len(seq) == 0:
        return None
    if len(seq) == 1:
        return seq[0], seq[0]
    if len(seq) == 2:
        if seq[0] < seq[1]:
            return seq[0], seq[1]
        else:
            return seq[1], seq[0]
    mid = len(seq) // 2
    min1, max1 = min_max(seq[0:mid])
    min2, max2 = min_max(seq[mid:len(seq)])
    if max1 < max2:
        max = max2
    else:
        max = max1
    if min1 > min2:
        min = min2
    else:
        min = min1
    return min, max


def int_log2(n):
    """Return the integer part of the base-two logarithm of n."""
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return int_log2(n // 2) + 1


def uniqueness(seq):
    """Return True if there are not two same elements in seq."""
    if len(seq) <= 1:
        return True
    for i in range(1, len(seq)):
        if seq[i] == seq[0]:
            return False
        else:
            return uniqueness(seq[1:len(seq)])


def multiply(m, n):
    """Return the product of two integers m and n,
        using only addition and subtraction."""
    if n == 0:
        return 0
    if n > 0:
        return multiply(m, n-1) + m


def hanoi(n, source, helper, target):
    """Recursive algorithm of Hanoi problem."""
    if n > 0:

        # move tower of size n - 1 to helper
        hanoi(n - 1, source, target, helper)

        # move disk from source peg to target peg
        if source:
            target.append(source.pop())

        # move tower of size n - 1 from helper to target
        hanoi(n - 1, helper, source, target)

# # test for hanoi
# source = [4, 3, 2, 1]
# target = []
# helper = []
# hanoi(len(source), source, helper, target)
# print(source, helper, target)


def subsets(seq):
    """Return all subsets of seq. Not counting empty sets."""
    if len(seq) == 0:
        return []
    if len(seq) == 1:
        return [seq]
    res = []
    subs = subsets(seq[0:-1])
    res += subs
    for sub in subs:
        res.append(sub + [seq[-1]])
    return res


def reverse_recursive(s):
    """Return the reverse of string s."""
    if len(s) <= 1:
        return s
    else:
        return reverse_recursive(s[1:len(s)]) + s[0]


def is_palindrome(s):
    """Test if s is a palindrome."""
    if len(s) <= 1:
        return True
    
    if s[0] == s[len(s)-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

