import random

def int_numbers_shuffled(n):
    numbers = [i for i in range(n)]
    random.shuffle(numbers)
    return numbers

def mediana_sort(L, left, right):
    #sortowanie - selectsort
    for i in range(left, right):
        k = i
        for j in range (i+1, right + 1):
            if L[j] < L[k]:
                k=j
        L[i], L[k] = L[k], L[i]

    #mediana
    if ((left+right) / 2) % 2 == 0:
        index = (left+right) // 2
        median = (L[index] + L[index+1]) / 2.0
        return median
    else:
        return L[(left+right)/2]


maxIndex = 10
L = int_numbers_shuffled(maxIndex)
print(mediana_sort(L,0,maxIndex - 1))