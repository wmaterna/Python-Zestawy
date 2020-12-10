import math
while True:
    x = input("Please, enter number: ")
    if x == "stop":
        break
    try:
        x = float(x)
    except ValueError:
        print("Not a number, please, enter number:")
    else:
        print("Para: " + str(x), str(x))
        result = pow(x,3)
        print("Potega: ", str(result))