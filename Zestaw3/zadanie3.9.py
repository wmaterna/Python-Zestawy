list1 = [[],[4],(1,2),[3,4],(5,6,7)]
listOfSums = []
sum = 0

for i in range(len(list1)):
    for j in range(0,len(list1[i])):
        sum = sum + list1[i][j]
    listOfSums.append(sum)
    sum = 0

print(listOfSums)