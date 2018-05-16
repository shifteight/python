def gcd(m, n):
    while m % n != 0:
        oldM = m
        oldN = n

        m = oldN
        n = oldM % oldN
    return n


class Fraction:

    def __init__(self, top, bottom):

        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError
        if bottom == 0:
            raise ValueError("denominator should not be 0")
        if bottom < 0:
            bottom *= -1
            top *= -1
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        if self.num == 0:
            return str(0)
        elif self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + '/' + str(self.den)

    def __add__(self, otherFraction):

        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen)

    def __sub__(self, otherFraction):
        newNum = self.num * otherFraction.den - self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen)

    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen)

    def __truediv__(self, otherFraction):
        if otherFraction.num == 0:
            raise ValueError
        else:
            return self.__mul__(Fraction(otherFraction.den, otherFraction.num))

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __gt__(self, other):
        return self.__sub__(other).num > 0
    
    def __ge__(self, other):
        return self.__sub__(other).num >= 0
    
    
if __name__ == '__main__':
    f1 = Fraction(1, -2)
    f2 = Fraction(-1, 2)
    print("f1 = ", f1)
    print("f2 = ", f2)
    f3 = f1 / f2
    print("f1 / f2 = ", f1 / f2)

    if f1 < f2:
        print("f1 < f2")
    elif f1 == f2:
        print("f1 = f2")
    else:
        print("f1 > f2")

