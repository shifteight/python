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

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherFraction):

        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den


f1 = Fraction(1, 4)
f2 = Fraction(1, 4)
f3 = f1 + f2
print(f3)

if f1 == f2:
    print("equal")
else:
    print("not equal")
