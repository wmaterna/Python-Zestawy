import math

def odwracanie_iteracyjne(L, left, right):
    changesNumber = math.floor((right - left)/2)
    for i in range(0,changesNumber):
        L[left + i], L[right - i],  =   L[right - i],L[left + i]
    return L


def odwracanie_rekurencja(L, left, right):
    if (right - left) == 0:
        return L
    L[left],L[right] = L[right], L[left]
    return odwracanie_rekurencja(L, left+1, right-1)




L=[0,1,2,3,4,5,6,7,8,9,10]
print(odwracanie_iteracyjne(L,4,7))

L=[0,1,2,3,4,5,6,7,8,9,10]
print(odwracanie_rekurencja(L,1,9))