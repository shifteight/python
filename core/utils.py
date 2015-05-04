#!/usr/bin/env python

def is_prime(n):
    'check whether a number is a prime.'
    
    import math

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def not_empty(s):
    'remove all empty strings.'
    
    return s and s.strip()

