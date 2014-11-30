__author__ = 'kevin'

"""
Some comprehension examples
"""


def first_n_squares(n):
    """
    Return first n squares in form of list, set and dict comprehension
    :param n:
    :return:
    """

    l = [k * k for k in range(1, n + 1)]  # list comprehension
    s = {k * k for k in range(1, n + 1)}  # set comprehension
    d = {k: k * k for k in range(1, n + 1)}  # dict comprehension

    return l, s, d

# generator comprehension
# This syntax is particularly attractive when results do not need
# to be stored in memory. For example, to compute the sum of the
# first n squares, the generator syntax is preferred to the use of
# an explicitly instantiated list comprehension as the parameter.


def sum_of_the_first_n_squares(n):
    total = sum(k * k for k in range(1, n + 1))  # generator comprehension
    return total
