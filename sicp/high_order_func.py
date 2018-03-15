#####################
# 高阶函数：函数作为参数
#####################

def summation(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def successor(k):
    return k + 1

def sum_naturals(n):
    return summation(n, identity, successor)

def sum_cubes(n):
    return summation(n, cube, successor)

# 另一个例子： 级数和逼近Pi

def pi_term(k):
    denominator = k * (k + 2)
    return 8 / denominator

def pi_next(k):
    return k + 4

def pi_sum(n):
    return summation(n, pi_term, pi_next)
