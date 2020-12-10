# dla okegu lezacego w srodku (0.5,0.5) o r = 0.5

import random

def calc_pi(n=100):
    insideCirclePoints = 0
    for i in range(0,n):
        x = random.random()  #[0.0,1.0)
        y = random.random()

        if ((x-0.5)*(x-0.5)) + ((y-0.5)*(y-0.5)) <= 0.25:
            insideCirclePoints = insideCirclePoints + 1
    print(insideCirclePoints)
    return 4 * insideCirclePoints / n

pi = calc_pi(1000000)
print(pi)