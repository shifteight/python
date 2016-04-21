## Problem 5
# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

def is_ed_1_10(n):
    for j in range(1, 11):
        if n % j != 0:
            return False
        if n // j % 2 == 1:
            return False
    return True

n = 21
while True:
    if is_ed_1_20(n):
        break
    n += 1

print(n)
