def makeMeasure(x):
    unit = '....|'
    rangeOfMeasure = range(0, int(x))
    measure = '|'
    for i in rangeOfMeasure:
        measure = measure + unit
    measure = measure + "\n"
    unitNum = ''
    txt = ''
    for i in rangeOfMeasure:
        length = txt.ljust(len(unit) - len(str(i + 1)))
        unitNum = unitNum + str(i) + length
    wholeString = measure + unitNum + str(x)
    return wholeString

def makeBoxes(x,y):
    horizontal = '+---'
    wholeString = ''
    for i in range(0, int(y)):
        for i in range(0, int(x)):
            wholeString = wholeString + horizontal
        wholeString = wholeString + '+' + '\n'
        for i in range(0, int(x)):
            wholeString = wholeString + '|' + ''.ljust(len('---'))
        wholeString = wholeString + '|' + '\n'

    for i in range(0, int(x)):
        wholeString = wholeString + horizontal
    wholeString = wholeString + '+' + '\n'
    return wholeString

def main():
    x = input("How long measure should be?  ")
    measure = makeMeasure(x)
    print(measure + "\n")
    x = input("What's the box width? ")
    y = input("What's the box high? ")
    box = makeBoxes(x,y)
    print(box)

main()