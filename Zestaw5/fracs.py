# w związku z komunikatem: DeprecationWarning: fractions.gcd() is deprecated. Use math.gcd() instead.
# zamieniłam fraction.gcd() na math.gcd()

import fractions
import math


def add_frac(frac1, frac2):
    numerator = (frac1[0]*frac2[1]) + (frac1[1]*frac2[0])
    denominator = frac1[1]*frac2[1]
    gcd = math.gcd(numerator, denominator)
    fraction = [int(numerator / gcd), int(denominator / gcd)]
    return fraction

def sub_frac(frac1, frac2):
    numenator = (frac1[0] * frac2[1]) - (frac1[1] * frac2[0])
    denominator = frac1[1] * frac2[1]
    fraction = [numenator,denominator]
    gcd = math.gcd(numenator, denominator)
    fraction = [int(numenator / gcd), int(denominator / gcd)]
    return fraction

def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(numerator,denominator)
    fraction = [int(numerator / gcd), int(denominator / gcd)]
    return fraction

def div_frac(frac1, frac2):
    numerator = frac1[0]*frac2[1]
    denominator = frac1[1]*frac2[0]
    gcd = math.gcd(numerator, denominator)
    if numerator<0 and denominator<0:
        fraction = [int(-1 * numerator / gcd), int(-1 * denominator / gcd)]
    else:
        fraction = [int(numerator / gcd), int(denominator / gcd)]
    return fraction

def is_positive(frac):
    if frac[0] < 0:
        if frac[1] < 0:
            return True
        else:
            return False
    elif frac[1] < 0:
        return False
    else:
        return True

def is_zero(frac):
    if frac[0] == 0:
        return True
    return False

def frac2float(frac):
    return float(frac[0] / frac [1])


def cmp_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[1]
    fraction1 = [numerator, denominator]

    numerator = frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    fraction2 = [numerator, denominator]

    if fraction1[0] > fraction2[0]:
        return -1
    elif fraction1[0] == fraction2[0]:
        return 0
    else:
        return 1


