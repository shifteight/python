#####################
# 高阶函数：装饰器
#####################

def trace1(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace1
def triple(x):
    return 3 * x


# 另一个例子：计算Fibonacci数列时进行记忆，避免重复计算
def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper

def trace(f):
    def helper(x):
        call_str = "{0}{1}".format(f.__name__, x)
        print("calling {0} ...".format(call_str))
        result = f(x)
        print("... returning from {0} = {1}".format(call_str, result))
        return result
    return helper

@memoize
@trace
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

