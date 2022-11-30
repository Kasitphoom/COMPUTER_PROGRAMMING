s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*sets):
    if len(sets) == 0:
        return set()
    if len(sets) == 1:
        return sets[0]
    if len(sets) == 2:
        return {(x, y) for x in sets[0] for y in sets[1]}
    else:
        return {(x, *y) for x in sets[0] for y in product(*sets[1:])}

print("Product of s1: " + str(product(s1)))
print("Product of s1 s2: " + str(product(s1, s2)))
print("Product of s1 s2 s3: " + str(product(s1, s2, s3)))