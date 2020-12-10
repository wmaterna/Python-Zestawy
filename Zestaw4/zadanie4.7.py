def flatten(sequence):
    flatten_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatten_list.extend(flatten(item))
        else:
            flatten_list.append(item)
    return flatten_list


list1 = [[1], [4], (1, 2), [3, 4], (5, 6, 7)]
print(flatten(list1))

