#####################
# 高阶函数：作为一般方法的函数
#####################

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess

def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

def golden_update(guess):
    return 1 / guess + 1

def golden_test(guess):
    return near(guess, square, successor)

def square(x):
    return x * x

def successor(x):
    return x + 1

# test:
#   iter_improve(golden_update, golden_test)
