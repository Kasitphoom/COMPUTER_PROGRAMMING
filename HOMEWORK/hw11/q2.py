dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p': '1', 'q': '2', 'r': '3'}

def composite(d1, d2):
    d3 = {}
    for key in d1:
        if d1[key] in d2:
            d3[key] = d2[d1[key]]
    return d3

print(composite(dict1, dict2))