numer = 65340870976035201520025
numberConverted = str(numer)
count = 0
for i in numberConverted:
    if i == '0':
        count = count + 1
print("Number of 0 in long number: " + str(count))