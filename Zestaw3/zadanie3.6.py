x = input("Enter length: ")
y = input("Enter hight: ")

horizontal = '+---'
wholeString = ''
for i in range(0,int(y)):
    for i in range(0, int(x)):
        wholeString = wholeString + horizontal
    wholeString = wholeString + '+' + '\n'
    for i in range(0, int(x)):
        wholeString = wholeString + '|' + ''.ljust(len('---'))
    wholeString = wholeString + '|' + '\n'

for i in range(0, int(x)):
    wholeString = wholeString + horizontal
wholeString = wholeString + '+' + '\n'
print(wholeString)