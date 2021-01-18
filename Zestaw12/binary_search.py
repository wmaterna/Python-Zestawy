

def binary_search(L, left, right, y):
    compare = (left + right) // 2
    if compare == 0:
        raise ValueError("Pusta lista")
    elif L[compare] == y:
        return compare
    elif y < L[compare]:
        return binary_search(L, left, compare-1, y)
    elif y > L[compare]:
        return binary_search(L,compare+1 ,right, y)
    else:
        return None

def int_numbers(n):
    numbers = [i for i in range(n)]
    return numbers


rangeOflist = 20
print(binary_search(int_numbers(rangeOflist), 0, rangeOflist, 6))