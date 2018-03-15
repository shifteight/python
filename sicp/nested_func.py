#####################
# 高阶函数：嵌套函数
#####################

def square(x):
    return x * x

def successor(x):
    return x + 1

def average(x, y):
    return (x + y) / 2

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess

##def near(x, f, g):
##    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

def sqrt_update(guess, x):
    return average(guess, x / guess)


def square_root(x):
    def update(guess):
        return average(guess, x / guess)
    def test(guess):
        return approx_eq(square(guess), x)
    return iter_improve(update, test)
