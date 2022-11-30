def my_union(list1, list2):
    return list1 + list2

def my_intersection(list1, list2):
    return [x for x in list1 if x in list2]

def my_difference(list1, list2):
    return [x for x in list1 if x not in list2]

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))