## Problems 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

from functools import reduce

def factors(n):
	# find a set of all factors of possibly VERY large integer n
	return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isPrime(n):
        # test if a number is prime
        if n < 2:
                return False
        if n == 2 or n == 3:
                return True
        x = int(n ** 0.5)
        for i in range(4, x):
                if i % 2 == 0:
                        continue
                if n % i == 0:
                        return False
        return True

print(max(filter(isPrime, factors(600851475143))))
