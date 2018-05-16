def gcd(m, n):
    while m % n != 0:
        oldM = m
        oldN = n

        m = oldN
        n = oldM % oldN
    return n


class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

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
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __sub__(self, otherFraction):
        newNum = self.num * otherFraction.den - self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __truediv__(self, otherFraction):
        if otherFraction.num == 0:
            raise ValueError
        else:
            return self.__mul__(Fraction(otherFraction.den, otherFraction.num))

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den


if __name__ == '__main__':
    f1 = Fraction(4, 8)
    f2 = Fraction(1, 8)
    f3 = f1 / f2
    print(f3)

    if f1 == f2:
        print("equal")
    else:
        print("not equal")
