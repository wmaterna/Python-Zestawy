import math
from random import shuffle
from random import gauss
import random


def int_numbers(n):
    numbers = [i for i in range(n)]
    shuffle(numbers)
    return numbers

def nearly_sorted(n):
    numbers = []
    for i in range(0,n):
        numbers.append(i)
    for i in range(0, n - 1,2):
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    if n % 2 == 1:
        numbers[n-1], numbers[n - 2] = numbers[n - 2], numbers[n-1]
    return numbers


def nearly_sorted_back(n):
    numbers = []
    for i in range(n-1,-1, -1):
        numbers.append(i)
    for i in range(0, n-1 ,2):
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    if n % 2 == 1:
        numbers[n-1], numbers[n - 2] = numbers[n - 2], numbers[n-1]
    return numbers

def gauss_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(gauss(0,1))
    return numbers

def int_random_repetitive(n):
    numbers = []
    for i in range(0,n):
        numbers.append(random.randint(0, math.floor(math.sqrt(n))-1))
    return numbers

# print(int_numbers(11))
# print(nearly_sorted(11))
# print(nearly_sorted_back(11))
# print(gauss_numbers(11))
# print(int_random_repetitive(11))