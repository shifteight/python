def which_not_in(S):
    """A sequence S contains n - 1 unique integers in [0, n-1].
    Determine which one from this range that is not in S.
    """
    return sum(range(len(S)+1)) - sum(S)
