unit = '....|'
x = input("Enter length of measure: ")
rangeOfMeasure = range(0, int(x))
measure = '|'
for i in rangeOfMeasure:
    measure = measure + unit
measure = measure + "\n"
unitNum = ''
txt = ''
for i in rangeOfMeasure:
    length = txt.ljust(len(unit) - len(str(i+1)))
    unitNum = unitNum + str(i) + length
holeString = measure + unitNum + str(x)
print(holeString)

