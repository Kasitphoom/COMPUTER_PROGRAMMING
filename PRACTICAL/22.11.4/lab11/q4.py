sup = set([1, 2, 3, 4])
sub = set([])

def is_subset(sup, sub):
    if all(i in sup for i in sub):
        return True
    else:
        return False
    
print(is_subset(sup, sub))