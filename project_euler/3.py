## Problems 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

def factors(n):
	# find a set of all factors of possibly VERY large integer n
	return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))