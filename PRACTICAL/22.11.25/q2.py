def list_reverse(list):
    if list == []:
        return []
    else:
        return list_reverse(list[1:]) + [list[0]]

print(list_reverse([1, 2, 3]))