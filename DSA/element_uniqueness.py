__author__ = 'kevin'

def unique1(S):
    """Return True if there are no duplicate elements in sequence S.
    Running time: O(n^2)
    """
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True


def unique2(S):
    """
    Use sorting (O(n-log-n)) as a tool.
    :param S:
    :return:
    """
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False
    return True