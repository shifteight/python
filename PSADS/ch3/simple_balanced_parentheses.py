from stack import Stack


def parChecker(symbolString):
    """check whether a string of parentheses is balanced."""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('(()))'))
