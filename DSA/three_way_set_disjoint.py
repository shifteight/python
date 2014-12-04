__author__ = 'kevin'


def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists.
    Running time: O(n^3)
    """
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def disjoint2(A, B, C):
    """
    Running time: O(n^2)
    """
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True

def disjoint3(A, B, C):
    """
    Using a n-log-n sorting algorithm as a tool
    """
    temp = sorted(A + B + C)
    for j in range(1, len(temp) - 1):
        if temp[j-1] == temp[j] == temp[j+1]:
            return False
    return True

if __name__ == '__main__':
    A = [11, 2, 3, 5]
    B = [1, 4, 3, 2]
    C = [0, 32, 11, 13, 2]
    print(disjoint3(A, B, C))  # False
