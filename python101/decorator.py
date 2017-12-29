def another_function(func):
    def other_func():
        val = 'The result of %s is %s' % (func(), eval(func()))
        return val
    return other_func

def a_function():
    return "1+1"

if __name__ == '__main__':
    value = a_function()
    print(value)
    decorator = another_function(a_function)
    print(decorator())