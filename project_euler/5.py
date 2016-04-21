## Problem 5
# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

def all_divisible(n, m):
    for j in range(1, m+1):
        if n % j != 0:
            return False
    return True

n = 2520
m = 20
while True:
    if all_divisible(n, m):
        break
    n += 1

print(n)
