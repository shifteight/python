# birthday paradox

from random import *


def generate_birthdays(n):
    """
    generates n random birthdays.
    Note: few wrong forms of birthday permitted.
    """
    birthdays = []
    for i in range(n):
        month = randint(1,12)
        day = randint(1,31)
        birthdays.append(str(month) + '.' + str(day))
    return birthdays

def prob_of_same(n):
    
    count = 0  # number of experiments having same birthdays

    for i in range(1000):
        birthdays = generate_birthdays(n)
        uniques = set(birthdays)
        if len(uniques) < len(birthdays):
            count += 1

    return count / 1000

def test_program():
    for i in range(5, 101, 5):
        print("%d\t%f" % (i, prob_of_same(i)))
    
