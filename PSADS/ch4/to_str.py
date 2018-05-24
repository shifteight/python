def toStr(n, base):
    """Converts an integer to a string in any base 
    between 2 and 16."""
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


print(toStr(1453, 16))
