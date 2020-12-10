def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum = sum + sum_seq(item)
        else:
            sum = sum + item
    return sum


list1 = [[1],[4],(1,2),[3,4],(5,6,7)]
print(sum_seq(list1))