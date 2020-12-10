from __future__ import division
import math



def gcd_maker(x,y):
    gcd = math.gcd(x, y)
    return int(x / gcd), int(y / gcd)

def same_denominator(x1, y1, x2, y2):
    denominator = y1*y2
    x1 = x1 * y2
    x2 = x2 * y1
    return x1,x2, denominator


class Frac:
    """Klasa reprezentująca ułamki."""


    def __init__(self, x=0, y=1):
        self.x = x
        if y == 0:
            raise ValueError("Mianownik nie moze byz zerem")
        else:
            self.y = y


    def __str__(self):
        if self.y == 1:
            return self.x
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):
        return "Frac({},{})".format(self.x, self.y)


    def __eq__(self, other):
        x1,x2,y = same_denominator(self.x,self.y, other.x,other.y)
        return x1 == x2


    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        x1, x2, y = same_denominator(self.x, self.y, other.x,other.y)
        return x1 < x2


    def __le__(self, other):
        x1, x2, y = same_denominator(self.x, self.y, other.x, other.y)
        return x1 <= x2

    def __gt__(self, other):
        x1, x2, y = same_denominator(self.x, self.y, other.x, other.y)
        return x1 > x2

    def __ge__(self, other):
        x1, x2, y = same_denominator(self.x, self.y, other.x, other.y)
        return x1 >= x2

    def __add__(self, other):
        if isinstance(other, int): #frac + int
            x1 = self.x + (self.y * other)
            x1 , y = gcd_maker(x1,self.y)
            return Frac(x1,y)

        if isinstance(other, float): #frac + float
            floatTuple = other.as_integer_ratio()
            x1, x2, y = same_denominator(self.x, self.y, floatTuple[0],floatTuple[1])
            x = x1 + x2
            x, y = gcd_maker(x, y)
            return Frac(x, y)

        if isinstance(other, Frac): #farc + frac
            x1, x2, y = same_denominator(self.x, self.y, other.x,other.y)
            x = x1 + x2
            x, y = gcd_maker(x,y)
            return Frac(x,y)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):    # frac1-frac2, frac-int
        if isinstance(other, Frac):
            x1, x2, y = same_denominator(self.x, self.y, other.x, other.y)
            x = x1-x2
            x,y = gcd_maker(x,y)
            return Frac(x,y)
        if isinstance(other, int):
            x = self.x - (other * self.y)
            x,y = gcd_maker(x,self.y)
            return Frac(x,y)
        if isinstance(other, float):
            floatTuple = other.as_integer_ratio()
            x1, x2, y = same_denominator(self.x, self.y, floatTuple[0], floatTuple[1])
            x = x1 - x2
            x,y = gcd_maker(x,y)
            return Frac(x,y)


    def __rsub__(self, other):      # int-frac
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other, Frac):
            x = self.x * other.x
            y = self.y * other.y
            x,y = gcd_maker(x,y)
            return Frac(x,y)
        if isinstance(other, int):
            x = self.x * other
            x, y = gcd_maker(x,self.y)
            return Frac(x,y)
        if isinstance(other, float):
            floatTuple = other.as_integer_ratio()
            x = self.x * floatTuple[0]
            y = self.y * floatTuple[1]
            x, y = gcd_maker(x, y)
            return Frac(x, y)

    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other):   # frac1/frac2, frac/int, Python
        if isinstance(other, Frac):
            x = self.x * other.y
            y = self.y * other.x
            x,y = gcd_maker(x,y)
            return Frac(x,y)
        if isinstance(other, int):
            x = self.x
            y = self.y * other
            x, y = gcd_maker(x, y)
            return Frac(x, y)
        if isinstance(other, float):
            floatTuple = other.as_integer_ratio()
            x = self.x * floatTuple[1]
            y = self.y * floatTuple[0]
            x, y = gcd_maker(x, y)
            return Frac(x, y)




    def __rdiv__(self, other): pass # int/frac, Python 2

    def __truediv__(self, other):   # frac1/frac2, frac/int, Python 3
        if isinstance(other, Frac):
            x = self.x * other.y
            y = self.y * other.x
            x,y = gcd_maker(x,y)
            return Frac(x,y)
        if isinstance(other, int):
            x = self.x
            y = self.y * other
            x, y = gcd_maker(x, y)
            return Frac(x, y)
        if isinstance(other, float):
            floatTuple = other.as_integer_ratio()
            x = self.x * floatTuple[1]
            y = self.y * floatTuple[0]
            x, y = gcd_maker(x, y)
            return Frac(x, y)

    def __rtruediv__(self, other):   # int/frac, Python 3
        x = self.x
        y = self.y * other
        x, y = gcd_maker(x, y)
        return Frac(x, y)


    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac(self.x * (-1),self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):        # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])