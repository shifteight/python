#!/usr/bin/env python

def find_dups(numbers):
    '''
    Takes a list of integers as arguments and returns a set of those integers
    that occur two or more times in the list.
    '''
    
    dups = set()
    helper = []
    helper.append(numbers[0])

    i = 1
    for value in numbers[1:]:
        if value in helper:
            dups.add(value)
        else:
            helper.append(value)

    return dups
