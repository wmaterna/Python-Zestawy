import math
# wzor Herona


def heron(a,b,c):
    p = (a + b + c)/2
    S = ((p-a) * (p-b) * (p-c)) * p
    area = math.sqrt(S)
    return area


def triangle(l):
    sum = 0
    maxValue = max(l)
    maxValueIndex = l.index(maxValue)
    for i in range(0,3):
        if i != maxValueIndex:
            sum = sum + l[i]

    if all(x > 0 for x in l) and sum > maxValue:
        return heron(l[0], l[1], l[2])
    else:
        raise ValueError("Cannot create triange")



l = [3,5,3]
print(triangle(l))