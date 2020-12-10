list1 = [1, 4, 32, 62, 2, 8, 84 ,20, 87, 765, 875, 362, 9, 80]
list2 = [4, 765, 32, 8, 65, 32, 99, 101, 13]
listOfRepet = []
listOfAllElements = list1


for i in list1:
    for j in list2:
        if i==j and j not in listOfRepet:
            listOfRepet.append(j)

for i in list2:
    if i not in list1:
        listOfAllElements.append(i)

print("Values that repeat: " + str(listOfRepet))
print("All values: " + str(listOfAllElements))
