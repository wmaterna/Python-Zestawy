# Sortowanie przez kopcowanie -  technika oparta na porównywaniu, a także na strukturze danych
# jaką jest kopiec. Założenie jest podobne do sortowania poprzez wybór.
# typowa implementacja nie jest stabilna, a złożoność czasowa sortowania na stosie to O(nlog n)

#jezeli k - index rodzice -  L dziecko 2*k+1, P dziecko 2*k+2, rodzic (i-1)/2


import math
from zadanie11_1 import *

def heapSort(n):
    length = len(n)
    for i in range(math.floor((length-2)/2), -1, -1):
        shift(n, length, i)
    for k in range(length - 1, -1, -1):
        n[k], n[0] = n[0], n[k]
        length = length - 1
        shift(n ,length, 0)
    return n

def shift(n, size, parent):
    maxIndex = parent
    leftChild = parent * 2 + 1
    rightChild = parent * 2 + 2

    if leftChild < size and n[leftChild] > n[maxIndex]:
        maxIndex = leftChild
    if rightChild < size and n[rightChild] > n[maxIndex]:
        maxIndex = rightChild
    if maxIndex != parent:
        n[maxIndex], n[parent] = n[parent], n[maxIndex]
        shift(n, size, maxIndex)


n = nearly_sorted_back(11)
print(n)
print(heapSort(n))