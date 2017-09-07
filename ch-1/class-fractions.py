def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
            self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    #My code begins here
    def __sub__(self, otherfraction):
        """Subtract two fractions

        Find the lowest common denominator
        Convert fractions as needed to LCD
        Subtract the numerators
        Put the answer over the same denominator.
        Simplify the fraction (if needed)."""

        #find LCM of denominators
        new_lcm = lcm(self.den, otherfraction.den)
        #if den <> LCM, multiply numerator by new_lcm/den
        #if den = new_lcm, leave fraction alone
        if new_lcm != self.den:
            new_self_num = self.num * (new_lcm/self.den)
        else:
            new_self_num = self.num

        if new_lcm != otherfraction.den:
            new_other_num = otherfraction.num * (new_lcm/otherfraction.den)
        else:
            new_other_num = otherfraction.num

        #subtract numerators
        sub_num = new_self_num - new_other_num

        #reduce new num over lcm den
        common = gcd(sub_num, new_lcm)
        newnum = sub_num//common
        newden = new_lcm//common

        return Fraction(newnum, newden)

        def __mul__(self, otherfraction):
            """Multiply two fractions

            Multipy the numerators
            Multiply the denominators"""

            newnum = self.num * otherfraction.num
            newden = self.den * otherfraction.den

            #reduce new num over lcm den
            common = gcd(sub_num, new_lcm)
            newnum = sub_num//common
            newden = new_lcm//common

            return Fraction(newnum, newden)

        def __truediv__(self, otherfraction):
            """ Divide two fractions
                Invert the number to the right of the sign.
                Multiply the fractions.
            """

            new_frac = Fraction(otherfraction.den, otherfraction.num)

            result = self * new_frac

            return result
