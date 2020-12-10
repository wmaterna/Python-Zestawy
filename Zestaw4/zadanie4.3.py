def factorial(n):

    factorial = 1
    if n == 0 or n==1:
        return 1
    else:
        for i in range(n):
            factorial = factorial * (i+1)
        return factorial

print(factorial(6))

