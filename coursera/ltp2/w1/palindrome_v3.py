def is_palindrome(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """

    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    return j <= i

	
