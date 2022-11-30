def subsetSumZero(list, result = [], Sum = 0):
    if list == []:
        return [x for x in [result] if sum(x) == 0 and x != []]
    else:
        return subsetSumZero(list[1:], result + [list[0]], Sum + list[0]) + subsetSumZero(list[1:], result, Sum)
        

print(subsetSumZero([-7, -3, -2, 5, 7]))
print(subsetSumZero([2, -3, 5, 8 ,11, 23, -1]))